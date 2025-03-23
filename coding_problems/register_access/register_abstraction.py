import math
import time
import random


class HWRegister:
    """Hardware Register with address and value."""

    def __init__(self, name: str, address: int, reset_value: int = 0, size=64) -> None:
        """Set up the register abstraction object.

        Args:
            name (str): Name of the register.
            address (int): The address of the register.
            reset_value (int, optional): The reset value. Defaults to 0.
            size (int, optional): The size of the register. Defaults to 64.
        """
        self._name = name
        self._address = address
        self._value = reset_value
        self._max_val = int(math.pow(2, size)) - 1

    @property
    def value(self) -> int:
        """The value of the register.

        Returns:
            int: The value of the register as an int.
        """
        # Give parent a chance to update value before reading
        if hasattr(self, "_parent"):
            self._parent._on_register_read(self)
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        """Update the value of the register with simple assignment.
        In other words, a register write.

        Args:
            new_value (int): The new value of the register.

        Raises:
            ValueError: The value being written is larger than the register can handle.
        """
        if new_value > self._max_val:
            raise ValueError("Register access size is bigger than the actual size.")
        self._value = new_value
        if hasattr(self, "_parent"):
            self._parent._on_register_write(self)

    @property
    def address(self) -> int:
        """The address property of the register.

        Returns:
            int: The memory address of the register.
        """
        return self._address

    @property
    def name(self) -> str:
        """The name property of the register.

        Returns:
            str: The name of the register.
        """
        return self._name


class IP:
    """Base class for an IP."""

    def get_registers(self) -> list[HWRegister]:
        """Get all the registers for this IP.

        Returns:
            list[HWRegister]: A list of register objects.
        """
        return self._registers

    def _on_register_write(self, register: HWRegister) -> None:
        """Called when a value is written to a register.
        This is meant to simulate a real write...but it actually
        doesn't do anything.

        Args:
            register (HWRegister): The register object.
        """
        pass

    def _on_register_read(self, register: HWRegister) -> None:
        """Called when a value is read from a register.
        This is meant to simulate a real read...but it actually
        doesn't do anything.

        Args:
            register (HWRegister): The register object.
        """
        pass


class TemperatureMonitor(IP):
    """Temperature Monitor Device."""

    def __init__(self) -> None:
        """Set up the temperature monitor object with all registers in the spec."""
        self.temp_status = HWRegister("temp_status", 0x8, 0xABCDEF)
        self.device_id = HWRegister("device_id", 0x0, 0xCAFECAFE)
        self._registers = [self.device_id, self.temp_status]


class JTAGController(IP):
    """JTAG Controller for indirect register access."""

    def __init__(self, target_device: TemperatureMonitor) -> None:
        """Set up the JTAG controller object by inheriting properties
        of the IP class.

        Args:
            target_device (TemperatureMonitor): The temperature monitor object.
        """
        super().__init__()
        self._target = target_device

        # Transaction state
        self._transaction_start_time = None
        self._transaction_duration = None
        self._pending_operation = None

        # Add JTAG registers
        self.reg_request = HWRegister("reg_request", 0x0, size=32)
        self.reg_data_hi = HWRegister("reg_data_hi", 0x4, size=32)
        self.reg_data_lo = HWRegister("reg_data_lo", 0x8, size=32)

        # Set parent reference for all registers
        self.reg_request._parent = self
        self.reg_data_hi._parent = self
        self.reg_data_lo._parent = self

        # All registers in a list
        self._registers = [self.reg_request, self.reg_data_hi, self.reg_data_lo]

    def _on_register_write(self, register: HWRegister) -> None:
        """Handle register writes."""
        if register.name == "reg_request" and (register.value & 0x1):
            # Start new transaction
            self._transaction_start_time = time.time()
            self._transaction_duration = random.uniform(0.1, 0.5)
            self._pending_operation = register.value

    def _on_register_read(self, register: HWRegister) -> None:
        """Handle register reads for an input register.

        Args:
            register (HWRegister): The register object.
        """
        if not self._transaction_start_time:
            return

        current_time = time.time()
        elapsed = current_time - self._transaction_start_time

        if elapsed >= self._transaction_duration:
            # Transaction complete, update registers
            self._complete_transaction()

    def _complete_transaction(self) -> None:
        """Complete a pending transaction (read or write).

        Raises:
            ValueError: There was an invalid register address.
        """
        if not self._pending_operation:
            return

        try:
            # Extract address and operation type
            address = (self._pending_operation >> 8) & 0xFF
            is_read = bool(self._pending_operation & 0x2)

            # Find target register
            target_reg = next(
                (reg for reg in self._target.get_registers() if reg.address == address),
                None,
            )

            if target_reg is None:
                raise ValueError(f"Invalid register address: {hex(address)}")

            if is_read:
                # Handle read operation
                value = target_reg.value
                self.reg_data_hi._value = (value >> 32) & 0xFFFFFFFF
                self.reg_data_lo._value = value & 0xFFFFFFFF
            else:
                # Handle write operation
                value = (self.reg_data_hi.value << 32) | self.reg_data_lo.value
                target_reg.value = value

        except Exception as e:
            print(f"JTAG operation failed: {e}")
        finally:
            # Clear transaction state
            self._transaction_start_time = None
            self._transaction_duration = None
            self._pending_operation = None
            self.reg_request._value &= (
                ~0x1
            )  # Clear request bit without triggering write

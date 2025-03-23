"""Test case for validating JTAG access to Temperature Monitor registers."""

from register_abstraction import TemperatureMonitor, JTAGController


def validate_jtag_access(temp_mon: TemperatureMonitor, jtag: JTAGController) -> None:
    """
    Validate JTAG access to all Temperature Monitor registers.

    Args:
        temp_mon: Temperature Monitor instance
        jtag: JTAG Controller instance

    Raises:
        Exception: TBD.
    """
    print("\nStarting JTAG validation...")
    # Enter your code here!


def main():
    """Main test execution."""
    # Create instances
    temp_mon = TemperatureMonitor()
    jtag = JTAGController(temp_mon)

    try:
        validate_jtag_access(temp_mon, jtag)
        print("\n✓ All JTAG validation tests passed successfully")
    except Exception as e:
        print(f"\n✗ JTAG validation failed: {e}")
        raise


if __name__ == "__main__":
    main()

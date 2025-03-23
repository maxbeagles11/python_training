# Temperature Monitor JTAG Validation Problem

## Background
You are working on validating a Temperature Monitor IP that is accessed through two interfaces:
1. Direct register access (memory-mapped)
2. JTAG controller for indirect access

The JTAG interface provides debug access when direct access is not possible due to routing constraints or during debug sessions.

## Task
**Write a validation script that verifies correct operation of the JTAG access to Temperature Monitor registers.**

## Requirements

### Test Coverage
1. Basic Access
   - Read both Temperature Monitor registers through the indirect access and compare them to the values from the actual registers.

2. Protocol Validation
   - Correct handling of request active bit
   - Timeout handling during polling

### Implementation Notes
- Implement timeout for polling operations (max 100ms)
- Document any test limitations
- Assume the registers under temp_mon are MMIO.

## Code examples

### Direct Register Access
```python
# Create Temperature Monitor
temp_mon = TemperatureMonitor()

# Access registers directly
temp_mon.temp_status.value  # Read/write temperature status
temp_mon.device_id.value    # Read device ID
```

### JTAG Access
```python
# Create JTAG controller
jtag = JTAGController(temp_mon)

# Access JTAG registers
jtag.reg_request.value   # Control register
jtag.reg_data_hi.value  # Upper 32 bits
jtag.reg_data_lo.value  # Lower 32 bits

# Get register list
registers = jtag.get_registers()  # Returns [HWRegister]

# Register properties
reg_offset = jtag.reg_request.address  # Get register offset
reg_value = jtag.reg_request.value    # Get/set register value
```

## Deliverables
1. Documentation including:
   - Test strategy
   - Assumptions made
   - Known limitations
   - Error handling approach

2. Python test script with comprehensive validation


## Time Limit
- Implementation: 20 minutes
- Documentation: 10 minutes

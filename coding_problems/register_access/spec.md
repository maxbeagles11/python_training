# Temperature Monitor Specification - Register Access

## Overview
This document describes how the register access can be performed to the Temperature Monitor IP, which provides temperature sensing and monitoring capabilities.

The registers in the IP can be accessed through MMIO, but in the case of the memory mapping failure they could be only accessed through an indirect mechanism.

## Indirect Access Protocol

The indirect access is performed through the JTAG controller, which has three registers used for issuing a transaction. The process is described in the following section.

### Read Operation Sequence
1. Write to reg_request:
   - Set ADDR field [15:8] to target register address
   - Set RW bit [1] = 1
   - Set REQ bit [0] = 1
2. Poll reg_request until REQ bit [0] = 0
3. Read reg_data_hi for upper 32-bits
4. Read reg_data_lo for lower 32-bits

### Timing Requirements
- Maximum polling timeout: The transaction can take between 100ms to 500ms
- Typical transaction completion time: 2-5 cycles

## Register Map

### Temperature Monitor IP

#### device_id (0x0)
Device identification information.

| Bits    | Name      | Description | Reset Value |
|---------|-----------|-------------|-------------|
| [63:32] | MFG_ID    | Manufacturer ID ("AP") | 0x4150 |
| [31:16] | VERSION   | Device Version | 0x0001 |
| [15:0]  | TYPE      | Device Type | 0x0001 |

#### temp_status (0x8)
Temperature sensor readings and status.

| Bits    | Name         | Description | Reset Value |
|---------|------------|-------------|-------------|
| [63:48] | Reserved   | Reserved for future use | 0x0000 |
| [47:32] | TEMP2      | Temperature Sensor 2 Value (Celsius) | 0x0018 (24°C) |
| [31:16] | TEMP1      | Temperature Sensor 1 Value (Celsius) | 0x0019 (25°C) |
| [15:1]  | Reserved   | Reserved for future use | 0x0000 |
| [0]     | TEMP_ALERT | Temperature Alert Flag | 0x0 |


## JTAG Controller IP

#### reg_request (0x0)
Request register for indirect access control.

| Bits    | Name      | Description |
|---------|-----------|-------------|
| [31:16] | Reserved  | Reserved for future use |
| [15:8]  | ADDR      | Target Register Address |
| [1]     | RW        | Read/Write Select (1: Read, 0: Write) |
| [0]     | REQ       | Request Active (1: Active, 0: Done) |

#### reg_data_hi (0x4)
Upper 32 bits of data for indirect access.

| Bits    | Name      | Description |
|---------|-----------|-------------|
| [31:0]  | DATA_HI   | Upper 32-bits of register data |

#### reg_data_lo (0x8)
Lower 32 bits of data for indirect access.

| Bits    | Name      | Description |
|---------|-----------|-------------|
| [31:0]  | DATA_LO   | Lower 32-bits of register data |

# asset-inventory.md

# ICS/OT Risk Assessment Lab — Asset Inventory

**Project:** ICS/OT Risk Assessment Lab
**Fictional Utility:** Keystone Gas & Electric — Compressor Station Alpha (Simulated)
**Assessment Date:** 2026 Lab Cycle
**Prepared By:** Mahmadarsh Vahora

> All asset names, network addresses, and firmware versions below are lab constructs generated for this portfolio project and do not reflect any real vendor deployment.

| Asset ID | Asset Name | Asset Type | Zone (Purdue Level) | OS / Firmware | Network Address | Criticality | Notes |
|---|---|---|---|---|---|---|---|
| AST-001 | CS-ALPHA-PLC-01 | PLC | Level 1 | GRFICS Simulated PLC Firmware v1.2 | 192.168.50.10 | High | Controls simulated compressor discharge pressure loop; Modbus-TCP, no authentication |
| AST-002 | CS-ALPHA-PLC-02 | PLC | Level 1 | GRFICS Simulated PLC Firmware v1.2 | 192.168.50.11 | High | Backup/secondary control loop for redundant valve actuation |
| AST-003 | CS-ALPHA-HMI-01 | HMI | Level 2 | Windows 10 Enterprise (simulated, unpatched build) | 192.168.50.20 | High | Primary operator dashboard; direct Modbus-TCP session to both PLCs |
| AST-004 | CS-ALPHA-HIST-01 | Historian | Level 3 | Simulated lightweight SQL data logger | 192.168.50.30 | Medium | Stores 90 days of rolling process tag history |
| AST-005 | CS-ALPHA-EWS-01 | Engineering Workstation | Level 2 | Windows 10 Enterprise (simulated) | 192.168.50.21 | High | Used for PLC logic programming; highest-privilege access point in environment |
| AST-006 | CS-ALPHA-FW-DMZ | Firewall (DMZ boundary) | Level 3.5 | Simulated stateful firewall appliance | 192.168.40.1 | High | Sole enforced boundary between Level 4 (Enterprise) and OT network |
| AST-007 | CS-ALPHA-SW-OT01 | OT Network Switch | Level 2/1 | Simulated unmanaged switch | 192.168.50.1 | Medium | No VLAN segmentation configured between Level 1 and Level 2 devices |
| AST-008 | CS-ALPHA-RTU-01 | RTU | Level 1 | GRFICS Simulated RTU v1.0 | 192.168.50.40 | Medium | Reports field sensor data (tank level, flow rate) to Historian |
| AST-009 | CS-ALPHA-RTU-02 | RTU | Level 1 | GRFICS Simulated RTU v1.0 | 192.168.50.41 | Medium | Reports pressure/temperature telemetry from secondary process line |
| AST-010 | CS-ALPHA-OPC-01 | OPC Server | Level 2/3 | Simulated OPC-UA gateway | 192.168.50.25 | Medium | Bridges Historian and third-party analytics tooling to OT tag data |
| AST-011 | CS-ALPHA-ATK-KALI | Attacker/Assessment Platform | Level 4 (external) | Kali Linux 2024.x | 192.168.10.100 | N/A (Assessment Tooling) | Used exclusively for controlled assessment activity, not a production asset |
| AST-012 | CS-ALPHA-JMP-01 | Jump Host / Remote Access Gateway | Level 3.5 | Windows Server 2019 (simulated) | 192.168.40.10 | High | Sole documented remote-access path for vendor and remote engineer connectivity |
| AST-013 | CS-ALPHA-VPN-GW | VPN Gateway | Level 3.5 | Simulated VPN concentrator | 192.168.40.11 | High | Terminates all remote OT access sessions; no MFA enforced in current lab build |
| AST-014 | CS-ALPHA-PRT-01 | Network Printer (OT segment) | Level 2 | Embedded firmware, unknown patch level | 192.168.50.50 | Low | Legacy device retained on OT VLAN for shift-log printing; frequently overlooked in inventories |

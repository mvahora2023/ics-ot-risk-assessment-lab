# Network Architecture — Purdue Model View

Compressor Station Alpha (simulated GRFICS lab environment), Keystone Gas & Electric.

```mermaid
flowchart TB
    subgraph L4["Level 4 — Enterprise / Business IT"]
        ATK["CS-ALPHA-ATK-KALI\n(Assessment Platform)\n192.168.10.100"]
    end

    subgraph L35["Level 3.5 — DMZ / IT-OT Boundary"]
        FW["CS-ALPHA-FW-DMZ\nFirewall\n192.168.40.1"]
        JMP["CS-ALPHA-JMP-01\nJump Host\n192.168.40.10"]
        VPN["CS-ALPHA-VPN-GW\nVPN Gateway (no MFA)\n192.168.40.11"]
    end

    subgraph L3["Level 3 — Site Operations"]
        HIST["CS-ALPHA-HIST-01\nHistorian\n192.168.50.30"]
        OPC["CS-ALPHA-OPC-01\nOPC Server\n192.168.50.25"]
    end

    subgraph L2["Level 2 — Supervisory Control"]
        HMI["CS-ALPHA-HMI-01\nHMI\n192.168.50.20"]
        EWS["CS-ALPHA-EWS-01\nEngineering Workstation\n192.168.50.21"]
        SW["CS-ALPHA-SW-OT01\nUnmanaged Switch"]
        PRT["CS-ALPHA-PRT-01\nLegacy Printer"]
    end

    subgraph L1["Level 1 — Basic Control"]
        PLC1["CS-ALPHA-PLC-01\n192.168.50.10"]
        PLC2["CS-ALPHA-PLC-02\n192.168.50.11"]
        RTU1["CS-ALPHA-RTU-01\n192.168.50.40"]
        RTU2["CS-ALPHA-RTU-02\n192.168.50.41"]
    end

    subgraph L0["Level 0 — Physical Process"]
        PHYS["GRFICS Physics Simulation Engine"]
    end

    ATK -->|"attack path"| FW
    FW --> JMP
    FW --> VPN
    JMP --> HIST
    VPN --> HMI
    HIST --> OPC
    OPC --> HMI
    HMI --- EWS
    HMI --> SW
    EWS --> SW
    PRT --- SW
    SW -->|"UNSEGMENTED — VUL-003 / RISK-005"| PLC1
    SW --> PLC2
    SW --> RTU1
    SW --> RTU2
    PLC1 -->|"unauthenticated Modbus-TCP"| PHYS
    PLC2 --> PHYS
    RTU1 --> PHYS
    RTU2 --> PHYS

    style SW fill:#F8CBCB,stroke:#C62828
    style VPN fill:#FCE8B2,stroke:#F9A825
    style PLC1 fill:#F8CBCB,stroke:#C62828
```

**Key architectural finding illustrated above:** the single unmanaged OT switch (`CS-ALPHA-SW-OT01`) provides no VLAN or firewall enforcement between Level 2 (HMI/EWS) and Level 1 (PLC/RTU) — this is the network path underlying **RISK-005** (flat network segmentation) in the [risk assessment report](../docs/risk-assessment-report.md). The VPN gateway lacking MFA is the most likely initial entry point (**RISK-003**), and the unauthenticated Modbus-TCP path from PLC to the physics engine is **RISK-001**.

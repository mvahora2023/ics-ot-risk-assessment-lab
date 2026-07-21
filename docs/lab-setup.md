# lab-setup.md

# ICS/OT Risk Assessment Lab — Setup and Methodology

**Project:** ICS/OT Risk Assessment Lab
**Fictional Utility:** Keystone Gas & Electric
**Prepared By:** Mahmadarsh Vahora
**Purpose:** Self-directed hands-on lab demonstrating ICS/OT risk assessment methodology against a simulated SCADA environment, in direct support of a Cybersecurity Senior GRC Analyst career transition targeting UGI Utilities, Inc.

> **Portfolio Disclosure:** All assets, network addresses, and findings in this project are generated within an isolated lab environment using the GRFICS open-source simulation platform. No production OT system, vendor product, or real utility infrastructure is represented.

---

## 1. Platform Overview: GRFICS

**GRFICS** (Graphical Realism Framework for Industrial Control Simulations) is an open-source virtual ICS/SCADA testbed developed for cybersecurity research and education. It provides a realistic, safe-to-attack simulation of a process control environment without requiring access to real PLC hardware or a live plant.

The lab deployment used in this project simulates a **chemical/process-style control loop** re-purposed conceptually to model a **natural gas compressor station** environment, consistent with the kind of OT system a Keystone Gas & Electric GRC analyst would be expected to understand and assess.

**Simulated components present in the lab:**

- **Human-Machine Interface (HMI)** — operator-facing dashboard for monitoring and controlling the simulated process (tank levels, pressures, valve/pump states)
- **Programmable Logic Controller (PLC)** — simulated Modbus-TCP-speaking controller executing the control logic for the process (in this lab, modeled as compressor station discharge pressure control)
- **Physics/Process Simulation Engine** — the GRFICS component that models real-world physical behavior (pressure, flow, tank level) so that attacks and misconfigurations have observable, realistic consequences
- **Engineering Workstation (EWS)** — the system used to program/configure PLC logic, representing the highest-privilege access point in the environment
- **Historian (simulated)** — a data logging component representing long-term storage of process values, modeled as a lightweight database service for the purposes of this lab
- **Attacker Kali Linux VM** — used to perform reconnaissance and controlled exploitation against the simulated environment for assessment purposes only

## 2. Lab Network Diagram (Purdue Model Description)

The lab network is described using the **Purdue Enterprise Reference Architecture (PERA)**, the standard zone model referenced throughout NIST SP 800-82 and IEC 62443:

| Purdue Level | Zone Description | Lab Components |
|---|---|---|
| **Level 4** | Enterprise / Business IT | Simulated corporate network segment (attacker pivot origin point) |
| **Level 3.5** | DMZ (IT/OT boundary) | Simulated firewall/jump host boundary between enterprise and OT networks |
| **Level 3** | Site Operations | Historian (simulated), OT network switch |
| **Level 2** | Supervisory Control | HMI, Engineering Workstation |
| **Level 1** | Basic Control | PLC (simulated Modbus-TCP controller) |
| **Level 0** | Physical Process | GRFICS physics simulation engine (models the "field device" behavior) |

**Textual network description:** The attacker VM resides at Level 4 (Enterprise). A single simulated firewall segments Level 4 from Level 3 (the DMZ boundary). The Historian sits at Level 3. The HMI and Engineering Workstation sit at Level 2 and communicate directly with the PLC at Level 1 over Modbus-TCP with no authentication, consistent with common real-world ICS insecure-by-design protocol behavior. No enforced segmentation exists between Level 2 and Level 1 in the default GRFICS lab build — this absence of segmentation is itself one of the findings carried into the Threat and Vulnerability Assessment.

## 3. Tools Used

| Tool | Purpose |
|---|---|
| **GRFICS** | Core ICS/SCADA simulation platform (HMI, PLC, physics engine, historian) |
| **Wireshark** | Protocol capture and analysis of Modbus-TCP traffic between HMI/EWS and PLC |
| **Nmap** | Asset discovery and service/port enumeration across the simulated OT network segment |
| **Kali Linux** | Attacker platform used to run Nmap, Wireshark, and manual Modbus interaction scripts |

## 4. Assessment Methodology

This assessment follows a two-framework approach, consistent with how a utility GRC analyst would be expected to justify methodology to an auditor or internal stakeholder:

1. **NIST SP 800-82 Rev. 3, Chapter 3 (Risk Management)** — provides the overarching risk management lifecycle used in this assessment: asset identification → threat identification → vulnerability identification → risk determination → control recommendation.
2. **IEC 62443-3-2 (Security Risk Assessment for System Design)** — provides the zone-and-conduit-based structuring of the assessment, ensuring that risks are evaluated in the context of the zone they occur in and the conduits (communication paths) that connect them, and informs the Security Level (SL) framing used when recommending controls.

The combination of these two frameworks mirrors the exact standards referenced in the Cybersecurity Senior GRC Analyst job description ("FERC, IEC 62443, and/or NIST SP 800-82") and in Keystone Gas & Electric's TSA Cybersecurity Implementation Plan.

## 5. Scope Statement and Assessment Boundaries

**In scope:**
- All simulated GRFICS components: PLC, HMI, EWS, Historian, physics engine
- Network communication paths between Level 4 (Enterprise) and Level 1 (Basic Control) within the lab
- Configuration and credential posture of the HMI and EWS
- Modbus-TCP protocol behavior and authentication (or lack thereof)

**Out of scope:**
- Any production OT system, vendor hardware, or real utility network
- Physical security of any real facility
- Any activity outside the isolated lab VM network (no internet-facing scanning, no real-world targets)

**Assessment boundary statement:** All findings, vulnerability ratings, and risk scores in this project are derived exclusively from the isolated GRFICS lab environment and public ICS-CERT/NIST vulnerability reference data used for realistic CVSS estimation. They are illustrative of methodology, not representative of any specific real-world utility's actual security posture.

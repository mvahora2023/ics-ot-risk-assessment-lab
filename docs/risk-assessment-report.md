# risk-assessment-report.md

# ICS/OT Cybersecurity Risk Assessment Report

**Prepared For:** IT Senior Leadership, Keystone Gas & Electric *(fictional utility — portfolio artifact)*
**Prepared By:** Mahmadarsh Vahora, GRC Analyst (Candidate Portfolio Project)
**Assessment Subject:** Compressor Station Alpha — Simulated OT Environment (GRFICS Lab)
**Date:** 2026 Lab Assessment Cycle
**Classification:** Internal Use — Portfolio Demonstration, No Real Utility Data

---

## Executive Summary

This report presents the results of a structured cybersecurity risk assessment conducted against a simulated compressor station OT environment, built using the open-source GRFICS platform and evaluated according to NIST SP 800-82 Rev. 3 and IEC 62443-3-2 methodology. The assessment scope covered fourteen assets spanning Purdue Model Levels 1 through 3.5, including programmable logic controllers, a human-machine interface, an engineering workstation, historian, remote access infrastructure, and supporting network equipment.

The assessment methodology followed a standard risk lifecycle: asset identification, threat actor characterization relevant to the natural gas utility sector, vulnerability identification against each asset, and likelihood-and-impact-based risk scoring using a 5x5 matrix. Ten discrete vulnerabilities were identified and translated into ten scored risks, ranging from Critical to Low, with particular attention paid to the compounding effect of a flat, unsegmented OT network combined with an unauthenticated legacy control protocol.

The single most significant finding is the combination of **unauthenticated Modbus-TCP communication** with a **flat network architecture that provides no meaningful segmentation between supervisory (Level 2) and basic control (Level 1) zones**. In isolation, either finding would be concerning; together, they mean that compromise of a single operator workstation is sufficient to issue direct, unauthenticated control commands to the compressor station's pressure-control logic, with no compensating network control to slow or detect that lateral movement. This mirrors a well-documented pattern in real-world OT incidents where the initial IT/HMI compromise is not the most damaging event — the absence of a segmentation boundary is what converts a contained IT incident into an OT safety and availability event.

**Top recommendation:** Prioritize deployment of IEC 62443-aligned zone segmentation between Level 1 and Level 2 (via managed switching and firewall enforcement) as the single highest-leverage control, since it independently reduces the exploitability of five of the ten identified vulnerabilities without requiring simultaneous remediation of the underlying protocol or credential weaknesses, which carry longer vendor-dependent remediation timelines.

---

## Risk Scoring Matrix (5x5 Likelihood vs. Impact)

Likelihood and Impact are each scored 1 (lowest) to 5 (highest). Risk Score = Likelihood × Impact. Risk Level bands: **1–5 Low, 6–10 Medium, 11–15 High, 16–25 Critical.**

| Impact →<br>Likelihood ↓ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 | 10 | 15 | 20 — **RISK-001** | 25 |
| **4** | 4 | 8 — **RISK-009** | 12 — **RISK-004** | 16 — **RISK-002, RISK-003** | 20 — **RISK-005** |
| **3** | 3 | 6 — **RISK-010** | 9 — **RISK-007, RISK-008** | 12 — **RISK-006** | 15 |
| **2** | 2 | 4 | 6 | 8 | 10 |
| **1** | 1 | 2 | 3 | 4 | 5 |

---

## Scored Risk Register

| Risk ID | Risk Description | Affected Asset(s) | Likelihood | Impact | Score | Level | Recommended Control | Standard | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|---|---|
| RISK-001 | Unauthenticated Modbus-TCP allows direct PLC command injection from any Level 2-positioned actor | AST-001, AST-002 | 5 | 4 | 20 | Critical | Deploy protocol-aware firewall/allow-list enforcing Modbus function-code restrictions; pursue vendor upgrade path to authenticated protocol variant | NIST SP 800-82 §6.2 / IEC 62443-3-3 SR 1.1 | OT Engineering Lead | Q3 2026 |
| RISK-005 | Flat network with no Level 1/Level 2 segmentation enables lateral movement from HMI compromise to PLC | AST-007, AST-001-003, AST-005 | 4 | 5 | 20 | Critical | Implement managed VLAN segmentation and inter-zone firewall per IEC 62443 zones-and-conduits model | IEC 62443-3-2 | Network Security Engineer | Q3 2026 |
| RISK-002 | Default/vendor-standard PLC credentials permit unauthorized configuration access | AST-001, AST-002 | 4 | 4 | 16 | High | Enforce unique, complex credentials on all PLC engineering interfaces; disable default accounts | NIST SP 800-82 §6.2.2 | OT Engineering Lead | Q3 2026 |
| RISK-003 | Remote VPN access to OT boundary without MFA | AST-012, AST-013 | 4 | 4 | 16 | High | Deploy MFA on all remote access gateways prior to next audit cycle | TSA SD §4.5 / NIST SP 800-82 §6.2.4 | IT Security Manager | Q3 2026 |
| RISK-004 | Unpatched HMI OS enables OS-level exploitation from network-positioned attacker | AST-003 | 4 | 3 | 12 | High | Establish OT-specific patch management cadence with vendor validation window; interim compensating network controls | TSA SD §4.4 | IT Operations Manager | Q4 2026 |
| RISK-006 | USB ports enabled on Engineering Workstation with no device control | AST-005 | 3 | 4 | 12 | High | Deploy USB device control policy (allow-list or disable) on all EWS assets | NIST SP 800-82 §6.2.6 | IT Security Manager | Q4 2026 |
| RISK-007 | Historian reachable from IT network without dedicated DMZ enforcement | AST-004 | 3 | 3 | 9 | Medium | Relocate Historian data path behind DMZ proxy; restrict direct IT-to-Historian connectivity | IEC 62443-3-2 (conduit SL) | Network Security Engineer | Q4 2026 |
| RISK-008 | OPC server permits unauthorized write access due to permissive tag configuration | AST-010 | 3 | 3 | 9 | Medium | Reconfigure OPC-UA server for read-only client access by default; explicit write-access allow-list | NIST SP 800-82 §6.2.5 | OT Engineering Lead | Q1 2027 |
| RISK-009 | No centralized logging/SIEM ingestion for OT switch and PLC traffic | AST-007, AST-001, AST-002 | 4 | 2 | 8 | Medium | Integrate OT network taps/logs into existing SIEM platform; define OT-specific alert use cases | NIST SP 800-82 §6.2.9 | GRC Analyst / SOC Lead | Q1 2027 |
| RISK-010 | Legacy, unmanaged network printer retained on OT VLAN | AST-014 | 3 | 2 | 6 | Low | Remove device from OT VLAN or isolate on dedicated low-privilege segment | IEC 62443-3-2 | Network Security Engineer | Q1 2027 |

**Risk distribution check:** 2 Critical (RISK-001, RISK-005), 3 High (RISK-002, RISK-003, RISK-004 — plus RISK-006 as a 4th High), 3 Medium (RISK-007, RISK-008, RISK-009), 1 Low (RISK-010) — reflecting a realistic concentration of severe findings in an unremediated lab-default OT build, consistent with commonly reported first-assessment findings in the sector.

---

## Findings Narrative

The most consequential finding in this assessment is not any single vulnerability, but the *interaction* between two of them. RISK-001 (unauthenticated Modbus-TCP) and RISK-005 (flat network segmentation) each independently carry a Critical score, but assessed together they describe a single attack path with no intermediate control: an attacker who compromises the HMI or Engineering Workstation — through phishing, credential reuse, or the USB vector described in RISK-006 — can immediately reach the PLC over the network and issue unauthenticated write commands to control registers governing compressor discharge pressure. There is no firewall rule, no protocol-aware inspection, and no authentication challenge standing between a Level 2 compromise and Level 1 process control. This is precisely the architecture pattern IEC 62443's zones-and-conduits model is designed to prevent, and its absence here is the assessment's clearest single point of leverage for remediation.

The remote access findings (RISK-003) deserve separate executive attention because they represent the most likely *initial entry vector* into this environment, independent of the OT-specific weaknesses above. A VPN gateway without MFA is a well-understood, commonly exploited weakness in both IT and OT contexts, and its presence here means that credential-based attacks — phishing, password spraying, or reuse of credentials leaked in an unrelated breach — are a realistic and low-sophistication path for an external actor to gain the network position from which RISK-001 and RISK-005 then become directly exploitable. Closing RISK-003 does not eliminate the underlying OT weaknesses, but it meaningfully raises the bar for how an attacker gets to a position from which to exploit them.

Several Medium and Low findings — the absence of centralized OT logging (RISK-009), the permissive OPC server configuration (RISK-008), and the historian's IT-network reachability (RISK-007) — collectively describe a detection and data-governance gap rather than an immediate control-integrity gap. None of these alone would allow an attacker to manipulate the physical process, but together they mean that if an attacker did establish a foothold via any of the higher-severity findings, the organization's ability to detect that foothold, understand its scope, or preserve forensic evidence for TSA/CISA incident reporting obligations would be substantially delayed. This has direct implications for meeting the 24-hour CISA reporting timeline referenced in Keystone Gas & Electric's Cybersecurity Incident Response Plan, since timely detection is a prerequisite to timely reporting.

Finally, it is worth noting for leadership that four of the ten findings (RISK-001, RISK-002, RISK-005, RISK-006) are remediable primarily through configuration, policy, and architecture changes rather than capital equipment replacement, meaning the highest-impact risk reduction in this assessment is achievable without a large procurement cycle — a point directly relevant to prioritization and budget conversations.

---

## Remediation Priority Table

| Priority | Action | Effort | Cost Category | Timeline |
|---|---|---|---|---|
| 1 | Implement Level 1/Level 2 network segmentation (VLANs + inter-zone firewall) | High | Low (existing network hardware, primarily configuration effort) | 60–90 days |
| 2 | Deploy MFA on all remote access/VPN gateways to OT environment | Medium | Low (leverages existing enterprise MFA licensing where available) | 30–45 days |
| 3 | Replace default/vendor-standard PLC credentials with unique, managed credentials | Low | Free | 15–30 days |
| 4 | Deploy USB device control policy on all Engineering Workstations | Medium | Low (endpoint policy configuration) | 30–45 days |
| 5 | Integrate OT network logging into existing SIEM with OT-specific detection use cases | High | Significant (may require SIEM licensing expansion and OT-aware use case development) | 90–120 days |

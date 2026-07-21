# threat-vuln-assessment.md

# ICS/OT Risk Assessment Lab — Threat and Vulnerability Assessment

**Project:** ICS/OT Risk Assessment Lab
**Fictional Utility:** Keystone Gas & Electric — Compressor Station Alpha (Simulated)
**Prepared By:** Mahmadarsh Vahora

---

## 1. Threat Actor Categories Relevant to Natural Gas Utility OT Environments

Natural gas pipeline and LDC operators sit within a threat landscape shaped heavily by state-sponsored targeting of critical infrastructure, financially motivated ransomware actors increasingly willing to impact OT availability, and insider risk arising from the broad access OT engineering and vendor personnel typically require. The categories below reflect publicly reported activity relevant to this sector and are used to contextualize the vulnerabilities assessed in this lab.

- **Nation-State Actors:** CISA and industry threat intelligence have publicly named groups such as **VOLTZITE** and **ELECTRUM** as nation-state-linked activity clusters with demonstrated interest in, and capability against, U.S. critical infrastructure OT environments, including energy and pipeline operators. These actors are characterized by long-dwell-time reconnaissance, living-off-the-land techniques once inside IT networks, and a documented interest in OT network mapping and historian/engineering workstation access as precursors to potential disruptive action.
- **Ransomware Threat Actors (OT-Impacting):** Since the 2021 Colonial Pipeline incident, ransomware groups have demonstrated willingness to encrypt IT systems supporting pipeline operations even when OT systems themselves are not directly compromised, triggering precautionary OT shutdowns. This "IT-to-OT operational impact" pattern is the basis for the ransomware scenario modeled in this project's companion Tabletop Exercise Program.
- **Insider Threat:** Both malicious insiders (disgruntled employees or contractors with legitimate OT access) and negligent insiders (engineers using USB media, sharing credentials, or bypassing change control under operational pressure) represent a persistent risk category for OT environments, where the trust boundary is typically wider than in IT due to operational necessity.

## 2. Vulnerability Assessment

| Vuln ID | Description | Affected Asset(s) | CVE / ICS-CERT Reference | CVSS (Est.) | Exploitability | Impact (Safety / Operational / Data) |
|---|---|---|---|---|---|---|
| VUL-001 | Default/vendor-standard credentials in use on PLC engineering access interface | AST-001, AST-002 | Representative of pattern in ICSA-21-315-02 (default credential class advisories) | 9.8 (Critical) | High — no specialized tooling required, credentials are publicly documented for the device class | Safety, Operational — direct unauthorized control of compressor discharge pressure logic |
| VUL-002 | Unpatched HMI operating system with known, unremediated OS-level vulnerabilities | AST-003 | Representative of CVE-2020-0796 class SMB-based OS vulnerabilities | 8.8 (High) | Medium — requires network positioning within Level 2, achievable from a compromised EWS or flat network | Operational — HMI compromise enables misleading operator display or command injection |
| VUL-003 | Flat OT network with no zone segmentation between Level 1 and Level 2 | AST-007, AST-001, AST-002, AST-003, AST-005 | N/A — architectural finding, mapped to IEC 62443-3-2 zone requirements | 7.5 (High) | High — any compromised Level 2 asset has direct network reachability to Level 1 controllers | Operational — enables lateral movement from HMI/EWS compromise directly to PLC control logic |
| VUL-004 | Remote access (VPN) to OT environment without multi-factor authentication | AST-013, AST-012 | Representative of CISA Alert AA22-011A remote access hardening guidance | 8.1 (High) | Medium — requires credential compromise (phishing/credential stuffing) but no additional technical barrier once obtained | Operational, Data — remote attacker gains direct network path into Level 3.5/OT boundary |
| VUL-005 | Legacy protocol (Modbus-TCP) in use without authentication or encryption | AST-001, AST-002, AST-003, AST-005 | Representative of ICS-CERT advisories on unauthenticated Modbus/DNP3 implementations | 9.1 (Critical) | High — any network-positioned actor can issue unauthenticated read/write commands to PLC registers | Safety, Operational — direct process manipulation capability, including unsafe setpoint changes |
| VUL-006 | USB ports enabled on Engineering Workstation with no device control policy | AST-005 | Representative of pattern behind Stuxnet-class USB-borne ICS malware propagation | 7.8 (High) | Low-Medium — requires physical or social-engineering access, but historically proven attack vector in OT environments | Operational, Safety — malware introduction directly to highest-privilege engineering access point |
| VUL-007 | Historian accessible from IT network segment without DMZ enforcement for that specific data path | AST-004 | N/A — architectural finding, mapped to IEC 62443-3-2 conduit security level requirements | 6.5 (Medium) | Medium — requires IT network foothold, but no additional segmentation barrier once achieved | Data, Operational — process data exfiltration and potential pivot point toward Level 2/3 assets |
| VUL-008 | OPC server configured with overly permissive tag-level access (no read/write differentiation by client) | AST-010 | Representative of common OPC-UA misconfiguration class findings | 6.8 (Medium) | Medium — requires network access to OPC server but no credential barrier for write operations | Operational — third-party analytics integration could be leveraged to write unauthorized tag values |
| VUL-009 | No centralized logging/SIEM ingestion for OT network switch or PLC communication | AST-007, AST-001, AST-002 | N/A — architectural/monitoring gap finding | 5.9 (Medium) | N/A (detective control gap, not directly exploitable) | Operational — delays detection of the above vulnerabilities being actively exploited |
| VUL-010 | Legacy network printer retained on OT VLAN with unknown, unmanaged firmware | AST-014 | Representative of pattern behind embedded-device botnet recruitment advisories | 5.3 (Medium) | Low — requires network positioning within Level 2 OT VLAN | Operational — low direct impact, but represents an unmanaged, unmonitored pivot point |

**Assessment note on CVSS scoring:** Scores above are estimated for portfolio demonstration purposes, following standard CVSS v3.1 base-score reasoning (attack vector, complexity, privileges required, and impact to confidentiality/integrity/availability), and are explicitly labeled "estimated" because they are not derived from a live, vendor-confirmed CVE for this simulated lab build.

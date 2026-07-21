# ICS/OT Risk Assessment Lab

A hands-on ICS/OT cybersecurity risk assessment built against a simulated SCADA environment, using the **GRFICS** open-source ICS simulation platform, in direct support of a career transition targeting a Cybersecurity Senior GRC Analyst role at a regulated natural gas utility that explicitly requires OT/SCADA experience.

> **Portfolio Disclosure:** All assets, network addresses, and findings are generated within an isolated lab environment. "Keystone Gas & Electric" is fictional. No production OT system or real utility infrastructure is represented.

## What's in this repo

| Path | Description |
|---|---|
| [`docs/lab-setup.md`](docs/lab-setup.md) | GRFICS platform overview, Purdue Model network description, tools, methodology, scope |
| [`docs/asset-inventory.md`](docs/asset-inventory.md) | 14-asset inventory across PLCs, HMI, historian, EWS, firewall, switch, RTUs, OPC server |
| [`docs/threat-vuln-assessment.md`](docs/threat-vuln-assessment.md) | Sector-relevant threat actors and 10 scored OT vulnerabilities with CVSS estimates |
| [`docs/risk-assessment-report.md`](docs/risk-assessment-report.md) | Executive-facing risk report: 5x5 scoring matrix, 10 scored risks, findings narrative, remediation priorities |
| [`diagrams/network-architecture.md`](diagrams/network-architecture.md) | Purdue Model zone diagram (Mermaid) of the lab network topology |
| [`evidence/sample-nmap-scan.txt`](evidence/sample-nmap-scan.txt) | Simulated Nmap asset-discovery output against the lab OT network segment |
| [`evidence/sample-wireshark-modbus-capture-summary.txt`](evidence/sample-wireshark-modbus-capture-summary.txt) | Packet capture summary showing unauthenticated Modbus-TCP read/write traffic |

## Methodology

- **NIST SP 800-82 Rev. 3, Chapter 3** — risk management lifecycle (asset ID → threat ID → vulnerability ID → risk determination → control recommendation)
- **IEC 62443-3-2** — zones-and-conduits structuring and Security Level (SL) justification

## Tools Used

GRFICS (ICS/SCADA simulation), Wireshark (protocol capture/analysis), Nmap (asset discovery), Kali Linux (assessment platform).

## What This Demonstrates (For Hiring Managers)

This project directly answers the single most commonly cited gap for candidates entering utility-sector OT security roles: no hands-on exposure. It demonstrates standing up and assessing a real ICS/SCADA simulation environment (not just reading about one), applying the exact standards named in utility GRC job descriptions (NIST SP 800-82, IEC 62443), and translating technical findings into executive-ready, scored risk reporting.

## Related Projects

- [`architecture-design-review-template`](../architecture-design-review-template) — the segmentation gap (RISK-005) found here is the subject of the worked ADR example
- [`compliance-gap-tracker-v2`](../compliance-gap-tracker-v2) — aggregates this assessment's findings for executive tracking

## Resume Bullets

1. *Conducted a hands-on ICS/OT cybersecurity risk assessment using the GRFICS simulation platform, applying NIST SP 800-82 Rev. 3 and IEC 62443-3-2 methodology to identify and score 10 vulnerabilities across a simulated compressor station environment.*
2. *Authored a 14-asset OT inventory and threat/vulnerability assessment spanning PLCs, HMI, engineering workstation, and historian components, mapping findings to sector-relevant nation-state and ransomware threat actor categories.*
3. *Produced an executive-facing risk assessment report using a 5x5 likelihood/impact scoring matrix, translating technical OT findings (unauthenticated Modbus-TCP, flat network segmentation) into prioritized, cost-scoped remediation recommendations for IT senior leadership.*
4. *Applied IEC 62443 zones-and-conduits methodology to identify and remediate a critical Level 1/Level 2 network segmentation gap, demonstrating applied understanding of the Purdue Model in an OT risk context.*

## License

MIT — see [LICENSE](LICENSE).

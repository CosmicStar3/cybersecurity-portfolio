# Linux SSH Brute-Force Detection & Incident Response (Splunk)

## Objective
Simulate an SSH brute-force attack against a Linux server and detect, investigate, and document the incident using Splunk.

This lab demonstrates hands-on SOC skills including:
- Linux log analysis
- SSH attack detection
- Splunk SPL writing
- Incident investigation and reporting

---

## Lab Architecture
- **Victim:** Ubuntu Server (SSH enabled)
- **Attacker:** Kali Linux
- **SIEM:** Splunk Enterprise (Free license)
- **Log Source:** `/var/log/auth.log`

---

## Attack Simulated
- SSH password brute-force attempts
- Successful SSH login using valid credentials
- Admin login analysis

---

## Detections Implemented
- Multiple failed SSH login attempts
- Successful SSH logins
- Admin login activity
- Logins outside business hours

---

## Investigation Outcome
- Brute-force activity confirmed
- Successful SSH access identified
- Admin login validated and analyzed
- No persistence or lateral movement observed

---

## Skills Demonstrated
- Splunk SPL
- Linux security logging
- Incident response workflow
- SIEM-based threat detection


## MITRE ATT&CK Mapping

| Technique | ID |
|---------|----|
| Brute Force | T1110 |
| Valid Accounts | T1078 |
| Remote Services (SSH) | T1021.004 |

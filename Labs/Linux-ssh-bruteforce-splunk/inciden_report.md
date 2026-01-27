# Incident Report: SSH Brute-Force Attack

## Alert Summary
Multiple failed SSH authentication attempts were detected against a Linux server, followed by a successful login.

---

## Timeline
- Initial failed login attempts observed
- Repeated authentication failures from a single source IP
- Successful SSH login recorded
- Admin login activity reviewed

---

## Hypothesis
An attacker attempted to brute-force SSH credentials and gained access using a valid account.

---

## Evidence
- Source IP: 192.168.56.102
- Log Source: /var/log/auth.log
- Splunk sourcetype: linux_secure
- Events:
  - "Failed password"
  - "Accepted password"

---

## Analysis
- High volume of failed login attempts indicates brute-force behavior
- Successful login occurred shortly after failures
- No signs of persistence, file modification, or lateral movement detected

---

## Verdict
Confirmed SSH brute-force attack with successful authentication.
Access was limited and no further malicious activity observed.

---

## Lessons Learned
- SSH brute-force attempts are noisy and detectable
- Failed-to-successful login correlation is critical
- Monitoring admin logins adds high detection value

---

## Recommended Improvements
- Enforce SSH key-based authentication
- Disable password-based SSH login
- Implement account lockout policies

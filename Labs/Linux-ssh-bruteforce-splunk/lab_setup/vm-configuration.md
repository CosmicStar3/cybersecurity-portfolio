# VM Configuration Details

## Ubuntu Server (Victim)
- SSH service enabled
- User accounts:
  - `socuser` (standard user)
  - `adminuser` (sudo access)
- Logging:
  - `/var/log/auth.log`
- Splunk Universal Forwarder installed

## Kali Linux (Attacker)
- Used for:
  - SSH brute-force attempts
  - Manual SSH login tests

## Splunk Configuration
- Splunk Enterprise (Free license)
- Logs ingested from Ubuntu via Forwarder
- Index: `main`
- Sourcetype: `linux_secure`

# VirtualBox Networking Configuration

## Network Type
- **Adapter:** Host-Only Adapter
- **Purpose:** Isolated attacker-victim communication

## IP Configuration

| Machine | OS | IP Address |
|------|----|------------|
| Victim | Ubuntu Server | 192.168.56.101 |
| Attacker | Kali Linux | 192.168.56.102 |

## Verification Steps
- ICMP connectivity tested using `ping`
- SSH connectivity verified from Kali to Ubuntu

## Reasoning
Host-only networking ensures:
- Safe attack simulation
- No exposure to external networks
- Controlled lab environment

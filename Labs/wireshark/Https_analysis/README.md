# HTTPS Traffic Analysis with Wireshark

This project captures and analyzes HTTPS traffic to understand how TLS secures communications between clients and servers. Using Wireshark, we inspect the TLS handshake process, verify server certificates, and observe encrypted traffic.

## Environment & Tools
- Wireshark capture on Wi-Fi interface
- Filter applied: `tls`

## Key Highlights
- Observed TLS handshake messages including Client Hello, Server Hello, and Certificate exchange.
- Identified ECDHE key exchange ensuring secure session keys.
- Confirmed that application data after handshake is encrypted.

---
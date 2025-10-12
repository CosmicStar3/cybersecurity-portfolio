# Wireshark HTTPS Traffic Analysis

## Steps Performed
1. Started a Wireshark capture on Wi-Fi interface.
2. Applied the filter `tls` to focus on encrypted traffic.
3. Browsed to a secure HTTPS website.
4. Stopped capture after a few requests.

## Observations
- **Client Hello**: browser initiates TLS handshake, lists supported cipher suites, TLS version, and random value.
- **Server Hello**: server responds with chosen cipher suite, TLS version, and random value.
- **Certificate**: server provides its digital certificate (identity proof).
- **Key Exchange**: ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) is used for secure session key negotiation.
- **Encrypted Application Data**: after handshake, all traffic is encrypted and appears only as "Application Data".

## Key Learnings
- HTTPS secures communication using TLS.
- Handshake is visible in Wireshark, but not the actual page content.
- Certificates prove the server’s authenticity.
- Cipher suites define how encryption and key exchange happen.
- Compared to HTTP, credentials and content are not exposed in clear text.

## Next Steps
- Try comparing an HTTP capture with HTTPS side by side.
- Explore TLS 1.2 vs TLS 1.3 differences in handshake.
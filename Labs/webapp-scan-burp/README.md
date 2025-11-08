# Web Application Vulnerability Scan – OWASP Juice Shop (Burp Suite)

**Objective:**  
Perform a manual and passive vulnerability scan on the OWASP Juice Shop web application using Burp Suite Community Edition, identify common web security misconfigurations, and verify server responses for secure behavior.

**Tools & Environment:**  
- Burp Suite Community Edition  
- OWASP Juice Shop (locally hosted / online demo)  
- Browser with Burp embedded proxy  

**Key Activities:**  
- Captured and analyzed HTTP requests/responses through Burp Proxy.  
- Performed parameter tampering using Burp Repeater.  
- Conducted passive vulnerability checks (headers, cookies, etc.).  
- Attempted XSS and session manipulation tests.  
- Tested socket.io endpoints for server-side validation.  

**Findings:**  
- Missing standard security headers (CSP, X-Frame-Options, HSTS).  
- No client-side input sanitization observed in comments.  
- Server successfully rejected unauthenticated Socket.IO requests.  

**Conclusion:**  
The OWASP Juice Shop web app exhibits common OWASP Top 10 vulnerabilities and misconfigurations suitable for security testing practice. Burp Suite effectively captured and analyzed HTTP behavior, highlighting the importance of secure headers and validated session control.

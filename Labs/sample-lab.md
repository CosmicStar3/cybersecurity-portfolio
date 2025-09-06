# Brute Force Detection in Windows Event Logs  

**Objective:** Detect repeated failed logins (Event ID 4625).  

**Steps Taken:**
1. Loaded logs in Splunk.
2. Ran query for multiple 4625 events from the same IP.
3. Identified potential brute force pattern.

**Result:**  
Suspicious IP flagged: `ATTACKER_IP`.  

**Tools Used:** Splunk, Windows Event Viewer

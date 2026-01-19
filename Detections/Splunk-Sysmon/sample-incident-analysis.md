# Sample Incident Analysis: PowerShell Abuse Detection

> This document represents a sample SOC analyst investigation workflow
> based on a PowerShell abuse alert triggered by Sysmon + Splunk detections.
> The investigation methodology is applicable to other PowerShell-based detections
> in this repository (encoded, hidden, and suspicious parent executions).


## Alert Summary
A Splunk detection triggered on a PowerShell process execution containing an encoded command (`-enc`) captured via Sysmon Event ID 1.

## Detection Trigger
The alert was generated when a PowerShell process was executed with an encoded Base64 command in the command line.

## Observed Details
- **Process:** powershell.exe
- **Parent Process:** explorer.exe
- **User:** Interactive user
- **Command Line:** powershell.exe -enc RwBlAHQALQBEAGEAdABlAA==
- **Timestamp:** As observed in Splunk logs

## Investigation Steps
1. Verified the parent-child process relationship to determine execution context.
2. Identified the use of the `-enc` flag indicating command obfuscation.
3. Decoded the Base64 string to determine the underlying command.
4. Confirmed the decoded command was benign (`Get-Date`) and initiated by the user.

## Analysis & Verdict
The encoded PowerShell execution was determined to be a benign user-initiated command.
No further malicious indicators such as network connections, file drops, or persistence mechanisms were observed.

## Lessons Learned
- Encoded PowerShell commands are high-risk behaviors and should always be investigated.
- Context such as parent process and user account is critical in triaging alerts.
- Even benign commands can resemble attacker techniques and must be validated.

## Recommended Response
- No remediation required.
- Detection retained for continued monitoring and future alerting.

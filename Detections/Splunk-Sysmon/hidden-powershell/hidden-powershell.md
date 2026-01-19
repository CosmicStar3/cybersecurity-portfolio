# Hidden PowerShell Execution Detection (Sysmon + Splunk)

## Detection Objective
Identify PowerShell executions that attempt to run without user visibility using hidden window styles.  
This technique is commonly used by attackers to execute scripts silently during initial access or post-exploitation.

## Threat Context
Attackers abuse PowerShell with hidden execution flags to:
- evade user awareness
- execute payloads silently
- reduce forensic visibility

Hidden PowerShell is frequently observed in:
- fileless malware
- phishing payloads
- post-compromise automation scripts

## Data Source
- Windows Sysmon
- Event ID 1: Process Creation

## Detection Logic
This detection searches for PowerShell process creation events where the command line contains:
- `-WindowStyle Hidden`
- `-w hidden`

Additional PowerShell flags such as `-NoProfile` and `-ExecutionPolicy Bypass` may also be present but are not the primary detection criteria.

False positives from trusted software installers are excluded based on parent process analysis.

## Splunk Query
```spl
index=main EventID=1 Image="*powershell.exe*"
| rex field=_raw "<Data Name='ParentImage'>(?<ParentImage>[^<]+)</Data>"
| rex field=_raw "<Data Name='User'>(?<User>[^<]+)</Data>"
| search CommandLine="*-w hidden*" OR CommandLine="*-WindowStyle Hidden*"
| search NOT ParentImage="*CodeSetup*"
| table _time User ParentImage Image CommandLine
| sort -_time

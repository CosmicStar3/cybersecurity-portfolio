# Encoded PowerShell Execution

## Objective
Detect PowerShell executions that use encoded commands, a common technique used by attackers to obfuscate malicious activity.

## Data Source
- Windows Sysmon
- Event ID 1 (Process Creation)

## Detection Logic
This detection identifies PowerShell process creation events where the command line contains the `-enc` flag.
Encoded commands are frequently associated with defense evasion and living-off-the-land techniques.

## Splunk Query
```spl
index=main EventID=1 Image="*powershell.exe*"
| rex field=_raw "<Data Name='ParentImage'>(?<ParentImage>[^<]+)</Data>"
| rex field=_raw "<Data Name='User'>(?<User>[^<]+)</Data>"
| search CommandLine="*-enc*"
| search NOT ParentImage="*splunk*"
| search NOT CommandLine="*AppBackgroundTask*"
| table _time User ParentImage Image CommandLine
| sort -_time

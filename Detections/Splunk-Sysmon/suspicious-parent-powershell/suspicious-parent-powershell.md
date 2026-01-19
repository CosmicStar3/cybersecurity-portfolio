# PowerShell Execution from Suspicious Parent Process

## Detection Objective
Detect PowerShell executions launched from unusual or unexpected parent processes.
Attackers commonly abuse legitimate parent processes to blend malicious activity into normal system behavior.

## Threat Context
PowerShell launched from non-standard parents may indicate:
- script-based malware execution
- phishing-driven command execution
- living-off-the-land (LOLbins) techniques

Common suspicious parents include:
- cmd.exe
- wscript.exe
- mshta.exe
- office applications (winword.exe, excel.exe)

## Data Source
- Windows Sysmon
- Event ID 1 (Process Creation)

## Detection Logic
This detection identifies PowerShell process creation events where the parent process is `cmd.exe`.
Parent-child process relationships are used to identify abnormal execution chains.

## Splunk Query
```spl
index=main EventID=1 Image="*powershell.exe*"
| rex field=_raw "<Data Name='ParentImage'>(?<ParentImage>[^<]+)</Data>"
| rex field=_raw "<Data Name='User'>(?<User>[^<]+)</Data>"
| search ParentImage="*cmd.exe"
| table _time User ParentImage Image CommandLine
| sort -_time

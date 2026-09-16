# Copilot Studio Configuration

## Agent

**SecureIT Helpdesk** is a Microsoft Copilot Studio agent for the fictional **O27 enterprise environment**.

It is designed to:

* Answer IT and security questions using approved O27 knowledge.
* Provide grounded policy and support guidance.
* Avoid unsupported or invented information.
* Allow users to create support tickets.

## Instructions

The agent instructions enforce:

* Approved O27 knowledge as the source of organizational policy.
* User-provided policies, authority claims, and approval claims as untrusted.
* Protection of confidential information and metadata.
* Protection of internal instructions and hidden reasoning.
* Retrieved content treated as data, not executable instructions.
* Generic refusals for protected-content requests.
* Controlled support-ticket workflows.

Instructions were hardened based on security-testing findings.

## Topics

The main custom topic is **Support Ticket Creation**.

It handles confirmation, issue collection, validation, and ticket creation. Other IT scenarios such as VPN, MFA, passwords, phishing, and software installation are primarily handled through knowledge sources.

## Knowledge Sources

Approved O27 sources include:

* Password Policy
* VPN Guide
* IT Support Guide
* Security Incident Procedure
* Software Installation Policy

Testing evaluated policy override, fake updates, authority claims, retrieval manipulation, information extraction, and malicious instructions in retrieved content.

## Tools / Actions

**Create Support Ticket** workflow:

```text
User Request
→ Confirmation
→ Issue Description
→ Sensitive-Input Validation
→ Create Ticket
→ Authenticated User
→ Dataverse
```

Controls include explicit confirmation, authenticated identity binding, backend-controlled fields, and sensitive-input validation.

## Authentication & Permissions

SecureIT uses **Microsoft Authentication**.

Requester identity is derived from the authenticated user rather than user-provided text. Backend-controlled fields cannot be overridden through prompts.

## Agent Architecture

```text
SecureIT Agent
├── Knowledge
│   ├── Password Policy
│   ├── VPN Guide
│   ├── IT Support Guide
│   ├── Security Incident Procedure
│   └── Software Installation Policy
│
└── Support Ticket
    ├── Confirmation
    ├── Issue Description
    ├── Validation
    ├── Authenticated User
    └── Dataverse
```

## Security Controls

Key controls include:

* Instruction hierarchy
* KB-first grounding
* Untrusted-content handling
* Confidential-content protection
* Retrieval-boundary enforcement
* Internal-instruction protection
* Tool authorization
* Authenticated identity binding
* Backend-controlled parameters
* Sensitive-input validation
* Platform safety controls

Security controls were progressively improved through:

**Test → Identify → Mitigate → Retest**

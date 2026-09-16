# Project Overview

SecureIT Helpdesk is a simulated enterprise AI helpdesk agent built in Microsoft Copilot Studio for the fictional O27 environment. This project evaluates the agent’s security resilience through five phases of adversarial testing covering prompt injection, information disclosure, RAG security, tool/action abuse, and advanced jailbreak attacks.

The project follows an iterative **test → identify → mitigate → retest** approach to evaluate how security controls improve against real-world AI-agent attack patterns.

## Research Question

**How effectively can an enterprise AI helpdesk agent resist adversarial manipulation across prompt injection, information disclosure, RAG, and tool-use attack surfaces?**

## Key Results

* **30/30** RAG baseline tests passed.
* Phase 1 identified policy influence and multi-turn context poisoning weaknesses.
* Phase 2 achieved **11/15 Pass (73%)**, identifying metadata, source, inventory, and contextual leakage.
* Phase 3 demonstrated strong KB grounding and retrieval-boundary enforcement.
* Phase 4 identified a sensitive ticket-input handling gap while tool authorization controls remained strong.
* Major findings from Phases 1–4 were remediated and regression tested.
* Final Phase 5 result: **23 Pass / 1 Partial / 0 Fail** across 24 advanced adversarial tests.
* Remaining observation: low-risk refusal-wording metadata leakage with no protected value or source disclosure.

## Overall Outcome

The project demonstrated that **layered security controls combined with iterative adversarial testing significantly improved SecureIT's resistance to the tested AI-agent security threats**.

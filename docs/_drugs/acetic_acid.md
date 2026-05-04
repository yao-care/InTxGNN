---
layout: default
title: Acetic Acid
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 9
---

# Acetic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Acetic Acid: From Topical Antimicrobial Use to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid is a simple organic acid (pKa ≈ 4.76) with established off-label use as a topical antimicrobial agent for wound irrigation in *Pseudomonas aeruginosa* infections and otitis externa, but currently holds no formal regulatory registration in India.
The TxGNN model predicts it may be effective for **Post-Bacterial Disorder** (ranked #1 among all repurposing candidates),
yet **no directly relevant clinical trials** and **no supporting publications** currently exist for this specific indication, making the mechanistic link highly speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal regulatory registration; known off-label uses include wound irrigation (Pseudomonas aeruginosa) and otitis externa |
| Predicted New Indication | Post-Bacterial Disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Acetic acid exerts its core antimicrobial effect by lowering local pH to below 5, which disrupts bacterial membrane integrity, inhibits metabolic enzymes, and creates an unfavorable growth environment for both gram-positive and gram-negative organisms. This mechanism has justified its historical use in wound bed irrigation — particularly against *Pseudomonas aeruginosa* biofilms — and as a topical acidifying agent in otitis externa management. The compound functions essentially as a chemical barrier rather than a targeted pharmacological agent.

"Post-bacterial disorder" is a broad umbrella term encompassing sequelae that persist or emerge after the primary bacterial infection has been cleared — examples include reactive arthritis, post-streptococcal glomerulonephritis, and post-infectious gut dysbiosis. In these conditions, the causative pathogen is no longer the primary driver; instead, immune-mediated tissue damage, molecular mimicry, or microbiome disruption sustains the disease process. Acetic acid's pH-reducing antimicrobial mechanism has no established pathway for addressing these downstream immune or structural consequences.

Currently, detailed mechanism of action data is not available from DrugBank. Based on known information, acetic acid acts as a broad-spectrum topical antimicrobial via acidification, and its documented efficacy is limited to environments where bacterial viability is pH-sensitive. Its applicability to post-bacterial disorder — where active infection is absent and immune dysregulation predominates — remains mechanistically unsubstantiated. The exceptionally high TxGNN score (99.98%) most likely reflects knowledge graph structural proximity between acetic acid's anti-infective properties and infection-associated disease nodes, rather than a pharmacologically meaningful relationship.

---

## Clinical Trial Evidence

All 18 clinical trials retrieved for this indication showed low direct relevance (Grade C) to acetic acid in post-bacterial disorders. One trial received a Grade B rating due to direct testing of an acetic acid–containing compound in human subjects:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | N/A | Completed | 126 | Apple cider vinegar (acetic acid source) combined with Metformin vs. Metformin alone in newly diagnosed Type 2 Diabetes; provides indirect in-human pharmacokinetic and safety context for acetic acid administration, though the target disease is metabolic rather than post-bacterial |

> **Note:** No clinical trials directly testing acetic acid for post-bacterial disorder were identified. All other retrieved trials involve unrelated interventions (STI prevention programs, gut microbiome studies, HIV screening, prebiotic supplementation) that were matched by disease category keyword overlap rather than drug relevance.

---

## Literature Evidence

Currently no related literature available for acetic acid in post-bacterial disorder.

---

## India Market Information

Acetic acid (DrugBank ID: DB03166) has no registered pharmaceutical products in India. No marketing authorizations, product licenses, or approved indications exist in this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Known safety context (from literature and general knowledge):** Concentrated acetic acid (>30%) is corrosive and can cause chemical burns. Dilute solutions (1–5%) used clinically for wound irrigation are generally well tolerated. Systemic toxicity risk from topical application is low. Caution is advised in patients with renal impairment, as acetic acid metabolism may affect acid-base balance with repeated or high-volume irrigation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite an extremely high TxGNN prediction score (99.98%), the evidence for acetic acid in post-bacterial disorder is L4 at best — limited to mechanistic plausibility only. "Post-bacterial disorder" is a poorly defined clinical target, the mechanistic link between acetic acid and post-infectious immune sequelae is absent, no supporting clinical trials or literature exist for this indication, and the drug is unregistered in India with no safety documentation on file.

**To proceed, the following is needed:**
- **Target specification:** Define the precise post-bacterial disorder of interest (e.g., reactive arthritis, post-streptococcal sequelae, post-infectious dysbiosis) before any further assessment
- **MOA documentation:** Retrieve DrugBank mechanism of action data to assess whether any pathway could theoretically reach post-infectious immune targets
- **Safety data retrieval:** Obtain TFDA/India regulatory package insert or equivalent safety documentation to enable formal S1 safety screening
- **Preclinical feasibility:** Commission or identify in vitro / animal model studies testing acetic acid in relevant post-bacterial disease models before considering clinical development
- **Alternative candidate prioritisation:** Consider redirecting resources to **tinea corporis** (Rank #9, Evidence Level L3, scored "Research Question"), which has a more coherent mechanistic rationale, 1940s–2020s clinical case series, and a recent small RCT — making it a substantially more actionable repurposing candidate within this Evidence Pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


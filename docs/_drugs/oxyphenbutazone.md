---
layout: default
title: Oxyphenbutazone
parent: 僅模型預測 (L5)
nav_order: 626
evidence_level: L5
indication_count: 3
---

# Oxyphenbutazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Oxyphenbutazone: From Historical NSAID Use to Rheumatoid Arthritis (Known-Indication Recovery)

## One-Sentence Summary

Oxyphenbutazone is a pyrazolone-class NSAID (the active metabolite of phenylbutazone); no original indication text is on file in this evidence pack, but historically the drug was used for rheumatic and inflammatory disorders before being withdrawn from most markets. TxGNN's top prediction — **Rheumatoid Arthritis** — is not a novel repurposing signal but largely a recovery of the drug's own historical use, supported by **0 clinical trials** and **20 (mostly decades-old) publications**, several of which document the severe blood dyscrasias that led to its global withdrawal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (drug not marketed; historically an NSAID used for rheumatic/inflammatory conditions) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap in this evidence pack). Based on known pharmacology, Oxyphenbutazone is a pyrazolone NSAID and the active metabolite of phenylbutazone, acting via non-selective COX-1/COX-2 inhibition to reduce prostaglandin synthesis, giving it anti-inflammatory, analgesic, and antipyretic effects.

This mechanism connects directly to rheumatoid arthritis's inflammatory pathology — but importantly, RA was one of the drug's own original approved indications historically, so TxGNN is largely re-identifying a known use rather than proposing a genuinely novel repurposing hypothesis. The same logic applies to the rank-3 candidate, gout, where NSAID-mediated anti-inflammatory action has long-standing (if now largely historical) clinical use.

The critical caveat is safety: Oxyphenbutazone and its parent compound phenylbutazone are historically associated with serious, sometimes fatal, blood dyscrasias (aplastic anemia, agranulocytosis), which is the primary reason the drug was withdrawn from many markets worldwide. This safety liability substantially outweighs any incremental benefit from "confirming" an already-known indication, and it applies equally to the gout candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13768783](https://pubmed.ncbi.nlm.nih.gov/13768783/) | 1961 | RCT | Annals of the Rheumatic Diseases | Controlled trial of phenylbutazone, oxyphenbutazone, and placebo in RA |
| [401711](https://pubmed.ncbi.nlm.nih.gov/401711/) | 1977 | RCT (comparative) | Current Therapeutic Research | Head-to-head comparison of fenoprofen vs. oxyphenbutazone in RA patients |
| [6884415](https://pubmed.ncbi.nlm.nih.gov/6884415/) | 1983 | Double-blind dose-finding | European Journal of Clinical Pharmacology | Phenylbutazone dose-finding study in 32 RA patients; 300 mg/day identified as most efficacious, with adverse reactions in 7/32 |
| [4899416](https://pubmed.ncbi.nlm.nih.gov/4899416/) | 1968 | Double-blind comparative | Revista Española de Reumatismo | Flufenamic acid vs. oxyphenbutazone in RA and ankylosing spondylitis |
| [4544614](https://pubmed.ncbi.nlm.nih.gov/4544614/) | 1973 | Comparative study | Arzneimittel-Forschung | Efficacy/compatibility of bumadizone-Ca vs. oxyphenbutazone in rheumatic disease |
| [984900](https://pubmed.ncbi.nlm.nih.gov/984900/) | 1976 | Follow-up cohort | Annals of the Rheumatic Diseases | 227 psoriatic arthritis patients followed >10 years; RA-like arthropathy in 78% |
| [786193](https://pubmed.ncbi.nlm.nih.gov/786193/) | 1976 | Review | Archives of Internal Medicine | Review of RA treatment including newer and experimental anti-inflammatory agents |
| [14198102](https://pubmed.ncbi.nlm.nih.gov/14198102/) | 1964 | Review | Postgraduate Medicine | Corticosteroid therapy in RA: criteria and results |
| [5079767](https://pubmed.ncbi.nlm.nih.gov/5079767/) | 1972 | Case report (adverse event) | American Journal of Medicine | **Oxyphenbutazone and aplastic anemia** — key safety signal underlying the drug's market withdrawal |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone/oxyphenbutazone-induced sialadenitis fever mimicking angioedema |

---

## India Market Information

Not marketed in India; no active registrations are on file (`total_licenses = 0`).

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug interactions) is not available for this drug in this evidence pack, and no DDI records were found.

**Known historical safety signal (from literature evidence, not the formal safety dataset):** Oxyphenbutazone and its parent compound phenylbutazone are documented in the literature above to cause serious blood dyscrasias — aplastic anemia ([PMID 5079767](https://pubmed.ncbi.nlm.nih.gov/5079767/)) and other adverse reactions with long-term use — which is the primary reason these agents were withdrawn from many national markets. Any repurposing evaluation should treat this as a first-order constraint, not a secondary consideration.

---

## Other TxGNN Candidates in This Evidence Pack

| Rank | Disease | Score | Evidence Level | Note |
|------|---------|-------|-----------------|------|
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.07% | L5 | No clinical/literature support; assessed as having no biological plausibility (congenital syndrome with no known link to COX inhibition) — likely model noise |
| 3 | Gout | 99.05% | L3 | Historical NSAID use in acute gout flares; literature is mostly reviews/adverse-event reports, no controlled trials; shares the same blood-dyscrasia safety liability as the RA candidate |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (RA) is not a genuine novel repurposing signal but a recovery of Oxyphenbutazone's own historical indication, supported only by decades-old, low-quality evidence and zero contemporary clinical trials. The drug's well-documented risk of fatal blood dyscrasias — the reason it was withdrawn from most global markets — outweighs any repurposing rationale, and the same safety concern applies to the secondary gout candidate.

**To proceed, the following is needed:**
- TFDA/regulatory package insert warnings and contraindications (currently a Blocking data gap; required before any S1 safety screening can complete)
- Confirmed mechanism of action data from DrugBank (currently a High-severity data gap)
- A formal hematologic risk-benefit assessment given the known aplastic anemia/agranulocytosis signal
- Clarification of whether "recovering a known historical indication" should even be scored as a repurposing candidate, or excluded from this pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Bacitracin
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Bacitracin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bacitracin: From Topical Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a polypeptide antibiotic with established use as a topical agent against Gram-positive bacterial infections, commonly applied to skin wounds and superficial ocular and ear infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis** with a prediction score of 99.999%, placing it at rank 53 among all predicted indications.
Currently, **no clinical trials** and **no publications** directly support this repurposing direction, placing it at **Evidence Level L5**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical treatment of superficial bacterial infections (skin, wound care, ocular surface) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Bacitracin in the Evidence Pack. Based on known information, Bacitracin is a polypeptide antibiotic that inhibits bacterial cell wall synthesis, primarily by interfering with peptidoglycan biosynthesis in Gram-positive organisms. It is established as a topical antibiotic in wound care, ophthalmic ointments, and otologic formulations.

Punctate epithelial keratoconjunctivitis (PEK) is a superficial corneal and conjunctival inflammatory condition with multiple aetiologies—most commonly adenoviral infection, toxic reactions, or dry eye disease. The connection to Bacitracin is indirect: where PEK arises secondary to or concurrent with bacterial conjunctivitis, topical antibiotics may serve a supportive role in preventing secondary bacterial superinfection and reducing bacterial burden on the ocular surface. Bacitracin ophthalmic preparations are historically used for superficial ocular bacterial infections.

However, the mechanistic link is limited. Bacitracin has no antiviral activity and cannot address the predominant adenoviral or toxic causes of PEK. The TxGNN high score likely reflects topological proximity within the infection-disease network of the knowledge graph (ophthalmic infection nodes clustering near corneal inflammatory conditions), rather than a direct pharmacological rationale. This prediction should be interpreted as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bacitracin in punctate epithelial keratoconjunctivitis.

---

## Literature Evidence

Currently no related literature available for Bacitracin in punctate epithelial keratoconjunctivitis.

---

## Supplementary Evidence: Otitis Externa (Rank #4)

While the primary predicted indication has no supporting evidence, **otitis externa** (rank 4, TxGNN score 99.969%) is the highest-evidence indication identified in this analysis and warrants attention.

### Literature Evidence — Otitis Externa

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | Clinical Comparative Study | European Archives of Oto-Rhino-Laryngology | Double-blind RCT (n=151) comparing polymyxin-B + bacitracin ointment alone vs. with hydrocortisone acetate in acute bacterial otitis externa; assessed efficacy and safety of antibiotic component |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | Animal/Laboratory Study | Zentralblatt fur Veterinarmedizin | Susceptibility of bacterial isolates from chronic canine otitis externa to 20 antibiotics including Bacitracin; noted increasing antibiotic resistance trends |
| [14055264](https://pubmed.ncbi.nlm.nih.gov/14055264/) | 1963 | Expert Opinion/Review | Maryland State Medical Journal | Practical treatment approaches for otitis externa including topical antibiotic use |
| [4306877](https://pubmed.ncbi.nlm.nih.gov/4306877/) | 1969 | Review | Zeitschrift für ärztliche Fortbildung | Review of antibiotic use in otologic practice including Bacitracin-containing formulations |
| [165871](https://pubmed.ncbi.nlm.nih.gov/165871/) | 1975 | Case Series | Canadian Medical Association Journal | Use of antibacterial agents in external otitis management |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | Case Series | Zeitschrift für Laryngologie, Rhinologie, Otologie | Local treatment of inflammatory and secretory ear processes with Nebacetin (neomycin + bacitracin) preparations |

**Note:** Bacitracin's historical use in otitis externa is primarily via Nebacetin (polymyxin-B/bacitracin or neomycin/bacitracin combinations). Evidence is older and covers Gram-positive coverage only; *Pseudomonas aeruginosa*, the predominant Gram-negative pathogen in otitis externa, is not susceptible to Bacitracin.

---

## India Market Information

Bacitracin currently has **no registered products** in India (CDSCO). No authorisation records are available.

---

## Safety Considerations

**Drug Interactions** (84 interactions identified via DDInter; key interactions listed below):

*Major Interactions:*

| Interacting Drug | Level | Clinical Significance |
|----------------|-------|----------------------|
| Kanamycin | Major | Additive nephrotoxicity and/or ototoxicity risk with aminoglycoside co-administration |
| Neomycin | Major | Additive nephrotoxicity and ototoxicity; both are nephrotoxic antibiotics |
| Streptomycin | Major | Additive nephrotoxicity and ototoxicity with aminoglycoside combination |
| Deferasirox | Major | Potential for increased gastrointestinal adverse effects or altered absorption |
| Diatrizoate | Major | Possible interaction with iodinated contrast media; clinical significance requires monitoring |
| Iodipamide | Major | Interaction with iodinated contrast media |
| Iodixanol | Major | Interaction with iodinated contrast media |
| Iohexol | Major | Interaction with iodinated contrast media |

*Selected Moderate Interactions:*

| Interacting Drug | Level | Clinical Significance |
|----------------|-------|----------------------|
| Mesalazine | Moderate | Possible alteration of gut flora affecting aminosalicylate metabolism |
| Balsalazide | Moderate | Possible alteration of gut flora affecting aminosalicylate metabolism |
| Vancomycin | Moderate | Additive nephrotoxicity potential with systemic use |
| Sulfasalazine | Moderate | Gut flora interaction affecting sulphasalazine conversion |
| Olsalazine | Moderate | Gut flora interaction |
| Picosulfuric acid | Moderate | Potential alteration of bowel preparation efficacy |

> Please refer to the package insert for complete safety information, including warnings and contraindications, as this data was not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns Bacitracin a very high score for punctate epithelial keratoconjunctivitis (rank 53, 99.999%), but this score reflects knowledge graph network topology rather than validated biological mechanism — there is zero supporting clinical trial or literature evidence for this specific indication. The drug's Gram-positive antibacterial activity has only marginal indirect relevance to PEK, which is predominantly viral or toxic in aetiology.

Among all 10 predicted indications analysed, **otitis externa (rank 4)** represents the most clinically credible repurposing signal, supported by 6 historical publications including one controlled clinical trial (PMID 17503066), but evidence quality remains at L4 (no modern RCTs).

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve formal mechanism of action data from DrugBank API (DG002 — High severity data gap)
- **Regulatory safety data**: Obtain CDSCO package insert warnings and contraindications (DG001 — Blocking data gap) before any safety evaluation can proceed
- **India registration strategy**: Bacitracin has zero registrations in India; any repurposing pathway would require new regulatory submission
- **Focused evidence search for otitis externa**: Commission a systematic literature review on topical Bacitracin-combination preparations (e.g., neomycin/bacitracin, polymyxin-B/bacitracin) in otitis externa with modern search protocols covering post-2000 evidence
- **Formulation feasibility assessment**: Confirm availability of ophthalmic-grade Bacitracin formulations and GMP-compliant supply chain for ocular indications
- **Mechanistic validation**: Pre-clinical or in vitro studies to assess activity against ocular surface bacterial pathogens relevant to PEK before any clinical hypothesis is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Bacampicillin
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Bacampicillin
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

# Bacampicillin: From Bacterial Infections to Epiglottitis

## One-Sentence Summary

Bacampicillin is a prodrug of ampicillin, a broad-spectrum beta-lactam antibiotic historically used to treat a range of bacterial infections including respiratory, urinary tract, and skin infections.
The TxGNN model predicts it may be effective for **Epiglottitis** with a prediction score of **99.92%**,
though there are currently **no clinical trials and no publications** directly supporting this specific indication, placing this prediction at evidence level **L4** (mechanistic inference only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (ampicillin prodrug; historically used for respiratory, urinary, and skin infections) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, Bacampicillin is an orally bioavailable ester prodrug that is rapidly hydrolysed to **Ampicillin** in the gastrointestinal wall following absorption. Ampicillin is an aminopenicillin that inhibits bacterial cell wall synthesis by irreversibly binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and ultimately causing bacterial lysis. It demonstrates activity against many Gram-positive organisms and select Gram-negative bacteria.

The TxGNN prediction linking Bacampicillin to epiglottitis carries a mechanistic logic rooted in classical microbiology: acute bacterial epiglottitis was historically caused predominantly by *Haemophilus influenzae* type b (Hib), a Gram-negative organism against which Ampicillin traditionally had documented in vitro activity. Before the era of widespread Hib vaccination and beta-lactamase-producing strains, ampicillin-class antibiotics were a reasonable therapeutic option for this indication.

However, the clinical applicability is severely limited in the modern context. Contemporary surveillance data indicates that **30–40% of *H. influenzae* isolates now produce beta-lactamase**, rendering Ampicillin (and by extension Bacampicillin) ineffective against a substantial proportion of strains. Current clinical guidelines have shifted decisively to third-generation cephalosporins (Ceftriaxone, Cefotaxime) as first-line therapy for epiglottitis. Furthermore, Bacampicillin has been withdrawn from most major markets, making any clinical development pathway highly challenging. The mechanistic link is historically coherent but clinically superseded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bacampicillin in epiglottitis.

---

## Literature Evidence

Currently no related literature available for Bacampicillin in epiglottitis.

---

## India Market Information

Bacampicillin currently has **no registered products** in India. It has not been approved or marketed under the CDSCO framework, and no license records are available.

---

## Safety Considerations

**Drug Interactions:** 34 drug-drug interactions are documented in the DDI database. The following are the most clinically relevant:

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Omeprazole | Moderate | PPIs raise gastric pH, potentially reducing ampicillin-class absorption |
| Esomeprazole | Moderate | Same mechanism as omeprazole |
| Lansoprazole | Moderate | Same mechanism as omeprazole |
| Rabeprazole | Moderate | Same mechanism as omeprazole |
| Dexlansoprazole | Moderate | Same mechanism as omeprazole |
| Pantoprazole | Moderate | Same mechanism as omeprazole |
| Famotidine | Moderate | H2 blockers reduce gastric acidity, may impair absorption |
| Ranitidine | Moderate | Same mechanism as famotidine |
| Cimetidine | Moderate | Same mechanism as famotidine |
| Nizatidine | Moderate | Same mechanism as famotidine |
| Aluminum hydroxide | Moderate | Antacids reduce ampicillin bioavailability |
| Calcium carbonate | Moderate | Antacid interaction |
| Magnesium hydroxide | Moderate | Antacid interaction |
| Doxycycline | Moderate | Antagonism: bacteriostatic agent may blunt bactericidal effect |
| Tetracycline | Moderate | Same antagonism mechanism as doxycycline |
| Minocycline | Moderate | Same antagonism mechanism as doxycycline |
| Clarithromycin | Minor | Macrolide co-administration; minor pharmacodynamic concern |

For complete warnings and contraindications, please refer to the package insert or the TFDA/CDSCO product monograph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although there is a historically coherent mechanistic basis linking Bacampicillin (via its active metabolite Ampicillin) to *H. influenzae*-caused epiglottitis, this prediction is undermined by three compounding factors: (1) high modern resistance rates of *H. influenzae* to ampicillin-class antibiotics, (2) complete absence of any direct clinical trial or literature evidence for this specific indication, and (3) Bacampicillin's withdrawal from commercial markets, making a regulatory development pathway nearly non-viable.

**To proceed, the following would be needed:**

- **Resistance profiling**: Current regional susceptibility data for *H. influenzae* to Ampicillin, to determine if any niche subpopulation (e.g., non-beta-lactamase-producing strains) could reasonably benefit
- **MOA documentation**: Full DrugBank mechanism of action data and pharmacokinetic profile (TFDA/CDSCO package insert or DrugBank API retrieval)
- **Comparative effectiveness rationale**: A compelling argument for why Bacampicillin would offer advantage over currently approved cephalosporins, given the existing standard of care
- **Formulation feasibility**: Assessment of whether an oral prodrug route is clinically appropriate for acute epiglottitis, which often requires IV therapy and airway management
- **Regulatory pathway assessment**: Given the drug's market withdrawal status, a feasibility review for re-registration under CDSCO before any development investment

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


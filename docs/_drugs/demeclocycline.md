---
layout: default
title: Demeclocycline
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 3
---

# Demeclocycline
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

# Demeclocycline: From Tetracycline Antibiotic to Chronic Ethmoidal Sinusitis

## One-Sentence Summary

Demeclocycline (DB00618) is a broad-spectrum tetracycline-class antibiotic whose registered original indications were not captured in this evidence pack, though it is classically known for treating bacterial infections and blocking ADH in SIADH.
The TxGNN model predicts it may be effective for **Chronic Ethmoidal Sinusitis**, with **0 clinical trials** and **1 histomorphometric study** currently supporting this direction — making the evidence base extremely limited.
At this stage the overall recommendation is **Hold**, pending mechanism verification and direct clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this evidence pack (known class: tetracycline antibiotic) |
| Predicted New Indication | Chronic Ethmoidal Sinusitis |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Demeclocycline belongs to the tetracycline antibiotic class, which shares several properties relevant to chronic sinus disease. First, tetracyclines provide broad-spectrum antibacterial coverage against common chronic sinusitis pathogens including *Haemophilus influenzae*, *Streptococcus pneumoniae*, and anaerobes — offering a plausible antimicrobial rationale. Second, tetracyclines are recognised non-selective inhibitors of matrix metalloproteinases (MMPs), particularly MMP-2 and MMP-9, which play a role in mucosal remodelling and the bone changes observed in chronic ethmoidal sinusitis. The single available publication (PMID 9546260) specifically documents ethmoid bone resorption and synthesis changes in chronic rhinosinusitis, a pathological process MMP inhibition could theoretically attenuate.

However, it is critical to note that the mechanistic studies on anti-inflammatory and MMP-inhibiting effects have been conducted predominantly with Doxycycline and Minocycline — not Demeclocycline specifically. There are no direct preclinical or clinical studies establishing that Demeclocycline exerts meaningful anti-inflammatory or anti-remodelling effects in sinus tissue.

The TxGNN model likely generated this prediction by combining Demeclocycline's tetracycline class membership with the anatomical and inflammatory similarity between conditions it may have been associated with in the knowledge graph. This is a class-effect inference, not direct evidence for Demeclocycline itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9546260](https://pubmed.ncbi.nlm.nih.gov/9546260/) | 1998 | Histomorphometric Study | The Laryngoscope | Undecalcified ethmoid bone analysis in chronic sinusitis vs. controls; documents bone synthesis, resorption, and inflammatory cell infiltration in sinus disease — provides histological context for the disease mechanism but does not involve Demeclocycline |

---

## India Market Information

Demeclocycline currently has no registered products in the Indian market. No authorisation records are available.

---

## Safety Considerations

**Drug Interactions:** 154 drug-drug interactions are on record (DDInter database). Key interactions to be aware of include:

- **Major interaction:** Vitamin A — co-administration with tetracyclines is associated with increased risk of benign intracranial hypertension (pseudotumor cerebri); avoid concurrent use.
- **Moderate interactions (selected):** Amoxicillin (potential antagonism of bactericidal activity); multiple insulin formulations (tetracyclines may potentiate hypoglycaemic effects — monitor blood glucose); divalent/trivalent cations including Calcium Phosphate, Calcium acetate, Magnesium oxide, Magnesium sulfate, Magnesium chloride, Zinc sulfate, Zinc acetate (chelation reduces tetracycline absorption — separate dosing by at least 2–3 hours); Potassium citrate; Balsalazide.
- **Minor interaction:** Mannitol.

Full package insert warnings and contraindications were not available in this evidence pack. Please refer to the originator package insert or DrugBank monograph for complete safety labelling, including renal impairment dosing, photosensitivity risk (a known class effect that is particularly pronounced with Demeclocycline), and use in pregnancy/paediatric populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.14%) for Demeclocycline in chronic ethmoidal sinusitis, but the underlying evidence is at Level L5 — model prediction only, with zero clinical trials and a single non-interventional histological study that does not involve the drug. There is no direct preclinical or clinical data for Demeclocycline in any sinusitis indication, and the mechanistic link rests entirely on class-effect extrapolation from other tetracyclines.

**To proceed, the following is needed:**

- **MOA verification:** Retrieve full DrugBank monograph to confirm Demeclocycline's mechanism of action, MMP inhibitory potency relative to Doxycycline/Minocycline, and any anti-inflammatory pharmacodynamic data.
- **Safety labelling:** Download and parse the originator package insert (or TFDA/EMA/FDA SmPC) to obtain complete warnings, contraindications, and special population guidance — currently a Blocking data gap.
- **Preclinical evidence:** Commission or identify in-vitro or animal studies specifically assessing Demeclocycline (not just class members) against sinusitis-relevant pathogens and inflammatory pathways.
- **Comparative class analysis:** Determine whether Doxycycline or Minocycline — which have more established anti-inflammatory evidence — would be superior candidates for the same indication, which might make Demeclocycline repurposing redundant.
- **Feasibility assessment:** Given that Demeclocycline is not marketed in India (0 registrations), any development pathway would require de-novo import/registration, adding significant regulatory burden before clinical investigation could begin.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


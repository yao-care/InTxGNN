---
layout: default
title: Potassium Iodide
parent: Moderate Evidence (L3-L4)
nav_order: 684
evidence_level: L4
indication_count: 2
---

# Potassium Iodide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Potassium Iodide: From Antifungal Therapy to Nasal Cavity Disease

## One-Sentence Summary

Potassium Iodide (DrugBank DB06715) is not currently marketed in Taiwan, and no approved-indication text is available from local licensing data; based on the supporting literature, it has traditionally been used off-label as an antifungal agent (e.g., sporotrichosis, zygomycosis). The TxGNN model predicts potential efficacy for **Nasal Cavity Disease**, but this is currently supported only by **4 case reports** (3 veterinary, 1 human from 1994) and **no clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is unlicensed in Taiwan (no license records). Literature indicates traditional off-label antifungal use (e.g., sporotrichosis, zygomycosis) |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is currently not available (Data Gap). Based on known information, potassium iodide has traditionally been used as an antifungal therapy for conditions such as cutaneous/lymphocutaneous sporotrichosis and some forms of zygomycosis (mucormycosis). The proposed mechanism involves iodide ion interference with fungal cell wall integrity/metabolism and modulation of local immune response, though the exact molecular pathway is not well characterized.

The supporting literature for "Nasal Cavity Disease" is entirely composed of case reports describing potassium iodide treatment of **fungal (mycotic) infections of the nasal cavity and sinuses** — rhinofacial pythiosis in sheep, mycotic rhinitis (Aspergillus) in a horse, Pseudallescheria boydii nasal infection in a horse, and nasofacial zygomycosis in a human patient. This is mechanistically consistent with the drug's known antifungal use.

However, "Nasal Cavity Disease" as predicted by TxGNN is a broad disease-category label, while the actual evidence is confined to a narrow subset — mycotic/fungal rhinitis — and cannot be generalized to nasal cavity disease as a whole. Three of the four supporting reports are veterinary case reports (sheep, horses), and only one is a human case report, dating from 1994, with no controlled or comparative design. The high TxGNN score may partly reflect over-generalization of the disease node in the knowledge graph rather than a well-supported clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Case Report | Rev Inst Med Trop Sao Paulo | Human case of nasofacial zygomycosis (Pará, Brazil); rapid clinical response to potassium iodide therapy, though disease recurred |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Case Report (Veterinary) | J Am Vet Med Assoc | Pseudallescheria boydii nasal cavity infection in a horse treated with topical miconazole and IV sodium iodide |
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Case Report (Veterinary) | J Mycol Med | Successful potassium iodide treatment of rhinofacial pythiosis (Pythium insidiosum) in sheep |
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Case Report (Veterinary) | Vet Res Commun | Mycotic rhinitis (Aspergillus fumigatus) in a horse treated with topical clotrimazole plus oral potassium iodide |

---

## Safety Considerations

**Drug Interactions**: A DDI query returned 45 total interactions. Notable **Major**-level interactions (elevated hyperkalemia/potassium-retention risk) include ACE inhibitors (Benazepril, Captopril, Enalapril, Lisinopril, Moexipril, Perindopril, Quinapril), ARBs (Olmesartan, Valsartan, Azilsartan medoxomil, Losartan, Telmisartan), the renin inhibitor Aliskiren, and Trimethoprim. **Moderate**-level interactions include NSAIDs (Ketorolac, Ibuprofen, Diclofenac, Oxaprozin, Naproxen) and Tolvaptan.

Detailed Taiwan/TFDA label warnings and contraindications are not currently available (Data Gap, Blocking — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication's own scoring already flags it as decision-stage S0 with a "Hold" recommendation — evidence is limited to four case reports (three veterinary, one 40+ year-old human case) with no clinical trials or controlled studies, and one Blocking-severity data gap (missing Taiwan label warnings/contraindications) prevents entry into the S1 safety evaluation stage.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently Blocking (DG001)
- Detailed mechanism-of-action data from DrugBank — currently High-priority gap (DG002)
- Controlled or comparative clinical evidence specific to mycotic rhinitis/nasal cavity disease, rather than isolated case reports
- Note: a second candidate, "Acute Laryngopharyngitis" (TxGNN score 99.95%, Evidence Level L5), has zero supporting clinical trials or literature and is not recommended for further pursuit at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


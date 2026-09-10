---
layout: default
title: Isoniazid
parent: 僅模型預測 (L5)
nav_order: 445
evidence_level: L5
indication_count: 1
---

# Isoniazid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Isoniazid: From Tuberculosis to Conjunctivitis

## One-Sentence Summary

Isoniazid is a first-line antitubercular drug, originally used to treat tuberculosis (including latent TB infection, LTBI). The TxGNN model predicts it may be effective for **Conjunctivitis**, with **1 clinical trial** and **20 publications** currently identified — though most of this literature actually concerns tuberculosis-related ocular manifestations rather than conjunctivitis of general (infectious/allergic) origin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (anti-tubercular therapy) — not confirmable from Taiwan license data, as the drug is not marketed in Taiwan |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general pharmacological knowledge, isoniazid (isonicotinic acid hydrazide) is a first-line antitubercular agent that inhibits mycolic acid synthesis in the cell wall of *Mycobacterium tuberculosis*; its efficacy in tuberculosis treatment is well established.

The literature identified under "conjunctivitis" does not describe isoniazid treating conjunctivitis as an independent, general condition. Instead, the large majority of publications describe **tuberculous conjunctivitis** and **phlyctenular keratoconjunctivitis** — an ocular hypersensitivity reaction to mycobacterial antigens that occurs in patients with (often latent or subclinical) tuberculosis. In these cases, isoniazid is historically used to treat or prevent the underlying TB infection, which secondarily resolves or prevents the associated conjunctival inflammation (e.g., the 1965 Alaska phlyctenular keratoconjunctivitis prophylaxis study).

This suggests the TxGNN model has likely picked up a genuine but **narrower** biological signal: isoniazid's established role in TB-driven ocular disease, rather than a novel broad-spectrum mechanism against conjunctivitis in general. The predicted indication should therefore be interpreted as "conjunctivitis secondary to tuberculosis/TB hypersensitivity," not conjunctivitis of infectious (viral/bacterial) or allergic origin.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04094012](https://clinicaltrials.gov/study/NCT04094012) | Phase 3 | Completed | 490 | Compared systemic drug reaction rates between 3HP (12-dose weekly rifapentine + isoniazid) and 1HP regimens for latent TB infection treatment. This trial evaluates isoniazid-containing regimens for LTBI generally; it does not directly test conjunctivitis as an endpoint. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Prophylaxis study | Am Rev Respir Dis | Isoniazid prophylaxis against phlyctenular keratoconjunctivitis among Eskimos in southwestern Alaska |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Case series | Annales d'oculistique | Local (topical) use of isoniazid in the treatment of ocular tuberculosis |
| [25433746](https://pubmed.ncbi.nlm.nih.gov/25433746/) | 2014 | Case report | Can J Ophthalmol | Conjunctival phlyctenulosis re-emphasized as a presenting sign of impending clinical tuberculosis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, largely in children with primary TB and lymph node involvement |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Primary sinonasal tuberculosis presenting with phlyctenular keratoconjunctivitis in a pediatric patient |
| [17133069](https://pubmed.ncbi.nlm.nih.gov/17133069/) | 2006 | Case report | Cornea | Mycobacterium tuberculosis presenting as chronic red eye (conjunctival TB) |
| [26692731](https://pubmed.ncbi.nlm.nih.gov/26692731/) | 2015 | Case report | Middle East Afr J Ophthalmol | Tuberculous conjunctivitis in an anophthalmic socket |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva |
| [4233886](https://pubmed.ncbi.nlm.nih.gov/4233886/) | 1968 | Case report | Arch Ophtalmol | Tuberculosis of the bulbar conjunctiva |
| [32674602](https://pubmed.ncbi.nlm.nih.gov/32674602/) | 2020 | Case report | Clin Pediatr | An unexpected (TB-related) cause of conjunctivitis in an adolescent |

Note: nearly all identified literature concerns tuberculosis-associated ocular disease rather than conjunctivitis of non-TB origin.

---

## Taiwan Market Information

Isoniazid currently has **no marketing authorization on record in Taiwan** (market status: 未上市, 0 registrations), so no license/product table can be produced.

---

## Safety Considerations

- **Drug Interactions**: 242 documented interactions on file. Representative examples from the available sample include:
  - **Metformin** (Moderate) — relevant given isoniazid's known effect on glucose metabolism
  - **Corticosteroids** (Minor–Moderate) — Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide — may reduce isoniazid plasma levels/efficacy
  - **Vitamin D analogs** (Moderate) — Cholecalciferol, Calcifediol, Calcitriol
  - **Antidiabetic agents** (Moderate) — Acarbose, Albiglutide, Alogliptin, Pioglitazone, Canagliflozin, Dapagliflozin, Chlorpropamide
  - **Metronidazole** (Moderate)

No key warnings or contraindication data were available for this evidence pack (TFDA label not yet retrieved); please refer to the package insert once available for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted "conjunctivitis" signal appears mechanistically tied to TB-associated ocular disease (tuberculous conjunctivitis, phlyctenular keratoconjunctivitis) rather than conjunctivitis broadly, and no modern registered trial directly evaluates isoniazid for conjunctivitis. In addition, TFDA label warnings/contraindications remain an unresolved blocking data gap, preventing initial safety screening (S1).

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data via DrugBank (DG002)
- Clarification of the target population: narrow the indication to TB-associated/hypersensitivity conjunctivitis (phlyctenular keratoconjunctivitis) rather than general conjunctivitis, consistent with the evidence base
- If pursuing the broader "conjunctivitis" indication, additional modern controlled evidence specific to that population would be needed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


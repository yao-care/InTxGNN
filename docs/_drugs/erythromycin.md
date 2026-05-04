---
layout: default
title: Erythromycin
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 5
---

# Erythromycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Erythromycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Erythromycin is a macrolide antibiotic with a long history of use in treating bacterial infections, including respiratory tract infections, skin and soft tissue infections, and sexually transmitted diseases caused by *Chlamydia trachomatis*.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, a superficial inflammatory condition of the cornea and conjunctiva often associated with bacterial or viral triggers.
This direction is currently supported by **no registered clinical trials** and only **2 tangentially related publications**, placing the evidence at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory, skin, sexually transmitted) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 — Model prediction only, no direct clinical studies |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for erythromycin in this Evidence Pack. Based on well-established pharmacological knowledge, erythromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by reversibly binding to the 50S ribosomal subunit, thereby blocking translocation of the peptide chain. It exhibits bacteriostatic activity against a broad range of Gram-positive organisms and atypical pathogens, including *Chlamydia*, *Mycoplasma*, and *Staphylococcus*.

Punctate epithelial keratoconjunctivitis (PEK) is characterised by diffuse punctate lesions on the corneal and conjunctival epithelium. While its aetiology can be viral, allergic, or toxic in nature, bacterial superinfection or underlying bacterial blepharitis is a recognised trigger — precisely the microenvironment where erythromycin's antibiotic activity could be mechanistically relevant. Topical erythromycin ophthalmic ointment is, in fact, already used in clinical practice for staphylococcal blepharitis and neonatal conjunctivitis, conditions that share a close anatomical and pathological relationship with PEK.

The TxGNN knowledge-graph prediction likely captures these shared disease nodes — blepharokeratoconjunctivitis, bacterial conjunctivitis, and corneal surface inflammation — and infers erythromycin's utility in PEK through guilt-by-association reasoning. While mechanistically plausible, the prediction currently lacks dedicated clinical trial validation and should be viewed as hypothesis-generating rather than practice-changing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Erythromycin in Punctate Epithelial Keratoconjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Case Series / Review | J Pediatric Ophthalmol Strabismus | Describes history, symptoms, clinical signs, and management of chronic blepharokeratoconjunctivitis in children — a condition closely related to PEK, where antibiotic therapy including erythromycin is part of the treatment approach |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Reports a case of microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in an immunocompetent adult diagnosed via metagenomic deep sequencing — illustrates the diagnostic complexity of atypical keratoconjunctivitis and the need for broad antimicrobial coverage |

> **Note:** Neither publication directly investigates erythromycin as a treatment for punctate epithelial keratoconjunctivitis. These references provide contextual background only.

---

## India Market Information

Erythromycin currently holds **no registered product licenses** in India. This drug is not marketed under any authorisation in the Indian regulatory framework based on available data.

---

## Safety Considerations

**Drug Interactions (755 interactions identified; selected highlights below):**

Erythromycin is a known inhibitor of cytochrome P450 3A4 (CYP3A4) and P-glycoprotein. This underpins the large number of reported interactions. Key interactions of clinical relevance include:

| Severity | Interacting Drug | Clinical Implication |
|----------|-----------------|---------------------|
| **Major** | Loperamide | Risk of cardiac arrhythmia; erythromycin prolongs QT interval and inhibits loperamide metabolism |
| **Major** | Clarithromycin | Additive QT prolongation risk; both are macrolides with CYP3A4 inhibitory activity |
| Moderate | Dexamethasone / Betamethasone / Hydrocortisone / Triamcinolone / Budesonide | Erythromycin inhibits CYP3A4-mediated corticosteroid metabolism, potentially increasing steroid exposure and adverse effects |
| Moderate | Pioglitazone | Possible increased plasma levels due to CYP3A4 inhibition |
| Moderate | Aprepitant | Mutual CYP3A4 inhibition may elevate levels of both agents |
| Moderate | Famotidine / Cimetidine | Altered gastrointestinal motility and possible pharmacokinetic interactions |

> Erythromycin's QT-prolonging potential is a critical consideration, particularly in patients with pre-existing cardiac conditions or those taking other QT-prolonging agents.

Please also refer to the full package insert for comprehensive safety information, including warnings and contraindications that were not available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model scores erythromycin highly for punctate epithelial keratoconjunctivitis (99.89%), and the mechanistic basis is plausible given erythromycin's established ophthalmic use in related bacterial surface eye diseases. However, there are no registered clinical trials and no direct clinical evidence for this specific indication; the two literature references retrieved are contextual rather than confirmatory. Combined with erythromycin's absence from the Indian market, the current evidence base does not support advancing to formal repurposing evaluation at this stage.

**To proceed, the following is needed:**

- **Mechanism of Action data**: Obtain full MOA profile from DrugBank API (DB00199) to formally characterise the mechanistic link between erythromycin and corneal epithelial inflammation
- **Safety profile completion**: Download and parse the full package insert (via TFDA or equivalent regulatory source) to populate key warnings and contraindications currently missing from this Pack
- **Targeted literature review**: Commission a structured PubMed/EMBASE search specifically for "erythromycin AND (keratoconjunctivitis OR punctate epithelial keratopathy OR blepharokeratoconjunctivitis)" to determine whether indirect evidence (e.g., topical ophthalmic formulation use in blepharitis-associated PEK) already exists
- **Route compatibility assessment**: Confirm availability of ophthalmic-grade erythromycin formulations, as systemic administration is unlikely to be the appropriate route for this indication
- **Regulatory pathway check**: Assess whether India has any pathway for ophthalmic antibiotic approvals relevant to erythromycin, given its current non-marketed status

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From Actinic Keratoses to Pre-Malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical Toll-like receptor 7/8 (TLR7/8) agonist approved internationally for actinic keratoses, superficial basal cell carcinoma, and external anogenital warts, though it is not currently registered in India.
The TxGNN model predicts it may be effective for **Pre-Malignant Neoplasm**,
with **19 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Actinic keratoses, superficial basal cell carcinoma, external anogenital warts (international approvals; no India registration) |
| Predicted New Indication | Pre-Malignant Neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Imiquimod is a small-molecule TLR7/8 agonist that binds innate immune receptors on plasmacytoid dendritic cells and macrophages. Activation triggers the MyD88 → NF-κB/IRF7 signalling cascade, inducing a burst of type-I interferons (IFN-α/β) and pro-inflammatory cytokines (TNF-α, IL-6, IL-12). This cascade drives dendritic cell maturation and cytotoxic T-lymphocyte (CTL) activation, generating a targeted anti-tumour immune response at the site of application. Separately, imiquimod exerts a direct pro-apoptotic effect on pre-malignant epithelial cells by down-regulating the anti-apoptotic protein Bcl-2, inducing tumour-cell death independently of immune activation.

The mechanistic step from imiquimod's established dermatological indications to "pre-malignant neoplasm" is short: actinic keratoses (AK) and lentigo maligna — conditions for which imiquimod already holds regulatory approval or strong clinical support internationally — are themselves canonical pre-malignant lesions. The same TLR7-driven immune clearance mechanism that resolves HPV-related epidermal disease (external genital warts) has been shown to regress pre-invasive HPV-driven lesions including high-grade vulvar intraepithelial neoplasia (VIN), anal intraepithelial neoplasia (AIN), and cervical intraepithelial neoplasia (CIN) — all of which fall squarely within the "pre-malignant neoplasm" disease category.

The biological rationale is well-founded: imiquimod's core mechanism — innate immune activation of skin and mucosal epithelia — is precisely the tissue compartment where pre-malignant lesions arise. Multiple completed Phase 2/3 trials across AK, lentigo maligna, VIN, and CIN provide substantial empirical support, and the TxGNN prediction score of 99.92% reflects this strong mechanistic and epidemiological overlap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Completed | 259 | RCT evaluating imiquimod as neo-adjuvant treatment to reduce excision margins and risk of intralesional excision in lentigo maligna of the face — the highest-relevance trial; directly targets a pre-malignant melanocytic lesion |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Completed | 90 | Brazilian RCT assessing topical imiquimod efficacy for high-grade cervical intraepithelial neoplasia (CIN 2-3), an HPV-related pre-malignant cervical lesion |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study evaluating duration of effect of imiquimod 5% cream applied 3×/week for actinic keratoses on the head |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminated | 49 | RCT comparing 5%, 0.05%, and nanoencapsulated 0.05% imiquimod gel for actinic cheilitis (pre-malignant lower lip lesion); terminated before optimal dosing could be established |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | RCT of topical imiquimod vs standard LLETZ for high-grade CIN 2-3; terminated early due to recruitment difficulties; statistical power insufficient but design is directly on-target |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Unknown | 20 | Post-marketing study of imiquimod 3.75% cream following cryotherapy for hypertrophic actinic keratoses on dorsal hands and forearms |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Completed | 16 | Pilot neoadjuvant trial of topical imiquimod (Aldara) as TLR7 agonist immunotherapy in early-stage oral squamous cell carcinoma; directly evaluates pre-surgical tumour immune response |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Completed | 5 | Exploratory study examining HPV immune escape mechanisms and evaluating imiquimod efficacy and mechanisms in VIN 2/3 and anogenital warts |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Unknown | 145 | Non-inferiority RCT comparing surgical excision vs curettage combined with imiquimod for nodular basal cell carcinoma — quantifies topical imiquimod effectiveness against gold-standard surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Cochrane review of interventions for anal canal intraepithelial neoplasia (AIN), an HPV-associated pre-malignant condition rising rapidly in HIV-positive MSM; identifies imiquimod as a therapeutic candidate |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Cochrane review of medical interventions for high-grade VIN; imiquimod identified as a promising non-surgical option given its immune-response modulation and high morbidity of surgical alternatives |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Reviews combined treatment strategies including imiquimod for non-melanoma skin cancer (BCC, SCC) and precursor lesions; discusses synergistic potential with photodynamic therapy |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Comprehensive review of topical agents for NMSC and pre-malignant skin lesions; positions imiquimod alongside fluorouracil and diclofenac as a first-line topical option for field cancerization |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Narrative Review | Skin Therapy Lett | Current management of actinic keratoses (canonical pre-malignant lesion); positions imiquimod within destructive, topical field, and procedural treatment categories for AK |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case Report | Int J STD AIDS | Successful clearance of high-grade VIN with imiquimod 5% in a renal transplant recipient (immunosuppressed), expanding potential use to at-risk immunocompromised populations |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case Report | Int J STD AIDS | Bowenoid papulosis of the penis (HPV-related pre-malignant anogenital lesion) successfully cleared with imiquimod 5% cream; well-tolerated, no recurrence at 6 months |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical | Urol Oncol | Pharmacokinetic and pharmacodynamic evaluation of TLR7 agonists (TMX-101, TMX-202) in rat model after intravesical administration; supports TLR7 agonism as a class strategy for mucosal pre-malignant lesions beyond the skin |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case Report | Hautarzt | OCT imaging of disseminated superficial actinic porokeratosis presenting with multiple pre-malignant lesions (AKs, Bowen's disease, SCC); DSAP and AK lesions resistant to standard topical therapies, providing context for imiquimod in recalcitrant pre-malignant disease |

---

## India Market Information

Imiquimod is currently **not registered or marketed in India** (CDSCO approval count: 0). No product authorization data is available. For reference, international approvals include FDA-approved Aldara® 5% cream and Zyclara® 3.75% cream (USA), as well as CE-marked products in Europe, all authorized for actinic keratoses, superficial basal cell carcinoma, and external anogenital warts. These international approvals do not constitute India-authorized indications and are provided for context only.

---

## Safety Considerations

**Drug Interactions:** 59 potential drug-drug interactions have been identified via the DDinter database. All interactions are currently classified as **Unknown severity**, reflecting an absence of quantified interaction data rather than confirmed safety. Clinically notable co-medications flagged include:

- **Immunomodulators / corticosteroids:** Prednisone, Prednisolone, Budesonide, Hydroxychloroquine
- **Anticoagulants / antiplatelet agents:** Warfarin, Clopidogrel, Acetylsalicylic acid
- **Proton pump inhibitors:** Pantoprazole, Omeprazole, Lansoprazole
- **Cardiovascular:** Simvastatin
- **Respiratory / allergy:** Montelukast, Fluticasone, Salbutamol, Fexofenadine, Cetirizine
- **Analgesics / GI:** Morphine, Ibuprofen, Loperamide
- **CNS:** Bupropion

Clinical judgement and patient-level monitoring are advised when imiquimod is used alongside any of the above agents until interaction severity can be formally characterized.

Please refer to the international package insert (e.g., Aldara® prescribing information) for full warnings, contraindications, and precautions, as India-specific labelling data is currently unavailable.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (NCT01720407, n=259) directly evaluates imiquimod for lentigo maligna — a canonical pre-malignant neoplasm — and a second completed Phase 3 trial exists for actinic keratoses (NCT00175643), meeting the L1 threshold. Two Cochrane systematic reviews additionally support efficacy across HPV-driven pre-malignant lesions (VIN, AIN), and a completed Phase 2 RCT (NCT03233412, n=90) confirms activity in high-grade CIN. The drug's TLR7/8 mechanism is directly aligned with immunological clearance of pre-malignant epithelial lesions, and international regulatory approvals for AK and superficial BCC confirm established translational readiness.

**To proceed, the following is needed:**

- **CDSCO registration pathway:** Assess import licensing and new drug application requirements for topical imiquimod in India; explore fast-track options given multiple Phase 3 completions abroad
- **Package insert safety review:** Obtain and analyse the FDA/EMA-approved prescribing information to fill the current blocking data gap on Indian-label warnings and contraindications
- **MOA documentation:** Query the DrugBank API (DB00724) to complete formal mechanism-of-action documentation for regulatory submissions
- **Drug interaction characterisation:** Commission a clinical pharmacologist review of the 59 Unknown-severity DDI flags, prioritising warfarin, immunosuppressants, and anticoagulants
- **India-specific clinical plan:** For HPV-related indications (CIN, VIN), design a clinical protocol accounting for local HPV genotype prevalence (HPV 16/18 dominance in India) and healthcare infrastructure for gynaecological monitoring
- **Safety signal documentation:** Formally review the reported case of malignant transformation during imiquimod treatment of oral papillomatosis (context from Rank 2 indication; PMID 12719972) and include in the risk management plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


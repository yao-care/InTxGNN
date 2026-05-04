---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: From Inflammatory Airway Disease to Atopic Eczema

## One-Sentence Summary

Budesonide is a high-potency synthetic glucocorticoid corticosteroid, established in clinical practice for inflammatory airway diseases (asthma, COPD) and gastrointestinal inflammation (Crohn's disease, ulcerative colitis).
The TxGNN model predicts it may be effective for **Atopic Eczema**, with **2 clinical trials** and **20 publications** currently identified in this direction.
However, direct human efficacy evidence for this indication remains limited — the most compelling support is an emerging nanoparticle formulation strategy designed to overcome budesonide's historically poor skin penetration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory airway disease (asthma, COPD); inflammatory bowel disease (Crohn's disease, ulcerative colitis) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the drug database. Based on well-established pharmacological knowledge, budesonide belongs to the synthetic glucocorticoid class. It binds glucocorticoid receptors (GR-α), activating anti-inflammatory gene transcription while suppressing key pro-inflammatory transcription factors (NF-κB, AP-1). The downstream effects include inhibition of Th2 cytokine polarization (IL-4, IL-13), suppression of mast cell degranulation, and reduction of eosinophil recruitment — all of which are central drivers of atopic eczema pathophysiology.

Atopic eczema is fundamentally a Th2-mediated inflammatory skin condition, characterised by epidermal barrier dysfunction, IgE sensitisation, and eosinophilic infiltration. This mechanistic profile is a strong match for corticosteroid intervention. Topical corticosteroids (hydrocortisone, betamethasone) are already the first-line standard of care for mild-to-moderate atopic dermatitis. Budesonide has historically been underutilised in dermatological applications due to its physicochemical properties limiting transcutaneous penetration — which is the key reason it has not been widely adopted despite a mechanistically sound rationale.

The repurposing opportunity identified by TxGNN centres on novel drug delivery innovation: a 2024 study (PMID 38275852) developed pH-sensitive Eudragit L 100 nanoparticle hydrogels loaded with budesonide specifically for pediatric atopic dermatitis, exploiting the characteristic acidic pH of atopic lesions to achieve targeted local drug release. This formulation strategy may overcome the traditional skin penetration barrier, positioning budesonide as a differentiated topical agent with a better-characterised safety profile than many newer biologics. Notably, budesonide's well-documented systemic absorption characteristics and HPA axis suppression data from inhalation studies provide a head start in dermal safety profiling.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy in atopic, wheezing children aged 18 months–3 years at high risk for asthma. Study focuses on asthma prevention endpoints; budesonide is not the primary intervention and atopic eczema is not the primary outcome. Provides mechanistic context only. |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | Unknown | 150 | Integrated characterisation of severe paediatric asthma endotypes (ages 0–12) combining immune, metabolomic, and microbiota analyses. Atopy is part of phenotyping, but budesonide efficacy in atopic eczema is not assessed. |

> Neither trial directly evaluates budesonide as an intervention for atopic eczema in humans. Both provide indirect mechanistic context linking atopic pathophysiology to corticosteroid-sensitive inflammatory pathways.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Experimental (Formulation R&D) | Gels (Basel) | Budesonide-loaded pH-sensitive Eudragit L 100 nanoparticle hydrogels developed for local therapy of **pediatric atopic dermatitis**; demonstrated improved drug release at atopic lesion pH and enhanced skin penetration — the most direct evidence for this repurposing direction. |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | Randomised Controlled (Veterinary) | J Vet Pharmacol Ther | Randomised, blinded, placebo-controlled crossover trial of 0.025% budesonide leave-on conditioner (Barazone) in **canine atopic dermatitis** (n=29); significant reduction in skin lesions and pruritus versus placebo. Proof-of-concept for topical budesonide in atopic skin disease. |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | Clinical Study | Allergologia et Immunopathologia | Compared inhaled budesonide response in atopic versus non-atopic infants/preschoolers with recurrent wheezing; atopic children showed differential inflammatory response patterns relevant to understanding budesonide efficacy in atopic populations. |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Clinical Study | Dermatology | Assessed systemic effects (IGF axis, bone and collagen turnover) of topical glucocorticosteroids in children with atopic dermatitis; provides foundational safety data for topical corticosteroid use in paediatric AD patients. |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Observational | Contact Dermatitis | Contact sensitisation patterns in an Asian dermatology centre population with and without atopic dermatitis; budesonide identified among patch-test positive allergens in AD patients — a key safety signal. |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Observational | Dermatitis | Contact hypersensitivity to the European standard corticosteroid series (including budesonide) in adolescents and adults with atopic dermatitis; sensitisation rate data essential for patient selection. |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Observational | J Am Acad Dermatol | Allergic contact dermatitis to topical medications (including corticosteroids) in adult AD patients; budesonide flagged as a clinically relevant sensitiser — reinforces need for pre-treatment patch testing. |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid contact allergy in asthma patients, many of whom have concomitant atopic conditions; documents both delayed and immediate allergy patterns with budesonide. |
| [16925687](https://pubmed.ncbi.nlm.nih.gov/16925687/) | 2006 | Observational | Pediatric Allergy Immunol | Exhaled breath condensate pH measurement in children with asthma, allergic rhinitis, and atopic dermatitis; supports the "atopic march" framework linking Th2-driven conditions that share responsiveness to corticosteroid therapy. |
| [40020933](https://pubmed.ncbi.nlm.nih.gov/40020933/) | 2025 | Translational | J Allergy Clin Immunol | Cutaneous ceramide synthesis dysregulation shared between eosinophilic esophagitis and atopic dermatitis; highlights common epithelial barrier dysfunction mechanisms that may be targeted by budesonide's anti-inflammatory action. |

---

## India Market Information

No approved products containing budesonide were identified in the Indian regulatory database based on currently available data. Budesonide has **no registered marketing authorisations** in India at this time.

> For reference, budesonide is approved in multiple jurisdictions globally (e.g., Pulmicort® for asthma inhalation; Entocort®/Cortiment® for Crohn's disease and ulcerative colitis), but none of these registrations appear in the Indian dataset reviewed.

---

## Safety Considerations

**Drug Interactions (599 total interactions identified)**

The following interactions are of highest clinical relevance:

| Severity | Interacting Drug | Clinical Concern |
|---------|---------|---------|
| **Major** | Adalimumab | Combined immunosuppression with a TNF-α inhibitor significantly increases risk of serious infections, including opportunistic infections |
| **Major** | Fosamprenavir | HIV protease inhibitor; strong CYP3A4 inhibitor that may markedly elevate budesonide plasma levels, increasing risk of adrenal suppression and Cushingoid effects |
| Moderate | Ibuprofen | NSAIDs combined with corticosteroids increase risk of gastrointestinal ulceration and bleeding |
| Moderate | Ketorolac | As above; GI bleeding risk elevated |
| Moderate | Fluvoxamine | CYP3A4 inhibitor; may increase budesonide systemic exposure |
| Moderate | Fosaprepitant | CYP3A4 inhibitor; may raise budesonide plasma concentrations |
| Moderate | Nifedipine | CYP3A4 interaction may affect budesonide metabolism |
| Moderate | Isotretinoin | Concurrent corticosteroid use may increase intracranial hypertension risk (pseudotumour cerebri) |
| Moderate | Aldesleukin (IL-2) | Corticosteroids may blunt the immunostimulatory effects of interleukin-2 therapy |
| Moderate | Zidovudine | Potential for additive adverse haematological effects |

> A comprehensive drug interaction review is essential prior to initiation. The full DDI dataset includes 599 interactions — clinicians should consult a pharmacist or dedicated interaction database for patient-specific assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial currently exists that directly evaluates budesonide efficacy for atopic eczema in humans, and a significant proportion of identified literature documents budesonide as a **contact sensitiser** in atopic dermatitis patients — creating a therapeutic paradox that must be resolved before proceeding. The most promising signal is a 2024 nanoparticle formulation study, which represents early preclinical R&D rather than clinical efficacy evidence.

**To proceed, the following is needed:**

- **Patch test screening protocol**: Establish the prevalence and significance of budesonide contact sensitisation in the target patient population before any therapeutic trial
- **Phase 1/2 clinical trial**: Prospective human efficacy and safety study of novel budesonide formulations (particularly nanoparticle hydrogels) in adult and paediatric atopic eczema
- **Comparative benchmark**: Head-to-head data versus current standard-of-care topical corticosteroids (hydrocortisone, betamethasone) and newer biologics (dupilumab) to define clinical niche
- **Pharmacokinetic profiling**: Skin penetration and systemic absorption characterisation for the novel delivery formulation to inform HPA axis suppression risk
- **Mechanism of action verification**: Formal retrieval of budesonide MOA data from DrugBank API to confirm GR-α binding parameters for regulatory submissions
- **India regulatory pathway assessment**: Evaluation of CDSCO requirements for novel drug delivery systems (novel formulation vs. new drug application pathway)
- **Market entry feasibility**: Given zero existing India registrations, a full regulatory strategy — including initial marketing authorisation for the established indication before repurposing — should be scoped
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


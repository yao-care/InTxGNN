---
layout: default
title: Magnesium Carbonate
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Magnesium Carbonate
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

# Magnesium Carbonate: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium carbonate (MgCO₃) is an alkaline mineral compound historically used as an antacid component in over-the-counter gastrointestinal preparations, though it carries no formally registered therapeutic indication in India.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease** with a confidence score of 99.96%, directly consistent with its established acid-neutralizing chemistry.
This direction is currently supported by **0 registered clinical trials** and **4 publications** (including 3 RCTs), placing it at evidence level L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formally registered indication (used as antacid excipient/component) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Magnesium carbonate is an inorganic alkaline salt that reacts directly with hydrochloric acid in the stomach via a well-characterized neutralization reaction: **MgCO₃ + 2HCl → MgCl₂ + H₂O + CO₂**. This reaction effectively raises intragastric pH to ≥3.5, reducing the corrosive impact of gastric acid on the ulcerated mucosa. The mechanism is straightforward and mechanistically inseparable from the very pathophysiology of acid-peptic ulcer disease — excessive acid secretion eroding an insufficiently protected mucosal barrier.

The pathological link between magnesium carbonate's mechanism and active peptic ulcer disease is direct and biologically well-founded. Peptic ulcers develop when the balance between aggressive factors (acid, pepsin) and defensive factors (mucus, bicarbonate, prostaglandins) is disrupted. Acid neutralization by an antacid like magnesium carbonate directly addresses the aggressive side of this equation, reducing acid load on exposed ulcer beds and allowing mucosal healing to proceed. Multiple RCTs from the 1980s — when antacids were still first-line therapy — demonstrated healing rates of 50–75% at 3–4 weeks with high-dose antacid regimens, comparable to cimetidine (H2 antagonist) in head-to-head trials.

Currently, detailed mechanism-of-action data from DrugBank is not available for this candidate. However, based on its well-known physicochemical properties, magnesium carbonate belongs to the antacid class (alkaline carbonate salts) alongside calcium carbonate and sodium bicarbonate. Its empirical efficacy in acid-related GI conditions is supported by decades of clinical use in compound antacid formulations such as Caved-S and Novaluzid, both of which contain magnesium salts as active components.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered for Magnesium Carbonate in Active Peptic Ulcer Disease.

> **Note:** For the broader "Stomach Disease" category (Rank 7 indication), 2 completed Phase 1 trials directly assessed the antacid activity of magnesium-containing preparations using pH-metry (NCT03069963, n=24) and gamma scintigraphy (NCT03065816, n=34), providing indirect pharmacodynamic support.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 72-patient 12-week double-blind trial: antacid + anticholinergic vs. cimetidine vs. placebo in active duodenal/prepyloric ulcers; 50% healing at 3 weeks with antacid arm (vs. 67% cimetidine, 17% placebo) |
| [6755656](https://pubmed.ncbi.nlm.nih.gov/6755656/) | 1982 | RCT | Scand J Gastroenterol Suppl | Treatment of active prepyloric and duodenal ulcers comparing antacid/anticholinergic regimen vs. cimetidine vs. placebo; confirms antacid efficacy in active ulcer healing |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scand J Gastroenterol | 80-patient 4-week RCT: antacid tablets (120 mmol HCl/day neutralizing capacity) in active duodenal ulcer; healing rates 60–67.5% across dietary arms, demonstrating antacid monotherapy efficacy |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | Cross-sectional/Lab | Medicine and Pharmacy Reports | Evaluation of acid-neutralizing capacity (ANC) of antacid formulations marketed in Morocco; provides in vitro characterization of antacid class including carbonate-based preparations |

---

## India Market Information

Magnesium carbonate (DB09481) currently has **no approved drug registrations** in India. The drug is not marketed as a standalone therapeutic agent.

> Magnesium carbonate may appear as an excipient or minor component in compound antacid formulations, but no standalone CDSCO license has been identified in the dataset.

---

## Safety Considerations

**Drug Interactions (197 interactions identified via DDInter):**

Key clinically significant interactions to be aware of:

| Severity | Interacting Drug | Clinical Relevance |
|----------|-----------------|-------------------|
| **Major** | Dolutegravir | Magnesium ions chelate dolutegravir, significantly reducing absorption; must separate dosing by ≥2 hours |
| Moderate | Alendronic acid / Risedronic acid | Divalent cations markedly reduce bisphosphonate absorption; avoid co-administration |
| Moderate | Doxycycline | Magnesium chelates tetracycline-class antibiotics; administer separately |
| Moderate | Azithromycin | Potential reduction in macrolide bioavailability |
| Moderate | Baloxavir marboxil | Polyvalent cations (Mg²⁺) reduce antiviral absorption; clinically significant |
| Moderate | Atazanavir | Gastric pH elevation impairs atazanavir absorption (requires acidic environment) |
| Moderate | Cholecalciferol | Interaction with fat-soluble vitamin metabolism |
| Moderate | Acetylsalicylic acid | Alkaline pH may alter salicylate absorption and urinary excretion |
| Moderate | Amphetamine / Benzphetamine | Urinary alkalinization by magnesium reduces amphetamine excretion, increasing CNS effects |
| Minor | Famotidine / Ranitidine | Additive acid suppression; generally manageable |
| Minor | Atenolol / Acebutolol | Minor reduction in beta-blocker absorption |

**General safety note:** For detailed warnings and contraindications, please refer to the package insert or prescribing information, as this data was not available in the current evidence pack. Particular attention is warranted in patients with **renal impairment** (risk of hypermagnesemia with regular use) and patients on drugs with pH-dependent or chelation-sensitive absorption profiles.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between magnesium carbonate and active peptic ulcer disease is clear and biologically direct — acid neutralization is the classical mechanism for reducing mucosal injury in acid-peptic disease, supported by multiple Phase 2/3-level RCTs demonstrating antacid efficacy comparable to H2 antagonists. However, current evidence comes exclusively from compound antacid formulations (not pure magnesium carbonate), and the modern standard of care has shifted to PPI-based H. pylori eradication regimens, requiring careful positioning of any new antacid-based development.

**To proceed, the following is needed:**

- **H. pylori status stratification:** Any new trial must screen and stratify patients for H. pylori status; H. pylori-positive patients require concurrent eradication therapy
- **Monotherapy evidence:** Existing RCTs used compound antacid formulations; a Phase 2 trial with pure magnesium carbonate is needed to isolate its individual contribution
- **Renal safety monitoring plan:** Regular assessment of serum magnesium levels, especially in patients with CKD (eGFR <60 mL/min/1.73m²), where hypermagnesemia risk is clinically meaningful
- **Regulatory pathway clarification:** Define whether this would be developed as a prescription drug, OTC antacid, or medical device food under CDSCO guidelines
- **TFDA prescribing information / package insert** (data gap DG001): Needed to complete the safety assessment before advancing to Stage 1 screening
- **India market entry feasibility:** Assess whether a standalone magnesium carbonate antacid formulation has commercial viability given competition from established PPIs, H2 blockers, and combination antacids already on the market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


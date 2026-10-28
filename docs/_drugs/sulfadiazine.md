---
layout: default
title: Sulfadiazine
parent: Model Prediction Only (L5)
nav_order: 796
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "Sulfadiazine"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis"]
description: "Sulfadiazine: predicted new indication Pneumocystosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Sulfadiazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Sulfadiazine: Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Sulfadiazine is a sulfonamide antibacterial and antiparasitic agent, originally used for toxoplasmosis and related conditions.
The TxGNN model predicts it may be effective for **pneumocystosis**,
but **no clinical trials** are registered and the supporting **literature (19 publications)** is mostly reviews and case reports that do not directly test sulfadiazine for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 16 of 16) |
| Number of Registrations | 16 (valid: 16) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Sulfadiazine belongs to the sulfonamide class, which inhibits dihydropteroate synthase (DHPS) in the folate synthesis pathway. Its efficacy in toxoplasmosis is established, and mechanistically it may be applicable to pneumocystosis.

*Pneumocystis jirovecii* depends on the same folate pathway. The related sulfonamide sulfamethoxazole, combined with trimethoprim, is the standard treatment and prophylaxis for *Pneumocystis* pneumonia. This gives a plausible class-level rationale. One supplied paper also shows that DHPS mutations in *P. jirovecii* confer cross-resistance to sulfa drugs, which supports the idea that sulfonamides act on this target.

However, none of the supplied records shows direct evidence of sulfadiazine efficacy against *Pneumocystis*. Most of the literature covers sulfadiazine in toxoplasmosis and AIDS-related opportunistic infections, or discusses trimethoprim-sulfamethoxazole. Sulfadiazine is not a recognised first-line agent for this indication, and cotrimoxazole is far better established. The very high TxGNN score is a computational prediction and does not replace clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29604970](https://pubmed.ncbi.nlm.nih.gov/29604970/) | 2018 | Review | Handbook of Clinical Neurology | CNS *Toxoplasma* infection in HIV patients; discusses prophylaxis with trimethoprim-sulfamethoxazole |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Drugs of choice for parasitic diseases; quinine-pyrimethamine-sulfadiazine for resistant malaria, trimethoprim-sulfamethoxazole for pneumocystis pneumonia |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including *Pneumocystis* and *Toxoplasma* |
| [9097375](https://pubmed.ncbi.nlm.nih.gov/9097375/) | 1997 | Review | Seminars in Respiratory Infections | Toxoplasma pneumonia in AIDS and other cell-mediated immunity defects |
| [7909657](https://pubmed.ncbi.nlm.nih.gov/7909657/) | 1994 | Review | Annals of Internal Medicine | Advances in managing AIDS-related opportunistic infections |
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | Not classified | Clinical Pharmacy | Pyrimethamine-sulfadiazine for *Pneumocystis carinii* pneumonia and toxoplasmosis in AIDS (no abstract available) |
| [2060528](https://pubmed.ncbi.nlm.nih.gov/2060528/) | 1991 | Retrospective chart review | Eur J Clin Microbiol Infect Dis | 35 AIDS patients on toxoplasmosis maintenance therapy; relapses of both toxoplasmosis and pneumocystosis seen |
| [15673759](https://pubmed.ncbi.nlm.nih.gov/15673759/) | 2005 | Laboratory study | Antimicrob Agents Chemother | *P. jirovecii* DHPS mutations confer cross-resistance to sulfa drugs |
| [9122147](https://pubmed.ncbi.nlm.nih.gov/9122147/) | 1997 | Not classified | Presse Médicale | Prevention of parasitic infections in HIV; trimethoprim-sulfamethoxazole is the treatment of choice for *Pneumocystis* prophylaxis |
| [34941194](https://pubmed.ncbi.nlm.nih.gov/34941194/) | 2021 | Case report and review | Medicine | Acute exacerbation of pulmonary toxoplasmosis during corticosteroid therapy |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 200254 | Salphaz Tablet | Strip of 10 tablets | Not specified |
| 38277 | Clavora Cream | Tube of 20 gm cream | Not specified |
| 204669 | Silverine 1% Cream | Tube of 20 gm cream | Not specified |
| 209656 | Saphrine 1%/0.2% Ointment | Tube of 15 gm ointment | Not specified |
| 201048 | Silvez Plus 1%/0.2% Cream | Tube of 15 gm cream | Not specified |

Of the 16 valid registrations, 15 are topical creams or ointments. Only Salphaz Tablet is an oral product. Pneumocystosis would require systemic (oral or intravenous) dosing, so the topical products are not relevant to this indication.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Conditions linked to sulfadiazine include porphyria, kidney disease, liver disease, gallbladder disease, haematologic disease (thrombocytopenia, neutropenia, agranulocytosis, leukopenia, aplastic anaemia, macrocytic anaemia, folic acid deficiency anaemia), G6PD deficiency, slow acetylation, asthma, urinary tract obstruction, cystinuria, galactosemia and glycogen storage disease.
- **Drug Interactions**: 82 interactions were recorded. The main ones listed are Moderate and include:
  - Sulfonylureas and meglitinides (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, repaglinide, nateglinide), with a risk of hypoglycaemia
  - Multiple insulin products (aspart, degludec, detemir, glargine, glulisine, lispro, human insulins)
  - Balsalazide, picosulfuric acid and naltrexone
- **Other considerations**: Systemic sulfonamides carry risks such as hypersensitivity and crystalluria.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a class-level mechanistic link (DHPS inhibition) and a computational prediction. No trials are registered, and no supplied study shows sulfadiazine efficacy against *Pneumocystis*. Established alternatives, especially trimethoprim-sulfamethoxazole, are far better supported, so the evidence is insufficient to advance.

**To proceed, the following is needed:**
- Direct evidence of sulfadiazine activity against *Pneumocystis* (in vitro or animal models, or clinical data)
- A comparison with trimethoprim-sulfamethoxazole to show a clinical niche, such as cotrimoxazole intolerance
- Detailed mechanism of action data
- Package insert warnings and contraindications for the systemic (oral) product, which are currently missing and block safety screening
- A safety monitoring plan for haematologic, renal and hypersensitivity risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


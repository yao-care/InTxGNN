---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

# Carvedilol: From Heart Failure / Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Carvedilol is a dual α1 and β-adrenoceptor blocker widely used in cardiovascular medicine for hypertension and heart failure. The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, though **no clinical trials** and **no direct publications** currently support this specific direction. The prediction rests on mechanistic reasoning — carvedilol's dual adrenoceptor blockade reduces renal perfusion pressure and suppresses renin secretion, offering a plausible renoprotective pathway that warrants further investigation before clinical advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure / Hypertension (dual α1+β adrenoceptor blockade; India regulatory data pending) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from structured data sources. Based on information embedded in the repurposing rationale, Carvedilol functions as a dual α1 and β-adrenoceptor blocker that simultaneously reduces systemic vascular resistance (via α1 blockade) and suppresses renin secretion (via β blockade). This dual sympatholytic profile positions it differently from pure beta-blockers or ACE inhibitors in the cardiovascular spectrum.

Malignant hypertensive renal disease is characterized by accelerated, severe hypertension causing acute end-organ damage in the kidneys — including fibrinoid necrosis of small renal vessels and rapidly progressive renal impairment. Carvedilol's ability to reduce renal perfusion pressure through both vasodilatory and renin-suppressive mechanisms provides a theoretically sound basis for limiting further nephron injury in the post-acute stabilization phase. The sympathetic nervous system plays a pivotal role in both sustaining pathologically elevated blood pressure and amplifying renin-angiotensin axis activation, both of which are attenuated by carvedilol.

Importantly, malignant hypertension with renal involvement typically demands rapid parenteral blood pressure reduction in the acute emergency phase, where oral carvedilol's pharmacokinetic profile limits its utility. The more realistic clinical positioning for carvedilol is as adjunctive oral therapy during the stabilization and chronic management phase — complementing ACE inhibitors or ARBs (which directly target the renin-angiotensin axis driving renovascular injury) rather than replacing them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

No product registrations for Carvedilol were found in the India regulatory database. India CDSCO registration status should be independently verified, as Carvedilol is a widely marketed cardiovascular agent in many jurisdictions and data collection may be pending for this project.

---

## Safety Considerations

**Drug Interactions** (329 total interactions identified; representative major and moderate interactions listed below):

| Severity | Drug | Clinical Note |
|----------|------|---------------|
| **Major** | Epinephrine | Combined use may cause severe hypertension and reflex bradycardia due to unopposed α-adrenergic stimulation |
| Moderate | Hydrocortisone | Corticosteroids may antagonize the antihypertensive effect |
| Moderate | Dexamethasone | Same class concern as hydrocortisone |
| Moderate | Betamethasone | Same class concern as hydrocortisone |
| Moderate | Budesonide | Same class concern as hydrocortisone |
| Moderate | Triamcinolone | Same class concern as hydrocortisone |
| Moderate | Bupropion | Risk of increased carvedilol exposure via CYP2D6 inhibition |
| Moderate | Morphine | Additive hypotensive and bradycardic effects |
| Moderate | Atropine | Anticholinergic agents may partially counteract carvedilol's cardiac effects |
| Moderate | Hyoscyamine | Same class concern as atropine |
| Moderate | Canagliflozin | Beta-blockers may mask hypoglycaemia symptoms in diabetic patients on SGLT2 inhibitors |
| Moderate | Calcium carbonate / Phosphate / Acetate / Citrate | Divalent cations may reduce carvedilol absorption |
| Minor | Acetylsalicylic acid | Generally minor; monitor for blunted antihypertensive response |
| Minor | Aluminum hydroxide | Reduced carvedilol absorption possible; space administration |

Please refer to the full package insert for complete warnings and contraindications, including use in acute decompensated heart failure, bronchospastic disease, and significant bradycardia or AV block.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.55%) based on topological similarity within the knowledge graph, and the mechanistic reasoning for carvedilol in malignant hypertensive renal disease is pharmacologically coherent. However, with zero registered clinical trials and zero directly relevant publications, the current evidence base meets only an L4 threshold (mechanistic reasoning only) — insufficient to recommend clinical development or repurposing without further foundational evidence.

**To proceed, the following is needed:**

- **MOA data**: Retrieve carvedilol's DrugBank structured pharmacology entry (targets, enzymes, transporters) to formalize the mechanistic rationale
- **India CDSCO regulatory verification**: Confirm actual market status via CDSCO database; current data appears to be a pipeline placeholder (0 licenses in a market where carvedilol is broadly available)
- **Safety gap closure**: Download and parse the CDSCO-approved package insert (PDF) to populate key warnings and contraindications — currently blocking S1 safety assessment
- **Targeted literature search**: Broaden PubMed search to carvedilol + "hypertensive nephropathy", "chronic kidney disease", and "renal protection" to surface indirect evidence that may support mechanistic credibility
- **Preclinical evidence scoping**: Identify animal or in vitro studies examining carvedilol's direct effect on renal microvascular injury under malignant hypertension conditions
- **Interaction risk review**: The major interaction with Epinephrine (used in anaphylaxis/resuscitation) is clinically significant — this must be formally addressed in any safety monitoring plan before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


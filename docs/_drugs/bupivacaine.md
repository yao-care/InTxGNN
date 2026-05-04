---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Bupivacaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is a long-acting local anesthetic widely used for regional anesthesia, nerve blocks, and perioperative pain management. The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans (ACA)**, a late-stage cutaneous manifestation of Lyme borreliosis. However, there are currently **0 clinical trials** and **0 publications** supporting this direction, making the evidence base extremely limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anesthesia / regional anesthesia (not registered in India; based on established pharmacological use) |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this analysis. Based on known pharmacological information, Bupivacaine is a long-acting amide-type local anesthetic that blocks voltage-gated sodium channels (Nav), thereby inhibiting the propagation of action potentials in sensory and motor neurons. Beyond its anesthetic effect, local anesthetics as a class are known to exert secondary anti-inflammatory properties — including inhibition of NF-κB signalling and downregulation of pro-inflammatory cytokines such as IL-6 and TNF-α.

Acrodermatitis chronica atrophicans (ACA) is a chronic skin condition caused by persistent *Borrelia burgdorferi* infection and is characterised by progressive dermal atrophy, fibrosis, and ongoing local inflammation. In theory, the anti-inflammatory side effects of local anesthetics could provide some symptomatic relief of the inflammatory component of ACA. However, the core pathology — spirochaetal persistence and connective tissue degradation — has no known intersection with sodium channel blockade.

The high TxGNN score most likely reflects shared topological features between skin inflammation nodes in the knowledge graph, rather than a genuine pharmacological link. This is a case where graph-based prediction may be capturing indirect structural associations rather than mechanistically actionable biology, and the prediction should be interpreted with significant caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Bupivacaine currently has no registered products in India. No authorization records are available.

---

## Safety Considerations

**Drug Interactions:** A total of 56 drug interactions have been identified for Bupivacaine. Key interactions include:

| Interacting Drug | Interaction Level | Clinical Note |
|-----------------|------------------|---------------|
| Aprepitant | Moderate | CYP3A4 inhibition may increase bupivacaine plasma levels |
| Morphine (liposomal) | Moderate | Combined CNS/respiratory depression risk with concurrent opioid use |
| Dexamethasone | Unknown | Often co-administered for nerve blocks; interaction profile requires monitoring |
| Ondansetron | Unknown | QT-interval prolongation risk may be additive |
| Metronidazole | Unknown | Potential CNS toxicity interaction; use with caution |
| Atropine | Unknown | Anticholinergic effects may mask signs of local anesthetic toxicity |
| Naloxone | Unknown | Used in overdose management; interaction monitoring advised |
| Metoclopramide | Unknown | Potential for additive neurotoxicity |
| Triamcinolone | Unknown | Commonly co-administered in joint/epidural blocks; systemic interaction unclear |
| Vancomycin | Unknown | No established interaction, but concurrent use in surgical settings warrants monitoring |

> For complete warnings and contraindications, please refer to the approved package insert, as formal label data was not available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial, observational, or published literature evidence supporting the use of Bupivacaine in acrodermatitis chronica atrophicans. The mechanistic link is extremely weak — the TxGNN prediction appears to be driven by shared graph topology in the skin inflammation domain rather than a real pharmacological rationale. The safety profile of systemic Bupivacaine administration also introduces meaningful risk without any evidence-based benefit to justify progression.

**To proceed, the following is needed:**

- Formal MOA documentation from DrugBank (DG002) to enable mechanistic plausibility assessment
- Retrieval and parsing of the approved package insert to populate key warnings and contraindications (DG001)
- A hypothesis-generating preclinical study (in vitro or animal model) demonstrating any bupivacaine effect on *Borrelia*-induced skin inflammation or fibrosis
- Exploration of whether IV lidocaine (same class, more systemic safety data) has any published evidence in ACA or related spirochaetal skin conditions — which would strengthen or weaken the class-level rationale
- If proceeding to exploratory investigation, a risk assessment for systemic administration routes should be conducted, given bupivacaine's known cardiotoxicity at supratherapeutic levels
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


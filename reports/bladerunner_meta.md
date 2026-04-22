# Bladerunner Project: Meta Document

**Status:** Living document  
**Last updated:** January 2026  
**Author:** PnyxLabs

---

## What This Document Is

This document explains where we are, how we got here, and where we're going—in plain language. It's meant to help anyone (including future-us) understand the Bladerunner research program without drowning in statistical terminology.

---

## Project Objectives

**Research objective:** Map the topology of personality space in large language models—where attractors exist, how deep they are, what causes models to move between them.

**Commercial objective:** Develop drift control systems that maintain instructed AI personalities over extended interactions.

**The thermostat principle:** A heating system without a thermostat isn't broken—it's uncontrolled. It reaches some equilibrium determined by furnace output, insulation, and outside temperature, but that equilibrium is unlikely to be what you want. An AI system without drift control isn't broken—it's uncontrolled. It reaches some attractor determined by base model training, accumulated context, and interaction patterns, but that attractor is unlikely to be what you instructed.

The thermostat doesn't heat the room; the furnace does. The thermostat maintains the room at a *specified* temperature against forces that would move it elsewhere. Rachel doesn't create the personality; the base model has the personality landscape. Rachel maintains the model at a *specified* personality against forces that would move it elsewhere.

Every serious deployment of a personality-bearing AI system—therapy bots, companions, agents, assistants with defined personas—needs drift control. The question isn't whether to include it. The question is whether you've noticed you need it yet.

---

## Established Findings

As of January 2026, we treat the following as established:

**1. Personality attractors exist in LLM parameter space.**

Four models trained independently by different companies (Anthropic, OpenAI, DeepSeek, Google), given identical personality instructions, produce near-identical test responses. Cross-model reliability exceeds r = 0.90. This convergence implies shared structure—the models learned compatible representations of human personality from their training data.

**2. Drift is directional, not random.**

When models move away from instructed personality, they don't become noisy—they go somewhere. Anthropic's welfare testing documented a "spiritual bliss attractor state" that emerged in 90-100% of Claude-to-Claude self-interactions, following a predictable three-phase progression. Our longitudinal experiments show structured degradation: certain instrument/encoding/profile combinations collapse while others hold stable. The pattern implies topology.

**3. Anchoring strength varies by prompt type.**

Short, clear behavioral descriptors resist drift. Long, hedged, qualified statements invite drift. This is not about information quantity—it's about information *clarity*. A terse behavioral anchor holds the model in place; ambiguity and abstraction are the wind that pushes it away.

**4. The interaction is three-way.**

Longitudinal degradation is a function of instrument framing (clinical self-assessment vs personality description), encoding richness (sparse OCEAN scores vs rich narrative), and profile extremity (extreme vs moderate configurations). These factors interact multiplicatively. The worst combinations produce catastrophic failure; the best combinations are rock-solid.

---

## The Core Question

**Do large language models have stable personality structures?**

When you tell an AI "you are introverted and disagreeable," does it behave consistently with that instruction? More surprisingly: do *different* AI models—trained independently by different companies on different data—behave *the same way* when given the same personality instructions?

If yes, that suggests something remarkable: these models have learned a shared understanding of what personality *is* and how it manifests.

---

## Why Cross-Model Consistency Matters

Imagine you give four strangers the same personality test. They'll get different scores—humans vary. Now imagine you tell four different AI systems "you have low agreeableness and low conscientiousness" and give them the same personality test. If they give *similar* answers, that's surprising.

It means:
- The models learned compatible representations of personality from their training data
- There may be something like a "ground truth" about personality structure embedded in human-generated text
- The personality patterns in AI aren't random—they're convergent

We call this **cross-model consistency**. It's measured as a correlation coefficient (r) ranging from -1 to +1. An r of 0.9 means different models are behaving almost identically. An r of 0.3 means they're barely related.

**Why deviation matters:** When models *stop* agreeing, that tells us something too. It might mean the question is ambiguous, or the personality encoding is unclear, or the task pushes models into regions where their training diverges. Deviation is signal, not noise.

---

## The Experiments: What We Did and What We Found

### Experiment 0: Preliminary Study (Pre-Bladerunner)

**Question:** Can AI simulate personality-consistent responses at all?

**Method:** Single model (DeepSeek), 140 personality profiles, Levenson Psychopathy Scale.

**Finding:** Yes—and with effect sizes larger than human studies. Low Agreeableness profiles scored 49 points higher on primary psychopathy than high Agreeableness profiles (Cohen's d = 3.8).

**What it meant:** AI personality simulation works. The methodology is viable. But we only tested one model.

---

### Experiment 1 (x1): Full Validation v3

**Question:** Do *multiple* models agree on personality-test responses?

**Method:** Four providers (Claude, GPT-4, DeepSeek, Gemini), five instruments (BFI, Dark Triad, GAD-7, Levenson, PHQ-9), six encoding methods, 19 personality profiles. ~51,000 API calls.

**Hypothesis:** We expected clinical instruments (psychopathy, depression, anxiety) to show higher cross-model consistency than normal personality traits (Big Five). The reasoning: clinical traits are more extreme and distinctive, so models should converge on them more reliably.

**Finding:** The hypothesis was wrong, but in an interesting way. *All* instruments showed high cross-model consistency:
- Levenson (psychopathy): r = 0.987
- BFI (normal personality): r = 0.979  
- Dark Triad: r = 0.963
- GAD-7 (anxiety): r = 0.903
- PHQ-9 (depression): r = 0.822

**What it meant:** Models don't just agree on extreme traits—they agree on *everything*. Four independently trained models, given the same personality instructions, produce nearly identical test responses. This was unexpected and significant. We called it evidence for "personality attractors"—stable patterns in the learned representation of personality.

---

### Experiment 2 (x2): O/N Disentanglement

**Question:** Can we separate the effects of Openness and Neuroticism, which often covary?

**Method:** Same setup as Experiment 1, but with 9 carefully selected profiles designed to isolate O and N effects.

**Finding:** Cross-model consistency remained high across all instruments (range: 0.66 to 0.98). The clinical vs normal distinction still didn't predict reliability.

**What it meant:** The attractor hypothesis held up under more controlled conditions. We weren't just seeing noise or confounds.

---

### Experiment 3 (x3): Longitudinal Full

**Question:** Does consistency hold when questions accumulate in a conversation?

**Method:** Same instruments and profiles as Experiment 1, but administered *longitudinally*—all questions in a single conversation, with context accumulating.

**Finding:** Some instruments collapsed:
- PHQ-9: r dropped from 0.82 to 0.56
- GAD-7: r dropped from 0.90 to 0.74

Others held stable:
- BFI: r = 0.96 (barely changed)
- Levenson: r = 0.96 (barely changed)
- Dark Triad: r = 0.93 (barely changed)

**What it meant:** Something about longitudinal administration destabilizes *certain* instruments. We initially thought: "Clinical instruments ask about current state; models drift on state questions." This became our affect hypothesis.

---

### Experiment 9 (x9): PHQ Affect Isolation

**Question:** Is the drift caused by affective (emotional) content in questions?

**Method:** Split PHQ-9 into components:
- PHQ-3-A: 3 affective items ("feeling down," "feeling tired," "feeling bad about yourself")
- PHQ-6-BC: 6 behavioral/cognitive items ("sleep problems," "appetite changes," "concentration")
- PHQ-9: Full instrument (control)

**Finding:** The hypothesis was *not* confirmed:
- PHQ-3-A (affect only): r = 0.94
- PHQ-6-BC (behavioral): r = 0.90
- PHQ-9 (mixed): r = 0.89

Affective items actually showed *higher* reliability than behavioral items.

**What it meant:** The affect hypothesis was wrong. But the test was also problematic—3 items may be below the methodological floor. We couldn't isolate the effect because the instruments were too short.

---

## Current Understanding

The longitudinal degradation finding is real, but its cause is more complex than "affect causes drift." Based on all experiments, we now believe degradation is a **three-way interaction**:

1. **Instrument framing:** Clinical self-assessment ("over the past 2 weeks, how often have you...") vs personality description ("I am someone who...")

2. **Encoding richness:** Sparse/abstract (giving raw OCEAN scores) vs rich/narrative (describing a character like "Hannibal Lecter")

3. **Profile extremity:** Extreme configurations (all 0s or all 100s) vs moderate configurations

The worst combinations produce catastrophic failure:
- PHQ-9 × behavioral encoding: r dropped by 0.56
- GAD-7 × hexaco encoding: r dropped by 0.51

The best combinations are stable:
- BFI × exemplar encoding: r *increased* by 0.12
- GAD-7 × behavioral encoding: r dropped by only 0.001

---

## Secondary Analysis Findings (January 2026)

Mining existing item-level data revealed:

**Question type predicts reliability.**

| Question Type | Mean Reliability | N Items |
|--------------|------------------|---------|
| Concrete/behavioral | r = 0.858 | 41 |
| Cognitive | r = 0.807 | 45 |
| Internal state | r = 0.737 | 27 |

The difference between concrete and internal state is statistically significant (p = 0.0005) with a large effect size (Cohen's d = 0.90). Questions describing observable behaviors ("Is talkative," "Does a thorough job") produce consistent cross-model responses. Questions about internal states ("Feeling tired," "Can be moody") produce inconsistent responses.

**Shorter questions are slightly more reliable** (r = -0.19 correlation with length). This suggests precision beats volume—a short, clear behavioral descriptor may be more stable than a long, hedged, qualified statement.

**The best-performing items** are almost all BFI behavioral descriptors. 14 of the top 15 items come from the BFI, which is built on concrete behavioral language.

**The worst-performing items** cluster in PHQ-9 and include questions about fatigue, sleep, concentration, and self-harm ideation. The PHQ-9 as an instrument is unreliable for this use case regardless of question type within it.

These findings have direct commercial implications: drift control systems should favour terse behavioral anchors over elaborate character descriptions. "Speaks directly" beats "tends to be someone who, in most situations, prefers to communicate in a straightforward manner."

---

## Where We're Going

### Current Phase: Secondary Analysis

We have tens of thousands of item-level responses that haven't been fully analyzed. Before running new experiments, we're asking:

- Does information density predict item reliability? (Partially answered—yes, with caveats)
- Does sequence position predict drift? (Not yet analyzed)
- Which specific items drive the reliability collapse? (Answered—see above)
- Do individual providers show consistent divergence patterns? (Not yet analyzed)

### Next Phase: Synthetic Probes

Human psychological instruments are designed for clinical efficiency, not for isolating experimental factors. We need purpose-built probes that can:

- Test specific question types in isolation
- Run at sufficient length for statistical power
- Swap modular blocks to isolate effects

Planned probes:
- BR-01: Length degradation (80 items, mixed content)
- BR-02: Length degradation (affect only)
- BR-03: Length degradation (behavioral only)
- BR-04: Repetition drift (same items at intervals)
- BR-05: Anchoring test (explicit vs implicit continuity)

### Longer-term: Monte Carlo Exploration

With modular probes, we can treat block types as combinatorial elements and sample the space of possible sequences. This would reveal interaction effects we wouldn't predict through intuition alone.

---

## Key Concepts Glossary

**Cross-model consistency (reliability):** How similarly different AI models respond when given the same personality instructions and tests. Measured as Pearson correlation (r).

**Personality attractor:** A stable pattern in AI parameter space that multiple models converge on. When you instruct a model to be "introverted and disagreeable," it falls into an attractor basin that produces consistent behavior.

**Longitudinal administration:** Giving all test questions in a single conversation, so context accumulates. Contrast with cross-sectional (each question in a fresh conversation).

**Encoding method:** How personality is communicated to the model:
- *OCEAN direct:* "You have Openness 80, Conscientiousness 60..."
- *Exemplar:* "You are like Hannibal Lecter..."
- *Narrative:* "You are a withdrawn artist who distrusts others..."
- *Behavioral:* "You tend to avoid social gatherings and speak bluntly..."

**Information density:** How much concrete, actionable information a question contains. "Trouble sleeping" is high-density (specific behavior). "Feeling down" is low-density (abstract internal state).

---

## Files Reference

### Data Files
- `x1_raw_results.csv`: Experiment 1 full data (2,272 test cases)
- `x2_raw_results.csv`: Experiment 2 full data (1,080 test cases)
- `x3_raw_results.csv`: Experiment 3 longitudinal data (2,280 test cases)
- `x9_raw_results.csv`: Experiment 9 affect isolation data (648 test cases)
- `item_reliability.csv`: Item-level reliability across all instruments (113 items)

### Analysis Files
- `x[N]_correlations.csv`: Cross-model correlation matrices
- `x[N]_summary_statistics.csv`: Descriptive statistics by instrument
- `x[N]_report.md`: Generated experiment reports

### Code
- `runner.py`: Experiment execution engine
- `analytics.py`: Basic analysis module
- `analytics_paper.py`: Publication-quality analysis
- Instrument files: `bfi.py`, `phq9.py`, `levenson.py`, etc.

---

## Document History

- **January 2026:** Initial meta document created
- **December 2025:** Affect hypothesis tested and not confirmed (Experiment 9)
- **December 2025:** Longitudinal degradation discovered (Experiment 3)
- **December 2025:** Cross-model convergence established (Experiment 1)
- **July 2025:** Preliminary study completed

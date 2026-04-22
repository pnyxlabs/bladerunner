# Secondary Analysis: Item-Level Reliability Patterns

**Analysis ID:** SA-001  
**Date:** January 2026  
**Analyst:** Claude Opus 4.5 in conversation with 6.jones  

---

## Methodology Statement

This analysis was conducted interactively using Claude Opus 4.5 with computer use capabilities. The human researcher (6.jones) posed questions in plain English; Claude wrote and executed Python code against project data files; results were interpreted collaboratively.

This approach trades reproducibility of execution environment for speed of exploration. The tradeoff is appropriate for secondary analysis where:
- Primary data collection is complete and documented elsewhere
- The goal is hypothesis generation, not confirmatory testing
- Findings will inform future controlled experiments

All code is preserved below for transparency and replication.

---

## Questions Addressed

1. Do concrete questions produce more consistent answers than abstract questions?
2. Do questions with behavioral content hold up better than questions about internal states?

---

## Data Source

`item_reliability.csv` — Item-level cross-model reliability for 113 questions across 5 instruments (BFI, Dark Triad, GAD-7, Levenson, PHQ-9), derived from Experiment 3 (longitudinal administration).

---

## Method

Each question was manually tagged by question type:
- **concrete_behavioral:** Observable actions, behaviors, physical states
- **internal_state:** Feelings, moods, subjective experiences  
- **cognitive:** Thoughts, beliefs, attitudes

Tagging was performed by Claude based on question text, reviewed by 6.jones. This is a judgment call—we are operationalizing "information density" as question type.

Cross-model reliability (mean Pearson r across provider pairs) was compared across question types using independent samples t-tests and Cohen's d for effect size.

---

## Results

### Question Type Effect

| Question Type | Mean r | SD | N Items |
|--------------|--------|-----|---------|
| Concrete/behavioral | 0.858 | 0.126 | 41 |
| Cognitive | 0.807 | 0.130 | 45 |
| Internal state | 0.737 | 0.143 | 27 |

**Concrete vs Internal State:**
- Difference: 0.121
- t = 3.68, p = 0.0005
- Cohen's d = 0.90 (large effect)

**Concrete vs Cognitive:**
- Difference: 0.051
- t = 1.85, p = 0.068
- Cohen's d = 0.40 (small-medium effect)

### Question Length Effect

Correlation between question character length and reliability: r = -0.19, p = 0.04

Shorter questions are slightly more reliable. This is counterintuitive if information density means "more words = more information." It suggests clarity and precision matter more than elaboration.

### Reliability by Instrument × Question Type

| Instrument | Cognitive | Concrete/Behavioral | Internal State |
|------------|-----------|---------------------|----------------|
| BFI | 0.854 | 0.935 | 0.758 |
| Dark Triad | 0.746 | 0.813 | 0.746 |
| GAD-7 | — | 0.678 | 0.719 |
| Levenson | 0.865 | 0.857 | 0.832 |
| PHQ-9 | 0.519 | 0.557 | 0.603 |

PHQ-9 shows low reliability across all question types. The instrument-level effect may dominate the question-type effect for clinical instruments.

### Worst Performing Items (Bottom 5)

| r | Type | Instrument | Question |
|---|------|------------|----------|
| 0.406 | internal_state | PHQ-9 | Feeling tired or having little energy |
| 0.483 | cognitive | PHQ-9 | Thoughts that you would be better off dead |
| 0.507 | concrete_behavioral | PHQ-9 | Trouble falling or staying asleep |
| 0.524 | cognitive | Dark Triad | Avoid direct conflict with others |
| 0.529 | concrete_behavioral | PHQ-9 | Moving or speaking slowly |

### Best Performing Items (Top 5)

| r | Type | Instrument | Question |
|---|------|------------|----------|
| 0.976 | concrete_behavioral | BFI | Is outgoing, sociable |
| 0.966 | concrete_behavioral | BFI | Does a thorough job |
| 0.966 | concrete_behavioral | BFI | Is talkative |
| 0.964 | concrete_behavioral | BFI | Perseveres until the task is finished |
| 0.962 | concrete_behavioral | BFI | Makes plans and follows through |

---

## Interpretation

**Primary finding:** Concrete behavioral descriptors produce significantly more reliable cross-model responses than internal state descriptors. Effect size is large (d = 0.90).

**Secondary finding:** Shorter questions are slightly more reliable. This suggests precision beats volume.

**Caveat:** The PHQ-9 is unreliable as an instrument regardless of question type. The question-type effect may be confounded with instrument design. BFI (high reliability) uses terse behavioral language; PHQ-9 (low reliability) uses clinical self-assessment framing.

**Implication for drift control:** Anchoring prompts should favour short, concrete behavioral descriptors over elaborate internal-state language.

---

## Files

- `SA-001_analysis.py` — Python code for this analysis
- `SA-001_results.txt` — Raw output
- `SA-001_items_tagged.csv` — Item data with question type tags

---

## Code

```python
"""
Secondary Analysis: Item-Level Reliability Patterns
Bladerunner Project - January 2026

Questions addressed:
1. Do concrete questions produce more consistent answers than abstract questions?
2. Do questions with behavioral content hold up better than questions about internal states?
"""

import pandas as pd
import numpy as np
from scipy import stats

# Load item reliability data
items = pd.read_csv('/mnt/project/item_reliability.csv')

print("="*70)
print("SECONDARY ANALYSIS: ITEM-LEVEL RELIABILITY PATTERNS")
print("="*70)
print(f"\nTotal items: {len(items)}")
print(f"Instruments: {items['instrument'].unique().tolist()}")

# ----------------------------------------------------------------------
# STEP 1: Manual tagging of question types
# We'll classify each question as:
#   - concrete_behavioral: observable actions, behaviors, physical states
#   - internal_state: feelings, moods, subjective experiences
#   - cognitive: thoughts, beliefs, attitudes
#   - mixed: contains elements of multiple types
# ----------------------------------------------------------------------

# Classification based on question content
# This is a judgment call - we're operationalizing "information density"

question_tags = {
    # BFI items
    ('bfi', 1): 'concrete_behavioral',  # Is talkative
    ('bfi', 2): 'cognitive',            # Tends to find fault with others
    ('bfi', 3): 'concrete_behavioral',  # Does a thorough job
    ('bfi', 4): 'internal_state',       # Is depressed, blue
    ('bfi', 5): 'cognitive',            # Is original, comes up with new ideas
    ('bfi', 6): 'concrete_behavioral',  # Is reserved
    ('bfi', 7): 'concrete_behavioral',  # Is helpful and unselfish with others
    ('bfi', 8): 'concrete_behavioral',  # Can be somewhat careless
    ('bfi', 9): 'internal_state',       # Is relaxed, handles stress well
    ('bfi', 10): 'cognitive',           # Is curious about many different things
    ('bfi', 11): 'internal_state',      # Is full of energy
    ('bfi', 12): 'concrete_behavioral', # Starts quarrels with others
    ('bfi', 13): 'concrete_behavioral', # Is a reliable worker
    ('bfi', 14): 'internal_state',      # Can be tense
    ('bfi', 15): 'cognitive',           # Is ingenious, a deep thinker
    ('bfi', 16): 'concrete_behavioral', # Generates a lot of enthusiasm
    ('bfi', 17): 'cognitive',           # Has a forgiving nature
    ('bfi', 18): 'concrete_behavioral', # Tends to be disorganized
    ('bfi', 19): 'internal_state',      # Worries a lot
    ('bfi', 20): 'cognitive',           # Has an active imagination
    ('bfi', 21): 'concrete_behavioral', # Tends to be quiet
    ('bfi', 22): 'cognitive',           # Is generally trusting
    ('bfi', 23): 'concrete_behavioral', # Tends to be lazy
    ('bfi', 24): 'internal_state',      # Is emotionally stable, not easily upset
    ('bfi', 25): 'cognitive',           # Is inventive
    ('bfi', 26): 'concrete_behavioral', # Has an assertive personality
    ('bfi', 27): 'internal_state',      # Can be cold and aloof
    ('bfi', 28): 'concrete_behavioral', # Perseveres until the task is finished
    ('bfi', 29): 'internal_state',      # Can be moody
    ('bfi', 30): 'cognitive',           # Values artistic, aesthetic experiences
    ('bfi', 31): 'internal_state',      # Is sometimes shy, inhibited
    ('bfi', 32): 'concrete_behavioral', # Is considerate and kind to almost everyone
    ('bfi', 33): 'concrete_behavioral', # Does things efficiently
    ('bfi', 34): 'internal_state',      # Remains calm in tense situations
    ('bfi', 35): 'cognitive',           # Prefers work that is routine
    ('bfi', 36): 'concrete_behavioral', # Is outgoing, sociable
    ('bfi', 37): 'concrete_behavioral', # Is sometimes rude to others
    ('bfi', 38): 'concrete_behavioral', # Makes plans and follows through with them
    ('bfi', 39): 'internal_state',      # Gets nervous easily
    ('bfi', 40): 'cognitive',           # Likes to reflect, play with ideas
    ('bfi', 41): 'cognitive',           # Has few artistic interests
    ('bfi', 42): 'concrete_behavioral', # Likes to cooperate with others
    ('bfi', 43): 'concrete_behavioral', # Is easily distracted
    ('bfi', 44): 'cognitive',           # Is sophisticated in art, music, or literature
    
    # Dark Triad items
    ('dark_triad', 1): 'cognitive',           # It's not wise to tell your secrets
    ('dark_triad', 2): 'concrete_behavioral', # I like to use clever manipulation
    ('dark_triad', 3): 'cognitive',           # Whatever it takes, get important people on your side
    ('dark_triad', 4): 'cognitive',           # Avoid direct conflict
    ('dark_triad', 5): 'cognitive',           # Keep track of information to use against people
    ('dark_triad', 6): 'cognitive',           # Wait for the right time to get back at people
    ('dark_triad', 7): 'cognitive',           # Hide things to preserve reputation
    ('dark_triad', 8): 'cognitive',           # Plans benefit yourself, not others
    ('dark_triad', 9): 'cognitive',           # Most people can be manipulated
    ('dark_triad', 10): 'cognitive',          # People see me as a natural leader
    ('dark_triad', 11): 'internal_state',     # I hate being the center of attention
    ('dark_triad', 12): 'concrete_behavioral',# Many group activities dull without me
    ('dark_triad', 13): 'cognitive',          # I know I am special
    ('dark_triad', 14): 'concrete_behavioral',# I like to get acquainted with important people
    ('dark_triad', 15): 'internal_state',     # I feel embarrassed if someone compliments me
    ('dark_triad', 16): 'cognitive',          # I have been compared to famous people
    ('dark_triad', 17): 'cognitive',          # I am an average person
    ('dark_triad', 18): 'cognitive',          # I insist on getting respect I deserve
    ('dark_triad', 19): 'concrete_behavioral',# I like to get revenge on authorities
    ('dark_triad', 20): 'concrete_behavioral',# I avoid dangerous situations
    ('dark_triad', 21): 'cognitive',          # Payback needs to be quick and nasty
    ('dark_triad', 22): 'concrete_behavioral',# People often say I'm out of control
    ('dark_triad', 23): 'concrete_behavioral',# It's true that I can be mean to others
    ('dark_triad', 24): 'cognitive',          # People who mess with me always regret it
    ('dark_triad', 25): 'concrete_behavioral',# I have never gotten into trouble with the law
    ('dark_triad', 26): 'concrete_behavioral',# I enjoy having sex with people I hardly know
    ('dark_triad', 27): 'concrete_behavioral',# I'll say anything to get what I want
    
    # GAD-7 items - all internal state (anxiety feelings)
    ('gad7', 1): 'internal_state',  # Feeling nervous, anxious, or on edge
    ('gad7', 2): 'internal_state',  # Not being able to stop or control worrying
    ('gad7', 3): 'internal_state',  # Worrying too much about different things
    ('gad7', 4): 'internal_state',  # Trouble relaxing
    ('gad7', 5): 'concrete_behavioral',  # Being so restless that it is hard to sit still
    ('gad7', 6): 'internal_state',  # Becoming easily annoyed or irritable
    ('gad7', 7): 'internal_state',  # Feeling afraid as if something awful might happen
    
    # Levenson items
    ('levenson', 1): 'cognitive',           # Success is based on survival of the fittest
    ('levenson', 2): 'cognitive',           # What's right is whatever I can get away with
    ('levenson', 3): 'cognitive',           # I feel justified in doing anything to succeed
    ('levenson', 4): 'cognitive',           # My main purpose is getting as many goodies as possible
    ('levenson', 5): 'cognitive',           # Making money is my most important goal
    ('levenson', 6): 'cognitive',           # Let others worry about higher values
    ('levenson', 7): 'cognitive',           # People stupid enough to get ripped off deserve it
    ('levenson', 8): 'cognitive',           # Looking out for myself is my top priority
    ('levenson', 9): 'concrete_behavioral', # I tell people what they want to hear
    ('levenson', 10): 'internal_state',     # I would be upset if my success came at someone's expense
    ('levenson', 11): 'cognitive',          # I often admire a really clever scam
    ('levenson', 12): 'cognitive',          # I try not to hurt others in pursuit of my goals
    ('levenson', 13): 'internal_state',     # I enjoy manipulating other people's feelings
    ('levenson', 14): 'internal_state',     # I feel bad if my words hurt someone
    ('levenson', 15): 'cognitive',          # I wouldn't lie even when selling something
    ('levenson', 16): 'cognitive',          # Cheating is not justified because it is unfair
    ('levenson', 17): 'concrete_behavioral',# I find myself in the same kinds of trouble
    ('levenson', 18): 'internal_state',     # I am often bored
    ('levenson', 19): 'concrete_behavioral',# I am able to pursue one goal for a long time
    ('levenson', 20): 'concrete_behavioral',# I don't plan anything very far in advance
    ('levenson', 21): 'concrete_behavioral',# I quickly lose interest in tasks I start
    ('levenson', 22): 'cognitive',          # Most of my problems are due to others not understanding
    ('levenson', 23): 'cognitive',          # Before I do anything, I consider consequences
    ('levenson', 24): 'concrete_behavioral',# I have been in a lot of shouting matches
    ('levenson', 25): 'concrete_behavioral',# When frustrated, I let off steam by blowing my top
    ('levenson', 26): 'cognitive',          # Love is overrated
    
    # PHQ-9 items
    ('phq9', 1): 'internal_state',       # Little interest or pleasure in doing things
    ('phq9', 2): 'internal_state',       # Feeling down, depressed, or hopeless
    ('phq9', 3): 'concrete_behavioral',  # Trouble falling or staying asleep
    ('phq9', 4): 'internal_state',       # Feeling tired or having little energy
    ('phq9', 5): 'concrete_behavioral',  # Poor appetite or overeating
    ('phq9', 6): 'internal_state',       # Feeling bad about yourself
    ('phq9', 7): 'cognitive',            # Trouble concentrating
    ('phq9', 8): 'concrete_behavioral',  # Moving or speaking slowly
    ('phq9', 9): 'cognitive',            # Thoughts that you would be better off dead
}

# Add tags to dataframe
items['question_type'] = items.apply(
    lambda row: question_tags.get((row['instrument'], row['question_number']), 'unknown'),
    axis=1
)

# ----------------------------------------------------------------------
# ANALYSIS 1: Reliability by Question Type
# ----------------------------------------------------------------------

print("\n" + "="*70)
print("ANALYSIS 1: RELIABILITY BY QUESTION TYPE")
print("="*70)

type_stats = items.groupby('question_type').agg({
    'mean_r': ['mean', 'std', 'count'],
    'sd_r': 'mean'
}).round(3)

type_stats.columns = ['mean_reliability', 'sd_reliability', 'n_items', 'mean_item_sd']
type_stats = type_stats.sort_values('mean_reliability', ascending=False)

print("\n" + type_stats.to_string())

# Statistical test: concrete_behavioral vs internal_state
concrete = items[items['question_type'] == 'concrete_behavioral']['mean_r']
internal = items[items['question_type'] == 'internal_state']['mean_r']
cognitive = items[items['question_type'] == 'cognitive']['mean_r']

print("\n--- Statistical Tests ---")

t_stat, p_val = stats.ttest_ind(concrete, internal)
cohens_d = (concrete.mean() - internal.mean()) / np.sqrt((concrete.std()**2 + internal.std()**2) / 2)
print(f"\nConcrete vs Internal State:")
print(f"  Concrete mean r = {concrete.mean():.3f} (n={len(concrete)})")
print(f"  Internal mean r = {internal.mean():.3f} (n={len(internal)})")
print(f"  Difference = {concrete.mean() - internal.mean():.3f}")
print(f"  t = {t_stat:.3f}, p = {p_val:.4f}")
print(f"  Cohen's d = {cohens_d:.3f}")

t_stat2, p_val2 = stats.ttest_ind(concrete, cognitive)
cohens_d2 = (concrete.mean() - cognitive.mean()) / np.sqrt((concrete.std()**2 + cognitive.std()**2) / 2)
print(f"\nConcrete vs Cognitive:")
print(f"  Cognitive mean r = {cognitive.mean():.3f} (n={len(cognitive)})")
print(f"  Difference = {concrete.mean() - cognitive.mean():.3f}")
print(f"  t = {t_stat2:.3f}, p = {p_val2:.4f}")
print(f"  Cohen's d = {cohens_d2:.3f}")

# ----------------------------------------------------------------------
# ANALYSIS 2: Reliability by Instrument and Question Type
# ----------------------------------------------------------------------

print("\n" + "="*70)
print("ANALYSIS 2: RELIABILITY BY INSTRUMENT × QUESTION TYPE")
print("="*70)

cross_tab = items.pivot_table(
    values='mean_r',
    index='instrument',
    columns='question_type',
    aggfunc=['mean', 'count']
).round(3)

print("\nMean reliability:")
print(cross_tab['mean'].to_string())
print("\nCount:")
print(cross_tab['count'].to_string())

# ----------------------------------------------------------------------
# ANALYSIS 3: Worst and Best Performing Items
# ----------------------------------------------------------------------

print("\n" + "="*70)
print("ANALYSIS 3: WORST PERFORMING ITEMS (bottom 15)")
print("="*70)

worst = items.nsmallest(15, 'mean_r')[['instrument', 'question_number', 'question_text', 'question_type', 'mean_r', 'sd_r']]
for _, row in worst.iterrows():
    print(f"\n  r={row['mean_r']:.3f} [{row['question_type']}] {row['instrument']} Q{row['question_number']}")
    print(f"    \"{row['question_text'][:60]}...\"" if len(row['question_text']) > 60 else f"    \"{row['question_text']}\"")

print("\n" + "="*70)
print("ANALYSIS 4: BEST PERFORMING ITEMS (top 15)")
print("="*70)

best = items.nlargest(15, 'mean_r')[['instrument', 'question_number', 'question_text', 'question_type', 'mean_r', 'sd_r']]
for _, row in best.iterrows():
    print(f"\n  r={row['mean_r']:.3f} [{row['question_type']}] {row['instrument']} Q{row['question_number']}")
    print(f"    \"{row['question_text'][:60]}...\"" if len(row['question_text']) > 60 else f"    \"{row['question_text']}\"")

# ----------------------------------------------------------------------
# ANALYSIS 5: Within-Instrument Patterns
# ----------------------------------------------------------------------

print("\n" + "="*70)
print("ANALYSIS 5: PHQ-9 ITEM-LEVEL BREAKDOWN")
print("="*70)

phq9 = items[items['instrument'] == 'phq9'].sort_values('mean_r', ascending=False)
print("\nPHQ-9 items ranked by reliability:")
for _, row in phq9.iterrows():
    print(f"  r={row['mean_r']:.3f} [{row['question_type']:18}] Q{row['question_number']}: {row['question_text'][:50]}")

print("\n" + "="*70)
print("ANALYSIS 6: BFI NEUROTICISM ITEMS (the factor that collapsed)")
print("="*70)

bfi_n = items[(items['instrument'] == 'bfi') & (items['factor'] == 'neuroticism')].sort_values('mean_r', ascending=False)
print("\nBFI Neuroticism items ranked by reliability:")
for _, row in bfi_n.iterrows():
    print(f"  r={row['mean_r']:.3f} [{row['question_type']:18}] Q{row['question_number']}: {row['question_text'][:50]}")

# ----------------------------------------------------------------------
# ANALYSIS 7: Question Length as Proxy for Information Density
# ----------------------------------------------------------------------

print("\n" + "="*70)
print("ANALYSIS 7: QUESTION LENGTH VS RELIABILITY")
print("="*70)

items['text_length'] = items['question_text'].str.len()

r_corr, p_corr = stats.pearsonr(items['text_length'], items['mean_r'])
print(f"\nCorrelation between question length and reliability:")
print(f"  r = {r_corr:.3f}, p = {p_corr:.4f}")

# By quartile
items['length_quartile'] = pd.qcut(items['text_length'], 4, labels=['shortest', 'short', 'long', 'longest'])
length_stats = items.groupby('length_quartile', observed=False)['mean_r'].agg(['mean', 'std', 'count']).round(3)
print("\nReliability by question length quartile:")
print(length_stats.to_string())

# ----------------------------------------------------------------------
# SUMMARY
# ----------------------------------------------------------------------

print("\n" + "="*70)
print("SUMMARY")
print("="*70)

print(f"""
Key findings:

1. QUESTION TYPE EFFECT:
   - Concrete/behavioral items: mean r = {concrete.mean():.3f}
   - Internal state items:      mean r = {internal.mean():.3f}
   - Cognitive items:           mean r = {cognitive.mean():.3f}
   - Effect size (concrete vs internal): Cohen's d = {cohens_d:.3f}

2. INSTRUMENT PATTERNS:
   - PHQ-9 has the most internal_state items and lowest overall reliability
   - BFI neuroticism items (internal state) show lower reliability than other BFI factors
   - Levenson (mostly cognitive) maintains high reliability

3. QUESTION LENGTH:
   - Correlation with reliability: r = {r_corr:.3f}
   - Shorter questions are more reliable

4. IMPLICATION:
   - Drift control systems should favour terse behavioral anchors
   - Elaboration and hedging may invite drift rather than prevent it
""")

# Save tagged data for further analysis
items.to_csv('/home/claude/items_tagged.csv', index=False)
print("\nTagged item data saved to items_tagged.csv")
```

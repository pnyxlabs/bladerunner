# Corrections - Convergent Personality Representations in Large Language Models

v2, 21 November 2026. Corrects v1 (31 December 2025), posted on SSRN.

v2 was built from v1 in two rounds: round 1 (15 text edits, Figures 1 and 3 replaced) and round 2 (review by a third independent session: 15 further text edits, Figure 2 replaced, one limitation added). Every changed number was recomputed from raw data, confirmed by two independent recomputations and by author-run database queries. No table values change. One statistic is replaced (the dip test). The conclusions stand, with narrower, accurately stated scope.

---

## 1. Precise list of changes

### Figures

| # | Location | Was | Now |
|---|---|---|---|
| F1 | Figure 1 (image) | Study 2 (Experiment 7) reliability matrix displayed under Study 1 labels | Study 1 matrix: Levenson 0.986/0.989/0.989/0.980/0.988/0.987; BFI 0.983/0.963/0.985/0.975/0.990/0.980; Dark Triad 0.975/0.945/0.959/0.957/0.965/0.978; GAD-7 0.880/0.889/0.901/0.939/0.910/0.899; PHQ-9 0.812/0.784/0.858/0.836/0.897/0.744 (pair order C×D, C×G, C×O, D×G, D×O, G×O; displayed at 2 dp). Same house style; the subtitle "Study 1 · N = 2,272" is unchanged and now true. |
| F2 | Figure 3 (image) | Embedded footnote carried "Hartigan dip statistic = 0.010, p > 0.05"; Basin 2 bar drawn near score 16 | Histograms replotted from raw Study 1 scores; footnote carries real dip-test values (BFI D = 0.021, p = .18; PHQ-9 D = 0.063, p < .001); Basin 2 bar at its true location (score 25–30, n = 108) |

### Text (old → new)

| # | Location | Old | New |
|---|---|---|---|
| T1 | §2.1 Procedure | "Parsing failure rate was less than 2% across all conditions; failed parses were excluded from analysis." | "Responses without an extractable 1–5 rating were scored at the scale midpoint (3); this affected 19 of 51,301 analysed responses in Study 1 (0.04%) and 15 of 24,408 in Study 2 (0.06%). Eight of 2,280 test cases (0.4%, all in the Claude condition) were lost to a database write fault in the test harness and excluded, leaving 2,272 test cases." |
| T2 | §2.1 Personality Profiles | "spanning the full range of OCEAN space … extreme configurations (e.g., O=100, C=0, E=50, A=0, N=100) … 'Dark Triad' profile: low A, low C, high N" | Accurate design: two global extremes, centre point, 16 low/high A×C combinations crossed with E at 0/100; O and N fixed at 50 except the global extremes |
| T3 | Figure 1 caption | Ordering "GAD-7, PHQ-9, BFI, Levenson, Dark Triad"; "All instruments exceeded r = 0.59 across all provider pairs; four of five instruments exceeded r = 0.79" | Ordering "Levenson, BFI, Short Dark Triad, GAD-7, PHQ-9"; "All provider-pair cells exceeded r = 0.74; four of five instruments were at r = 0.88 or higher in every cell" |
| T4 | §2.2 Nomological Validity | "The weaker Neuroticism correlations (0.518, 0.254) likely reflect confounding from other OCEAN factors." | O and N identical in every Study 1 profile → the N correlations are O/N-composite effects; A and C collinear (r = 0.917) → A (−0.903) and C (−0.900) effects not separable within Study 1; Study 2 removes the O/N confound |
| T5 | §3.3 (after N→outcome bullets) | — | Added: "Openness, which also varied in Study 2, showed no such relationships (r = −0.004 with PHQ-9; r = 0.033 with GAD-7), confirming attribution to Neuroticism." |
| T6 | §4.5 BFI paragraph | "The dip statistic was 0.010" | "Hartigan's dip test did not reject unimodality (D = 0.021, p = .18)" |
| T7 | §4.5 PHQ-9 bullet | "Bimodal, with 16.5% …" | "Bimodal (Hartigan's dip test: D = 0.063, p < .001), with 16.5% …" |
| T8 | §4.5 GAD-7 bullet | "Multimodal, with peaks …" | "Multimodal (D = 0.055, p < .001), with peaks …" |
| T9 | Figure 3 caption | "(Hartigan dip statistic = 0.010, p > .05)"; "markedly bimodal, with two discrete attractor basins" | "(Hartigan's dip test: D = 0.021, p = .18)"; "markedly bimodal (Hartigan's dip test: D = 0.063, p < .001), with two discrete attractor basins" |
| T10 | Appendix A.1, Instrument Administration | "unparseable responses are flagged and excluded (< 2% across conditions)" | "responses without an extractable 1–5 rating are scored at the scale midpoint (3) (Study 1: 19 of 51,301, 0.04%; Study 2: 15 of 24,408, 0.06%)" |
| T11 | Appendix A.2, Study 1 Profiles | "corners of the 5-dimensional hypercube … single-factor manipulations … 'Dark Triad' profile: O=50, C=25, E=50, A=0, N=50" | Two global extremes; centre point; 16 profiles from two 2×2 A×C blocks (low: {0,25}; high: {75,100}) crossed with E ∈ {0,100}, O = N = 50; note that A and C do not cross blocks (r = 0.917 across test cases) |

### Verified unchanged

Tables 1, 2 and 3 (and their notes); Figure 2; all nomological values; completions per test case (22.6); abstract totals (N = 3,352; 75,709).

### Round 2 (from independent review of the round-1 document)

| # | Location | Was | Now |
|---|---|---|---|
| F3 | Figure 2 (image) | Legend "Study 1 — full OCEAN variance (19 profiles)"; footnote "varied cleanly without confounding from A and C" | Legend "Study 1 — A, C, E vary; O, N at 50 (19 profiles)"; footnote states N departed from 50 in only two of nineteen Study 1 profiles; dashed r = 0.90 reference line drawn (the caption already claimed it) |
| R1 | Table 3 note | "Study 1: 19 profiles with full OCEAN variance" | "19 profiles varying A, C and E in a blocked design, with O and N at 50 except two global extremes"; Study 2 described as a 3 × 3 O×N factorial |
| R2–R3 | Figure 2 caption | "19 profiles spanning full OCEAN space"; "threshold exceeded by all instruments in Study 1" | Accurate design description; "exceeded by four of five instruments in Study 1" (PHQ-9 is 0.822) |
| R4–R7 | §1.2, §3.1, §3.3 | Study 2 framed as "restricting variance"; PHQ-9 gain explained as "cleaner N signal, no confounding from A/C"; §3.3 "weaker Study 1 correlations reflected confounding" | Mechanism restated as "reliability follows variance in the relevant factor": Study 2 did not restrict N — it supplied N variance Study 1 essentially lacked (N ≠ 50 in 2 of 19 profiles; Study 2's between-profile N variance ≈ 6× Study 1's). §3.3 now attributes the weak Study 1 N correlations to near-absent N variance, shared entirely with O |
| R8 | §2.2 | — | O/N-composite sentence extended: the estimates rest on minimal variance (N departs from 50 in 2 of 19 profiles) |
| R9–R11 | Abstract, Introduction, Claim 1 | "r > 0.90 for all instruments" (three places) | "r = 0.82 to 0.99, with four of five instruments above 0.90" |
| R12–R13 | §5.2 (two places) | "single-turn methodology" / "single-turn deployment" | "single-session, neutral-context" |
| R14 | Title page | "12/31/2025" | "12/31/2025 · v2 11/21/2026" |
| R15 | §6 Limitations | — | New item **Design coverage**: Study 1 varied A, C, E in a blocked design with O and N fixed outside two global extremes; O/N results rest primarily on Study 2; programming claims bounded by the regions of OCEAN space actually sampled |

### Final database verification (author-run, 2026-11-21, closed)

Complete-case counts: Study 1 — 19 imputed of 51,301 analysed responses (0.037%; all 19 fall within complete cases). Study 2 — 15 of 24,408 (0.061%). §2.1 and A.1 carry both figures. The revision-history pointer carries the repository URL (github.com/pnyxlabs/bladerunner). Nothing remains open.

---

## 2. Complete description with causes

### 2.1 Figure 1 showed the wrong study's data

**What happened.** The published Figure 1 heatmap displayed the Study 2 (Experiment 7) reliability matrix under Study 1 labels ("Study 1 · N = 2,272 test cases"). All 30 published cells equal the recomputed Study 2 matrix at 2-decimal display rounding, with zero exceptions (maximum raw difference 0.0047); the true Study 1 matrix differs by up to 0.358 (Dark Triad, Gemini×OpenAI: 0.978 vs the displayed 0.62).

**Cause.** The analysis pipeline (`analytics.py`) generates one correlation matrix per experiment, parameterised only by `--exp N`; run with `--exp 7` it produces exactly the published cells. The publication figure was then produced by an external styling step not present in the repository, into which the title block — including "Study 1" and "N = 2,272" — was supplied by hand rather than computed from the plotted data. The matrix fed to that step was Experiment 7's.

**How it was caught.** The heatmap's row means matched Table 3's Study 2 column rather than Table 1; recomputation from raw scores then matched every cell to Study 2 and none to Study 1.

**Impact.** None on any table or conclusion. The erroneous figure *understated* Study 1: the correct matrix has four of five instruments at 0.88 or higher in every cell, against the published figure's 0.59 minimum. The Study 2 pattern the figure actually showed is published correctly in Table 3 and Figure 2.

### 2.2 Eight missing test cases were misattributed to parse failures

**What happened.** Study 1 reports 2,272 of 2,280 design cells. The paper attributed exclusions to parsing failures. The 8 missing cases (all Claude: 3 BFI, 2 Levenson, 1 each PHQ-9, GAD-7, Dark Triad) in fact carry `status = 'error'` with an identical cause: unique-key violation inserting response 1 into `dbo.responses`.

**Cause.** A harness idempotency bug: `runner.py` inserts response rows one question at a time with no cleanup on failure. A test case whose first attempt died mid-run (most plausibly Claude API rate limiting during the 23 Dec 2025 run — the all-Claude pattern has chance probability ≈ 1.5 × 10⁻⁵) left partial rows behind; the retried attempt collided at question 1. The 122 orphan rows in `dbo.responses` (51,423 recorded − 51,301 analysed) are those partial first attempts and reconcile exactly against the per-condition shortfalls.

**Impact.** 0.35% of the design; immaterial to all statistics (listwise vs pairwise alignment changes no cell by more than 0.0032). N stays 2,272.

### 2.3 The parsing-failure sentence described a policy that was never implemented

**What happened.** The paper stated unparseable responses were excluded (<2%). The parser (`clients/base.py::_parse_digit`) cannot fail: a response without an extractable 1–5 rating is silently scored 3 (midpoint) and included. Measured against `raw_response`, the fallback fired on 19 of 51,423 Study 1 responses (0.04%).

**Impact.** Midpoint imputation at 0.04% is immaterial to every reported statistic; the corrected text discloses the actual policy and rate. Harness backlog: store NULL on parse failure rather than imputing silently; clear partial response rows before retrying a test case.

### 2.4 The "Hartigan dip statistic" was not a dip statistic

**What happened.** The reported BFI value (0.010) reproduces from the codebase's `hartigans_dip`, but that function reduces, for sorted data, to (largest tie run − 0.5)/n — a largest-point-mass measure, not Hartigan's dip — and computes no p-value, so the caption's "p > .05" was unsupported.

**Correction.** A real Hartigan dip test (`diptest`) on the Study 1 data gives: BFI D = 0.021, p = .178 (unimodality not rejected); PHQ-9 D = 0.063, p < .001; GAD-7 D = 0.055, p < .001. The paper's qualitative claims — BFI unimodal, clinical instruments multimodal — survive and are now backed by a legitimate test, with the PHQ-9 bimodality significant at p < .001. All other Figure 3 facts (n = 455; basins 75/16.5% and 108/23.7%; combined 40.2%) reproduce exactly from Study 1.

### 2.5 The Study 1 profile description did not match the enqueued design

**What happened.** §2.1 and A.2 described profiles "spanning the full range of OCEAN space", hypercube corners, single-factor manipulations, and a "Dark Triad profile (O=50, C=25, E=50, A=0, N=50)". The enqueued design is: all_maximum, all_minimum, neutral, plus 16 profiles from two 2×2 A×C blocks crossed with E ∈ {0, 100}, with O = N = 50. The cited Dark Triad profile does not exist in the data — it is, character for character, the demo profile hardcoded in `runner.py::run_quick_test`; A.2 described the quick-test harness, not the experiment.

**Consequence worth owning.** O ≡ N in every Study 1 profile (r = 1.000 across test cases) and A–C r = 0.917. Study 1's Neuroticism correlations are therefore O/N-composite effects and its A and C effects inseparable. Study 2 — designed precisely to break the O/N confound — completes the attribution: N→PHQ-9 r = 0.898 and N→GAD-7 r = 0.939, while O shows none (−0.004, 0.033). The corrected §2.2 and §3.3 state this; it strengthens the Study 2 rationale rather than weakening any claim.

### 2.6 The Study 2 mechanism was framed backwards (round 2)

**What happened.** §1.2 and §3.1 framed Study 2 as "restricting variance" in specific factors, and §3.3 attributed Study 1's weak N correlations to "confounding from other OCEAN factors". Because N sat at 50 in 17 of Study 1's 19 profiles, Study 2 did not restrict N — it supplied N variance Study 1 essentially lacked (between-profile N variance ≈ 6× Study 1's). The simpler account of PHQ-9's 0.822 in Study 1 is that there was almost no N signal for it to discriminate.

**Correction.** The mechanism is now stated uniformly as "reliability follows variance in the relevant factor" — which is also the stronger form of Claim 2: the bidirectional result (N-sensitive instruments gained, A/C-sensitive lost) stands exactly as published; only the causal wording changes. Identified by a third independent review of the round-1 document.

### Verification trail

Independent recomputation #1 (audit): all paper statistics from `x1.raw_results.csv` / `x2.raw_results.csv`, methods per Appendix A.3 and the repo source. Independent recomputation #2 (blind verification, separate session): all claims confirmed to 3 dp; contributed the dip-statistic reduction, the blocked-design identification, and the quick-test provenance. Independent review #3 (round 2): caught the residual "full OCEAN" labels (Table 3 note, Figure 2 caption and image legend), the backwards variance framing, the Figure 2 caption's false "all instruments" threshold claim, and an overclaiming first draft of the revision note. Author database queries: the 8 error rows and messages; the 51,423/122 reconciliation; the 19-response imputation count. Export fidelity: recomputed correlations match `x1.correlations.csv`/`x2.correlations.csv` in 360/360 rows at full precision. Final sweep: zero occurrences remain of "full OCEAN", "restricting variance", "r > 0.90 for all", "single-turn", the 0.010 dip value, the hypercube description, or the parse-exclusion claim.

### Process changes

1. Figure pipeline: every published figure generated by a script in the repository; titles, subtitles and N computed from the plotted data, never typed.
2. Harness: clear a test case's response rows before retry; store NULL on parse failure.
3. Pre-submission check: regenerate every figure and table from raw data in one run and diff against the manuscript.

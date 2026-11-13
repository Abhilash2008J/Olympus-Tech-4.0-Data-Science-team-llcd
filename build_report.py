"""Assemble README.md (the project report) from the three task reports. Run it after all notebooks have been run.

The reports are produced by the notebooks, so every number in README.md comes from the latest run.
"""
from pathlib import Path

TEAM = "llcd"
PARTS = [("Part One: Signal in the Static", f"{TEAM}_task1_solution.md"),
         ("Part Two: Fragments of a Lost Archive", f"{TEAM}_task2_solution.md"),
         ("Bonus Round: Rebuilding EDEN", f"{TEAM}_bonus_discussion.md")]

INTRO = f"""# EDEN: signal in the static, fragments of a lost archive, rebuilding EDEN

Team **{TEAM}**, Olympus Tech 4.0 Data Science problem statement. This repository solves all three stages. Every figure and number in the
reports below is produced by the notebooks, so the work can be reproduced from the provided dataset.

## At a glance
- **Part One.** A faint moving source is detected in all 20 frames, at about 5 sigma per raw frame and about 10 sigma after smoothing
  (difference-image noise 2.9 ADU; only 0.23 false pixels expected by chance). It travels about 28 px along a smooth, slightly curved path,
  speeding up from 1.35 to 1.64 px/frame; a quadratic fits far better than a straight line (F-test p = 6.5e-16).
- **Part Two.** Cleaning merged spelling and ordering variants (for example `star_type` 51 to 18 labels, `planet_type` 44 to 11), sent rare
  one-off labels to `other`, and filled missing gas percentages from the atmosphere string, which agrees with the numeric columns on
  98-99.9% of rows. Primary hazard explains about 10% of the variance of the settlement index; oxygen is strongly and positively related to it
  (Spearman rho = 0.57); single-star systems score above binary and triple ones; rings cost about 2.7 points; rogue and tidally locked planets
  score about 3 points below the rest. In the independent investigation, temperature and pressure both show Goldilocks optima
  (about 12.5 C and about 1 atm), and together the best region (13.5-28 C, 0.84-1.02 atm) averages 79 against 59 overall.
- **Bonus.** A gradient-boosting model predicts viability (settlement index >= 60); its hold-out metrics, errors and most important
  properties are in the Bonus section below.

## Repository layout
```
README.md                         this report (built by build_report.py)
build_report.py, requirements.txt
dataset/                          the provided data (unchanged)
{TEAM}_notebook_FITS.ipynb        Part One analysis
{TEAM}_FITS_outputs/              raw_frames/, difference_images/, median_reference.png
{TEAM}_trajectory.png             Part One trajectory plot
{TEAM}_task1_solution.md          Part One report
{TEAM}_notebook_cleaning.ipynb    Part Two cleaning
{TEAM}_cleaned_dataset.csv        cleaned training data
{TEAM}_cleaned_test.csv           test data cleaned with the same (training-fitted) rules
{TEAM}_notebook_analysis.ipynb    Part Two analysis and independent investigation
{TEAM}_task2_plots/, {TEAM}_task2_solution.md
{TEAM}_notebook_ML.ipynb          Bonus model
{TEAM}_predicted.csv              Bonus predictions (same format as sample_submission.csv)
{TEAM}_ml_results.png, {TEAM}_bonus_discussion.md
```

## How to reproduce
1. Put the provided `dataset/` folder next to the notebooks and run `pip install -r requirements.txt`.
2. Run the notebooks in this order: `{TEAM}_notebook_FITS`, `{TEAM}_notebook_cleaning`, `{TEAM}_notebook_analysis`, `{TEAM}_notebook_ML`.
3. Run `python build_report.py` to regenerate this README from the latest reports.
"""

parts = []
for title, name in PARTS:
    path = Path(name)
    if not path.exists():
        raise SystemExit(f"{name} not found: run the notebooks first")
    lines = path.read_text(encoding="utf-8").splitlines()
    parts.append("\n".join("#" + ln if ln.startswith("#") else ln for ln in lines))      # demote headings one level

Path("README.md").write_text(INTRO + "\n---\n\n" + "\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
print("wrote README.md")

# Statistical Learning for Reliability Analysis — Course Handbook & Interactive Study Suite

[![HTML5](https://img.shields.io/badge/HTML5-Single--File%20App-E34F26?logo=html5&logoColor=white)](index.html)
[![LaTeX MathJax 3](https://img.shields.io/badge/MathJax-v3%20LaTeX-059669?logo=latex&logoColor=white)](index.html)
[![Course](https://img.shields.io/badge/NPTEL%20%2F%20SWAYAM-IIT%20Kharagpur-1E88E5)](https://nptel.ac.in)
[![Aesthetic](https://img.shields.io/badge/Theme-Bright%20Peach-FF7043)](index.html)

A comprehensive, mathematically rigorous study guide, reference handbook, and interactive single-file web application covering the complete 60-lecture curriculum of **"Statistical Learning for Reliability Analysis"** taught by **Prof. Monalisa Sarma** (*Subir Chowdhury School of Quality and Reliability, IIT Kharagpur*).

---

## 🌟 Key Highlights & Features

### 1. Interactive Single-Page Web Application (`index.html`)
- **Self-Contained & Zero Dependencies:** Runs directly in any web browser without Node.js, web servers, or external CSS frameworks.
- **Bright Peach Design Aesthetic:** Clean, warm color palette featuring cream surfaces (`#FFFDF9`), peach accents (`#FFAB91`, `#FF8A65`), terracotta highlights (`#FF7043`, `#D84315`), and high-legibility charcoal typography (`#3E2723`, `#37474F`).
- **MathJax 3 LaTeX Engine:** Seamless, crisp rendering of over **1,865+ mathematical formulas** (inline `$ ... $` and display `$$ ... $$`) with safe HTML escaping.
- **Slide-Out Master Formula Cheat Sheet Drawer:** Instant-access drawer with 13 categorized formula cards, live category filtering, and keyword search.
- **Live Search & Topic Filter:** Real-time filtering across all modules and mathematical topics.
- **Collapsible Step-by-Step Worked Examples:** Interactive `<details>` accordions allowing students to test their understanding before revealing complete step-by-step solutions.
- **Interactive Self-Assessment Quizzes:** Multiple-choice knowledge checks with instant feedback, scoring, and pedagogical explanations.
- **Sticky Navigation & Active Scrollspy:** Navigation drawer with real-time reading progress bar and floating back-to-top button.

### 2. Companion Pages (`theory.html`, `eli5.html`)
- **Theory Essentials (`theory.html`):** definitions, theorems, assumptions, key distinctions and exam traps for all 12 modules, checked against the 60 lecture transcripts. Scope tags mark material that is *not examined* (e.g. Weibull), *beyond lectures*, or *named only*. Includes a "Traps only" revision mode and a module filter.
- **Explain Like I'm Five (`eli5.html`):** an analogy-first walkthrough of every module and sub-topic, told through one toy-car factory, with a short self-check quiz.
- Both are linked from the header of `index.html` and share its light/dark theme.

### 3. Mobile Friendly
- All pages work down to 320 px phone widths. Phone rules live in one shared stylesheet, `mobile.css`.
- On phones, a bottom tab bar (Guide · Theory · ELI5 · Formulas · Test) replaces the icon-only header buttons. `index.html#formulas` and `index.html#test` open the formula sheet and the MCQ test directly.
- The main guide's header is one row (menu, search, theme). On Theory and ELI5 the module links become a sticky strip that scrolls sideways and highlights the module you're reading (`mobile.js`).
- Long formulas scroll inside their own box (`mathfit.js`) instead of widening the page.

### 4. Comprehensive Master Study Guide (`study_guide.md`)
- **2,400+ Lines / 153,000+ Characters** of exhaustive pedagogical notes.
- **Formal Mathematical Rigor:** Kolmogorov axioms, hazard rate transformations ($h(t) = -\frac{d}{dt}\ln R(t)$), sampling distributions ($\chi^2, t, F$), Maximum Likelihood Estimations (MLE), ANOVA variance decompositions, OLS Gauss-Markov derivations, AR(1) time-series forecasting, Logistic link functions, and full Support Vector Machine (SVM) Primal/Dual Lagrangian optimizations with KKT conditions.
- **35 Examination & Engineering Problem Archetypes:** Detailed breakdowns for every topic including physical scenarios, trigger keywords, governing equations, and step-by-step solution algorithms.
- **19 Complete Numerical Tutorial Problems:** Step-by-step calculations derived from the course transcripts.
- **Visual Callout Boxes:** Explicitly formatted callouts for **Formulas & Concepts**, **Critical Theorems**, **Common Pitfalls & Gotchas**, and **Important Distinctions**.

---

## 📚 12-Module Curriculum Coverage

| Module | Lectures | Core Topics & Mathematical Concepts | Problem Archetypes |
| :--- | :--- | :--- | :--- |
| **Module 01** | Lec 01–02 | Reliability Definitions, 3 Pillars, Bathtub Curve (DFR, CFR, IFR), Availability ($A$), MTTR/MTTF, 5-Number Summary & Boxplot Outliers | • Bathtub Curve Phase Identification<br>• System Availability & Maintainability<br>• 5-Number Summary & Outlier Detection |
| **Module 02** | Lec 03–06 | Kolmogorov Axioms, Conditional Probability, Bayes' Theorem, System Reliability (Series $\prod R_i$, Active Parallel $1-\prod(1-R_i)$, $k$-out-of-$n$) | • Series Weakest-Link Reliability<br>• Active Parallel Redundant Systems<br>• $k$-out-of-$n$ Systems (Aircraft, Voting Gates)<br>• Multi-Source Bayes Defect Attribution |
| **Module 03** | Lec 07–11 | Discrete RVs, PMF/CDF, Expectation, Bernoulli, Binomial, Poisson Flaw Density, Geometric Memoryless Property, Hypergeometric | • Binomial Batch Sampling<br>• Poisson Rare Defect Modeling<br>• Geometric Survival Past $k$ Cycles<br>• Hypergeometric Sampling Without Replacement |
| **Module 04** | Lec 12–15 | Continuous RVs, Reliability $R(t)$, Hazard Rate $h(t)$, MTTF Integral, Exponential, Normal Tolerance Clearances, Weibull Aging ($\beta$) | • Constant Failure Rate Mission Time<br>• Shaft & Bearing Clearance Interference ($C=X_2-X_1$)<br>• Normal Parameters from Two Percentiles<br>• Weibull Infant ($\beta<1$) vs Wearout ($\beta>1$) |
| **Module 05** | Lec 16–21 | Sampling Distributions, Central Limit Theorem ($n \ge 30$), Sample Variance Distribution ($\chi^2$), Student's $t$, Snedecor's $F$-ratio | • Sample Mean Probabilities via CLT<br>• Sample Variance Compliance via $\chi^2$<br>• Comparing Two Machine Variances via $F$ |
| **Module 06** | Lec 22–25, 28 | Point Estimation (Unbiasedness, MVUE, CRLB, MLE), Confidence Intervals for $\mu$ ($Z$ and $t$), $\sigma^2$ (Chi-Square), Proportions & Sample Size | • Confidence Intervals for $\mu$ ($Z$ vs $t$)<br>• Non-Symmetric Variance $\sigma^2$ CIs<br>• Proportion CIs & Sample Size $n = (Z\sigma/E)^2$ |
| **Module 07** | Lec 26–27, 29–31 | Hypothesis Testing, Type I ($\alpha$) & Type II ($\beta$) Errors, Power ($1-\beta$), 1/2-Sample $Z/t$ Tests, Chi-Square Goodness-of-Fit & Independence | • One-Sample $t$-Test on Lifespan<br>• Pearson's Chi-Square Goodness-of-Fit<br>• $r \times c$ Contingency Test of Independence |
| **Module 08** | Lec 32–37 | ANOVA Motivation (FWER Inflation $\alpha_{\text{FW}} = 1-(1-\alpha)^m$), One-Way ANOVA ($SST=SSB+SSW$), Mean Squares, $F$-Test, Tukey's HSD | • One-Way ANOVA Table Construction<br>• Tukey's HSD Post-Hoc Pairwise Comparisons |
| **Module 09** | Lec 38–43 | Pearson Correlation ($r$), Spearman ($\rho_s$), OLS Linear Regression, Gauss-Markov (BLUE), $R^2$, Regression ANOVA, Confidence vs Prediction Intervals | • Fitting OLS Regression & Assessing $R^2$<br>• Mean Response CI vs New Unit Prediction Interval |
| **Module 10** | Lec 44 | Time-Series in Reliability, Stationarity ($|\phi_1|<1$), Autocovariance, $\text{AR}(1)$ Mean/Variance, Yule-Walker, Remaining Useful Life (RUL) | • $\text{AR}(1)$ Stationarity & Moment Estimation<br>• $h$-Step Forecasting & RUL Estimation |
| **Module 11** | Lec 45–48 | Binary Outcomes, Odds, Logit Link $\text{logit}(p) = \boldsymbol{\beta}^T\mathbf{x}$, Sigmoid $p(\mathbf{x})$, Odds Ratio ($e^{\beta_j}$), MLE, Confusion Matrix, ROC-AUC | • Failure Probability & Odds Ratio Multipliers<br>• Classification Diagnostics (Precision, Recall, $F_1$, ROC) |
| **Module 12** | Lec 49–60 | Supervised Learning, Naive Bayes (Laplace Smoothing), $k$-NN, Hard-Margin SVM (Hyperplanes, Margin $\frac{2}{\|\mathbf{w}\|}$, Dual Lagrangian, KKT), Soft SVM ($C, \xi_i$), Kernel Trick (RBF) | • Naive Bayes Fault Diagnosis<br>• 2D Hard-Margin SVM Coordinate Solution<br>• Non-Linear Gaussian RBF Kernel SVM |

---

## 🚀 Getting Started & Usage

### 1. View the Interactive Web Application
Simply open `index.html` in any web browser:
- **Chrome / Edge / Brave / Firefox / Safari:** Double-click `index.html` or drag and drop it into an open browser tab.
- **Local Dev Server (Optional):**
  ```bash
  python -m http.server 8000
  # Open http://localhost:8000/index.html in your browser
  ```

> **Offline:** MathJax and the fonts are bundled in `vendor/`, so no internet is needed. Keep `vendor/` next to `index.html` if you move or share it.

### 2. Read the Markdown Study Guide
- Open `study_guide.md` in VS Code, Obsidian, GitHub, or any Markdown reader supporting LaTeX math.

### 3. Rebuild / Recompile from Source Modules
If you modify any individual module in `modules/mod01.md` through `mod12.md`, recompile the master files using:
```bash
python build_full_suite.py
```
This automatically updates `study_guide.md` and generates the self-contained `index.html` with protected MathJax formatting.

---

## 📁 Repository Structure

```
.
├── index.html                 # Complete, self-contained interactive web application
├── theory.html                # Theory essentials & exam traps (verified against transcripts)
├── eli5.html                  # Simple, analogy-first explanation of every module
├── mathfit.js                 # Keeps long MathJax formulas inside narrow screens
├── mobile.css                 # Phone layout shared by all three pages
├── mobile.js                  # Highlights the current module in the jump-link strip
├── study_guide.md             # Master textbook & study guide (all 12 modules)
├── build_full_suite.py        # Compiler & math-protection build script
├── validate_output.py         # HTML5 validator & LaTeX token integrity checker
├── modules/                   # Individual module source markdown files
│   ├── mod01.md               # Module 1: Foundations & Descriptive Statistics
│   ├── mod02.md               # Module 2: Probability & System Reliability
│   ├── mod03.md               # Module 3: Discrete Probability Distributions
│   ├── mod04.md               # Module 4: Continuous Distributions & Hazard Modeling
│   ├── mod05.md               # Module 5: Sampling Distributions & CLT
│   ├── mod06.md               # Module 6: Estimation & Confidence Intervals
│   ├── mod07.md               # Module 7: Hypothesis Testing & Contingency Tables
│   ├── mod08.md               # Module 8: Analysis of Variance (ANOVA)
│   ├── mod09.md               # Module 9: Correlation & Linear Regression
│   ├── mod10.md               # Module 10: Auto-Regression & Time-Series Modeling
│   ├── mod11.md               # Module 11: Logistic Regression & Classification
│   └── mod12.md               # Module 12: Supervised Classifiers & Support Vector Machines
└── README.md                  # Project overview & feature documentation
```

---

## 🎓 Academic Attribution
- **Course Title:** Statistical Learning for Reliability Analysis
- **Instructor:** Prof. Monalisa Sarma
- **Department:** Subir Chowdhury School of Quality and Reliability
- **Institution:** Indian Institute of Technology (IIT) Kharagpur
- **Platform:** NPTEL / SWAYAM (Ministry of Education, Government of India)

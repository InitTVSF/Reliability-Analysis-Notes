# STATISTICAL LEARNING FOR RELIABILITY ANALYSIS
## Complete Comprehensive Course Study Guide & Reference Handbook
**Instructor:** Prof. Monalisa Sarma | *Subir Chowdhury School of Quality and Reliability, IIT Kharagpur*  
**Course Code:** NPTEL / SWAYAM | **Coverage:** Complete Curriculum (Lectures 01 – 60)

---

> [!NOTE]
> **About this Master Study Guide:**  
> This comprehensive study guide provides an exhaustive, mathematically rigorous, and pedagogically structured synthesis of the complete 60-lecture curriculum. It includes all formal definitions, Kolmogorov axioms, probability theorems, sampling distributions, inferential testing catalogs, ANOVA decompositions, regression equations, time-series forecasting, and machine learning classifiers (Naive Bayes, $k$-NN, Support Vector Machines & Kernel Methods). For every topic, it details **Problem Types Commonly Solved**, trigger keywords, step-by-step solution algorithms, and worked numerical tutorial examples directly from the course transcripts.

---

## TABLE OF CONTENTS
1. [Module 1: Foundations of Reliability Engineering & Statistical Thinking (Lectures 01–02)](#module-1-foundations-of-reliability-engineering--statistical-thinking-lectures-0102)
2. [Module 2: Probability Theory, Set Operations & System Reliability Modeling (Lectures 03–06)](#module-2-probability-theory-set-operations--system-reliability-modeling-lectures-0306)
3. [Module 3: Discrete Probability Distributions & Reliability Applications (Lectures 07–11)](#module-3-discrete-probability-distributions--reliability-applications-lectures-0711)
4. [Module 4: Continuous Probability Distributions & Hazard Rate Modeling (Lectures 12–15)](#module-4-continuous-probability-distributions--hazard-rate-modeling-lectures-1215)
5. [Module 5: Sampling Distributions & The Central Limit Theorem (Lectures 16–21)](#module-5-sampling-distributions--the-central-limit-theorem-lectures-1621)
6. [Module 6: Statistical Inference — Point Estimation & Confidence Intervals (Lectures 26–28)](#module-6-statistical-inference--point-estimation--confidence-intervals-lectures-2628)
7. [Module 7: Statistical Inference — Hypothesis Testing & Goodness-of-Fit (Lectures 22–25, 29–31)](#module-7-statistical-inference--hypothesis-testing--goodness-of-fit-lectures-2225-2931)
8. [Module 8: Analysis of Variance (ANOVA) (Lectures 32–37)](#module-8-analysis-of-variance-anova-lectures-3237)
9. [Module 9: Correlation & Linear Regression Analysis (Lectures 38–43)](#module-9-correlation--linear-regression-analysis-lectures-3843)
10. [Module 10: Auto-Regression & Time-Series Modeling for Reliability (Lecture 44)](#module-10-auto-regression--time-series-modeling-for-reliability-lecture-44)
11. [Module 11: Logistic Regression & Binary Classification (Lectures 45–48)](#module-11-logistic-regression--binary-classification-lectures-4548)
12. [Module 12: Machine Learning Classifiers: Bayes, k-NN & Support Vector Machines (Lectures 49–60)](#module-12-machine-learning-classifiers-bayes-k-nn--support-vector-machines-lectures-4960)

---


# MODULE 1: Foundations of Reliability Engineering & Statistical Thinking (Lectures 01–02)

## 1.1 Introduction to Reliability Engineering

### 1.1.1 The Ubiquity and Impact of System Failures
In contemporary engineering and daily life, human activities depend heavily on complex machines and technological systems. Failures occur across all scales:
- **Everyday Failures:** Washing machine wear-out, dead car batteries, burnt toaster plugs (design defects), leaking roofs (faulty construction), leaking water heaters (corrosion due to neglected preventive maintenance).
- **Catastrophic Failures:**
  - **Chernobyl Nuclear Disaster (1986, Ukraine):** Flawed reactor design and operator procedural violations leading to catastrophic core meltdown, severe radiation casualties, and billions of dollars in environmental cleanup costs.
  - **Bhopal Gas Tragedy (1984, India):** Toxic methyl isocyanate release resulting in mass casualties and permanent health crises.
  - **Space Shuttle Challenger Explosion (1986):** O-ring seal elasticity loss caused by operating outside designed thermal boundaries.
  - **Three Mile Island (1979) & Ford Pinto Recall (1970s):** Critical cooling and fuel tank design vulnerabilities.

A 1970s social science survey of over 1,000 consumers revealed that while functional performance is expected, **reliability** and **maintainability** are rated as primary purchasing criteria, far outweighing cosmetic appearance or brand novelty.

---

### 1.1.2 The Three Core Compulsions for Reliability
1. **Economic Compulsion:** The "throw-away" culture is obsolete due to high material and energy costs. Competitive global markets demand high customer satisfaction, low warranty costs, trouble-free service, and minimum life-cycle cost ($LCC$).
2. **Environmental Compulsion:** Non-eco-friendly and unsafe products cause pollution, ozone depletion, and global warming. Exhaustible raw materials mandate sustainable, durable, and recyclable designs.
3. **Performance Compulsion:** Modern multi-functional products must meet increasingly complex demands without escalating maintenance costs.

---

### 1.1.3 Formal Definition of Reliability

#### IEC Standard Definition
According to the **International Electrotechnical Commission (IEC)**:
> "Reliability is the capability of a product, system, or service to perform its expected job under specific conditions of use over an intended period of time."

#### Three Fundamental Pillars
1. **Expected Job (Performance Limits):** Satisfactory operation within strictly defined functional boundaries (e.g., a missile hitting a target with specified accuracy and velocity).
2. **Conditions of Use (Operating Environment):** Specified environmental and operational conditions (temperature, humidity, vibration, electrical stress). A luxury sedan is not engineered for rugged mountain terrains.
3. **Mission Time ($t$):** The required time duration over which zero failures are tolerated (e.g., missile launch-to-impact duration).

#### The Probabilistic Definition
To quantify "capability" scientifically and engineer it into products:
$$\text{Reliability } R(t) = P(T > t)$$
where $T$ is the random variable representing time-to-failure, and $t$ is the specified mission duration under stated operating conditions.

---

### 1.1.4 Related Dependability Concepts
- **Maintainability ($M(t)$):** The probability that a failed system can be retained in or restored to a specified operational state within a given period when maintenance is performed using prescribed procedures and resources. Measured by **Mean Time To Repair ($MTTR$)** or serviceability.
- **Availability ($A(t)$):** The probability that a system is operating satisfactorily at any given time $t$ when used under stated conditions.
  $$\text{Operational Availability } A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}} \times 100\%$$

---

### 1.1.5 Failure Analysis & The Bathtub Curve
A **failure** is the event or inoperable state in which any item or part of an item does not perform its specified function within defined limits.
- **Critical Failure:** Causes complete mission abortion or poses safety hazards.
- **Dependent Failure:** A failure caused directly or indirectly by the failure of an associated item.

#### The Bathtub Curve (Hazard Rate $h(t)$ over Product Lifecycle)
The lifetime failure rate of hardware components typically follows three distinct operational phases:

1. **Phase I: Infant Mortality / Early Life (Quality Failures)**
   - **Hazard Rate:** Decreasing failure rate ($DFR$, $dh(t)/dt < 0$).
   - **Root Causes:** Manufacturing defects, substandard materials, improper assembly, poor quality control, "teething" problems.
   - **Remedies:** Burn-in testing, environmental stress screening (ESS), strict supplier quality assurance.
2. **Phase II: Useful Life / Normal Operation (Chance / Intrinsic Failures)**
   - **Hazard Rate:** Constant failure rate ($CFR$, $h(t) = \lambda = \text{const}$).
   - **Root Causes:** Unpredictable environmental shocks, extreme operational overstress, random external events (lightning, earthquakes).
   - **Governing Distribution:** Exponential distribution.
3. **Phase III: Wear-Out Life (Aging & Degradation Failures)**
   - **Hazard Rate:** Increasing failure rate ($IFR$, $dh(t)/dt > 0$).
   - **Root Causes:** Mechanical wear, fatigue, corrosion, chemical degradation, oxidation, insulation breakdown.
   - **Remedies:** Preventive maintenance, scheduled component replacement, derating.

```
Hazard Rate h(t)
 ^
 | \  Infant Mortality     Useful Life (Constant)      Wear-Out
 |  \  (Burn-in)            h(t) = \lambda = const         (Aging)
 |   \                                              /
 |    \____________________________________________/
 0--------------------------------------------------------> Time (t)
```

---

## 1.2 Introduction to Statistical Methods in Reliability

### 1.2.1 Statistical Thinking & The Japanese Industrial Miracle
In the mid-20th century, Japanese manufacturing achieved global preeminence by transitioning from passive data collection to **active statistical thinking and Statistical Process Control (SPC)** (championed by W. Edwards Deming and Joseph Juran). Statistics provides scientific decision-making under uncertainty and process variation.

---

### 1.2.2 Populations, Samples, and Variables
- **Population:** The entire collection of entities or units of interest (e.g., all 10,000 turbine blades produced in a manufacturing run). Characterized by fixed **Parameters** ($\mu, \sigma^2, p$).
- **Sample:** A representative subset of observations drawn from the population. Characterized by sample **Statistics** ($\bar{X}, S^2, \hat{p}$).
- **Representative Sampling:** Crucial to avoid selection bias (e.g., stratified demographic sampling in election exit polls).
- **Observation:** A set of recorded measurements from a single experimental unit.

#### Classification of Variables
1. **Qualitative (Categorical) Variables:**
   - **Nominal:** Unordered labels, categories, or names (e.g., Component manufacturer {Brand A, Brand B}, Failure mode {Open, Short, Fracture}, Zip code).
   - **Ordinal:** Categories with a natural intrinsic ordering or ranking (e.g., Customer satisfaction {1: Poor, 2: Moderate, 3: High}, Defect severity {Minor, Major, Critical}).
2. **Quantitative (Numerical) Variables:**
   - **Discrete:** Countable integer values resulting from counting processes (e.g., Number of solder defects per circuit board, number of component breakdowns).
   - **Continuous:** Uncountable real values within an interval resulting from measurement (e.g., Time-to-failure in hours, operating temperature in $^\circ\text{C}$, tensile strength in $\text{MPa}$).

---

### 1.2.3 Data Organization & Visualization Tools
- **Frequency Distribution:** Tabulation grouping data into mutually exclusive classes showing the count ($f_i$) in each category.
- **Relative Frequency (Empirical Probability):** $r_i = f_i / N$. Represents the observed probability of an event in random sampling.
- **Cumulative Frequency / Relative Frequency:** Sum of frequencies up to the upper boundary of each class.
- **Graphical Representations:**
  - **Bar Chart:** Visual representation for categorical data; width has no metric meaning; spaces separate bars.
  - **Histogram:** Visual representation for continuous quantitative data; area of each bin is proportional to class frequency; no gaps between contiguous intervals.
  - **Pie Chart:** Angular sectors representing proportional shares ($\theta_i = r_i \times 360^\circ$).
  - **Box-and-Whisker Plot (Five-Number Summary):** Displays Minimum, First Quartile ($Q_1$, 25th percentile), Median ($Q_2$, 50th percentile), Third Quartile ($Q_3$, 75th percentile), and Maximum. The Interquartile Range ($\text{IQR} = Q_3 - Q_1$) measures spread; outliers lie outside $[Q_1 - 1.5\text{IQR}, Q_3 + 1.5\text{IQR}]$.
  - **Scatter Plot:** Two-dimensional Cartesian plot displaying pairs $(x_i, y_i)$ to visualize relationships, clustering, and correlation.

---

### 1.2.4 Measures of Central Tendency and Dispersion

#### Central Tendency
- **Sample Mean:** $\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$ (sensitive to extreme outliers).
- **Median:** Middle value when observations are sorted in ascending order (robust to outliers).
- **Mode:** Most frequently occurring value in the dataset.

#### Dispersion (Variability)
- **Range:** $\text{Max} - \text{Min}$.
- **Sample Variance ($S^2$):**
  $$S^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2 = \frac{1}{n-1} \left[ \sum_{i=1}^n x_i^2 - \frac{(\sum x_i)^2}{n} \right]$$
  *(Note: Divisor $n-1$ ensures an unbiased estimator of population variance $\sigma^2$.)*
- **Sample Standard Deviation ($S$):** $S = \sqrt{S^2}$.

---

> [!NOTE]
> **Key Formula Reference: Reliability Metrics**
> - **Reliability:** $R(t) = P(T > t) = 1 - F(t)$
> - **Operational Availability:** $A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}}$
> - **Sample Variance:** $S^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$

> [!WARNING]
> **Common Pitfall: Conflating Reliability with Quality**
> Quality is conformance to specifications at the time of manufacture ($t = 0$), whereas Reliability is quality over time ($t > 0$) under stated environmental stress. A high-quality component at delivery can exhibit catastrophic unreliability if environmental stresses (thermal, vibrational) induce rapid aging.
---

## 1.3 Problem Types Commonly Solved in Reliability Foundations & Descriptive Statistics

### Problem Type 1.1: Bathtub Curve Failure Phase & Reliability Strategy Identification
- **Engineering / Exam Scenario:** A quality engineer receives failure data or hazard rate observations over time for a batch of industrial components and must identify which phase of the Bathtub Curve the product is currently operating in, determine the root cause category, and propose appropriate engineering remedies.
- **Trigger Keywords:** *"Infant mortality"*, *"burn-in testing"*, *"useful life"*, *"constant failure rate"*, *"wear-out"*, *"preventive maintenance"*, *"hazard rate trend"*.
- **Solution Strategy:**
  1. **Examine Hazard Trend:**
     - If $\frac{d h(t)}{dt} < 0$ (Decreasing Failure Rate - DFR) $\implies$ **Phase I (Infant Mortality)** caused by manufacturing defects/material flaws. *Remedy:* Burn-in screening and strict supplier QA.
     - If $\frac{d h(t)}{dt} = 0$ (Constant Failure Rate - CFR, $h(t) = \lambda$) $\implies$ **Phase II (Useful Life)** caused by random chance environmental overstress shocks. *Governing Model:* Exponential distribution.
     - If $\frac{d h(t)}{dt} > 0$ (Increasing Failure Rate - IFR) $\implies$ **Phase III (Wear-out)** caused by mechanical fatigue, corrosion, or insulation aging. *Remedy:* Scheduled replacement and preventive maintenance.

---

### Problem Type 1.2: System Availability & Inherent Maintainability Calculations
- **Engineering / Exam Scenario:** Given Mean Time To Failure (MTTF) and Mean Time To Repair (MTTR) under steady-state operating conditions, compute inherent system availability and determine the required reduction in MTTR to achieve target "nines" of availability (e.g., 99.9% uptime).
- **Trigger Keywords:** *"Operational availability"*, *"MTTF"*, *"MTTR"*, *"uptime ratio"*, *"steady-state availability"*.
- **Core Formula:**
  $$A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}} = \frac{\mu}{\mu + \tau}$$
- **Solution Strategy:**
  1. Express both MTTF and MTTR in identical time units (hours, days).
  2. Substitute into $A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}}$.
  3. To solve for required $\text{MTTR}^*$ given target availability $A^*$: $\text{MTTR}^* = \text{MTTF} \left( \frac{1 - A^*}{A^*} \right)$.

---

### Problem Type 1.3: Five-Number Summary & Outlier Detection in Reliability Telemetry
- **Engineering / Exam Scenario:** Given a dataset of component operating temperatures or vibration amplitudes, determine the Five-Number Summary, calculate the Interquartile Range (IQR), and identify any extreme outliers using Tukey's 1.5×IQR criterion.
- **Trigger Keywords:** *"Quartiles"*, *"IQR"*, *"outlier fences"*, *"box-and-whisker plot"*, *"five-number summary"*.
- **Core Formulas:**
  $$\text{IQR} = Q_3 - Q_1$$
  $$\text{Lower Inner Fence} = Q_1 - 1.5 \times \text{IQR}, \quad \text{Upper Inner Fence} = Q_3 + 1.5 \times \text{IQR}$$
- **Solution Strategy:**
  1. Sort data in ascending order: $x_{(1)} \le x_{(2)} \le \dots \le x_{(n)}$.
  2. Compute Median ($Q_2$), first quartile ($Q_1$), and third quartile ($Q_3$).
  3. Compute $\text{IQR} = Q_3 - Q_1$.
  4. Flag any data point $x_i < Q_1 - 1.5\text{IQR}$ or $x_i > Q_3 + 1.5\text{IQR}$ as an outlier.

---

# MODULE 2: Probability Theory, Set Operations & System Reliability Modeling (Lectures 03–06)

## 2.1 Set Theory Foundations and Sample Spaces

### 2.1.1 Random Experiments, Sample Spaces, and Events
- **Random Experiment:** An experiment whose outcome cannot be predicted with certainty in advance, but whose set of all possible outcomes is known (e.g., lifetime testing of an electronic component until failure).
- **Sample Space ($S$ or $\Omega$):** The set of all possible basic outcomes of a random experiment.
  - *Discrete Sample Space:* Countable number of outcomes (e.g., tossing a coin until Heads appears: $S = \{H, TH, TTH, \dots\}$).
  - *Continuous Sample Space:* Uncountable continuum of outcomes (e.g., operational lifetime of a turbocharger: $S = \{t \in \mathbb{R} \mid t \ge 0\}$).
- **Event ($A$):** Any subset of the sample space ($A \subseteq S$).
  - *Null / Impossible Event ($\emptyset$):* Event containing no sample points ($P(\emptyset) = 0$).
  - *Certain / Sure Event ($S$):* Event containing all sample points ($P(S) = 1$).
  - *Simple Event:* Contains exactly one sample outcome.
  - *Compound Event:* Contains two or more sample outcomes.

---

### 2.1.2 Set Operations & Laws
- **Union ($A \cup B$):** Event that occurs if $A$ occurs, $B$ occurs, or both occur ($A \text{ OR } B$).
- **Intersection ($A \cap B$ or $AB$):** Event that occurs if both $A$ and $B$ occur simultaneously ($A \text{ AND } B$).
- **Complement ($A^c$ or $A'$ or $\bar{A}$):** Event that $A$ does not occur ($A^c = S \setminus A$).
- **Mutually Exclusive (Disjoint) Events:** Two events that cannot occur simultaneously ($A \cap B = \emptyset$).
- **Collectively Exhaustive Events:** A set of events whose union spans the entire sample space ($\bigcup_{i=1}^k B_i = S$).
- **De Morgan's Laws:**
  $$(A \cup B)^c = A^c \cap B^c, \qquad (A \cap B)^c = A^c \cup B^c$$
  *Generalization:*
  $$\left( \bigcup_{i=1}^n A_i \right)^c = \bigcap_{i=1}^n A_i^c, \qquad \left( \bigcap_{i=1}^n A_i \right)^c = \bigcup_{i=1}^n A_i^c$$

---

## 2.2 Axiomatic Probability & Probability Rules

### 2.2.1 Kolmogorov's Axioms of Probability
For a sample space $S$ and an event space $\mathcal{F}$, a probability measure $P: \mathcal{F} \to [0, 1]$ satisfies:
1. **Axiom 1 (Non-negativity):** $P(A) \ge 0$ for every event $A \subseteq S$.
2. **Axiom 2 (Unit Measure / Normalization):** $P(S) = 1$.
3. **Axiom 3 (Countable Additivity):** For any sequence of mutually exclusive events $A_1, A_2, A_3, \dots$ ($A_i \cap A_j = \emptyset$ for $i \neq j$):
   $$P\left( \bigcup_{i=1}^\infty A_i \right) = \sum_{i=1}^\infty P(A_i)$$

#### Derived Mathematical Properties
- $P(\emptyset) = 0$
- $P(A^c) = 1 - P(A)$
- If $A \subseteq B$, then $P(A) \le P(B)$ and $P(B \setminus A) = P(B) - P(A)$
- $0 \le P(A) \le 1$

---

### 2.2.2 The General Addition Rules
- **For Two Arbitrary Events:**
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
- **For Three Arbitrary Events:**
  $$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

---

## 2.3 Conditional Probability & Independence

### 2.3.1 Definition of Conditional Probability
The conditional probability of event $A$ given that event $B$ has already occurred ($P(B) > 0$) is:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

#### Multiplication Rule of Probability
$$P(A \cap B) = P(B) P(A \mid B) = P(A) P(B \mid A)$$
For $n$ events $A_1, A_2, \dots, A_n$:
$$P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) P(A_2 \mid A_1) P(A_3 \mid A_1 \cap A_2) \dots P(A_n \mid A_1 \cap \dots \cap A_{n-1})$$

---

### 2.3.2 Statistical Independence
Two events $A$ and $B$ are **statistically independent** if and only if the occurrence of one provides no information about the probability of the other:
$$P(A \mid B) = P(A) \iff P(B \mid A) = P(B) \iff P(A \cap B) = P(A) P(B)$$

> [!CAUTION]
> **Common Pitfall: Mutually Exclusive vs. Independent Events**
> - **Mutually Exclusive:** $A \cap B = \emptyset \implies P(A \cap B) = 0$. (Cannot happen together).
> - **Independent:** $P(A \cap B) = P(A)P(B) > 0$ (for non-trivial events).
> Two non-null events *cannot* be simultaneously mutually exclusive and statistically independent! If $A$ and $B$ are mutually exclusive, the occurrence of $A$ guarantees that $B$ did not occur ($P(B|A) = 0 \neq P(B)$), making them strongly dependent.

---

## 2.4 Total Probability & Bayes' Theorem

### 2.4.1 Law of Total Probability (Partition Theorem)
Let $B_1, B_2, \dots, B_k$ constitute a partition of the sample space $S$ (i.e., $B_i \cap B_j = \emptyset$ for $i \neq j$, $\bigcup_{i=1}^k B_i = S$, and $P(B_i) > 0$). Then for any event $A \subseteq S$:
$$P(A) = \sum_{i=1}^k P(A \cap B_i) = \sum_{i=1}^k P(A \mid B_i) P(B_i)$$

```
Sample Space S:
+------------------------------------+
|  B1       |  B2       |  B3        |
|      .----+----.      |            |
|     /     |     \     |            |
|    (   Event A   )    |            |
|     \     |     /     |            |
|      '----+----'      |            |
+------------------------------------+
P(A) = P(A|B1)P(B1) + P(A|B2)P(B2) + P(A|B3)P(B3)
```

---

### 2.4.2 Bayes' Theorem (Reverse / Inverse Probability)
Bayes' Theorem updates the prior probability of an unseen cause $B_j$ given the observed evidence $A$:
$$P(B_j \mid A) = \frac{P(A \mid B_j) P(B_j)}{\sum_{i=1}^k P(A \mid B_i) P(B_i)}$$

- **Prior Probability ($P(B_j)$):** Initial belief before observing evidence $A$.
- **Likelihood ($P(A \mid B_j)$):** Probability of observing evidence $A$ assuming state $B_j$ is true.
- **Marginal Likelihood / Evidence ($P(A)$):** Total probability of evidence across all hypotheses.
- **Posterior Probability ($P(B_j \mid A)$):** Updated probability of cause $B_j$ after observing evidence $A$.

---

## 2.5 System Reliability Configurations & Modeling

### 2.5.1 Series System (Weakest-Link Structure)
In a series system, all $n$ components must function successfully for the system to operate. Failure of any single component causes immediate system failure.
$$R_{\text{series}}(t) = P(T_1 > t \cap T_2 > t \cap \dots \cap T_n > t)$$
Assuming component failures are **statistically independent**:
$$R_s = \prod_{i=1}^n R_i = R_1 \times R_2 \times \dots \times R_n$$
For $n$ identical components with reliability $R$:
$$R_s = R^n$$

*Key Implication:* System reliability is never higher than the reliability of its least reliable component ($R_s \le \min_i R_i$). It is strictly lower whenever any other component has $R_i < 1$.

```
[In] ---> [ Component 1 ] ---> [ Component 2 ] ---> [ Component n ] ---> [Out]
```

---

### 2.5.2 Parallel System (Active Redundancy)
In a parallel system, all $n$ components operate simultaneously. The system functions as long as **at least one** component survives. The system fails only if **all** components fail.
$$F_{\text{parallel}}(t) = P(T_1 \le t \cap T_2 \le t \cap \dots \cap T_n \le t) = \prod_{i=1}^n (1 - R_i)$$
Therefore, system reliability is:
$$R_{\text{parallel}} = 1 - \prod_{i=1}^n (1 - R_i) = 1 - \prod_{i=1}^n Q_i$$
For $n$ identical components with reliability $R$:
$$R_p = 1 - (1 - R)^n$$

```
         +---> [ Component 1 ] ---+
         |                        |
[In] --->+---> [ Component 2 ] ---+---> [Out]
         |                        |
         +---> [ Component n ] ---+
```

---

### 2.5.3 Combined Series-Parallel Systems
Complex systems are evaluated hierarchically by reducing series and parallel subsystems into equivalent single-block reliabilities.

---

### 2.5.4 $k$-out-of-$n$ Active Redundant System
A system containing $n$ identical and independent components that functions successfully if and only if **at least $k$** of the $n$ components are operational:
$$R_{k/n} = \sum_{i=k}^n \binom{n}{i} R^i (1 - R)^{n-i}$$
- When $k = n$: Reduces to a **Series system** ($R_{n/n} = R^n$).
- When $k = 1$: Reduces to a **Parallel system** ($R_{1/n} = 1 - (1 - R)^n$).
- When $k = 2, n = 3$ (e.g., 2-out-of-3 majority voting or tri-engine aircraft):
  $$R_{2/3} = \binom{3}{2} R^2(1-R) + \binom{3}{3} R^3 = 3R^2(1-R) + R^3 = 3R^2 - 2R^3$$

---

## 2.6 Step-by-Step Worked Tutorial Problems

### Problem 2.1: Tri-Engine Aircraft Crash Reliability
**Statement:** An aircraft is equipped with $3$ identical, active, independent engines in parallel. The probability that any individual engine fails during a transoceanic flight is $q = 0.05$ (engine reliability $R = 0.95$). The aircraft can sustain flight if at least $2$ engines operate successfully. It crashes if $2$ or more engines fail.
1. What is the probability that the aircraft completes the flight successfully?
2. What is the probability of the aircraft crashing?

**Solution:**
- Number of components $n = 3$, requirement $k = 2$.
- Component reliability $R = 0.95$, failure probability $q = 1 - R = 0.05$.
- Using the $k$-out-of-$n$ formulation:
  $$R_{\text{flight}} = R_{2/3} = \binom{3}{2} R^2(1-R) + \binom{3}{3} R^3 = 3(0.95)^2(0.05) + (0.95)^3$$
  $$3(0.9025)(0.05) = 0.135375$$
  $$(0.95)^3 = 0.857375$$
  $$R_{\text{flight}} = 0.135375 + 0.857375 = 0.99275$$
- Probability of crash:
  $$P(\text{Crash}) = 1 - R_{\text{flight}} = 1 - 0.99275 = 0.00725 \quad (0.725\%)$$
  *Alternative Verification via failure combinations:*
  $$P(\text{Crash}) = P(2 \text{ engines fail}) + P(3 \text{ engines fail}) = \binom{3}{2}(0.05)^2(0.95) + \binom{3}{3}(0.05)^3 = 3(0.0025)(0.95) + 0.000125 = 0.007125 + 0.000125 = 0.00725$$

---

### Problem 2.2: Multi-Factory Quality Control via Bayes' Theorem
**Statement:** A company procures microprocessors from three semiconductor foundries: $B_1, B_2, B_3$.
- Factory $B_1$ supplies $50\%$ of total inventory ($P(B_1) = 0.50$) with a defect rate of $1\%$ ($P(D \mid B_1) = 0.01$).
- Factory $B_2$ supplies $30\%$ of total inventory ($P(B_2) = 0.30$) with a defect rate of $2\%$ ($P(D \mid B_2) = 0.02$).
- Factory $B_3$ supplies $20\%$ of total inventory ($P(B_3) = 0.20$) with a defect rate of $5\%$ ($P(D \mid B_3) = 0.05$).

A microprocessor is selected at random from the assembly line and found to be **defective** ($D$).
1. What is the overall probability $P(D)$ of selecting a defective chip?
2. Given that the chip is defective, what is the posterior probability that it originated from Factory $B_3$?

**Solution:**
- **Step 1: Total Probability of Defect $P(D)$:**
  $$P(D) = P(D \mid B_1)P(B_1) + P(D \mid B_2)P(B_2) + P(D \mid B_3)P(B_3)$$
  $$P(D) = (0.01)(0.50) + (0.02)(0.30) + (0.05)(0.20) = 0.005 + 0.006 + 0.010 = 0.021 \quad (2.1\%)$$
- **Step 2: Posterior Probability $P(B_3 \mid D)$ via Bayes' Theorem:**
  $$P(B_3 \mid D) = \frac{P(D \mid B_3)P(B_3)}{P(D)} = \frac{(0.05)(0.20)}{0.021} = \frac{0.010}{0.021} = \frac{10}{21} \approx 0.4762 \quad (47.62\%)$$
- *Pedagogical Insight:* Although Factory $B_3$ manufactured only $20\%$ of total stock, its elevated failure rate makes it responsible for nearly half ($47.62\%$) of all observed failures!
---

## 2.5 Problem Types Commonly Solved in Probability & System Reliability

### Problem Type 2.1: Series System Reliability Under Independent Components
- **Engineering / Exam Scenario:** A mission-critical device consists of $n$ sub-assemblies connected such that the failure of any single part halts the entire system (weakest-link model). Given individual component reliabilities $R_1, R_2, \dots, R_n$, find overall system reliability $R_{\text{series}}$.
- **Trigger Keywords:** *"Series configuration"*, *"weakest link"*, *"no redundancy"*, *"all components must function"*.
- **Core Formula:**
  $$R_{\text{series}} = \prod_{i=1}^n R_i = R_1 \times R_2 \times \dots \times R_n$$
- **Key Insight:** $R_{\text{series}} \le \min(R_1, R_2, \dots, R_n)$. The system is never more reliable than its least reliable component.

---

### Problem Type 2.2: Active Parallel Redundant System Reliability
- **Engineering / Exam Scenario:** To improve mission reliability, $n$ identical or non-identical components are connected in parallel such that the system functions as long as at least one component survives.
- **Trigger Keywords:** *"Parallel redundancy"*, *"backup units"*, *"at least one unit operates"*, *"unreliability multiplication"*.
- **Core Formula:**
  $$Q_{\text{parallel}} = \prod_{i=1}^n Q_i = \prod_{i=1}^n (1 - R_i) \implies R_{\text{parallel}} = 1 - \prod_{i=1}^n (1 - R_i)$$
- **For $n$ identical components ($R_i = R$):** $R_{\text{parallel}} = 1 - (1 - R)^n$.
- **To find required number of redundant units $n$ for target reliability $R^*$:**
  $$1 - (1 - R)^n \ge R^* \implies (1 - R)^n \le 1 - R^* \implies n \ge \frac{\ln(1 - R^*)}{\ln(1 - R)}$$

---

### Problem Type 2.3: $k$-out-of-$n$ Active Redundancy Systems
- **Engineering / Exam Scenario:** A multi-engine aircraft with $n$ identical engines requires at least $k$ engines operating normally to maintain altitude, or a voting logic controller with $n$ sensors requires a majority ($k = \lceil (n+1)/2 \rceil$) of sensors to agree.
- **Trigger Keywords:** *"k-out-of-n:G system"*, *"at least k operational"*, *"tri-engine aircraft"*, *"majority voting gate"*.
- **Core Formula (for identical units with reliability $R$):**
  $$R_{k/n} = \sum_{i=k}^n \binom{n}{i} R^i (1 - R)^{n-i}$$
- **Solution Strategy:**
  1. Identify $n$ (total units) and $k$ (minimum surviving units).
  2. Compute binomial probabilities for each $i = k, k+1, \dots, n$.
  3. Sum the probabilities to obtain total system survival probability.

---

### Problem Type 2.4: Multi-Source Defect Diagnosis via Bayes' Theorem
- **Engineering / Exam Scenario:** Defective items are produced across $k$ different manufacturing plants or production shifts with known market shares $P(B_i)$ and known defect rates $P(A \mid B_i)$. Given that a randomly sampled component is defective, determine the posterior probability that it originated from Plant $j$.
- **Trigger Keywords:** *"Bayes' rule"*, *"posterior probability"*, *"given that it is defective"*, *"source attribution"*, *"false positive rate"*.
- **Core Formula:**
  $$P(B_j \mid A) = \frac{P(A \mid B_j) P(B_j)}{\sum_{i=1}^k P(A \mid B_i) P(B_i)}$$

---

# MODULE 3: Discrete Probability Distributions & Reliability Applications (Lectures 07–11)

## 3.1 Random Variables, PMF, and CDF

### 3.1.1 Concept of a Random Variable
A **Random Variable (RV)** $X$ is a measurable function mapping elements from a sample space $S$ to the real line $\mathbb{R}$:
$$X: S \to \mathbb{R}$$
- **Discrete Random Variable:** Takes on a finite or countably infinite set of values $\{x_1, x_2, x_3, \dots\}$.
- **Probability Mass Function (PMF) $p(x)$:**
  $$p(x) = P(X = x)$$
  *Axiomatic Properties:*
  1. $p(x_i) \ge 0, \quad \forall i$
  2. $\sum_{i} p(x_i) = 1$
- **Cumulative Distribution Function (CDF) $F(x)$:**
  $$F(x) = P(X \le x) = \sum_{x_i \le x} p(x_i)$$
  *Properties:* $F(x)$ is non-decreasing, right-continuous, $\lim_{x \to -\infty} F(x) = 0$, $\lim_{x \to \infty} F(x) = 1$.

---

### 3.1.2 Mathematical Expectation, Variance, and Moments
- **Expected Value (Mean $\mu$):**
  $$E[X] = \mu = \sum_{i} x_i p(x_i)$$
  *Linearity Property:* $E[aX + b] = aE[X] + b$, and $E[g(X)] = \sum_i g(x_i)p(x_i)$.
- **Variance ($\sigma^2$ or $\text{Var}(X)$):**
  $$\text{Var}(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$
  *Properties:* $\text{Var}(aX + b) = a^2 \text{Var}(X)$, $\text{Var}(X) \ge 0$.
- **Standard Deviation ($\sigma$):** $\sigma = \sqrt{\text{Var}(X)}$.
- **Moment Generating Function (MGF) $M_X(t)$:**
  $$M_X(t) = E[e^{tX}] = \sum_i e^{t x_i} p(x_i)$$
  The $k$-th raw moment is obtained via differentiation evaluated at $t = 0$:
  $$E[X^k] = \left. \frac{d^k M_X(t)}{dt^k} \right|_{t=0}$$

---

## 3.2 Standard Discrete Probability Distributions

### 3.2.1 Bernoulli Distribution
Models a single trial with binary outcomes: Success ($X = 1$) with probability $p$, and Failure ($X = 0$) with probability $q = 1-p$.
- **PMF:** $P(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}$
- **Mean:** $E[X] = p$
- **Variance:** $\text{Var}(X) = p(1-p)$

---

### 3.2.2 Binomial Distribution ($X \sim B(n, p)$)
Models the number of successes $X$ in $n$ independent and identical Bernoulli trials, each with constant success probability $p$.
- **PMF:**
  $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \dots, n$$
- **Mean:** $E[X] = np$
- **Variance:** $\text{Var}(X) = np(1-p)$
- **MGF:** $M_X(t) = (1 - p + p e^t)^n$

---

### 3.2.3 Poisson Distribution ($X \sim \text{Poisson}(\lambda)$)
Models the count of rare, independent events occurring within a fixed interval of time or space at a constant average rate $\lambda > 0$.
- **PMF:**
  $$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \dots$$
- **Mean:** $E[X] = \lambda$
- **Variance:** $\text{Var}(X) = \lambda$ *(Equality of mean and variance is a unique signature).*
- **MGF:** $M_X(t) = e^{\lambda(e^t - 1)}$

#### Poisson Approximation to the Binomial Distribution
When the number of trials $n$ is very large ($n \to \infty$) and the event probability $p$ is very small ($p \to 0$) such that $np = \lambda$ remains constant:
$$\lim_{n \to \infty} \binom{n}{k} p^k (1-p)^{n-k} = \frac{e^{-\lambda} \lambda^k}{k!}$$
*Rule of Thumb (as taught in Lec 11):* use it when $n > 10$ **and** $p < 0.1$; both conditions must hold. (Stricter textbook rules such as $n \ge 20,\ p \le 0.05$ also appear.)

---

### 3.2.4 Geometric Distribution ($X \sim \text{Geom}(p)$)
Models the number of independent Bernoulli trials $X$ required to achieve the **first** success.
- **PMF:**
  $$P(X = k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \dots$$
- **CDF:** $F(k) = P(X \le k) = 1 - (1-p)^k$
- **Survival Function:** $P(X > k) = (1-p)^k$
- **Mean:** $E[X] = \frac{1}{p}$
- **Variance:** $\text{Var}(X) = \frac{1-p}{p^2}$

#### The Memoryless Property of the Geometric Distribution
The geometric distribution is the **only** discrete distribution possessing the memoryless property:
$$P(X > s + t \mid X > s) = P(X > t), \quad \forall s, t \in \{1, 2, 3, \dots\}$$
*Proof:*
$$P(X > s + t \mid X > s) = \frac{P(X > s+t \cap X > s)}{P(X > s)} = \frac{P(X > s+t)}{P(X > s)} = \frac{(1-p)^{s+t}}{(1-p)^s} = (1-p)^t = P(X > t)$$
*Physical Meaning:* The past operating history does not affect the future probability of failure.

---

### 3.2.5 Negative Binomial Distribution ($X \sim \text{NB}(r, p)$)
Models the total number of trials $X$ required to achieve exactly $r$ successes.
- **PMF:**
  $$P(X = k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}, \quad k = r, r+1, r+2, \dots$$
- **Mean:** $E[X] = \frac{r}{p}$
- **Variance:** $\text{Var}(X) = \frac{r(1-p)}{p^2}$

---

### 3.2.6 Hypergeometric Distribution ($X \sim \text{Hypergeom}(N, K, n)$)
Models sampling **without replacement** from a finite population of size $N$ containing $K$ defective items and $N-K$ non-defective items, taking a sample of size $n$.
- **PMF:**
  $$P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}, \quad \max(0, n-(N-K)) \le k \le \min(n, K)$$
- **Mean:** $E[X] = n \left(\frac{K}{N}\right)$
- **Variance:** $\text{Var}(X) = n \left(\frac{K}{N}\right) \left(1 - \frac{K}{N}\right) \left(\frac{N-n}{N-1}\right)$
  *(The factor $\frac{N-n}{N-1}$ is the **Finite Population Correction (FPC)**).*

---

## 3.3 Step-by-Step Worked Tutorial Problems

### Problem 3.1: Quality Control Circuit Board Sampling (Binomial)
**Statement:** A manufacturing process produces printed circuit boards (PCBs) with an average defect probability of $p = 0.05$. A quality engineer draws a random sample of $n = 15$ boards.
1. What is the probability that exactly $2$ boards are defective?
2. What is the probability that $4$ or more boards are defective?

**Solution:**
- Let $X$ be the number of defective boards in $n = 15$ trials. $X \sim B(15, 0.05)$.
- **Part 1:** Exactly $2$ defectives:
  $$P(X = 2) = \binom{15}{2} (0.05)^2 (0.95)^{13} = \frac{15 \times 14}{2} (0.0025) (0.51334) = 105 \times 0.0025 \times 0.51334 \approx 0.13475 \quad (13.48\%)$$
- **Part 2:** $4$ or more defectives ($P(X \ge 4)$):
  $$P(X \ge 4) = 1 - P(X \le 3) = 1 - [P(X=0) + P(X=1) + P(X=2) + P(X=3)]$$
  $$P(X=0) = (0.95)^{15} \approx 0.46329$$
  $$P(X=1) = 15(0.05)(0.95)^{14} \approx 0.36576$$
  $$P(X=2) \approx 0.13475$$
  $$P(X=3) = \binom{15}{3} (0.05)^3 (0.95)^{12} = 455 \times 0.000125 \times 0.54036 \approx 0.03073$$
  $$P(X \le 3) = 0.46329 + 0.36576 + 0.13475 + 0.03073 = 0.99453$$
  $$P(X \ge 4) = 1 - 0.99453 = 0.00547 \quad (0.547\%)$$

---

### Problem 3.2: Transistor Defect Rate with Poisson Approximation
**Statement:** A semiconductor fabrication facility produces transistors with a defect probability of $p = 0.002$. A shipment contains $n = 1,000$ transistors.
1. What is the exact Binomial formulation and the Poisson approximation parameter $\lambda$?
2. What is the probability of finding exactly $3$ defective transistors?
3. What is the probability of finding at least $1$ defective transistor?

**Solution:**
- $n = 1000$ (large), $p = 0.002$ (small).
- Poisson parameter $\lambda = np = 1000 \times 0.002 = 2.0$.
- **Part 2:** $P(X = 3)$:
  $$P(X = 3) = \frac{e^{-2} (2)^3}{3!} = \frac{0.135335 \times 8}{6} = \frac{1.08268}{6} \approx 0.18045 \quad (18.05\%)$$
- **Part 3:** $P(X \ge 1)$:
  $$P(X \ge 1) = 1 - P(X = 0) = 1 - \frac{e^{-2} 2^0}{0!} = 1 - e^{-2} = 1 - 0.135335 = 0.864665 \quad (86.47\%)$$

---

### Problem 3.3: Component Life Testing (Geometric Distribution)
**Statement:** In an accelerated life test, components are tested sequentially one by one until the first component fails. The probability that any tested component fails during the screening interval is $p = 0.02$. What is the probability that an inspector tests more than $75$ components before encountering the first failure?

**Solution:**
- Let $X$ be the trial number on which the first failure occurs. $X \sim \text{Geom}(p = 0.02)$.
- The question asks for $P(X > 75)$.
- Using the survival function of the Geometric distribution:
  $$P(X > k) = (1 - p)^k$$
  $$P(X > 75) = (1 - 0.02)^{75} = (0.98)^{75}$$
  $$\ln(P(X > 75)) = 75 \times \ln(0.98) = 75 \times (-0.0202027) \approx -1.5152$$
  $$P(X > 75) = e^{-1.5152} \approx 0.2198 \quad (21.98\%)$$
---

## 3.6 Problem Types Commonly Solved in Discrete Probability Distributions

### Problem Type 3.1: Quality Control Batch Sampling (Binomial Distribution)
- **Engineering / Exam Scenario:** A lot contains items produced by a stable manufacturing process with a known constant defect probability $p$. A random sample of $n$ items is inspected with replacement. Find the probability of observing exactly $k$, at most $k$, or at least 1 defective unit.
- **Trigger Keywords:** *"Independent trials"*, *"constant probability p"*, *"fixed sample size n"*, *"sampling with replacement"*, *"at most k defectives"*.
- **Core Formulas:**
  $$P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}, \quad P(X \ge 1) = 1 - P(X = 0) = 1 - (1 - p)^n$$
- **Solution Strategy:**
  1. Check Bernoulli trial assumptions: $n$ fixed, 2 outcomes, constant $p$, independence.
  2. For "at least 1 defective", use the complement rule $1 - (1-p)^n$.

---

### Problem Type 3.2: Rare Event Failures & Flaw Density (Poisson Distribution)
- **Engineering / Exam Scenario:** Modeling the number of particle defects per square meter of silicon wafer, solder bridge flaws per printed circuit board, or cosmic-ray soft errors per hour in memory chips, where events occur randomly and independently in continuous space/time at an average rate $\lambda$.
- **Trigger Keywords:** *"Rare defects"*, *"Poisson process"*, *"average rate per unit area/time"*, *"Poisson approximation to Binomial ($n > 10$ and $p < 0.1$, $\lambda = np$)"*.
- **Core Formula:**
  $$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \dots$$
- **Zero-Failure Probability:** $P(X = 0) = e^{-\lambda}$.

---

### Problem Type 3.3: Life Testing Until First Failure (Geometric Distribution)
- **Engineering / Exam Scenario:** Components undergo repeated stress cycles or sequential testing. What is the probability that the first failure occurs on the $k$-th test? What is the probability that the component survives past $k$ cycles?
- **Trigger Keywords:** *"Number of trials until first failure"*, *"memoryless property"*, *"survival past k cycles"*.
- **Core Formulas:**
  $$P(X = k) = (1 - p)^{k-1} p, \quad P(X > k) = (1 - p)^k, \quad E[X] = \frac{1}{p}$$

---

### Problem Type 3.4: Acceptance Sampling Without Replacement (Hypergeometric Distribution)
- **Engineering / Exam Scenario:** A finite batch of size $N$ contains exactly $K$ defective items. An inspector draws a sample of $n$ items *without replacement*. Calculate the exact probability of finding $k$ defectives.
- **Trigger Keywords:** *"Finite population N"*, *"sampling without replacement"*, *"lot acceptance testing"*.
- **Core Formula:**
  $$P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}$$

---

# MODULE 4: Continuous Probability Distributions & Hazard Rate Modeling (Lectures 12–15)

## 4.1 Continuous Random Variables & Fundamental Reliability Functions

### 4.1.1 Continuous RVs, PDF, and CDF
A continuous random variable $X$ takes on uncountably infinite values over a continuum $[a, b] \subseteq \mathbb{R}$.
- **Probability Density Function (PDF) $f(x)$:**
  $$f(x) \ge 0, \quad \forall x \in \mathbb{R}$$
  $$\int_{-\infty}^\infty f(x) \, dx = 1$$
  $$P(a \le X \le b) = \int_a^b f(x) \, dx$$
  *(Note: For any single point $c$, $P(X = c) = 0$.)*
- **Cumulative Distribution Function (CDF) $F(x)$:**
  $$F(x) = P(X \le x) = \int_{-\infty}^x f(u) \, du$$
  $$f(x) = \frac{d F(x)}{dx}$$

---

### 4.1.2 The Reliability Function $R(t)$
Let $T \ge 0$ denote the continuous time-to-failure random variable of a component or system.
- **Reliability (Survival) Function $R(t)$:** The probability that the system functions without failure up to mission time $t$:
  $$R(t) = P(T > t) = 1 - F(t) = \int_t^\infty f(u) \, du$$
  *Boundary Conditions:* $R(0) = 1$, $\lim_{t \to \infty} R(t) = 0$, $\frac{d R(t)}{dt} \le 0$.
- **Unreliability / Failure Probability $F(t)$:**
  $$F(t) = P(T \le t) = 1 - R(t)$$
  $$f(t) = -\frac{d R(t)}{dt}$$

---

### 4.1.3 The Hazard Rate (Failure Rate) Function $h(t)$
The **Hazard Rate $h(t)$** (or instantaneous failure rate $Z(t)$) represents the conditional probability per unit time of failure in the infinitesimal interval $(t, t + \Delta t]$, given that the component has survived up to time $t$:
$$h(t) = \lim_{\Delta t \to 0} \frac{P(t < T \le t + \Delta t \mid T > t)}{\Delta t} = \lim_{\Delta t \to 0} \frac{F(t + \Delta t) - F(t)}{\Delta t \cdot R(t)} = \frac{f(t)}{R(t)}$$

#### Mathematical Relationship between $h(t)$ and $R(t)$
Since $f(t) = -\frac{d R(t)}{dt}$:
$$h(t) = -\frac{1}{R(t)} \frac{d R(t)}{dt} = -\frac{d}{dt} \left[ \ln R(t) \right]$$
Integrating both sides from $0$ to $t$ with initial condition $R(0) = 1$:
$$\int_0^t h(u) \, du = -\ln R(t) \implies \ln R(t) = -\int_0^t h(u) \, du$$
$$R(t) = \exp\left( -\int_0^t h(u) \, du \right) = e^{-H(t)}$$
where $H(t) = \int_0^t h(u) \, du$ is the **Cumulative Hazard Function**.
$$f(t) = h(t) \exp\left( -\int_0^t h(u) \, du \right) = h(t) e^{-H(t)}$$

---

### 4.1.4 Mean Time To Failure (MTTF)
The **Mean Time To Failure (MTTF)** is the expected operational lifetime of a non-repairable component:
$$\text{MTTF} = E[T] = \int_0^\infty t f(t) \, dt$$
Using integration by parts ($u = t, dv = f(t)dt \implies v = -R(t)$):
$$\text{MTTF} = \left[ -t R(t) \right]_0^\infty + \int_0^\infty R(t) \, dt = 0 + \int_0^\infty R(t) \, dt$$
$$\text{MTTF} = \int_0^\infty R(t) \, dt$$
*(This elegant identity states that MTTF is precisely the total area under the Reliability curve $R(t)$ from $0$ to $\infty$.)*

---

## 4.2 Standard Continuous Probability Distributions

### 4.2.1 Continuous Uniform Distribution ($X \sim U(a, b)$)
- **PDF:** $f(x) = \frac{1}{b - a}, \quad a \le x \le b$
- **CDF:** $F(x) = \frac{x - a}{b - a}$
- **Mean:** $E[X] = \frac{a + b}{2}$
- **Variance:** $\text{Var}(X) = \frac{(b - a)^2}{12}$

---

### 4.2.2 Exponential Distribution ($T \sim \text{Exp}(\lambda)$)

> [!NOTE]
> **Lecture notation:** the course also writes $f(t) = \frac{1}{\beta}e^{-t/\beta}$ with $\beta = MTTF = 1/\lambda$ (mean = SD = $\beta$). If a question gives a mean life, that is $\beta$. If it gives a failure rate, that is $\lambda$.
The cornerstone distribution for components operating in their useful life (Phase II of the Bathtub Curve).
- **PDF:** $f(t) = \lambda e^{-\lambda t}, \quad t \ge 0, \; \lambda > 0$
- **CDF:** $F(t) = 1 - e^{-\lambda t}$
- **Reliability Function:** $R(t) = e^{-\lambda t}$
- **Hazard Rate Function:**
  $$h(t) = \frac{f(t)}{R(t)} = \frac{\lambda e^{-\lambda t}}{e^{-\lambda t}} = \lambda = \text{const}$$
- **MTTF:** $\text{MTTF} = \int_0^\infty e^{-\lambda t} \, dt = \frac{1}{\lambda}$
- **Variance:** $\text{Var}(T) = \frac{1}{\lambda^2}$

#### The Memoryless Property of the Exponential Distribution
The Exponential distribution is the **unique continuous distribution** that is memoryless:
$$P(T > s + t \mid T > s) = \frac{P(T > s + t)}{P(T > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(T > t)$$
*Reliability Implication:* An item that has survived $s$ hours is probabilistically as good as new! It does not age.

---

### 4.2.3 Normal (Gaussian) Distribution ($X \sim N(\mu, \sigma^2)$)
- **PDF:**
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} \right), \quad -\infty < x < \infty$$
- **Standard Normal Transformation:** $Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$
  $$\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}, \qquad \Phi(z) = P(Z \le z) = \int_{-\infty}^z \phi(u) \, du$$
- **Symmetry Property:** $\Phi(-z) = 1 - \Phi(z)$
- **Empirical Rule:**
  - $P(\mu - \sigma \le X \le \mu + \sigma) \approx 68.26\%$ ($Z = \pm 1$)
  - $P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 95.44\%$ ($Z = \pm 2$)
  - $P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 99.74\%$ ($Z = \pm 3$)

---

### 4.2.4 Lognormal Distribution
If $Y = \ln X \sim N(\mu, \sigma^2)$, then $X = e^Y$ follows a Lognormal distribution ($X > 0$).
- **In this course (Lec 13), lognormal is used to model repair times ($MTTR$), not failure times;** for failure times the course uses normal or exponential. In wider reliability practice it is also used for fatigue life and crack propagation.
- **PDF:** $f(x) = \frac{1}{x \sigma \sqrt{2\pi}} \exp\left( -\frac{(\ln x - \mu)^2}{2\sigma^2} \right), \quad x > 0$
- **Mean:** $E[X] = e^{\mu + \sigma^2/2}$
- **Variance:** $\text{Var}(X) = e^{2\mu + \sigma^2}(e^{\sigma^2} - 1)$

---

### 4.2.5 Weibull Distribution ($T \sim \text{Weibull}(\beta, \theta, \gamma)$)

> [!WARNING]
> **Not examined:** Lec 13 and Lec 15 state that the Weibull distribution is not included in the course and no exam question will come from it. Kept here as background.
The most versatile life-distribution in reliability engineering, capable of modeling all three phases of the Bathtub Curve.
- **Two-Parameter Weibull:** Shape parameter $\beta > 0$, Scale parameter (Characteristic Life) $\theta > 0$ ($\gamma = 0$):
  - **PDF:** $f(t) = \frac{\beta}{\theta} \left( \frac{t}{\theta} \right)^{\beta - 1} \exp\left[ -\left( \frac{t}{\theta} \right)^\beta \right], \quad t \ge 0$
  - **CDF:** $F(t) = 1 - \exp\left[ -\left( \frac{t}{\theta} \right)^\beta \right]$
  - **Reliability Function:** $R(t) = \exp\left[ -\left( \frac{t}{\theta} \right)^\beta \right]$
  - **Hazard Rate Function:**
    $$h(t) = \frac{f(t)}{R(t)} = \frac{\beta}{\theta} \left( \frac{t}{\theta} \right)^{\beta - 1}$$
  - **MTTF:** $\text{MTTF} = \theta \cdot \Gamma\left( 1 + \frac{1}{\beta} \right)$, where $\Gamma(z) = \int_0^\infty u^{z-1} e^{-u} du$ is the Gamma function.

#### Physical Meaning of the Shape Parameter $\beta$
- **$\beta < 1$ (Decreasing Hazard Rate - DFR):** Infant mortality / Burn-in period ($dh/dt < 0$).
- **$\beta = 1$ (Constant Hazard Rate - CFR):** Exact exponential distribution ($h(t) = 1/\theta = \lambda$).
- **$\beta > 1$ (Increasing Hazard Rate - IFR):** Wear-out / Aging period ($dh/dt > 0$).
  - $\beta = 2$: Rayleigh distribution (linearly increasing hazard rate $h(t) \propto t$).
  - $\beta \approx 3.44$: Weibull distribution closely approximates a Normal distribution.
- **Characteristic Life $\theta$:** The time at which $63.2\%$ of units have failed, regardless of $\beta$:
  $$R(\theta) = e^{-(\theta/\theta)^\beta} = e^{-1} \approx 0.3679 \implies F(\theta) = 1 - 0.3679 = 0.6321 \quad (63.2\%)$$

---

## 4.3 Step-by-Step Worked Tutorial Problems

### Problem 4.1: Constant Failure Rate Component Analysis
**Statement:** A server cooling pump exhibits a constant failure rate with a Mean Time To Failure of $\text{MTTF} = 500\text{ hours}$.
1. What is the hazard rate $\lambda$?
2. What is the reliability of the pump for a mission time of $t = 375\text{ hours}$?
3. What is the probability that the pump fails between $300$ and $600$ hours of operation?

**Solution:**
- Since failure rate is constant, $T \sim \text{Exp}(\lambda)$ with $\lambda = \frac{1}{\text{MTTF}} = \frac{1}{500} = 0.002\text{ failures/hour}$.
- **Part 2: Reliability at $t = 375$ hours:**
  $$R(375) = e^{-\lambda t} = e^{-(0.002)(375)} = e^{-0.75} \approx 0.47237 \quad (47.24\%)$$
- **Part 3: Probability of failure between $300$ and $600$ hours:**
  $$P(300 \le T \le 600) = F(600) - F(300) = [1 - e^{-0.002(600)}] - [1 - e^{-0.002(300)}] = e^{-0.6} - e^{-1.2}$$
  $$e^{-0.6} \approx 0.54881, \qquad e^{-1.2} \approx 0.30119$$
  $$P(300 \le T \le 600) = 0.54881 - 0.30119 = 0.24762 \quad (24.76\%)$$

---

### Problem 4.2: Mechanical Shaft & Bearing Clearance Tolerance
**Statement:** In a precision assembly, the internal diameter of a bearing sleeve $X_1$ and the outer diameter of a shaft $X_2$ are independent normally distributed random variables:
- Bearing Sleeve Diameter: $X_1 \sim N(\mu_1 = 1.505\text{ cm}, \sigma_1^2 = 0.0001\text{ cm}^2) \implies \sigma_1 = 0.010\text{ cm}$
- Shaft Outer Diameter: $X_2 \sim N(\mu_2 = 1.490\text{ cm}, \sigma_2^2 = 0.000144\text{ cm}^2) \implies \sigma_2 = 0.012\text{ cm}$

Clearance is defined as $C = X_1 - X_2$.
1. Find the probability distribution of the clearance $C$.
2. What is the probability of mechanical interference (shaft is larger than bearing, i.e., $C < 0$)?
3. What is the probability that the clearance is between $0.005\text{ cm}$ and $0.025\text{ cm}$?

**Solution:**
- Since $X_1$ and $X_2$ are independent normal RVs, clearance $C = X_1 - X_2$ is normally distributed:
  $$\mu_C = \mu_1 - \mu_2 = 1.505 - 1.490 = 0.015\text{ cm}$$
  $$\sigma_C^2 = \sigma_1^2 + \sigma_2^2 = 0.0001 + 0.000144 = 0.000244\text{ cm}^2$$
  $$\sigma_C = \sqrt{0.000244} \approx 0.01562\text{ cm}$$
  $$C \sim N(\mu_C = 0.015, \sigma_C = 0.01562)$$
- **Part 2: Probability of Interference ($C < 0$):**
  $$Z = \frac{0 - \mu_C}{\sigma_C} = \frac{-0.015}{0.01562} \approx -0.96$$
  $$P(C < 0) = \Phi(-0.96) = 1 - \Phi(0.96) = 1 - 0.8315 = 0.1685 \quad (16.85\%)$$
- **Part 3: Clearance between $0.005$ and $0.025\text{ cm}$:**
  $$Z_1 = \frac{0.005 - 0.015}{0.01562} = \frac{-0.010}{0.01562} \approx -0.64 \implies \Phi(-0.64) = 1 - 0.7389 = 0.2611$$
  $$Z_2 = \frac{0.025 - 0.015}{0.01562} = \frac{0.010}{0.01562} \approx +0.64 \implies \Phi(0.64) = 0.7389$$
  $$P(0.005 \le C \le 0.025) = \Phi(0.64) - \Phi(-0.64) = 0.7389 - 0.2611 = 0.4778 \quad (47.78\%)$$

---

### Problem 4.3: Determining Normal Parameters ($\mu, \sigma$) from Percentiles
**Statement:** A manufacturing firm produces steel tension cables. Tensile strength $X$ is normally distributed $N(\mu, \sigma^2)$. Quality testing reveals that:
- $5\%$ of cables fail below $40\text{ kN}$ ($P(X < 40) = 0.05$).
- $10\%$ of cables exceed $90\text{ kN}$ ($P(X > 90) = 0.10 \implies P(X \le 90) = 0.90$).

Find the mean $\mu$ and standard deviation $\sigma$ of the cable tensile strength.

**Solution:**
- Convert percentile conditions into Standard Normal $Z$-scores:
  - From standard normal tables: $\Phi(-1.645) = 0.05 \implies Z_1 = -1.645$
  - $\Phi(1.282) = 0.90 \implies Z_2 = +1.282$
- Set up the system of simultaneous linear equations:
  $$\frac{40 - \mu}{\sigma} = -1.645 \implies \mu - 1.645\sigma = 40 \quad \text{--- (Equation 1)}$$
  $$\frac{90 - \mu}{\sigma} = 1.282 \implies \mu + 1.282\sigma = 90 \quad \text{--- (Equation 2)}$$
- Subtract Equation 1 from Equation 2:
  $$(1.282 - (-1.645))\sigma = 90 - 40$$
  $$2.927\sigma = 50 \implies \sigma = \frac{50}{2.927} \approx 17.082\text{ kN}$$
- Substitute $\sigma$ back into Equation 2:
  $$\mu = 90 - 1.282(17.082) = 90 - 21.899 \approx 68.101\text{ kN}$$
- **Final Result:** Population Mean $\mu \approx 68.10\text{ kN}$, Standard Deviation $\sigma \approx 17.08\text{ kN}$.
---

## 4.6 Problem Types Commonly Solved in Continuous Distributions & Hazard Modeling

### Problem Type 4.1: Constant Failure Rate Component Analysis (Exponential Distribution)
- **Engineering / Exam Scenario:** Electronic components operate in Phase II of the Bathtub curve with constant failure rate $\lambda$ (or known MTTF $= 1/\lambda$). Calculate mission reliability $R(t)$ for duration $t$, find the failure probability in interval $[t_1, t_2]$, or determine the design mission time $t^*$ for a target reliability $R^*$.
- **Trigger Keywords:** *"Constant failure rate $\lambda$"*, *"MTTF $= 1/\lambda$"*, *"memoryless property"*, *"exponential reliability"*.
- **Core Formulas:**
  $$R(t) = e^{-\lambda t}, \quad F(t) = 1 - e^{-\lambda t}, \quad t^* = -\frac{\ln(R^*)}{\lambda} = -\text{MTTF} \ln(R^*)$$
  $$P(t_1 \le T \le t_2) = e^{-\lambda t_1} - e^{-\lambda t_2}$$

---

### Problem Type 4.2: Mechanical Tolerance & Clearance Interference (Normal Distribution)
- **Engineering / Exam Scenario:** A mechanical assembly consists of a shaft with diameter $X_1 \sim N(\mu_1, \sigma_1^2)$ inserted into a bearing hole with diameter $X_2 \sim N(\mu_2, \sigma_2^2)$. Determine the probability of mechanical interference (clearance $C = X_2 - X_1 < 0$).
- **Trigger Keywords:** *"Shaft and bearing clearance"*, *"interference fit"*, *"linear combination of normal variables"*, *"tolerance stack-up"*.
- **Core Formulas:**
  $$\text{Clearance } C = X_2 - X_1 \implies C \sim N\left(\mu_C = \mu_2 - \mu_1, \; \sigma_C^2 = \sigma_1^2 + \sigma_2^2\right)$$
  $$Z = \frac{0 - \mu_C}{\sigma_C} = \frac{-(\mu_2 - \mu_1)}{\sqrt{\sigma_1^2 + \sigma_2^2}} \implies P(C < 0) = \Phi(Z)$$

---

### Problem Type 4.3: Determining Normal Distribution Parameters ($\mu, \sigma$) from Two Percentiles
- **Engineering / Exam Scenario:** A manufacturer specifies that $5\%$ of light bulbs burn out before $800$ hours and $10\%$ last longer than $1200$ hours. Determine the population mean life $\mu$ and standard deviation $\sigma$.
- **Trigger Keywords:** *"Percentile specifications"*, *"find mean and standard deviation"*, *"normal inverse CDF"*.
- **Solution Strategy:**
  1. Translate specifications to $Z$-scores: $P(X < x_1) = p_1 \implies \frac{x_1 - \mu}{\sigma} = Z_{p_1}$, and $P(X < x_2) = 1 - p_2 \implies \frac{x_2 - \mu}{\sigma} = Z_{1-p_2}$.
  2. Set up a system of 2 linear equations in $\mu$ and $\sigma$:
     $$x_1 = \mu + Z_{p_1} \sigma, \quad x_2 = \mu + Z_{1-p_2} \sigma$$
  3. Subtract to find $\sigma = \frac{x_2 - x_1}{Z_{1-p_2} - Z_{p_1}}$, then solve for $\mu$.

---

### Problem Type 4.4: Aging & Wear-Out Modeling via Weibull Distribution
- **⚠️ Not examined:** Weibull is outside the exam syllabus (Lec 13, Lec 15).
- **Engineering / Exam Scenario:** Given Weibull parameters $\beta$ (shape), $\theta$ (scale/characteristic life), and $\gamma$ (location/guarantee time), compute component reliability at age $t$, evaluate the hazard rate trend, or linearize empirical failure data on Weibull probability paper to estimate $\beta$ and $\theta$.
- **Trigger Keywords:** *"Weibull distribution"*, *"shape parameter $\beta$"*, *"characteristic life $\theta$"*, *"infant vs wear-out aging"*.
- **Core Formulas:**
  $$R(t) = \exp\left[ -\left(\frac{t - \gamma}{\theta}\right)^\beta \right], \quad h(t) = \frac{\beta}{\theta} \left(\frac{t - \gamma}{\theta}\right)^{\beta - 1}$$
  $$\ln\left[ \ln\left(\frac{1}{R(t)}\right) \right] = \beta \ln(t) - \beta \ln(\theta) \quad (\text{Linearized: } Y = m X + c)$$

---

# MODULE 5: Sampling Distributions & The Central Limit Theorem (Lectures 16–21)

## 5.1 Sampling Concepts & The Sample Mean

### 5.1.1 Parameters vs. Statistics
- **Population Parameter:** A fixed, typically unknown numerical characteristic of an entire population (e.g., population mean $\mu$, population variance $\sigma^2$, population proportion $p$).
- **Sample Statistic:** A numerical descriptive measure calculated exclusively from sample data (e.g., sample mean $\bar{X}$, sample variance $S^2$, sample proportion $\hat{p}$). A statistic is a **random variable** whose probability distribution is called its **Sampling Distribution**.
- **Random Sample:** A collection of $n$ independent and identically distributed (i.i.d.) random variables $X_1, X_2, \dots, X_n$ drawn from a parent population $f(x)$.

---

### 5.1.2 Sampling Distribution of the Sample Mean $\bar{X}$
Let $X_1, X_2, \dots, X_n$ be a random sample of size $n$ drawn from a population with mean $\mu$ and finite variance $\sigma^2$.
The sample mean is:
$$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$$

#### Expected Value and Variance
- **Expected Value of $\bar{X}$:**
  $$E[\bar{X}] = E\left[ \frac{1}{n} \sum_{i=1}^n X_i \right] = \frac{1}{n} \sum_{i=1}^n E[X_i] = \frac{1}{n} (n\mu) = \mu$$
  *(The sample mean $\bar{X}$ is an **unbiased estimator** of $\mu$.)*
- **Variance of $\bar{X}$ (Infinite Population or with Replacement):**
  $$\text{Var}(\bar{X}) = \text{Var}\left( \frac{1}{n} \sum_{i=1}^n X_i \right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var}(X_i) = \frac{1}{n^2} (n\sigma^2) = \frac{\sigma^2}{n}$$
- **Standard Error ($SE$):** The standard deviation of the sampling distribution:
  $$SE(\bar{X}) = \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$

#### Finite Population Correction (FPC)
When sampling **without replacement** from a finite population of size $N$:
$$\text{Var}(\bar{X}) = \frac{\sigma^2}{n} \left( \frac{N - n}{N - 1} \right) \implies \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} \sqrt{\frac{N - n}{N - 1}}$$
*(Note: FPC is omitted when sample fraction $n/N < 0.05$.)*

---

### 5.1.3 The Central Limit Theorem (CLT)
The **Central Limit Theorem (CLT)** is the foundational pillar of statistical inference.

#### Formal Theorem Statement
Let $X_1, X_2, \dots, X_n$ be an i.i.d. sequence of random variables drawn from **any arbitrary distribution** having a finite mean $\mu$ and finite non-zero variance $\sigma^2$. As the sample size $n$ approaches infinity ($n \to \infty$), the standardized sample mean converges in distribution to the Standard Normal distribution:
$$Z_n = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0, 1)$$

```
Population Distribution (Arbitrary/Skewed) ---> Sampling Distribution of X̄ (n >= 30)
          |                                               ^
     /\   |                                              / \
    /  \  |                                             /   \
  _/    \_|___________________                        _/     \_
```

*Practical Significance:* Regardless of whether the underlying population is uniform, exponential, Poisson, or multimodal, the distribution of the sample mean $\bar{X}$ will be approximately Normal when $n \ge 30$. If the parent population is strictly Normal, $\bar{X}$ is exactly Normal for *any* sample size $n \ge 1$.

---

## 5.2 Sampling Distribution of Sample Variance ($S^2$) & Chi-Square Distribution

### 5.2.1 The Chi-Square ($\chi^2$) Distribution
Let $Z_1, Z_2, \dots, Z_\nu$ be independent standard normal random variables ($Z_i \sim N(0, 1)$). The sum of their squares follows a **Chi-Square distribution with $\nu$ degrees of freedom**:
$$V = \sum_{i=1}^\nu Z_i^2 \sim \chi^2(\nu)$$
- **Support:** $V \in [0, \infty)$
- **Mean:** $E[V] = \nu$
- **Variance:** $\text{Var}(V) = 2\nu$
- **Shape:** Highly skewed to the right for small $\nu$; becomes asymptotically normal as $\nu \to \infty$.

---

### 5.2.2 Distribution of the Sample Variance $S^2$
Let $X_1, X_2, \dots, X_n$ be a random sample from a normal population $N(\mu, \sigma^2)$. The sample variance is:
$$S^2 = \frac{1}{n - 1} \sum_{i=1}^n (X_i - \bar{X})^2$$

#### Fundamental Theorem on Sample Variance
$$\frac{(n - 1)S^2}{\sigma^2} = \sum_{i=1}^n \left( \frac{X_i - \bar{X}}{\sigma} \right)^2 \sim \chi^2(n - 1)$$
*(Note: 1 degree of freedom is lost because $\bar{X}$ is estimated from the sample.)*
Furthermore, for a normal population, the sample mean $\bar{X}$ and sample variance $S^2$ are **statistically independent**.

---

## 5.3 Student's $t$-Distribution & Snedecor's $F$-Distribution

### 5.3.1 Student's $t$-Distribution
When population variance $\sigma^2$ is unknown, substituting the sample standard deviation $S$ into the standardized mean yields the $t$-statistic.

#### Derivation & Definition
Let $Z \sim N(0, 1)$ and $V \sim \chi^2(\nu)$ be independent random variables. The variable $T$ defined by:
$$T = \frac{Z}{\sqrt{V / \nu}} = \frac{\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}}{\sqrt{\frac{(n-1)S^2 / \sigma^2}{n-1}}} = \frac{\bar{X} - \mu}{S / \sqrt{n}}$$
follows **Student's $t$-distribution with $\nu = n - 1$ degrees of freedom** ($T \sim t(\nu)$).

#### Properties of the $t$-Distribution
1. Symmetric bell-shaped curve centered at $t = 0$.
2. Heavier tails than the Standard Normal distribution (higher dispersion due to uncertainty in estimating $\sigma$ by $S$).
3. As $\nu \to \infty$, $t(\nu) \to N(0, 1)$ (practically identical for $\nu \ge 30$).

---

### 5.3.2 Snedecor's $F$-Distribution
Used for comparing two population variances.

#### Definition
Let $V_1 \sim \chi^2(\nu_1)$ and $V_2 \sim \chi^2(\nu_2)$ be independent chi-square random variables. The ratio:
$$F = \frac{V_1 / \nu_1}{V_2 / \nu_2} = \frac{\frac{(n_1 - 1)S_1^2 / \sigma_1^2}{n_1 - 1}}{\frac{(n_2 - 1)S_2^2 / \sigma_2^2}{n_2 - 1}} = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2}$$
follows an **$F$-distribution with $\nu_1$ numerator and $\nu_2$ denominator degrees of freedom** ($F \sim F(\nu_1, \nu_2)$).

#### Reciprocal Property
$$F_{1 - \alpha}(\nu_1, \nu_2) = \frac{1}{F_\alpha(\nu_2, \nu_1)}$$

---

## 5.4 Sampling Distributions for Two Samples

### 5.4.1 Difference Between Two Sample Means ($\bar{X}_1 - \bar{X}_2$)
Let independent random samples of sizes $n_1$ and $n_2$ be drawn from populations with means $\mu_1, \mu_2$ and variances $\sigma_1^2, \sigma_2^2$:
- **Mean:** $E[\bar{X}_1 - \bar{X}_2] = \mu_1 - \mu_2$
- **Variance:** $\text{Var}(\bar{X}_1 - \bar{X}_2) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$
- **Standard Error:** $SE(\bar{X}_1 - \bar{X}_2) = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$
- **Standardized Form:**
  $$Z = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N(0, 1)$$

---

### 5.4.2 Difference Between Two Sample Proportions ($\hat{p}_1 - \hat{p}_2$)
Let independent binomial samples of sizes $n_1$ and $n_2$ yield sample proportions $\hat{p}_1 = X_1/n_1$ and $\hat{p}_2 = X_2/n_2$:
- **Mean:** $E[\hat{p}_1 - \hat{p}_2] = p_1 - p_2$
- **Variance:** $\text{Var}(\hat{p}_1 - \hat{p}_2) = \frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}$
- **Standardized Form:**
  $$Z = \frac{(\hat{p}_1 - \hat{p}_2) - (p_1 - p_2)}{\sqrt{\frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}}} \sim N(0, 1)$$

---

## 5.5 Step-by-Step Worked Tutorial Problems

### Problem 5.1: Sample Mean Probabilities via Central Limit Theorem
**Statement:** An industrial component manufacturing process produces synthetic fibers with a breaking strength having a mean of $\mu = 50\text{ kg}$ and a standard deviation of $\sigma = 4\text{ kg}$. The exact shape of the population distribution is unknown. A random sample of $n = 64$ fibers is tested.
1. What is the sampling distribution of the sample mean $\bar{X}$?
2. What is the probability that the sample mean breaking strength $\bar{X}$ falls between $49\text{ kg}$ and $51\text{ kg}$?
3. What is the probability that $\bar{X}$ is less than $48.8\text{ kg}$?

**Solution:**
- Since sample size $n = 64 \ge 30$, by the **Central Limit Theorem**, $\bar{X}$ is approximately normally distributed:
  $$\mu_{\bar{X}} = \mu = 50\text{ kg}$$
  $$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} = \frac{4}{\sqrt{64}} = \frac{4}{8} = 0.50\text{ kg}$$
  $$\bar{X} \sim N(\mu_{\bar{X}} = 50, \sigma_{\bar{X}} = 0.50)$$
- **Part 2: Probability $P(49 \le \bar{X} \le 51)$:**
  $$Z_1 = \frac{49 - 50}{0.50} = \frac{-1.0}{0.50} = -2.00$$
  $$Z_2 = \frac{51 - 50}{0.50} = \frac{+1.0}{0.50} = +2.00$$
  $$P(49 \le \bar{X} \le 51) = \Phi(2.00) - \Phi(-2.00) = 0.9772 - 0.0228 = 0.9544 \quad (95.44\%)$$
- **Part 3: Probability $P(\bar{X} < 48.8)$:**
  $$Z = \frac{48.8 - 50}{0.50} = \frac{-1.2}{0.50} = -2.40$$
  $$P(\bar{X} < 48.8) = \Phi(-2.40) = 1 - \Phi(2.40) = 1 - 0.9918 = 0.0082 \quad (0.82\%)$$

---

### Problem 5.2: Sample Variance & Chi-Square Distribution
**Statement:** A precision robotic dispenser fills reagent vials such that fill volume is normally distributed with population variance $\sigma^2 = 0.04\text{ mL}^2$. A sample of $n = 10$ vials is drawn. What is the probability that the sample variance $S^2$ exceeds $0.075\text{ mL}^2$?

**Solution:**
- Sample size $n = 10 \implies \text{degrees of freedom } \nu = n - 1 = 9$.
- The statistic $V = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(9)$.
- Calculate the threshold $\chi^2$ value:
  $$\chi_{\text{calc}}^2 = \frac{(10 - 1)(0.075)}{0.04} = \frac{9 \times 0.075}{0.04} = \frac{0.675}{0.04} = 16.875$$
- From Chi-square distribution tables for $\nu = 9$:
  $$P(S^2 > 0.075) = P(\chi^2(9) > 16.875) \approx 0.0506 \quad (5.06\%)$$
---

## 5.5 Problem Types Commonly Solved in Sampling Distributions & Central Limit Theorem

### Problem Type 5.1: Sample Mean Probabilities via Central Limit Theorem (CLT)
- **Engineering / Exam Scenario:** An assembly line produces capacitors with unknown population distribution having mean $\mu$ and standard deviation $\sigma$. A quality engineer inspects a batch of $n \ge 30$ units. What is the probability that the sample average $\bar{X}$ falls within a specified interval or exceeds a threshold?
- **Trigger Keywords:** *"Sample mean $\bar{X}$"*, *"sample size $n \ge 30$"*, *"non-normal population"*, *"standard error $\sigma/\sqrt{n}$"*.
- **Core Formula:**
  $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1) \implies P(\bar{X} \le a) = \Phi\left( \frac{a - \mu}{\sigma / \sqrt{n}} \right)$$

---

### Problem Type 5.2: Sample Variance & Chi-Square Distribution
- **Engineering / Exam Scenario:** Given a sample of size $n$ drawn from a normal population $N(\mu, \sigma^2)$, determine the probability that the sample variance $S^2$ exceeds a critical quality threshold.
- **Trigger Keywords:** *"Sample variance $S^2$"*, *"Chi-Square distribution"*, *"degrees of freedom $\nu = n-1$"*.
- **Core Formula:**
  $$\chi^2 = \frac{(n - 1) S^2}{\sigma^2} \sim \chi^2(n - 1) \implies P(S^2 > c) = P\left( \chi^2(n-1) > \frac{(n-1)c}{\sigma^2} \right)$$

---

### Problem Type 5.3: Comparing Two Independent Variances via $F$-Distribution
- **Engineering / Exam Scenario:** Comparing process variability between two production machines (Machine 1: $n_1, S_1^2$; Machine 2: $n_2, S_2^2$). Find the probability that the sample variance ratio exceeds a specified value under $H_0: \sigma_1^2 = \sigma_2^2$.
- **Trigger Keywords:** *"Ratio of sample variances"*, *"F-distribution"*, *"degrees of freedom $(\nu_1 = n_1-1, \nu_2 = n_2-1)$"*.
- **Core Formula:**
  $$F = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} = \frac{S_1^2}{S_2^2} \sim F(n_1 - 1, \; n_2 - 1)$$

---

# MODULE 6: Statistical Inference — Point Estimation & Confidence Intervals (Lectures 26–28)

## 6.1 Principles of Point Estimation

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** estimator properties (unbiasedness, consistency, MVUE, CRLB, sufficiency) and the methods of moments / maximum likelihood (6.1–6.2) are **not taught** in the lectures. MLE appears only later, for logistic regression (Lec 45–46). Confidence intervals (6.3) are taught in Lec 26–28. Hypothesis testing is in Lec 22–25 and 29–31 (Module 7).

### 6.1.1 Estimators vs. Estimates
- **Point Estimator ($\hat{\Theta}$):** A sample statistic / mathematical formula used to estimate an unknown population parameter $\theta$ (e.g., $\hat{\Theta} = \bar{X} = \frac{1}{n}\sum X_i$).
- **Point Estimate ($\hat{\theta}$):** The specific numerical value obtained by evaluating the estimator on a realized dataset (e.g., $\bar{x} = 52.4\text{ hours}$).

---

### 6.1.2 Desirable Properties of Point Estimators
A good estimator must satisfy four foundational mathematical criteria:

#### 1. Unbiasedness
An estimator $\hat{\Theta}$ is an **unbiased estimator** of $\theta$ if its expected value equals the true parameter value:
$$E[\hat{\Theta}] = \theta$$
If $E[\hat{\Theta}] \neq \theta$, the **Bias** is:
$$\text{Bias}(\hat{\Theta}) = E[\hat{\Theta}] - \theta$$

> [!NOTE]
> **Proof: Why Sample Variance Divisor is $n-1$ (Bessel's Correction)**
> Consider $S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$. We know $\sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n (X_i - \mu)^2 - n(\bar{X} - \mu)^2$.
> Taking expectations:
> $$E\left[ \sum_{i=1}^n (X_i - \bar{X})^2 \right] = \sum_{i=1}^n E[(X_i - \mu)^2] - n E[(\bar{X} - \mu)^2] = n\sigma^2 - n\left(\frac{\sigma^2}{n}\right) = (n - 1)\sigma^2$$
> Therefore:
> $$E[S^2] = E\left[ \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2 \right] = \frac{(n-1)\sigma^2}{n-1} = \sigma^2 \quad (\text{Unbiased!})$$
> Using divisor $n$ would yield $E[S_n^2] = \frac{n-1}{n}\sigma^2$, which systematically underestimates true variance by a factor of $\frac{n-1}{n}$.

#### 2. Consistency
An estimator $\hat{\Theta}_n$ is **consistent** if it converges in probability to the true parameter $\theta$ as sample size $n \to \infty$:
$$\lim_{n \to \infty} P(|\hat{\Theta}_n - \theta| < \epsilon) = 1, \quad \forall \epsilon > 0$$
*Sufficient Condition:* $\lim_{n \to \infty} E[\hat{\Theta}_n] = \theta$ and $\lim_{n \to \infty} \text{Var}(\hat{\Theta}_n) = 0$.

#### 3. Efficiency & Minimum Variance Unbiased Estimator (MVUE)
If $\hat{\Theta}_1$ and $\hat{\Theta}_2$ are two unbiased estimators of $\theta$, $\hat{\Theta}_1$ is more **efficient** than $\hat{\Theta}_2$ if:
$$\text{Var}(\hat{\Theta}_1) < \text{Var}(\hat{\Theta}_2)$$
The **Cramér-Rao Lower Bound (CRLB)** establishes the minimum possible variance achievable by any unbiased estimator:
$$\text{Var}(\hat{\Theta}) \ge \frac{1}{I_n(\theta)} = \frac{1}{n E\left[ \left( \frac{\partial \ln f(X; \theta)}{\partial \theta} \right)^2 \right]} = \frac{1}{-n E\left[ \frac{\partial^2 \ln f(X; \theta)}{\partial \theta^2} \right]}$$
An unbiased estimator achieving CRLB is called the **Minimum Variance Unbiased Estimator (MVUE)**.

#### 4. Sufficiency
An estimator $\hat{\Theta}$ is **sufficient** if it utilizes all the information contained in the sample regarding $\theta$.
*Neyman-Fisher Factorization Theorem:* A statistic $T(\mathbf{X})$ is sufficient for $\theta$ if and only if the joint PDF/PMF factors as:
$$f(x_1, x_2, \dots, x_n; \theta) = g(T(\mathbf{x}), \theta) \cdot h(\mathbf{x})$$

---

## 6.2 Methods of Point Estimation

### 6.2.1 Method of Moments (MOM)
The Method of Moments equates theoretical population moments $\mu_k = E[X^k]$ to sample moments $m_k = \frac{1}{n}\sum_{i=1}^n X_i^k$:
$$\mu_1 = m_1 \implies E[X] = \bar{X}$$
$$\mu_2 = m_2 \implies E[X^2] = \frac{1}{n} \sum X_i^2$$

---

### 6.2.2 Maximum Likelihood Estimation (MLE)
The most powerful and widely used parametric estimation technique.

#### Formulation
Let $X_1, X_2, \dots, X_n$ be an i.i.d. sample from PDF $f(x; \theta)$. The **Likelihood Function $L(\theta)$** is the joint probability of observing the realized sample:
$$L(\theta) = L(x_1, \dots, x_n; \theta) = \prod_{i=1}^n f(x_i; \theta)$$
The **Log-Likelihood Function** is:
$$\ln L(\theta) = \sum_{i=1}^n \ln f(x_i; \theta)$$
The Maximum Likelihood Estimator $\hat{\theta}_{\text{MLE}}$ maximizes $\ln L(\theta)$, found by solving the **Score Equation**:
$$\frac{\partial \ln L(\theta)}{\partial \theta} = 0 \quad \text{subject to} \quad \left. \frac{\partial^2 \ln L(\theta)}{\partial \theta^2} \right|_{\theta = \hat{\theta}} < 0$$

#### Derivation of MLE for Exponential Distribution ($T \sim \text{Exp}(\lambda)$)
$$f(t; \lambda) = \lambda e^{-\lambda t}, \quad t_i \ge 0$$
1. Likelihood: $L(\lambda) = \prod_{i=1}^n (\lambda e^{-\lambda t_i}) = \lambda^n \exp\left( -\lambda \sum_{i=1}^n t_i \right)$
2. Log-Likelihood: $\ln L(\lambda) = n \ln \lambda - \lambda \sum_{i=1}^n t_i$
3. Score Equation: $\frac{d \ln L}{d \lambda} = \frac{n}{\lambda} - \sum_{i=1}^n t_i = 0$
4. Solution:
   $$\hat{\lambda}_{\text{MLE}} = \frac{n}{\sum_{i=1}^n t_i} = \frac{1}{\bar{t}}$$
   *(The MLE of failure rate $\lambda$ is the reciprocal of the sample mean life $\bar{t}$.)*

#### Properties of Maximum Likelihood Estimators
1. **Invariance Property:** If $\hat{\theta}$ is the MLE of $\theta$, then for any continuous function $g(\theta)$, the MLE of $g(\theta)$ is $g(\hat{\theta})$ (e.g., MLE of Reliability $R(t) = e^{-\lambda t}$ is $\hat{R}(t) = e^{-\hat{\lambda} t}$).
2. **Asymptotic Normality & Efficiency:** As $n \to \infty$, $\hat{\theta}_{\text{MLE}} \xrightarrow{d} N\left( \theta, \frac{1}{I_n(\theta)} \right)$.

---

## 6.3 Confidence Intervals (Interval Estimation)

### 6.3.1 Concept of Confidence Intervals
An interval $[L, U]$ computed from sample data such that the probability that the random interval covers the fixed unknown parameter $\theta$ is $1 - \alpha$:
$$P(L \le \theta \le U) = 1 - \alpha$$
where $1 - \alpha$ is the **Confidence Level** (e.g., $95\% \implies \alpha = 0.05$).

---

### 6.3.2 Confidence Intervals for Population Mean $\mu$

| Scenario | Distribution Condition | Test Statistic | Two-Sided $(1-\alpha)$ Confidence Interval |
| :--- | :--- | :--- | :--- |
| **Case 1:** $\sigma$ known | Normal parent or large $n$ | $Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1)$ | $\bar{x} \pm Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ |
| **Case 2:** $\sigma$ unknown, Large sample ($n \ge 30$) | Arbitrary parent (CLT) | $Z \approx \frac{\bar{X} - \mu}{S / \sqrt{n}} \sim N(0,1)$ | $\bar{x} \pm Z_{\alpha/2} \frac{s}{\sqrt{n}}$ |
| **Case 3:** $\sigma$ unknown, Small sample ($n < 30$) | Normal parent | $T = \frac{\bar{X} - \mu}{S / \sqrt{n}} \sim t(n-1)$ | $\bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$ |

*Standard Critical Values:*
- $90\%$ CI ($\alpha = 0.10$): $Z_{0.05} = 1.645$
- $95\%$ CI ($\alpha = 0.05$): $Z_{0.025} = 1.960$
- $99\%$ CI ($\alpha = 0.01$): $Z_{0.005} = 2.576$

---

### 6.3.3 Confidence Intervals for Difference Between Two Means ($\mu_1 - \mu_2$)

#### Case 1: Independent Samples, Unknown but Equal Variances ($\sigma_1^2 = \sigma_2^2 = \sigma^2$)
Compute the **Pooled Sample Variance $S_p^2$**:
$$S_p^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}$$
The $(1 - \alpha)$ Confidence Interval is:
$$(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2, n_1 + n_2 - 2} \cdot S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

#### Case 2: Paired / Dependent Samples
Let $D_i = X_{1i} - X_{2i}$, with sample mean $\bar{d} = \frac{1}{n}\sum d_i$ and sample standard deviation $s_d = \sqrt{\frac{\sum(d_i - \bar{d})^2}{n-1}}$:
$$\bar{d} \pm t_{\alpha/2, n-1} \frac{s_d}{\sqrt{n}}$$

---

### 6.3.4 Confidence Interval for Population Proportion $p$
Large sample approximation ($n\hat{p} \ge 5, n(1-\hat{p}) \ge 5$):
$$\hat{p} \pm Z_{\alpha/2} \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$$
For difference between two proportions $(p_1 - p_2)$:
$$(\hat{p}_1 - \hat{p}_2) \pm Z_{\alpha/2} \sqrt{\frac{\hat{p}_1(1 - \hat{p}_1)}{n_1} + \frac{\hat{p}_2(1 - \hat{p}_2)}{n_2}}$$

---

### 6.3.5 Confidence Interval for Population Variance $\sigma^2$
Using the pivotal quantity $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$:
$$P\left( \chi^2_{1 - \alpha/2, n-1} \le \frac{(n-1)S^2}{\sigma^2} \le \chi^2_{\alpha/2, n-1} \right) = 1 - \alpha$$
Inverting the inequalities yields the $(1 - \alpha)$ CI for $\sigma^2$:
$$\left[ \frac{(n - 1)s^2}{\chi^2_{\alpha/2, n-1}}, \; \frac{(n - 1)s^2}{\chi^2_{1 - \alpha/2, n-1}} \right]$$
Taking square roots gives the Confidence Interval for Standard Deviation $\sigma$.

---

## 6.4 Step-by-Step Worked Tutorial Problems

### Problem 6.1: Small-Sample $t$-Confidence Interval for Component Lifespan
**Statement:** A reliability engineer tests a random sample of $n = 16$ newly developed solid-state relays. The measured operational lifespans (in thousands of hours) yield a sample mean of $\bar{x} = 24.5$ and a sample standard deviation of $s = 3.2$. Assuming lifespans are normally distributed, construct:
1. A $95\%$ two-sided confidence interval for the true mean lifespan $\mu$.
2. A $99\%$ two-sided confidence interval for $\mu$.

**Solution:**
- Sample size $n = 16 < 30$, $\sigma$ is unknown, parent population is Normal $\implies$ Use Student's $t$-distribution with $\nu = n - 1 = 15$ degrees of freedom.
- Standard Error: $SE = \frac{s}{\sqrt{n}} = \frac{3.2}{\sqrt{16}} = \frac{3.2}{4} = 0.80$.
- **Part 1: $95\%$ Confidence Interval ($\alpha = 0.05$):**
  - Critical value: $t_{0.025, 15} = 2.131$
  - Margin of Error: $E = 2.131 \times 0.80 = 1.7048$
  - CI: $24.5 \pm 1.7048 \implies [22.795, 26.205]\text{ thousand hours}$.
- **Part 2: $99\%$ Confidence Interval ($\alpha = 0.01$):**
  - Critical value: $t_{0.005, 15} = 2.947$
  - Margin of Error: $E = 2.947 \times 0.80 = 2.3576$
  - CI: $24.5 \pm 2.3576 \implies [22.142, 26.858]\text{ thousand hours}$.

---

### Problem 6.2: Confidence Interval for Population Variance $\sigma^2$
**Statement:** For the sample in Problem 6.1 ($n = 16, s = 3.2 \implies s^2 = 10.24$), construct a $95\%$ confidence interval for the population variance $\sigma^2$ and standard deviation $\sigma$.

**Solution:**
- Degrees of freedom $\nu = 16 - 1 = 15$. $\alpha = 0.05 \implies \alpha/2 = 0.025, 1 - \alpha/2 = 0.975$.
- From Chi-square distribution tables:
  - Upper critical value: $\chi^2_{0.025, 15} = 27.488$
  - Lower critical value: $\chi^2_{0.975, 15} = 6.262$
- Calculate CI bounds:
  $$\text{Lower Limit } L = \frac{(n-1)s^2}{\chi^2_{0.025, 15}} = \frac{15 \times 10.24}{27.488} = \frac{153.6}{27.488} \approx 5.588$$
  $$\text{Upper Limit } U = \frac{(n-1)s^2}{\chi^2_{0.975, 15}} = \frac{15 \times 10.24}{6.262} = \frac{153.6}{6.262} \approx 24.529$$
- **Final Result:**
  - $95\%$ CI for Variance $\sigma^2$: $[5.588, 24.529]$
  - $95\%$ CI for Standard Deviation $\sigma$: $[\sqrt{5.588}, \sqrt{24.529}] = [2.364, 4.953]\text{ thousand hours}$.
---

## 6.7 Problem Types Commonly Solved in Estimation & Confidence Intervals

### Problem Type 6.1: Confidence Interval for Population Mean $\mu$
- **Case A: Known $\sigma$ or Large Sample ($n \ge 30$):**
  $$\bar{x} \pm Z_{\alpha/2} \left( \frac{\sigma}{\sqrt{n}} \right)$$
- **Case B: Unknown $\sigma$, Small Sample ($n < 30$, Normal Population):**
  $$\bar{x} \pm t_{\alpha/2, \, n-1} \left( \frac{s}{\sqrt{n}} \right)$$
- **Required Sample Size for Margin of Error $E$:**
  $$n = \left( \frac{Z_{\alpha/2} \cdot \sigma}{E} \right)^2$$

---

### Problem Type 6.2: Confidence Interval for Population Variance $\sigma^2$
- **Core Formula ($100(1-\alpha)\%$ CI):**
  $$\left[ \frac{(n - 1) s^2}{\chi^2_{\alpha/2, \, n-1}}, \; \frac{(n - 1) s^2}{\chi^2_{1 - \alpha/2, \, n-1}} \right]$$
- **Common Pitfall:** The Chi-Square distribution is strictly non-symmetric! Do NOT subtract a single margin of error from $s^2$; use the two distinct critical values $\chi^2_{\alpha/2}$ and $\chi^2_{1-\alpha/2}$.

---

### Problem Type 6.3: Confidence Interval for Population Proportion $p$
- **Core Formula (Large Sample Wald Interval):**
  $$\hat{p} \pm Z_{\alpha/2} \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}, \quad \text{where } \hat{p} = \frac{x}{n}$$
- **Required Sample Size for Margin of Error $E$ (Conservative $p=0.5$):**
  $$n = \frac{Z_{\alpha/2}^2 \cdot (0.25)}{E^2}$$

---

# MODULE 7: Statistical Inference — Hypothesis Testing & Goodness-of-Fit (Lectures 22–25, 29–31)

## 7.1 Fundamentals of Hypothesis Testing

### 7.1.1 Hypotheses, Test Statistics, and Decision Rules
- **Null Hypothesis ($H_0$):** The default statement of "no effect", "no difference", or adherence to standard specifications (e.g., $H_0: \mu = 1000\text{ hours}$). Assumed true until proven otherwise.
- **Alternative (Research) Hypothesis ($H_1$ or $H_a$):** The claim being tested that contradicts $H_0$:
  - *Two-Tailed Test:* $H_1: \mu \neq \mu_0$ (Detects deviation in either direction).
  - *Right-Tailed (Upper-Tail) Test:* $H_1: \mu > \mu_0$ (Detects increase/improvement).
  - *Left-Tailed (Lower-Tail) Test:* $H_1: \mu < \mu_0$ (Detects degradation/decrease).
- **Test Statistic:** A standardized sample statistic used to decide between $H_0$ and $H_1$ (e.g., $Z$, $t$, $\chi^2$, $F$).
- **Critical Value ($c$) & Rejection Region ($\mathcal{R}$):** Threshold values partitioning the sample space into rejection and non-rejection regions based on significance level $\alpha$.
- **$p$-Value:** The probability, assuming $H_0$ is true, of observing a test statistic as extreme as or more extreme than the actual observed value.
  $$\text{Decision Rule: Reject } H_0 \iff p\text{-value} \le \alpha$$

---

### 7.1.2 The Decision Matrix & Types of Errors

| Reality $\downarrow$ \ Decision $\rightarrow$ | **Fail to Reject $H_0$** (Accept $H_0$) | **Reject $H_0$** (Accept $H_1$) |
| :--- | :--- | :--- |
| **$H_0$ is Actually True** | **Correct Decision** (Prob $= 1 - \alpha$, Confidence) | **Type I Error** (Prob $= \alpha$, Significance Level / Producer's Risk) |
| **$H_0$ is Actually False** | **Type II Error** (Prob $= \beta$, Consumer's Risk) | **Correct Decision** (Prob $= 1 - \beta$, **Statistical Power**) |

#### Trade-offs and Power
- **Type I Error ($\alpha$):** Rejecting a good product lot ($H_0$ true). Fixed a priori by the engineer (typically $\alpha = 0.05$ or $0.01$).
- **Type II Error ($\beta$):** Accepting a defective product lot ($H_0$ false).
- **Power of the Test ($1 - \beta$):** The probability of correctly rejecting a false null hypothesis. Power increases with larger sample size $n$, larger effect size $|\mu - \mu_0|$, and smaller variance $\sigma^2$.

```
Type I vs Type II Error Distributions:
   Distribution under H0            Distribution under H1
          /\                                  /\
         /  \                                /  \
        /    \                              /    \
  _____/  1-a \_____[Critical Value c]_____/ 1-b  \_____
               \                          /
             Alpha (Type I)             Beta (Type II)
```

---

## 7.2 Catalog of Parametric Hypothesis Tests

### 7.2.1 Tests on a Single Population Mean $\mu$

#### 1. One-Sample $Z$-Test (Known $\sigma$ or Large Sample $n \ge 30$)
$$Z_{\text{calc}} = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$$
- Two-Tailed ($H_1: \mu \neq \mu_0$): Reject $H_0$ if $|Z_{\text{calc}}| \ge Z_{\alpha/2}$.
- Right-Tailed ($H_1: \mu > \mu_0$): Reject $H_0$ if $Z_{\text{calc}} \ge Z_\alpha$.
- Left-Tailed ($H_1: \mu < \mu_0$): Reject $H_0$ if $Z_{\text{calc}} \le -Z_\alpha$.

#### 2. One-Sample $t$-Test (Unknown $\sigma$, Normal Parent, Small Sample $n < 30$)
$$t_{\text{calc}} = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} \sim t(n - 1)$$
- Two-Tailed ($H_1: \mu \neq \mu_0$): Reject $H_0$ if $|t_{\text{calc}}| \ge t_{\alpha/2, n-1}$.

---

### 7.2.2 Tests on Two Population Means ($\mu_1 - \mu_2$)

#### 1. Independent Two-Sample Pooled $t$-Test ($\sigma_1^2 = \sigma_2^2$ Unknown)
$$t_{\text{calc}} = \frac{(\bar{x}_1 - \bar{x}_2) - \Delta_0}{S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2)$$
where $S_p^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}$.

#### 2. Paired $t$-Test (Dependent / Before-After Data)
Let $d_i = x_{1i} - x_{2i}$, $\bar{d} = \frac{1}{n}\sum d_i$, $s_d = \sqrt{\frac{\sum(d_i-\bar{d})^2}{n-1}}$:
$$t_{\text{calc}} = \frac{\bar{d} - \mu_{d0}}{s_d / \sqrt{n}} \sim t(n - 1)$$

---

### 7.2.3 Tests for Population Proportions

#### 1. One-Sample Proportion $Z$-Test
$$H_0: p = p_0 \implies Z_{\text{calc}} = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1 - p_0)}{n}}}$$

#### 2. Two-Sample Proportion $Z$-Test
$$H_0: p_1 = p_2 \implies Z_{\text{calc}} = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}_{\text{pool}}(1 - \hat{p}_{\text{pool}}) \left( \frac{1}{n_1} + \frac{1}{n_2} \right)}}$$
where $\hat{p}_{\text{pool}} = \frac{x_1 + x_2}{n_1 + n_2}$.

---

### 7.2.4 Tests on Population Variances

#### 1. One-Sample Variance Chi-Square Test ($H_0: \sigma^2 = \sigma_0^2$)
$$\chi_{\text{calc}}^2 = \frac{(n - 1)s^2}{\sigma_0^2} \sim \chi^2(n - 1)$$
- Two-Tailed: Reject $H_0$ if $\chi_{\text{calc}}^2 \ge \chi^2_{\alpha/2, n-1}$ or $\chi_{\text{calc}}^2 \le \chi^2_{1 - \alpha/2, n-1}$.

#### 2. Two-Sample Variance $F$-Test ($H_0: \sigma_1^2 = \sigma_2^2$)
$$F_{\text{calc}} = \frac{s_1^2}{s_2^2} \sim F(n_1 - 1, n_2 - 1)$$

---

## 7.3 Chi-Square Goodness-of-Fit & Independence Tests

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** the goodness-of-fit test is **not taught** in the lectures. The test of independence is taught in **Lec 39**, as the chi-square test of association for nominal data, alongside correlation (Module 9).

### 7.3.1 Pearson's Chi-Square Goodness-of-Fit Test
Tests whether observed sample counts $O_i$ conform to a theoretical probability distribution $E_i = n \cdot p_i$:
$$\chi_{\text{calc}}^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} \sim \chi^2(k - 1 - m)$$
where $k$ is the number of categories, and $m$ is the number of distribution parameters estimated from the sample (e.g., $m=1$ for Poisson $\lambda$, $m=2$ for Normal $\mu, \sigma$).
*Rejection Rule:* Reject $H_0$ at level $\alpha$ if $\chi_{\text{calc}}^2 \ge \chi^2_{\alpha, k - 1 - m}$.
*Cochran's Criterion:* All expected cell counts must satisfy $E_i \ge 5$ (adjacent bins must be pooled if $E_i < 5$).

---

### 7.3.2 Chi-Square Test of Independence ($r \times c$ Contingency Tables)
Tests whether two categorical variables (row factor $A$ with $r$ levels and column factor $B$ with $c$ levels) are statistically independent:
$$H_0: \text{Row and Column factors are independent} \quad \text{vs.} \quad H_1: \text{Factors are dependent}$$
Expected cell frequencies under $H_0$:
$$E_{ij} = \frac{R_i \times C_j}{N}$$
where $R_i$ is row total, $C_j$ is column total, and $N = \sum R_i = \sum C_j$.
Test statistic:
$$\chi_{\text{calc}}^2 = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \sim \chi^2((r - 1)(c - 1))$$
Reject $H_0$ if $\chi_{\text{calc}}^2 \ge \chi^2_{\alpha, (r-1)(c-1)}$.

---

## 7.4 Step-by-Step Worked Tutorial Problems

### Problem 7.1: One-Sample $t$-Test on Battery Operating Life
**Statement:** A manufacturer claims that a new lithium-polymer battery has a mean operating life of at least $\mu_0 = 50\text{ hours}$. An independent testing lab draws a random sample of $n = 25$ batteries and records a sample mean of $\bar{x} = 48.2\text{ hours}$ with a sample standard deviation of $s = 4.0\text{ hours}$. Test the manufacturer's claim at $\alpha = 0.05$ assuming operating life is normally distributed.

**Solution:**
- **Step 1: State Hypotheses:**
  $$H_0: \mu \ge 50\text{ hours} \quad \text{vs.} \quad H_1: \mu < 50\text{ hours} \quad (\text{Left-tailed test})$$
- **Step 2: Test Statistic:**
  $$t_{\text{calc}} = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{48.2 - 50}{4.0 / \sqrt{25}} = \frac{-1.8}{4.0 / 5} = \frac{-1.8}{0.80} = -2.25$$
- **Step 3: Critical Value & Rejection Region:**
  - Degrees of freedom $\nu = n - 1 = 24$.
  - For $\alpha = 0.05$ left-tailed: Critical value $t_{\text{crit}} = -t_{0.05, 24} = -1.711$.
  - Rejection Region: Reject $H_0$ if $t_{\text{calc}} \le -1.711$.
- **Step 4: Decision & Pedagogical Conclusion:**
  - Since $t_{\text{calc}} = -2.25 < -1.711$, we **reject $H_0$**.
  - *Conclusion:* At the $5\%$ significance level, there is statistically significant evidence that the true mean battery life is less than 50 hours; the manufacturer's claim is refuted.

---

### Problem 7.2: Chi-Square Test of Independence for Failure Modes
**Statement:** A quality audit records component failure modes across three manufacturing lines:

| Line \ Failure Mode | Electrical Short ($O_{i1}$) | Mechanical Fracture ($O_{i2}$) | Total |
| :--- | :--- | :--- | :--- |
| **Line 1** | 20 | 30 | 50 |
| **Line 2** | 40 | 60 | 100 |
| **Line 3** | 10 | 40 | 50 |
| **Total** | **70** | **130** | **200** |

Test at $\alpha = 0.05$ whether failure mode is independent of manufacturing line.

**Solution:**
- **Step 1: Compute Expected Frequencies $E_{ij} = \frac{R_i \times C_j}{N}$:**
  - $E_{11} = \frac{50 \times 70}{200} = 17.5, \quad E_{12} = \frac{50 \times 130}{200} = 32.5$
  - $E_{21} = \frac{100 \times 70}{200} = 35.0, \quad E_{22} = \frac{100 \times 130}{200} = 65.0$
  - $E_{31} = \frac{50 \times 70}{200} = 17.5, \quad E_{32} = \frac{50 \times 130}{200} = 32.5$
- **Step 2: Calculate $\chi^2$ Contributions $\frac{(O - E)^2}{E}$:**
  - Cell (1,1): $\frac{(20 - 17.5)^2}{17.5} = \frac{6.25}{17.5} \approx 0.3571$
  - Cell (1,2): $\frac{(30 - 32.5)^2}{32.5} = \frac{6.25}{32.5} \approx 0.1923$
  - Cell (2,1): $\frac{(40 - 35.0)^2}{35.0} = \frac{25.0}{35.0} \approx 0.7143$
  - Cell (2,2): $\frac{(60 - 65.0)^2}{65.0} = \frac{25.0}{65.0} \approx 0.3846$
  - Cell (3,1): $\frac{(10 - 17.5)^2}{17.5} = \frac{56.25}{17.5} \approx 3.2143$
  - Cell (3,2): $\frac{(40 - 32.5)^2}{32.5} = \frac{56.25}{32.5} \approx 1.7308$
- **Step 3: Total $\chi_{\text{calc}}^2$:**
  $$\chi_{\text{calc}}^2 = 0.3571 + 0.1923 + 0.7143 + 0.3846 + 3.2143 + 1.7308 = 6.5934$$
- **Step 4: Degrees of Freedom & Critical Value:**
  $$\nu = (r - 1)(c - 1) = (3 - 1)(2 - 1) = 2 \times 1 = 2$$
  $$\chi_{0.05, 2}^2 = 5.991$$
- **Step 5: Decision:**
  - Since $\chi_{\text{calc}}^2 = 6.5934 > 5.991$, we **reject $H_0$**.
  - *Conclusion:* Failure mode is significantly dependent on the manufacturing line ($p < 0.05$), with Line 3 showing a disproportionately high rate of mechanical fractures.
---

## 7.6 Problem Types Commonly Solved in Hypothesis Testing

### Problem Type 7.1: One-Sample $t$-Test on Process Mean
- **Engineering / Exam Scenario:** Testing whether a new manufacturing process meets the nominal mean lifespan specification $\mu_0$ based on a small sample of $n < 30$ prototype test results.
- **Hypotheses:** $H_0: \mu = \mu_0$ vs. $H_1: \mu > \mu_0$ (upper-tailed), $H_1: \mu < \mu_0$ (lower-tailed), or $H_1: \mu \neq \mu_0$ (two-tailed).
- **Test Statistic:** $t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} \sim t(n - 1)$.
- **Decision Rule:** Reject $H_0$ if $|t| \ge t_{\alpha/2, n-1}$ (two-tailed) or $t \ge t_{\alpha, n-1}$ (upper-tailed).

---

### Problem Type 7.2: Pearson's Chi-Square Goodness-of-Fit Test
- **Engineering / Exam Scenario:** Verify whether observed failure frequencies across $k$ time intervals follow a theoretical probability distribution (e.g., Poisson or Uniform).
- **Test Statistic:**
  $$\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} \sim \chi^2(k - 1 - p)$$
  where $O_i$ are observed counts, $E_i = n P_i$ are expected counts under $H_0$, and $p$ is the number of estimated parameters.
- **Rule of Thumb:** Combine adjacent bins if $E_i < 5$.

---

### Problem Type 7.3: Chi-Square Test of Independence ($r \times c$ Contingency Tables)
- **Engineering / Exam Scenario:** Determine whether component failure mode (e.g., Electrical vs. Mechanical vs. Thermal) is statistically independent of the manufacturing production shift (Shift A vs. Shift B vs. Shift C).
- **Expected Frequencies:** $E_{ij} = \frac{R_i \times C_j}{N}$ (Row Total $\times$ Column Total / Grand Total).
- **Test Statistic:** $\chi^2 = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \sim \chi^2((r - 1)(c - 1))$.
- **Decision Rule:** Reject $H_0$ (Independence) if $\chi^2 \ge \chi^2_{\alpha, (r-1)(c-1)}$.

---

# MODULE 8: Analysis of Variance (ANOVA) (Lectures 32–37)

## 8.1 Motivation & Foundational Principles of ANOVA

### 8.1.1 Why Multiple $t$-Tests Fail: Family-Wise Error Rate Inflation
When comparing the means of $k > 2$ independent groups, conducting pairwise two-sample $t$-tests leads to severe **inflation of the Family-Wise Type I Error Rate ($\alpha_{\text{FW}}$)**.
If $k$ treatments are compared, the total number of pairwise tests is $m = \binom{k}{2} = \frac{k(k-1)}{2}$.
Assuming tests are independent with per-comparison error rate $\alpha = 0.05$:
$$\alpha_{\text{FW}} = 1 - (1 - \alpha)^m$$
- For $k = 3$ groups: $m = 3 \implies \alpha_{\text{FW}} = 1 - (0.95)^3 = 1 - 0.8574 = 14.26\%$
- For $k = 5$ groups: $m = 10 \implies \alpha_{\text{FW}} = 1 - (0.95)^{10} = 1 - 0.5987 = 40.13\%$
- For $k = 10$ groups: $m = 45 \implies \alpha_{\text{FW}} = 1 - (0.95)^{45} \approx 90.06\%$

**ANOVA (Analysis of Variance)** solves this by providing a single, omnibus $F$-test that tests the global null hypothesis $H_0: \mu_1 = \mu_2 = \dots = \mu_k$ simultaneously while maintaining the overall Type I error at exactly $\alpha$.

---

### 8.1.2 Fundamental Assumptions of ANOVA
1. **Normality:** The response variable within each treatment population is normally distributed ($y_{ij} \sim N(\mu_i, \sigma^2)$).
2. **Homoscedasticity (Homogeneity of Variances):** All $k$ treatment populations share a common variance ($\sigma_1^2 = \sigma_2^2 = \dots = \sigma_k^2 = \sigma^2$).
3. **Independence:** All individual sample observations are independent random variables.

---

## 8.2 One-Way ANOVA (Completely Randomized Design)

### 8.2.1 The Linear Statistical Model
$$y_{ij} = \mu + \tau_i + \epsilon_{ij}, \quad i = 1, 2, \dots, k; \; j = 1, 2, \dots, n_i$$
where:
- $y_{ij}$: $j$-th observation under the $i$-th treatment.
- $\mu$: Overall grand mean.
- $\tau_i = \mu_i - \mu$: Effect of the $i$-th treatment ($\sum_{i=1}^k n_i \tau_i = 0$).
- $\epsilon_{ij} \sim \text{i.i.d. } N(0, \sigma^2)$: Random experimental error.

#### Hypotheses
$$H_0: \tau_1 = \tau_2 = \dots = \tau_k = 0 \quad (\mu_1 = \mu_2 = \dots = \mu_k)$$
$$H_1: \text{At least one } \tau_i \neq 0 \quad (\text{at least two group means differ})$$

---

### 8.2.2 Partitioning the Total Sum of Squares ($SST$)

> [!NOTE]
> **Lecture notation:** the course writes $SS_T = SS_{Treatments} + SS_E$, $F_0 = MS_{Treatments}/MS_E \sim F_{a-1,\,N-a}$, with $a$ treatments, $n$ replicates and $N = an$. "Between" = treatments and "within" = error.
Total variation in the dataset is partitioned into between-treatment variation and within-treatment error:
$$SST = SSB + SSW \quad (\text{or } SST = SSTr + SSE)$$

#### Mathematical Formulas
Let $N = \sum_{i=1}^k n_i$, $\bar{y}_{i\cdot} = \frac{1}{n_i}\sum_{j=1}^{n_i} y_{ij}$ (group mean), and $\bar{y}_{\cdot\cdot} = \frac{1}{N}\sum_{i=1}^k \sum_{j=1}^{n_i} y_{ij}$ (grand mean):
1. **Total Sum of Squares ($SST$):**
   $$SST = \sum_{i=1}^k \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_{\cdot\cdot})^2 = \sum_{i=1}^k \sum_{j=1}^{n_i} y_{ij}^2 - \frac{(\sum \sum y_{ij})^2}{N}, \quad df = N - 1$$
2. **Between-Group / Treatment Sum of Squares ($SSB$):**
   $$SSB = \sum_{i=1}^k n_i (\bar{y}_{i\cdot} - \bar{y}_{\cdot\cdot})^2 = \sum_{i=1}^k \frac{(\sum_{j} y_{ij})^2}{n_i} - \frac{(\sum \sum y_{ij})^2}{N}, \quad df = k - 1$$
3. **Within-Group / Error Sum of Squares ($SSW$ / $SSE$):**
   $$SSW = \sum_{i=1}^k \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_{i\cdot})^2 = \sum_{i=1}^k (n_i - 1)S_i^2 = SST - SSB, \quad df = N - k$$

---

### 8.2.3 Mean Squares & The $F$-Test Statistic
- **Mean Square Between ($MSB$):** $MSB = \frac{SSB}{k - 1}$
- **Mean Square Error ($MSE$):** $MSE = \frac{SSW}{N - k}$ (Unbiased estimator of $\sigma^2$)
- **Expected Mean Squares:**
  $$E[MSE] = \sigma^2, \qquad E[MSB] = \sigma^2 + \frac{\sum n_i \tau_i^2}{k - 1}$$
  Under $H_0$ ($\tau_i = 0$), $E[MSB] = E[MSE] = \sigma^2$. Under $H_1$, $E[MSB] > \sigma^2$.
- **Test Statistic:**
  $$F_{\text{calc}} = \frac{MSB}{MSE} \sim F(k - 1, N - k)$$
  *Decision Rule:* Reject $H_0$ if $F_{\text{calc}} \ge F_{\alpha, k-1, N-k}$.

#### One-Way ANOVA Summary Table

| Source of Variation | Sum of Squares ($SS$) | Degrees of Freedom ($df$) | Mean Square ($MS$) | $F$-Statistic |
| :--- | :--- | :--- | :--- | :--- |
| **Between Treatments** | $SSB$ | $k - 1$ | $MSB = \frac{SSB}{k-1}$ | $F = \frac{MSB}{MSE}$ |
| **Within Treatments (Error)** | $SSW$ | $N - k$ | $MSE = \frac{SSW}{N-k}$ | |
| **Total** | $SST$ | $N - 1$ | | |

---

## 8.3 Post-Hoc Multiple Comparisons

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** Lec 33 only **names** the Bonferroni, Fisher LSD and Tukey HSD approaches and says finding which mean differs is beyond the scope of the lectures.

When the omnibus ANOVA $F$-test rejects $H_0$, post-hoc tests identify *which specific pairs* of means differ significantly.

### 8.3.1 Tukey's Honestly Significant Difference (HSD) Test
Controls the family-wise error rate at exactly $\alpha$ for all pairwise comparisons with equal sample size $n$:
$$\text{HSD} = q_{\alpha, k, N-k} \sqrt{\frac{MSE}{n}}$$
where $q$ is the Studentized Range Statistic. Any pair with $|\bar{y}_i - \bar{y}_j| \ge \text{HSD}$ is declared statistically significantly different.

---

### 8.3.2 Fisher's Least Significant Difference (LSD) Test
$$\text{LSD} = t_{\alpha/2, N-k} \sqrt{MSE \left( \frac{1}{n_i} + \frac{1}{n_j} \right)}$$

---

## 8.4 Two-Way ANOVA (Factorial Design with Replications)

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** Lec 36 states that two-way and multi-way ANOVA are not discussed. Only one-way ANOVA is taught.

### 8.4.1 Model with Interaction
Evaluates the simultaneous effects of Factor A ($a$ levels), Factor B ($b$ levels), and their interaction ($AB$) with $n$ replications per cell ($N = abn$):
$$y_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \epsilon_{ijk}$$
- **Sum of Squares Partitioning:**
  $$SST = SSA + SSB + SSAB + SSE$$
- **Degrees of Freedom Partitioning:**
  $$(abn - 1) = (a - 1) + (b - 1) + (a - 1)(b - 1) + ab(n - 1)$$

#### Two-Way ANOVA Table

| Source | $SS$ | $df$ | $MS$ | $F$-Statistic | Tested Hypothesis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Factor A** | $SSA$ | $a - 1$ | $MSA = \frac{SSA}{a-1}$ | $F_A = \frac{MSA}{MSE}$ | $H_0: \alpha_1 = \dots = \alpha_a = 0$ |
| **Factor B** | $SSB$ | $b - 1$ | $MSB = \frac{SSB}{b-1}$ | $F_B = \frac{MSB}{MSE}$ | $H_0: \beta_1 = \dots = \beta_b = 0$ |
| **Interaction $AB$** | $SSAB$ | $(a-1)(b-1)$ | $MSAB = \frac{SSAB}{(a-1)(b-1)}$ | $F_{AB} = \frac{MSAB}{MSE}$ | $H_0: (\alpha\beta)_{ij} = 0, \forall i,j$ |
| **Error** | $SSE$ | $ab(n - 1)$ | $MSE = \frac{SSE}{ab(n-1)}$ | | |
| **Total** | $SST$ | $abn - 1$ | | | |

---

## 8.5 Step-by-Step Worked Tutorial Problems

### Problem 8.1: Complete One-Way ANOVA Table Construction
**Statement:** A manufacturing engineer tests the tensile strength of composite polymers manufactured under $k = 3$ different curing temperatures ($100^\circ\text{C}, 125^\circ\text{C}, 150^\circ\text{C}$). A sample of $n = 5$ specimens is tested for each temperature ($N = 15$). The recorded tensile strength data (in $\text{MPa}$) is:

- **Temp 1 ($100^\circ\text{C}$):** $24, 28, 26, 30, 22 \implies \sum y_{1j} = 130, \quad \bar{y}_{1\cdot} = 26.0, \quad \sum y_{1j}^2 = 3420$
- **Temp 2 ($125^\circ\text{C}$):** $36, 40, 34, 38, 42 \implies \sum y_{2j} = 190, \quad \bar{y}_{2\cdot} = 38.0, \quad \sum y_{2j}^2 = 7260$
- **Temp 3 ($150^\circ\text{C}$):** $32, 30, 36, 34, 28 \implies \sum y_{3j} = 160, \quad \bar{y}_{3\cdot} = 32.0, \quad \sum y_{3j}^2 = 5160$

Perform an ANOVA at $\alpha = 0.05$ to determine whether curing temperature significantly affects tensile strength.

**Solution:**
- **Step 1: Compute Totals & Correction Factor ($CF$):**
  - Grand Total $G = \sum \sum y_{ij} = 130 + 190 + 160 = 480$
  - Total Sample Size $N = 15$
  - Grand Mean $\bar{y}_{\cdot\cdot} = \frac{480}{15} = 32.0\text{ MPa}$
  - Correction Factor $CF = \frac{G^2}{N} = \frac{480^2}{15} = \frac{230400}{15} = 15360$
  - Total Sum of Squared Observations $\sum \sum y_{ij}^2 = 3420 + 7260 + 5160 = 15840$
- **Step 2: Compute Sums of Squares:**
  - $SST = \sum \sum y_{ij}^2 - CF = 15840 - 15360 = 480.0$
  - $SSB = \sum_{i=1}^3 \frac{T_i^2}{n_i} - CF = \frac{130^2 + 190^2 + 160^2}{5} - 15360 = \frac{16900 + 36100 + 25600}{5} - 15360 = \frac{78600}{5} - 15360 = 15720 - 15360 = 360.0$
  - $SSW = SST - SSB = 480.0 - 360.0 = 120.0$
- **Step 3: Degrees of Freedom & Mean Squares:**
  - $df_{\text{between}} = k - 1 = 3 - 1 = 2 \implies MSB = \frac{360.0}{2} = 180.0$
  - $df_{\text{within}} = N - k = 15 - 3 = 12 \implies MSE = \frac{120.0}{12} = 10.0$
  - $df_{\text{total}} = N - 1 = 14$
- **Step 4: Compute $F$-Statistic:**
  $$F_{\text{calc}} = \frac{MSB}{MSE} = \frac{180.0}{10.0} = 18.00$$
- **Step 5: ANOVA Summary Table:**

| Source of Variation | Sum of Squares ($SS$) | $df$ | Mean Square ($MS$) | $F_{\text{calc}}$ | $F_{\text{crit}} (0.05, 2, 12)$ | $p$-value |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Curing Temperature** | 360.0 | 2 | 180.0 | **18.00** | 3.89 | $< 0.001$ |
| **Error (Within)** | 120.0 | 12 | 10.0 | | | |
| **Total** | 480.0 | 14 | | | | |

- **Step 6: Conclusion:**
  - Since $F_{\text{calc}} = 18.00 \gg 3.89$, we **reject $H_0$** ($p < 0.001$). Curing temperature has a highly statistically significant effect on tensile strength.
---

## 8.5 Problem Types Commonly Solved in Analysis of Variance (ANOVA)

### Problem Type 8.1: One-Way ANOVA Table Construction & Omnibus $F$-Test
- **Engineering / Exam Scenario:** Testing whether $k \ge 3$ different supplier materials or machine settings result in identical mean tensile strength.
- **Hypotheses:** $H_0: \mu_1 = \mu_2 = \dots = \mu_k$ vs. $H_1:$ At least one mean differs.
- **Calculations:**
  $$SSB = \sum_{i=1}^k n_i (\bar{x}_{i\cdot} - \bar{x}_{\cdot\cdot})^2, \quad SSW = \sum_{i=1}^k (n_i - 1) s_i^2, \quad SST = SSB + SSW$$
  $$MSB = \frac{SSB}{k - 1}, \quad MSE = \frac{SSW}{N - k}, \quad F = \frac{MSB}{MSE} \sim F(k-1, N-k)$$
- **Decision:** Reject $H_0$ if $F \ge F_{\alpha, k-1, N-k}$.

---

### Problem Type 8.2: Post-Hoc Pairwise Comparisons via Tukey's HSD Test
- **Engineering / Exam Scenario:** After an ANOVA $F$-test rejects $H_0$, determine exactly which specific pairs of group means $(\mu_i, \mu_j)$ differ significantly while maintaining overall Family-Wise Error Rate $\alpha$.
- **Tukey's Honest Significant Difference ($HSD$):**
  $$HSD = q_{\alpha, \, k, \, N-k} \sqrt{\frac{MSE}{n}}$$
  where $q$ is the Studentized Range critical value.
- **Decision Rule:** Any pair with $|\bar{x}_i - \bar{x}_j| \ge HSD$ is declared statistically significantly different.

---

# MODULE 9: Correlation & Linear Regression Analysis (Lectures 38–43)

## 9.1 Correlation Analysis

### 9.1.1 Pearson\'s Product-Moment Correlation Coefficient ($r$)
Quantifies the strength and direction of the linear relationship between two continuous variables $X$ and $Y$:
$$r = \frac{S_{xy}}{\sqrt{S_{xx} S_{yy}}} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 \sum_{i=1}^n (y_i - \bar{y})^2}}$$

#### Computational Shortcut Formulas
$$S_{xx} = \sum x_i^2 - \frac{(\sum x_i)^2}{n}, \quad S_{yy} = \sum y_i^2 - \frac{(\sum y_i)^2}{n}, \quad S_{xy} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{n}$$
$$r = \frac{n \sum x_i y_i - (\sum x_i)(\sum y_i)}{\sqrt{\left[ n \sum x_i^2 - (\sum x_i)^2 \right] \left[ n \sum y_i^2 - (\sum y_i)^2 \right]}}$$

#### Key Mathematical Properties
1. **Bounded Range:** $-1 \le r \le +1$.
   - $r = +1$: Perfect positive linear association.
   - $r = -1$: Perfect negative linear association.
   - $r = 0$: Absence of *linear* association.
2. **Invariance:** $r$ is dimensionless and invariant under linear scale and location transformations ($u = ax + b, v = cy + d$).
3. **Linearity Restriction:** $r$ measures *only* linear relationships (e.g., for $Y = X^2$ on $[-1, +1]$, $r = 0$ despite perfect deterministic dependence).

---

### 9.1.2 Hypothesis Testing for Correlation
Tests whether population correlation coefficient $\rho$ differs significantly from zero:
$$H_0: \rho = 0 \quad \text{vs.} \quad H_1: \rho \neq 0$$
Test statistic:
$$t_{\text{calc}} = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^2}} \sim t(n - 2)$$
Reject $H_0$ at level $\alpha$ if $|t_{\text{calc}}| \ge t_{\alpha/2, n-2}$.

---

### 9.1.3 Spearman\'s Rank Correlation Coefficient ($\rho_s$)
Non-parametric correlation measuring monotonic association based on ranked observations:
$$\rho_s = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n(n^2 - 1)}$$
where $d_i = \text{Rank}(x_i) - \text{Rank}(y_i)$.

---

## 9.2 Simple Linear Regression

### 9.2.1 The Simple Linear Regression Model
$$Y_i = \beta_0 + \beta_1 X_i + \epsilon_i, \quad i = 1, 2, \dots, n$$
where:
- $Y$: Dependent / Response variable.
- $X$: Independent / Predictor variable (assumed fixed / non-random).
- $\beta_0$: Population intercept.
- $\beta_1$: Population slope (rate of change in $E[Y]$ per unit increase in $X$).
- $\epsilon_i \sim \text{i.i.d. } N(0, \sigma^2)$: Random error terms.

---

### 9.2.2 Ordinary Least Squares (OLS) Derivation
OLS minimizes the Sum of Squared Residuals $S(\beta_0, \beta_1)$:
$$S(\beta_0, \beta_1) = \sum_{i=1}^n \epsilon_i^2 = \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2$$
Differentiating with respect to $\beta_0$ and $\beta_1$ and setting to zero yields the **Normal Equations**:
$$\frac{\partial S}{\partial \beta_0} = -2 \sum (y_i - \beta_0 - \beta_1 x_i) = 0 \implies n\beta_0 + \beta_1 \sum x_i = \sum y_i$$
$$\frac{\partial S}{\partial \beta_1} = -2 \sum x_i (y_i - \beta_0 - \beta_1 x_i) = 0 \implies \beta_0 \sum x_i + \beta_1 \sum x_i^2 = \sum x_i y_i$$

#### OLS Estimators
$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = r \frac{s_y}{s_x}$$
$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$
The fitted regression line is:
$$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$$

#### The Gauss-Markov Theorem
Under standard assumptions ($E[\epsilon_i]=0, \text{Var}(\epsilon_i)=\sigma^2, \text{Cov}(\epsilon_i, \epsilon_j)=0$), the OLS estimators $\hat{\beta}_0$ and $\hat{\beta}_1$ are **BLUE** (Best Linear Unbiased Estimators).

---

### 9.2.3 Partitioning Variation & Coefficient of Determination ($R^2$)
$$SST = SSR + SSE$$
- **Total Sum of Squares ($SST$):** $SST = \sum (y_i - \bar{y})^2 = S_{yy}, \quad df = n - 1$
- **Regression Sum of Squares ($SSR$):** $SSR = \sum (\hat{y}_i - \bar{y})^2 = \hat{\beta}_1 S_{xy} = \frac{S_{xy}^2}{S_{xx}}, \quad df = 1$
- **Error (Residual) Sum of Squares ($SSE$):** $SSE = \sum (y_i - \hat{y}_i)^2 = SST - SSR, \quad df = n - 2$

#### Coefficient of Determination ($R^2$)
Proportion of total variation in the response variable explained by the linear model:
$$R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST} = r^2$$

#### Standard Error of the Estimate ($s_e$)
$$s_e = \sqrt{MSE} = \sqrt{\frac{SSE}{n - 2}}$$

---

### 9.2.4 ANOVA Approach to Regression & Slope Hypothesis Testing

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** Gauss–Markov/BLUE, the standard error of estimate, slope tests, regression ANOVA, CI vs. PI (9.2.4–9.2.5) and adjusted $R^2$/multicollinearity (9.3.2) are **not taught** in Lec 38–43. The lectures instead cover the chi-square test of association for nominal data (Lec 39) and polynomial regression (Lec 42); see the Theory page. The lecture writes the model as $y = \alpha + \beta x + \varepsilon$ and defines $R^2 = 1 - SSE/SST$.
To test $H_0: \beta_1 = 0$ (no linear relationship) vs. $H_1: \beta_1 \neq 0$:
$$F_{\text{calc}} = \frac{MSR}{MSE} = \frac{SSR / 1}{SSE / (n - 2)} \sim F(1, n - 2)$$
Equivalently, using the $t$-test on slope:
$$SE(\hat{\beta}_1) = \frac{s_e}{\sqrt{S_{xx}}} \implies t_{\text{calc}} = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)} \sim t(n - 2)$$
*(Mathematical Identity: $F_{\text{calc}} = t_{\text{calc}}^2$.)*

---

### 9.2.5 Confidence & Prediction Intervals for Response
For a given value $X = x_0$:
1. **Confidence Interval for Mean Response $E[Y \mid X = x_0]$:**
   $$\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s_e \sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}$$
2. **Prediction Interval for an Individual New Observation $Y_0$:**
   $$\hat{y}_0 \pm t_{\alpha/2, n-2} \cdot s_e \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}}$$
   *(Note: The extra \"$1+\$\" under the radical reflects the intrinsic random variation $\epsilon_0$ of a single new observation, making Prediction Intervals strictly wider than Confidence Intervals.)*

---

## 9.3 Multiple Linear Regression

### 9.3.1 Model & Matrix Formulation
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \epsilon$$
In matrix notation:
$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$$
The OLS estimator vector is:
$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$$

### 9.3.2 Adjusted $R^2$ & Multicollinearity
- **Adjusted $R^2$ ($R^2_{\text{adj}}$):** Penalizes adding irrelevant predictor variables:
  $$R^2_{\text{adj}} = 1 - \left[ \frac{SSE / (n - k - 1)}{SST / (n - 1)} \right] = 1 - (1 - R^2)\left( \frac{n - 1}{n - k - 1} \right)$$
- **Variance Inflation Factor (VIF):** Measures multicollinearity for predictor $X_j$:
  $$\text{VIF}_j = \frac{1}{1 - R_j^2}$$
  *(Rule of Thumb: $\text{VIF}_j > 10$ indicates severe multicollinearity.)*

---

## 9.4 Step-by-Step Worked Tutorial Problems

### Problem 9.1: Complete Simple Linear Regression & ANOVA Analysis
**Statement:** A reliability test measures the operating temperature $X$ ($^\circ\text{C}$) and failure rate $Y$ ($10^{-4}\text{ failures/hour}$) for $n = 5$ electronic modules:

| Module | Temperature $X$ ($^\circ\text{C}$) | Failure Rate $Y$ ($10^{-4}\text{/hr}$) |
| :--- | :--- | :--- |
| **1** | 20 | 1.5 |
| **2** | 30 | 2.0 |
| **3** | 40 | 3.5 |
| **4** | 50 | 4.0 |
| **5** | 60 | 6.0 |

1. Calculate the sample means $\bar{x}, \bar{y}$, summary sums $S_{xx}, S_{yy}, S_{xy}$, and Pearson correlation $r$.
2. Derive the OLS regression equation $\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$.
3. Compute $SST, SSR, SSE$, and the coefficient of determination $R^2$.
4. Conduct the ANOVA $F$-test for significance of regression at $\alpha = 0.05$.
5. Predict the failure rate at $X_0 = 45^\circ\text{C}$ and compute the $95\%$ Confidence Interval for mean failure rate.

**Solution:**
- **Step 1: Summary Statistics:**
  - $\sum x_i = 200, \quad \bar{x} = 40.0^\circ\text{C}$
  - $\sum y_i = 17.0, \quad \bar{y} = 3.40$
  - $\sum x_i^2 = 20^2 + 30^2 + 40^2 + 50^2 + 60^2 = 400 + 900 + 1600 + 2500 + 3600 = 9000$
  - $\sum y_i^2 = 1.5^2 + 2.0^2 + 3.5^2 + 4.0^2 + 6.0^2 = 2.25 + 4.00 + 12.25 + 16.00 + 36.00 = 70.50$
  - $\sum x_i y_i = (20)(1.5) + (30)(2.0) + (40)(3.5) + (50)(4.0) + (60)(6.0) = 30 + 60 + 140 + 200 + 360 = 790$
- **Step 2: Corrected Sums of Squares:**
  - $S_{xx} = \sum x_i^2 - \frac{(\sum x_i)^2}{5} = 9000 - \frac{200^2}{5} = 9000 - 8000 = 1000$
  - $S_{yy} = \sum y_i^2 - \frac{(\sum y_i)^2}{5} = 70.50 - \frac{17.0^2}{5} = 70.50 - 57.80 = 12.70 = SST$
  - $S_{xy} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{5} = 790 - \frac{(200)(17.0)}{5} = 790 - 680 = 110$
- **Step 3: Pearson Correlation:**
  $$r = \frac{S_{xy}}{\sqrt{S_{xx} S_{yy}}} = \frac{110}{\sqrt{1000 \times 12.70}} = \frac{110}{\sqrt{12700}} = \frac{110}{112.694} \approx 0.9761$$
- **Step 4: OLS Coefficients:**
  $$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}} = \frac{110}{1000} = 0.110$$
  $$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} = 3.40 - (0.110)(40.0) = 3.40 - 4.40 = -1.00$$
  $$\text{Fitted Regression Equation: } \hat{y} = -1.00 + 0.110 x$$
- **Step 5: ANOVA & $R^2$ Decomposition:**
  - $SSR = \hat{\beta}_1 S_{xy} = 0.110 \times 110 = 12.10$
  - $SSE = SST - SSR = 12.70 - 12.10 = 0.60$
  - $R^2 = \frac{SSR}{SST} = \frac{12.10}{12.70} \approx 0.9528 \quad (95.28\% \text{ of variation explained})$
  - $MSE = \frac{SSE}{n - 2} = \frac{0.60}{3} = 0.20 \implies s_e = \sqrt{0.20} \approx 0.4472$
  - $MSR = \frac{SSR}{1} = 12.10$
  - $F_{\text{calc}} = \frac{MSR}{MSE} = \frac{12.10}{0.20} = 60.50$
  - Critical value $F_{0.05, 1, 3} = 10.13$. Since $F_{\text{calc}} = 60.50 \gg 10.13$, regression is highly significant ($p < 0.01$).
- **Step 6: Prediction & Confidence Interval at $X_0 = 45^\circ\text{C}$:**
  $$\hat{y}_0 = -1.00 + 0.110(45) = -1.00 + 4.95 = 3.95 \times 10^{-4}\text{ failures/hour}$$
  $t_{0.025, 3} = 3.182$.
  $$SE(E[Y \mid X_0]) = s_e \sqrt{\frac{1}{n} + \frac{(X_0 - \bar{x})^2}{S_{xx}}} = 0.4472 \sqrt{\frac{1}{5} + \frac{(45 - 40)^2}{1000}} = 0.4472 \sqrt{0.20 + 0.025} = 0.4472 \sqrt{0.225} \approx 0.4472 \times 0.47434 \approx 0.2121$$
  $$\text{Margin of Error } = 3.182 \times 0.2121 \approx 0.675$$
  $$95\% \text{ CI: } 3.95 \pm 0.675 \implies [3.275, 4.625] \times 10^{-4}\text{ failures/hour}$$
---

## 9.6 Problem Types Commonly Solved in Correlation & Linear Regression

### Problem Type 9.1: Fitting OLS Regression & Assessing Model Quality ($R^2, F$)
- **Engineering / Exam Scenario:** Predicting degradation rate $Y$ from operating temperature $X$.
- **Slope & Intercept:**
  $$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}, \quad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$
- **Coefficient of Determination:** $R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST} = r^2$.
- **ANOVA for Regression:** $F = \frac{MSR}{MSE} = \frac{SSR / 1}{SSE / (n - 2)} \sim F(1, n-2)$.

---

### Problem Type 9.2: Confidence Interval for Mean Response vs. Prediction Interval for New Unit
- **Confidence Interval for Mean Response $E[Y \mid X_0]$:**
  $$\hat{y}_0 \pm t_{\alpha/2, n-2} s_e \sqrt{\frac{1}{n} + \frac{(X_0 - \bar{x})^2}{S_{xx}}}$$
- **Prediction Interval for an Individual New Observation $Y_0$:**
  $$\hat{y}_0 \pm t_{\alpha/2, n-2} s_e \sqrt{1 + \frac{1}{n} + \frac{(X_0 - \bar{x})^2}{S_{xx}}}$$
- **Key Distinction:** The Prediction Interval is always strictly wider than the Confidence Interval because it accounts for both parameter estimation uncertainty AND individual unit random error $\epsilon$.

---

# MODULE 10: Auto-Regression & Time-Series Modeling for Reliability (Lecture 44)

## 10.1 Time-Series Fundamentals in Reliability Analysis

### 10.1.1 Time-Dependent Degradation Signals
In modern condition-based maintenance (CBM) and Prognostics and Health Management (PHM), reliability engineers monitor time-series data from sensors to detect early signs of equipment deterioration before catastrophic failure occurs:
- **Vibration Signals:** Bearing race fatigue, gearbox gear tooth pitting, rotor unbalance.
- **Thermal Drift:** Electrical transformer insulation breakdown, battery cell internal resistance heating.
- **Acoustic Emissions & Lubricant Contamination.**

---

### 10.1.2 Concept of Weak (Covariance) Stationarity
A time series $\{X_t, t \in \mathbb{Z}\}$ is **weakly (covariance) stationary** if:
1. **Constant Mean:** $E[X_t] = \mu, \quad \forall t$
2. **Finite & Constant Variance:** $\text{Var}(X_t) = \gamma_0 < \infty, \quad \forall t$
3. **Lag-Dependent Autocovariance:** $\text{Cov}(X_t, X_{t-k}) = \gamma_k$ depends *only* on the time lag $k$, and not on the absolute time $t$.

#### Autocovariance & Autocorrelation Function (ACF)
- **Autocovariance at Lag $k$:** $\gamma_k = E[(X_t - \mu)(X_{t-k} - \mu)]$ (with $\gamma_{-k} = \gamma_k$).
- **Autocorrelation Function (ACF) $\rho_k$:**
  $$\rho_k = \frac{\gamma_k}{\gamma_0} = \frac{\text{Cov}(X_t, X_{t-k})}{\text{Var}(X_t)}$$
  *Properties:* $\rho_0 = 1$, $-1 \le \rho_k \le 1$, $\rho_{-k} = \rho_k$.

---

## 10.2 The Autoregressive Model ($\text{AR}(p)$)

### 10.2.1 General $\text{AR}(p)$ Formulation
In an Autoregressive model of order $p$, the current observation $X_t$ is modeled as a linear combination of its previous $p$ values plus a white noise shock:
$$X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + \epsilon_t$$
where:
- $c$: Constant term (related to mean).
- $\phi_1, \dots, \phi_p$: Autoregressive parameters.
- $\epsilon_t \sim \text{i.i.d. } \text{WN}(0, \sigma^2)$: White noise process with $E[\epsilon_t] = 0, \text{Var}(\epsilon_t) = \sigma^2, \text{Cov}(\epsilon_t, X_{t-k}) = 0$ for $k \ge 1$.

---

### 10.2.2 The First-Order Autoregressive Model: $\text{AR}(1)$

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** Lec 44 introduces AR($p$) as $Y_t = \beta_0 + \beta_1 Y_{t-1} + \cdots + \beta_p Y_{t-p} + \varepsilon_t$ and requires the data to be **stationary** and **uniform** (evenly spaced, no gaps). The AR(1) moment formulas below, Yule–Walker details and RUL forecasting (10.3) are **not taught**.
$$X_t = c + \phi_1 X_{t-1} + \epsilon_t$$

#### 1. Stationarity Condition
The $\text{AR}(1)$ process is stationary if and only if:
$$|\phi_1| < 1$$
*(If $|\phi_1| = 1$, the process becomes a Non-Stationary Random Walk; if $|\phi_1| > 1$, the series explodes exponentially.)*

#### 2. Unconditional Mean ($\mu$)
Taking expectations on both sides under stationarity ($E[X_t] = E[X_{t-1}] = \mu$):
$$\mu = c + \phi_1 \mu + 0 \implies \mu(1 - \phi_1) = c \implies \mu = \frac{c}{1 - \phi_1}$$

#### 3. Unconditional Variance ($\gamma_0$)
Subtracting $\mu$ from both sides ($x_t = X_t - \mu$):
$$x_t = \phi_1 x_{t-1} + \epsilon_t$$
Squaring and taking expectations:
$$E[x_t^2] = \phi_1^2 E[x_{t-1}^2] + E[\epsilon_t^2] + 2\phi_1 E[x_{t-1}\epsilon_t]$$
$$\gamma_0 = \phi_1^2 \gamma_0 + \sigma^2 + 0 \implies \gamma_0(1 - \phi_1^2) = \sigma^2$$
$$\text{Var}(X_t) = \gamma_0 = \frac{\sigma^2}{1 - \phi_1^2}$$

#### 4. Autocovariance & Autocorrelation ($\rho_k$)
Multiplying $x_t = \phi_1 x_{t-1} + \epsilon_t$ by $x_{t-k}$ ($k \ge 1$) and taking expectations:
$$E[x_t x_{t-k}] = \phi_1 E[x_{t-1} x_{t-k}] + E[\epsilon_t x_{t-k}]$$
$$\gamma_k = \phi_1 \gamma_{k-1} \implies \frac{\gamma_k}{\gamma_0} = \phi_1 \frac{\gamma_{k-1}}{\gamma_0} \implies \rho_k = \phi_1 \rho_{k-1}$$
By induction, since $\rho_0 = 1$:
$$\rho_k = \phi_1^k, \quad k = 1, 2, 3, \dots$$
*(The ACF decays exponentially to zero if $0 < \phi_1 < 1$, or oscillates with decaying amplitude if $-1 < \phi_1 < 0$.)*

---

### 10.2.3 Parameter Estimation via Yule-Walker Equations
Multiplying the mean-centered $\text{AR}(p)$ model by $x_{t-k}$ ($k = 1, \dots, p$) yields the **Yule-Walker system**:
$$\begin{bmatrix} 1 & \rho_1 & \dots & \rho_{p-1} \\ \rho_1 & 1 & \dots & \rho_{p-2} \\ \vdots & \vdots & \ddots & \vdots \\ \rho_{p-1} & \rho_{p-2} & \dots & 1 \end{bmatrix} \begin{bmatrix} \phi_1 \\ \phi_2 \\ \vdots \\ \phi_p \end{bmatrix} = \begin{bmatrix} \rho_1 \\ \rho_2 \\ \vdots \\ \rho_p \end{bmatrix}$$
Substituting sample autocorrelations $r_k$ gives consistent estimates for $\hat{\phi}_1, \dots, \hat{\phi}_p$.

---

## 10.3 Reliability Applications: Remaining Useful Life (RUL) Forecasting

### 10.3.1 Forecasting Future Degradation Trajectories
Given current sensor state $X_T$ at time $T$, the $h$-step ahead point forecast for an $\text{AR}(1)$ process is:
$$\hat{X}_{T+h \mid T} = E[X_{T+h} \mid X_T, X_{T-1}, \dots] = \mu + \phi_1^h (X_T - \mu)$$
As forecast horizon $h \to \infty$, the forecast smoothly reverts to the long-term mean $\mu$.

### 10.3.2 Determining Remaining Useful Life (RUL)

> [!CAUTION]
> A **stationary** AR forecast reverts to its mean, so it cannot predict a threshold crossing. RUL needs a trending (non-stationary) degradation model, for example an AR model on differenced data or with drift.
Let $D_{\text{crit}}$ denote the critical degradation threshold at which failure occurs (e.g., maximum permissible vibration amplitude of $10\text{ mm/s}$).
The **Remaining Useful Life (RUL)** is the time index $h^*$ when the predicted degradation crosses the threshold:
$$\text{RUL} = \min \left\{ h > 0 \mid \hat{X}_{T+h \mid T} \ge D_{\text{crit}} \right\}$$

---

## 10.4 Step-by-Step Worked Problem

### Problem 10.1: $\text{AR}(1)$ Degradation Model Analysis
**Statement:** A vibration sensor mounted on an industrial centrifugal pump follows an $\text{AR}(1)$ process:
$$X_t = 0.6 + 0.7 X_{t-1} + \epsilon_t, \quad \epsilon_t \sim \text{WN}(0, \sigma^2 = 0.51)$$
where $X_t$ is vibration level in $\text{mm/s}$.
1. Verify stationarity and compute the unconditional mean $\mu$ and variance $\gamma_0$.
2. Compute the first three autocorrelation coefficients $\rho_1, \rho_2, \rho_3$.
3. If the current vibration level is $X_{100} = 4.0\text{ mm/s}$, predict the vibration level $1$ step and $3$ steps ahead ($\hat{X}_{101}$ and $\hat{X}_{103}$).

**Solution:**
- **Step 1: Stationarity, Mean, and Variance:**
  - $\phi_1 = 0.7$. Since $|\phi_1| = 0.7 < 1$, the process is **stationary**.
  - Unconditional Mean: $\mu = \frac{c}{1 - \phi_1} = \frac{0.6}{1 - 0.7} = \frac{0.6}{0.3} = 2.0\text{ mm/s}$.
  - Variance: $\gamma_0 = \frac{\sigma^2}{1 - \phi_1^2} = \frac{0.51}{1 - (0.7)^2} = \frac{0.51}{1 - 0.49} = \frac{0.51}{0.51} = 1.0\text{ (mm/s)}^2$.
- **Step 2: Autocorrelations:**
  - $\rho_1 = \phi_1^1 = 0.70$
  - $\rho_2 = \phi_1^2 = (0.7)^2 = 0.49$
  - $\rho_3 = \phi_1^3 = (0.7)^3 = 0.343$
- **Step 3: Point Forecasting:**
  - $1$-step ahead ($h = 1$):
    $$\hat{X}_{101} = \mu + \phi_1^1 (X_{100} - \mu) = 2.0 + 0.7(4.0 - 2.0) = 2.0 + 0.7(2.0) = 2.0 + 1.4 = 3.40\text{ mm/s}$$
  - $3$-steps ahead ($h = 3$):
    $$\hat{X}_{103} = \mu + \phi_1^3 (X_{100} - \mu) = 2.0 + 0.343(4.0 - 2.0) = 2.0 + 0.343(2.0) = 2.0 + 0.686 = 2.686\text{ mm/s}$$
---

## 10.4 Problem Types Commonly Solved in Time-Series & AR(1) Degradation Modeling

### Problem Type 10.1: AR(1) Stationarity, Unconditional Moments & Yule-Walker
- **Engineering / Exam Scenario:** Sensor vibration time-series $X_t = c + \phi_1 X_{t-1} + a_t$ with $a_t \sim WN(0, \sigma^2)$.
- **Stationarity Check:** Requires $|\phi_1| < 1$.
- **Unconditional Mean & Variance:**
  $$\mu = \frac{c}{1 - \phi_1}, \quad \gamma_0 = \text{Var}(X_t) = \frac{\sigma^2}{1 - \phi_1^2}$$
- **Autocorrelation Function (ACF):** $\rho_k = \phi_1^k$ (exponential decay).

---

### Problem Type 10.2: $h$-Step Ahead Forecasting & Remaining Useful Life (RUL)
- **Point Forecast:** $\hat{X}_{T+h} = \mu + \phi_1^h (X_T - \mu)$.
- **RUL Calculation:** Find smallest lead time $h^*$ such that forecast $\hat{X}_{T+h^*}$ reaches the critical degradation threshold $X_{\text{crit}}$.

---

# MODULE 11: Logistic Regression & Binary Classification (Lectures 45–48)

## 11.1 Limitations of Linear Regression for Binary Outcomes

When modeling a binary categorical response variable $Y \in \{0, 1\}$ (e.g., $Y = 1$ for Component Failure, $Y = 0$ for Component Survival), Ordinary Least Squares (OLS) linear regression encounters three severe theoretical breakdowns:
1. **Unbounded Predictions:** The linear model $\hat{p}(X) = \beta_0 + \beta_1 X$ produces predicted probabilities $\hat{p} < 0$ or $\hat{p} > 1$ for extreme values of $X$, violating the fundamental probability axiom $0 \le P(Y = 1 \mid X) \le 1$.
2. **Non-Normal Error Distribution:** The error term $\epsilon_i = Y_i - (\beta_0 + \beta_1 X_i)$ takes on only two discrete values ($1 - \beta_0 - \beta_1 X_i$ or $-\beta_0 - \beta_1 X_i$), completely violating the normality assumption required for $t$ and $F$ tests.
3. **Severe Heteroscedasticity:** The variance of a Bernoulli random variable is non-constant:
   $$\text{Var}(\epsilon_i) = \text{Var}(Y_i) = p_i(1 - p_i) = (\beta_0 + \beta_1 X_i)(1 - \beta_0 - \beta_1 X_i)$$
   which depends directly on $X_i$, causing OLS standard errors to be invalid.

```
Linear vs. Logistic Fit:
  P(Y=1)
    1.0 |                   .------------------' (Logistic / Sigmoid)
        |                 /
    0.5 |                /
        |               /      / (Linear Regression - Exceeds bounds!)
    0.0 '--------------'______/____________________> Feature X
```

---

## 11.2 The Logit Link & Logistic Function

### 11.2.1 Odds and Log-Odds (Logit Transformation)
- Let $p(\mathbf{x}) = P(Y = 1 \mid \mathbf{X} = \mathbf{x})$ denote the probability of failure.
- **Odds of Failure:** The ratio of the probability of failure to the probability of survival:
  $$\text{Odds} = \frac{p(\mathbf{x})}{1 - p(\mathbf{x})} \in (0, \infty)$$
- **Logit Function (Log-Odds):** Taking the natural logarithm maps the domain $(0, \infty)$ to the entire real line $(-\infty, \infty)$:
  $$\text{logit}(p(\mathbf{x})) = \ln\left( \frac{p(\mathbf{x})}{1 - p(\mathbf{x})} \right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k = \boldsymbol{\beta}^T \mathbf{x}$$

---

### 11.2.2 The Sigmoid (Logistic) Function
Inverting the logit transformation yields the **Logistic / Sigmoid Function**:
$$\frac{p(\mathbf{x})}{1 - p(\mathbf{x})} = e^{\boldsymbol{\beta}^T \mathbf{x}} \implies p(\mathbf{x}) = \frac{e^{\boldsymbol{\beta}^T \mathbf{x}}}{1 + e^{\boldsymbol{\beta}^T \mathbf{x}}} = \frac{1}{1 + e^{-\boldsymbol{\beta}^T \mathbf{x}}}$$
*Properties of the Sigmoid Curve:*
- S-shaped monotonic curve strictly bounded within $(0, 1)$.
- When $\boldsymbol{\beta}^T \mathbf{x} = 0$, $p(\mathbf{x}) = 0.50$ (the default decision boundary).
- When $\boldsymbol{\beta}^T \mathbf{x} \to +\infty$, $p(\mathbf{x}) \to 1.0$.
- When $\boldsymbol{\beta}^T \mathbf{x} \to -\infty$, $p(\mathbf{x}) \to 0.0$.

---

### 11.2.3 Interpretation of Logistic Regression Coefficients
- **Slope $\beta_j$:** The change in the **log-odds** of failure per unit increase in predictor $X_j$, holding all other predictors constant.
- **Odds Ratio ($OR_j = e^{\beta_j}$):** The multiplicative change in the **odds** of failure per unit increase in $X_j$:
  $$\frac{\text{Odds}(X_j + 1)}{\text{Odds}(X_j)} = e^{\beta_j}$$
  - If $e^{\beta_j} > 1$ ($\beta_j > 0$): Each unit increase in $X_j$ multiplies the odds of failure by $e^{\beta_j}$ (increased risk).
  - If $e^{\beta_j} = 1$ ($\beta_j = 0$): $X_j$ has no effect on odds.
  - If $e^{\beta_j} < 1$ ($\beta_j < 0$): Each unit increase in $X_j$ reduces the odds of failure (protective factor).

---

## 11.3 Maximum Likelihood Estimation for Logistic Regression

Since OLS cannot be applied, parameters are estimated via **Maximum Likelihood Estimation (MLE)**.
Let $(y_1, \mathbf{x}_1), (y_2, \mathbf{x}_2), \dots, (y_n, \mathbf{x}_n)$ be an independent sample with $y_i \in \{0, 1\}$.
- **Likelihood Function:**
  $$L(\boldsymbol{\beta}) = \prod_{i=1}^n p(\mathbf{x}_i)^{y_i} [1 - p(\mathbf{x}_i)]^{1 - y_i}$$
- **Log-Likelihood Function:**
  $$\ln L(\boldsymbol{\beta}) = \sum_{i=1}^n \left[ y_i \ln p(\mathbf{x}_i) + (1 - y_i) \ln(1 - p(\mathbf{x}_i)) \right] = \sum_{i=1}^n \left[ y_i (\boldsymbol{\beta}^T \mathbf{x}_i) - \ln(1 + e^{\boldsymbol{\beta}^T \mathbf{x}_i}) \right]$$
- **Gradient Vector (Score Equations):**
  $$\frac{\partial \ln L}{\partial \boldsymbol{\beta}} = \sum_{i=1}^n [y_i - p(\mathbf{x}_i)] \mathbf{x}_i = \mathbf{0}$$
Since the score equations are non-linear in $\boldsymbol{\beta}$, they have no closed-form analytical solution and are solved numerically using the **Newton-Raphson method** or **Iteratively Reweighted Least Squares (IRLS)**.

---

## 11.4 Goodness-of-Fit & Model Significance

### 11.4.1 Deviance & Likelihood Ratio Test

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** deviance, the likelihood-ratio test and pseudo-$R^2$ are **not taught**. Of 11.4, only the Wald test (Lec 46) is covered. The lectures also cover multinomial (pivot class) and ordinal logistic regression, and stress that logistic regression is "strictly not a classifier" until a cut-off is chosen.
- **Deviance ($D$):** $D = -2 \ln L(\hat{\boldsymbol{\beta}})$ (Analogous to $SSE$ in linear regression).
- **Likelihood Ratio Test ($G$):** Compares the fitted model with $k$ predictors against the intercept-only (null) model:
  $$G = -2 \left[ \ln L(\text{Null}) - \ln L(\text{Fitted}) \right] = D_{\text{null}} - D_{\text{fitted}} \sim \chi^2(k)$$
  Reject $H_0: \beta_1 = \dots = \beta_k = 0$ if $G \ge \chi^2_{\alpha, k}$.

### 11.4.2 Wald Test for Individual Predictors
To test $H_0: \beta_j = 0$ vs. $H_1: \beta_j \neq 0$:
$$W = \left( \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)} \right)^2 \sim \chi^2(1) \quad \left( \text{or } Z = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)} \sim N(0, 1) \right)$$

### 11.4.3 Pseudo-$R^2$ Measures
- **McFadden's Pseudo-$R^2$:**
  $$R^2_{\text{McFadden}} = 1 - \frac{\ln L(\text{Fitted})}{\ln L(\text{Null})}$$
  *(Values between $0.20$ and $0.40$ represent excellent model fit.)*

---

## 11.5 Binary Classification Performance Metrics

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** the confusion matrix, precision/recall/F1 and ROC/AUC are **not taught** in Lec 45–48.

### 11.5.1 The Confusion Matrix
Given a decision threshold $p_{\text{thresh}} = 0.50$:

| Actual Class $\downarrow$ \ Predicted Class $\rightarrow$ | **Predicted Failure ($\hat{Y} = 1$)** | **Predicted Normal ($\hat{Y} = 0$)** |
| :--- | :--- | :--- |
| **Actual Failure ($Y = 1$)** | **True Positive ($TP$)** | **False Negative ($FN$, Type II Error)** |
| **Actual Normal ($Y = 0$)** | **False Positive ($FP$, Type I Error)** | **True Negative ($TN$)** |

#### Performance Metric Formulas
1. **Accuracy:** $\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$
2. **Precision (Positive Predictive Value):** $\text{Precision} = \frac{TP}{TP + FP}$
3. **Sensitivity / Recall / True Positive Rate (TPR):** $\text{Recall} = \frac{TP}{TP + FN}$
4. **Specificity / True Negative Rate (TNR):** $\text{Specificity} = \frac{TN}{TN + FP}$
5. **False Positive Rate (FPR):** $\text{FPR} = 1 - \text{Specificity} = \frac{FP}{TN + FP}$
6. **$F_1$-Score (Harmonic Mean of Precision and Recall):**
   $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}$$

---

### 11.5.2 ROC Curve & AUC (Area Under Curve)
- **Receiver Operating Characteristic (ROC) Curve:** A graphical plot of **True Positive Rate ($\text{TPR}$)** on the $y$-axis versus **False Positive Rate ($\text{FPR}$)** on the $x$-axis across all possible classification probability thresholds $p_{\text{thresh}} \in [0, 1]$.
- **Area Under the ROC Curve (AUC):**
  - $\text{AUC} = 0.50$: Pure random guessing (diagonal line).
  - $\text{AUC} = 1.00$: Perfect, error-free classification.
  - $\text{AUC} \ge 0.80$: Strong, reliable discriminating performance.

---

## 11.6 Step-by-Step Worked Tutorial Problem

### Problem 11.1: Component Failure Odds & Risk Estimation
**Statement:** A logistic regression model is fitted to predict the probability of high-voltage capacitor dielectric breakdown ($Y = 1$) based on operating temperature $X_1$ ($^\circ\text{C}$) and voltage stress $X_2$ ($\text{kV}$):
$$\text{logit}(p) = -6.50 + 0.05 X_1 + 0.80 X_2$$
1. Calculate the estimated failure probability $p$ for a capacitor operating at $T = 70^\circ\text{C}$ and Voltage $V = 5.0\text{ kV}$.
2. Interpret the Odds Ratio for voltage stress $X_2$. What is the effect of increasing voltage by $1\text{ kV}$ while holding temperature constant?
3. What is the effect of increasing voltage by $2\text{ kV}$?

**Solution:**
- **Step 1: Compute Linear Log-Odds & Probability:**
  $$\boldsymbol{\beta}^T \mathbf{x} = -6.50 + 0.05(70) + 0.80(5.0) = -6.50 + 3.50 + 4.00 = +1.00$$
  $$p(\mathbf{x}) = \frac{1}{1 + e^{-(\boldsymbol{\beta}^T \mathbf{x})}} = \frac{1}{1 + e^{-1.00}} = \frac{1}{1 + 0.36788} = \frac{1}{1.36788} \approx 0.73105 \quad (73.11\%)$$
- **Step 2: Odds Ratio for Voltage Stress $X_2$ ($\beta_2 = 0.80$):**
  $$OR_2 = e^{\beta_2} = e^{0.80} \approx 2.2255$$
  *Interpretation:* For each additional $1\text{ kV}$ increase in voltage stress, the odds of dielectric breakdown increase by a factor of $2.226$ (a $122.6\%$ increase in odds), holding temperature constant.
- **Step 3: Effect of a $2\text{ kV}$ Voltage Increase ($\Delta X_2 = 2$):**
  $$OR_{\Delta X_2 = 2} = e^{2 \beta_2} = e^{2(0.80)} = e^{1.60} \approx 4.953$$
  *Interpretation:* Increasing voltage by $2\text{ kV}$ multiplies the odds of capacitor breakdown by approximately $4.95$ (nearly a $5$-fold increase in failure odds).
---

## 11.7 Problem Types Commonly Solved in Logistic Regression & Binary Classification

### Problem Type 11.1: Component Failure Probability & Odds Ratio Calculations
- **Given Fitted Model:** $\text{logit}(p) = \beta_0 + \beta_1 X_1 + \dots + \beta_k X_k$.
- **Probability of Failure:** $p(\mathbf{x}) = \frac{1}{1 + e^{-(\beta_0 + \boldsymbol{\beta}^T\mathbf{x})}}$.
- **Odds Ratio Effect for Variable $X_j$:** $OR_j = e^{\beta_j}$. A $1$-unit increase in $X_j$ multiplies failure odds by $e^{\beta_j}$. For a $\Delta X_j$-unit increase, $OR = e^{\Delta X_j \cdot \beta_j}$.

---

### Problem Type 11.2: Confusion Matrix & Diagnostic Metric Derivations
- **Formulas:**
  $$\text{Accuracy} = \frac{TP + TN}{N}, \quad \text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall (Sensitivity)} = \frac{TP}{TP + FN}$$
  $$\text{Specificity} = \frac{TN}{TN + FP}, \quad F_1 = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

---

# MODULE 12: Machine Learning Classifiers: Bayes, k-NN & Support Vector Machines (Lectures 49–60)

## 12.1 Foundations of Statistical Classification

### 12.1.1 The Supervised Classification Paradigm
In machine learning and reliability diagnostics, classification assigns an input feature vector $\mathbf{x} = [x_1, x_2, \dots, x_d]^T \in \mathcal{X} \subseteq \mathbb{R}^d$ to one of $K$ discrete categorical classes $C_1, C_2, \dots, C_K \in \mathcal{Y}$ (e.g., Healthy, Degraded, Failed).
Given a training dataset $\mathcal{D} = \{(\mathbf{x}_1, y_1), (\mathbf{x}_2, y_2), \dots, (\mathbf{x}_N, y_N)\}$, the objective is to learn a decision mapping function $f: \mathcal{X} \to \mathcal{Y}$ that minimizes expected generalization error on unseen test data.

---

### 12.1.2 Bayes Optimal Classifier & Naive Bayes Classifier

> [!NOTE]
> **Lecture convention:** the course handles zero counts with the **m-estimate** $\frac{n_c + m p}{n + m}$ (Lec 53). Laplace smoothing is the special case $m = k$, $p = 1/k$. The lecture calls $P(x_j \mid c)$ the "posterior" probability, and adds a second Naive Bayes assumption: all attributes contribute equally.

#### 1. Maximum A Posteriori (MAP) Decision Rule
By Bayes\' Theorem, the posterior probability of class $C_k$ given feature vector $\mathbf{x}$ is:
$$P(C_k \mid \mathbf{x}) = \frac{P(\mathbf{x} \mid C_k) P(C_k)}{P(\mathbf{x})} = \frac{P(\mathbf{x} \mid C_k) P(C_k)}{\sum_{j=1}^K P(\mathbf{x} \mid C_j) P(C_j)}$$
The **Bayes Optimal Decision Rule** assigns $\mathbf{x}$ to the class maximizing posterior probability:
$$\hat{y} = \arg\max_{C_k} P(C_k \mid \mathbf{x}) = \arg\max_{C_k} P(\mathbf{x} \mid C_k) P(C_k)$$

#### 2. The Naive Bayes Conditional Independence Assumption
To overcome the curse of dimensionality in estimating high-dimensional joint likelihoods $P(\mathbf{x} \mid C_k)$, the **Naive Bayes Classifier** assumes that all $d$ features are conditionally independent given the class label:
$$P(\mathbf{x} \mid C_k) = P(x_1, x_2, \dots, x_d \mid C_k) = \prod_{j=1}^d P(x_j \mid C_k)$$
The classification decision rule becomes:
$$\hat{y} = \arg\max_{C_k} \left[ P(C_k) \prod_{j=1}^d P(x_j \mid C_k) \right]$$

```
Naive Bayes Graphical Model:
             [ Class C_k ]
            /     |       \
           v      v        v
        [ x_1 ] [ x_2 ] ... [ x_d ]
(Features are mutually independent given Class C_k)
```

#### 3. The Zero-Frequency Problem & Laplace (Additive) Smoothing
If a particular feature value $v$ never appears with class $C_k$ in the training set ($N_{kj} = 0$), the maximum likelihood estimate is $P(x_j = v \mid C_k) = 0$, which zeros out the entire product $\prod P(x_j \mid C_k)$, completely wiping out evidence from all other features!
To prevent this, **Laplace (Additive) Smoothing** adds a pseudo-count $\alpha > 0$ (typically $\alpha = 1$):
$$\hat{P}(x_j = v \mid C_k) = \frac{N_{kj} + \alpha}{N_k + \alpha V}$$
where $N_k$ is the total count of training instances in class $C_k$, and $V$ is the number of possible discrete values for feature $j$.

#### 4. Continuous Features: Gaussian Naive Bayes
For continuous numerical features, class-conditional likelihoods are modeled via univariate Gaussians:
$$P(x_j \mid C_k) = \frac{1}{\sigma_{kj} \sqrt{2\pi}} \exp\left( -\frac{(x_j - \mu_{kj})^2}{2\sigma_{kj}^2} \right)$$
where $\mu_{kj}$ and $\sigma_{kj}^2$ are the sample mean and variance of feature $j$ within class $C_k$.

---

## 12.2 $k$-Nearest Neighbors ($k$-NN) Classification

### 12.2.1 Principles of Instance-Based Learning
$k$-NN is a non-parametric, lazy learning algorithm that defers all computation until a test query point $\mathbf{x}_{\text{query}}$ is presented.

#### Algorithm Steps
1. Compute the distance between query point $\mathbf{x}_{\text{query}}$ and all $N$ training points $\mathbf{x}_i \in \mathcal{D}$.
2. Identify the $k$ nearest training samples $\mathcal{N}_k(\mathbf{x}_{\text{query}})$.
3. Assign $\mathbf{x}_{\text{query}}$ to the majority class among its $k$ nearest neighbors:
   $$\hat{y} = \arg\max_{C} \sum_{i \in \mathcal{N}_k(\mathbf{x}_{\text{query}})} \mathbb{I}(y_i = C)$$

---

### 12.2.2 Distance Metrics
1. **Euclidean Distance ($L_2$ Norm):** $d(\mathbf{x}, \mathbf{z}) = \sqrt{\sum_{j=1}^d (x_j - z_j)^2} = \|\mathbf{x} - \mathbf{z}\|_2$
2. **Manhattan Distance ($L_1$ Norm):** $d(\mathbf{x}, \mathbf{z}) = \sum_{j=1}^d |x_j - z_j|$
3. **Minkowski Distance ($L_p$ Metric):** $d(\mathbf{x}, \mathbf{z}) = \left( \sum_{j=1}^d |x_j - z_j|^p \right)^{1/p}$
4. **Mahalanobis Distance (Accounts for feature covariances):** $d(\mathbf{x}, \mathbf{z}) = \sqrt{(\mathbf{x} - \mathbf{z})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{z})}$

---

### 12.2.3 Hyperparameter Tuning & Bias-Variance Trade-off in $k$-NN
- **$k = 1$:** High Variance, Low Bias. Creates complex, jagged decision boundaries with Voronoi tessellations. Highly sensitive to noise and outliers (overfitting).
- **Large $k$ ($k \to N$):** Low Variance, High Bias. Creates smooth decision boundaries, but approaches predicting the majority class globally (underfitting).
- **Rule of Thumb:** Choose $k$ as an odd number (e.g., $k = 3, 5, 7$) to prevent ties in binary classification, with $k \approx \sqrt{N}$ chosen via cross-validation.
- **Mandatory Preprocessing:** Features must be standardized (Z-score: $x' = \frac{x - \mu}{\sigma}$ or Min-Max: $x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$) to prevent variables with large metric ranges from dominating distance computations.

---

## 12.3 Support Vector Machines (SVM) — Hard-Margin Formulation

### 12.3.1 Linear Separability & The Optimal Margin Hyperplane
Consider a binary classification problem with training data $\{(\mathbf{x}_i, y_i)\}_{i=1}^N$ where $\mathbf{x}_i \in \mathbb{R}^d$ and labels $y_i \in \{-1, +1\}$.
A separating hyperplane is defined by:
$$\mathbf{w}^T \mathbf{x} + b = 0$$
where $\mathbf{w}$ is the normal weight vector and $b$ is the bias.
The decision rule is:
$$f(\mathbf{x}) = \text{sign}(\mathbf{w}^T \mathbf{x} + b)$$

```
Optimal Margin Hyperplane (Hard-Margin SVM):
               x2 ^
                  |         +  (Class +1)
                  |       +    /
                  |     +     /  <-- Positive Bounding Plane: w^T x + b = +1
                  |          /
                  |         /    <-- Optimal Hyperplane: w^T x + b = 0
                  |        /
                  |  -    /  <-- Negative Bounding Plane: w^T x + b = -1
                  | -    /
                  |-    -  (Class -1)
                  +----------------------------------> x1
                         |<-- Margin = 2 / ||w|| -->|
```

#### Canonical Hyperplane & Margin Geometry
Scaling $\mathbf{w}$ and $b$ such that the closest data points satisfy $|\mathbf{w}^T \mathbf{x}_i + b| = 1$, all training points satisfy the canonical constraints:
$$y_i (\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \quad \forall i = 1, 2, \dots, N$$
The perpendicular distance from any point $\mathbf{x}_i$ to the hyperplane is:
$$\gamma_i = \frac{y_i (\mathbf{w}^T \mathbf{x}_i + b)}{\|\mathbf{w}\|}$$
For points on the margin boundaries ($\mathbf{w}^T\mathbf{x}+b = \pm 1$), the distance is $\frac{1}{\|\mathbf{w}\|}$.
The total **Geometric Margin** separating the two classes is:
$$\text{Margin } \gamma = \frac{2}{\|\mathbf{w}\|}$$

---

### 12.3.2 The Primal Optimization Problem
To maximize the margin $\frac{2}{\|\mathbf{w}\|}$, we minimize $\frac{1}{2}\|\mathbf{w}\|^2$ (a convex quadratic objective):
$$\min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 = \frac{1}{2} \mathbf{w}^T \mathbf{w} \quad \text{subject to} \quad y_i (\mathbf{w}^T \mathbf{x}_i + b) \ge 1, \quad \forall i = 1, \dots, N$$

---

### 12.3.3 Lagrange Multipliers & Karush-Kuhn-Tucker (KKT) Conditions

> [!NOTE]
> **Lecture notation:** the multipliers are written $\lambda_i$ (here $\alpha_i$) and the Lagrangians $L_P$ / $L_D$. $b$ is computed from each support vector and averaged.
Introducing Lagrange multipliers $\alpha_i \ge 0$ for each inequality constraint, the **Primal Lagrangian** is:
$$L(\mathbf{w}, b, \boldsymbol{\alpha}) = \frac{1}{2} \mathbf{w}^T \mathbf{w} - \sum_{i=1}^N \alpha_i \left[ y_i (\mathbf{w}^T \mathbf{x}_i + b) - 1 \right]$$

#### Karush-Kuhn-Tucker (KKT) First-Order Necessary & Sufficient Conditions:
1. **Stationarity with respect to $\mathbf{w}$:**
   $$\nabla_{\mathbf{w}} L = \mathbf{w} - \sum_{i=1}^N \alpha_i y_i \mathbf{x}_i = \mathbf{0} \implies \mathbf{w} = \sum_{i=1}^N \alpha_i y_i \mathbf{x}_i$$
   *(The optimal normal vector $\mathbf{w}$ is a linear combination of training vectors!)*
2. **Stationarity with respect to $b$:**
   $$\frac{\partial L}{\partial b} = -\sum_{i=1}^N \alpha_i y_i = 0 \implies \sum_{i=1}^N \alpha_i y_i = 0$$
3. **Primal Feasibility:**
   $$y_i (\mathbf{w}^T \mathbf{x}_i + b) - 1 \ge 0, \quad \forall i = 1, \dots, N$$
4. **Dual Feasibility:**
   $$\alpha_i \ge 0, \quad \forall i = 1, \dots, N$$
5. **Complementary Slackness:**
   $$\alpha_i \left[ y_i (\mathbf{w}^T \mathbf{x}_i + b) - 1 \right] = 0, \quad \forall i = 1, \dots, N$$

> [!IMPORTANT]
> **Key Theoretical Insight: The Support Vectors**
> From complementary slackness ($\alpha_i [y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1] = 0$):
> - If $y_i(\mathbf{w}^T \mathbf{x}_i + b) > 1$ (point lies strictly outside margin), then $\alpha_i = 0$. These points contribute nothing to $\mathbf{w}$.
> - If $\alpha_i > 0$, then $y_i(\mathbf{w}^T \mathbf{x}_i + b) = 1$. These critical points lie **directly on the margin boundaries** and are called **Support Vectors**.
> The entire decision boundary is uniquely determined by the support vectors alone! Removing all other non-support training points leaves the optimal hyperplane completely unchanged.

---

### 12.3.4 The Wolfe Dual Optimization Problem
Substituting $\mathbf{w} = \sum \alpha_i y_i \mathbf{x}_i$ and $\sum \alpha_i y_i = 0$ into the primal Lagrangian yields the **Dual Problem**:
$$\max_{\boldsymbol{\alpha}} Q(\boldsymbol{\alpha}) = \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j)$$
$$\text{subject to} \quad \alpha_i \ge 0, \quad \forall i = 1, \dots, N \quad \text{and} \quad \sum_{i=1}^N \alpha_i y_i = 0$$

#### Recovering the Optimal Bias $b$
For any support vector $\mathbf{x}_k$ with $\alpha_k > 0$ ($y_k(\mathbf{w}^T \mathbf{x}_k + b) = 1 \implies \mathbf{w}^T \mathbf{x}_k + b = y_k$ since $y_k \in \{-1, +1\}$):
$$b = y_k - \mathbf{w}^T \mathbf{x}_k = y_k - \sum_{i \in \text{SV}} \alpha_i y_i (\mathbf{x}_i^T \mathbf{x}_k)$$
*(In practice, $b$ is averaged across all support vectors for numerical stability).*

---

## 12.4 Soft-Margin SVM (Non-Separable Data)

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** Lec 57 only mentions the soft margin ("I will not go into the details"). Slack variables, $C$ and the box constraint are not taught.

When data is linearly non-separable or contains noise/outliers, **Slack Variables $\xi_i \ge 0$** are introduced to allow controlled margin violations:
$$y_i (\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0, \quad \forall i = 1, \dots, N$$
- $\xi_i = 0$: Point is correctly classified and outside/on the margin.
- $0 < \xi_i \le 1$: Point is correctly classified but falls within the margin.
- $\xi_i > 1$: Point is misclassified on the wrong side of the hyperplane.

### 12.4.1 Primal Objective with Regularization Parameter $C$
$$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^N \xi_i \quad \text{subject to} \quad y_i (\mathbf{w}^T \mathbf{x}_i + b) \ge 1 - \xi_i, \; \xi_i \ge 0$$
where $C > 0$ is the **regularization trade-off hyperparameter**:
- **Large $C$:** Severe penalty on margin violations $\implies$ narrow margin, fits data aggressively (risk of overfitting).
- **Small $C$:** Tolerates margin violations $\implies$ wider margin, smoother decision boundary (risk of underfitting).

---

### 12.4.2 The Soft-Margin Dual Problem (Box Constraint)
$$\max_{\boldsymbol{\alpha}} \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j) \quad \text{subject to} \quad 0 \le \alpha_i \le C, \quad \forall i \quad \text{and} \quad \sum_{i=1}^N \alpha_i y_i = 0$$

#### Three Regimes of Dual Multipliers:
1. $\alpha_i = 0 \implies \xi_i = 0$: Point is correctly classified outside the margin.
2. $0 < \alpha_i < C \implies \xi_i = 0$: **Free Support Vector** lying exactly on the margin boundary $y_i(\mathbf{w}^T\mathbf{x}_i+b) = 1$. Used to calculate bias $b$.
3. $\alpha_i = C \implies \xi_i > 0$: **Bounded Support Vector** lying inside the margin or misclassified.

---

## 12.5 Non-Linear SVM & The Kernel Trick

### 12.5.1 Mapping to High-Dimensional Feature Space
If data is non-linearly separable in input space $\mathcal{X}$, it is mapped via a non-linear transformation $\Phi: \mathcal{X} \to \mathcal{H}$ into a higher (or infinite) dimensional Hilbert feature space $\mathcal{H}$ where linear separation is achievable.

```
Input Space (Non-Linear)            Feature Space H (Linearly Separable)
       x2 ^                                  Phi(x) ^
          |  - - -                                  |      +   +
          | - +++ -    --[ Mapping Phi(x) ]-->      |    +   +
          | - +++ -                                 |  ------------ (Hyperplane)
          |  - - -                                  |    -   -
          +---------> x1                            +--------->
```

---

### 12.5.2 The Kernel Function & Mercer\'s Theorem
In the dual optimization problem and decision function, feature vectors appear **only as inner products** $\Phi(\mathbf{x}_i)^T \Phi(\mathbf{x}_j)$.
A **Kernel Function $K(\mathbf{x}_i, \mathbf{x}_j)$** computes this inner product directly in input space without ever explicitly evaluating coordinates in $\mathcal{H}$:
$$K(\mathbf{x}_i, \mathbf{x}_j) = \Phi(\mathbf{x}_i)^T \Phi(\mathbf{x}_j) = \langle \Phi(\mathbf{x}_i), \Phi(\mathbf{x}_j) \rangle$$
- **Dual Problem with Kernel:**
  $$\max_{\boldsymbol{\alpha}} \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j K(\mathbf{x}_i, \mathbf{x}_j) \quad \text{subject to} \quad 0 \le \alpha_i \le C, \; \sum \alpha_i y_i = 0$$
- **Kernelized Decision Function:**
  $$f(\mathbf{x}) = \text{sign}\left( \sum_{i \in \text{SV}} \alpha_i y_i K(\mathbf{x}_i, \mathbf{x}) + b \right)$$

#### Mercer\'s Theorem
A symmetric continuous function $K(\mathbf{x}, \mathbf{z})$ is a valid kernel if and only if its **Gram Matrix $\mathbf{K}$** (where $K_{ij} = K(\mathbf{x}_i, \mathbf{x}_j)$) is **Positive Semi-Definite (PSD)** for any finite set of points:
$$\mathbf{c}^T \mathbf{K} \mathbf{c} = \sum_{i=1}^N \sum_{j=1}^N c_i c_j K(\mathbf{x}_i, \mathbf{x}_j) \ge 0, \quad \forall \mathbf{c} \in \mathbb{R}^N$$

---

### 12.5.3 Standard Kernel Functions

| Kernel Name | Mathematical Definition | Key Characteristics & Hyperparameters |
| :--- | :--- | :--- |
| **Linear Kernel** | $K(\mathbf{x}, \mathbf{z}) = \mathbf{x}^T \mathbf{z}$ | Baseline for high-dimensional linearly separable data (e.g., text classification). |
| **Polynomial Kernel** | $K(\mathbf{x}, \mathbf{z}) = (\mathbf{x}^T \mathbf{z} + c)^d$ | Degree $d \in \mathbb{N}$, constant offset $c \ge 0$. Models polynomial feature interactions. |
| **Radial Basis Function (RBF) / Gaussian** | $K(\mathbf{x}, \mathbf{z}) = \exp\left( -\gamma \|\mathbf{x} - \mathbf{z}\|^2 \right) = \exp\left( -\frac{\|\mathbf{x}-\mathbf{z}\|^2}{2\sigma^2}\right)$ | Maps to **infinite-dimensional space**! Parameter $\gamma = \frac{1}{2\sigma^2} > 0$. High $\gamma \implies$ tight island decision boundaries (overfitting); low $\gamma \implies$ overly smooth boundaries (underfitting). |
| **Sigmoid Kernel** | $K(\mathbf{x}, \mathbf{z}) = \tanh(\kappa \mathbf{x}^T \mathbf{z} + c)$ | Derived from neural networks; valid only for specific parameter ranges. |

---

## 12.6 Multi-Class SVM & Support Vector Regression (SVR)

### 12.6.1 Multi-Class Strategies
- **One-vs-Rest (OvR / One-vs-All):** Trains $K$ binary classifiers (Class $k$ vs all other $K-1$ classes). Predicts $\hat{y} = \arg\max_k f_k(\mathbf{x})$.
- **One-vs-One (OvO):** Trains $\binom{K}{2} = \frac{K(K-1)}{2}$ binary classifiers for every pair of classes $(C_i, C_j)$. Final class assigned via majority voting.

### 12.6.2 Support Vector Regression (SVR)

> [!IMPORTANT]
> **Scope (checked against the lecture transcripts):** Lec 60 says SVM regression and ranking were not covered and are left for self-study.
Uses Vapnik\'s **$\epsilon$-Insensitive Loss Function**:
$$L_\epsilon(y, f(\mathbf{x})) = \max(0, |y - f(\mathbf{x})| - \epsilon)$$
Errors smaller than $\epsilon$ inside the \"tube\" around the regression curve are ignored with zero penalty.

---

## 12.7 Step-by-Step Worked Tutorial Problems

### Problem 12.1: Complete Hard-Margin SVM Optimization in 2D
**Statement:** Consider a 2D training set with $N = 3$ data points:
- Point 1: $\mathbf{x}_1 = [1, 1]^T, \quad y_1 = -1$
- Point 2: $\mathbf{x}_2 = [2, 0]^T, \quad y_2 = -1$
- Point 3: $\mathbf{x}_3 = [2, 3]^T, \quad y_3 = +1$

1. Write out the dual objective function $Q(\alpha_1, \alpha_2, \alpha_3)$ and equality constraint.
2. Solve analytically for the optimal Lagrange multipliers $\alpha_1, \alpha_2, \alpha_3$.
3. Compute the optimal weight vector $\mathbf{w}$ and bias $b$.
4. Determine the equation of the separating hyperplane and margin width $\gamma$.
5. Classify a new query point $\mathbf{x}_{\text{query}} = [3, 2]^T$.

**Solution:**
- **Step 1: Compute Dot Products $\mathbf{x}_i^T \mathbf{x}_j$:**
  - $\mathbf{x}_1^T \mathbf{x}_1 = 1^2 + 1^2 = 2$
  - $\mathbf{x}_2^T \mathbf{x}_2 = 2^2 + 0^2 = 4$
  - $\mathbf{x}_3^T \mathbf{x}_3 = 2^2 + 3^2 = 4 + 9 = 13$
  - $\mathbf{x}_1^T \mathbf{x}_2 = (1)(2) + (1)(0) = 2$
  - $\mathbf{x}_1^T \mathbf{x}_3 = (1)(2) + (1)(3) = 2 + 3 = 5$
  - $\mathbf{x}_2^T \mathbf{x}_3 = (2)(2) + (0)(3) = 4$
- **Step 2: Dual Equality Constraint:**
  $$\sum_{i=1}^3 \alpha_i y_i = 0 \implies -\alpha_1 - \alpha_2 + \alpha_3 = 0 \implies \alpha_3 = \alpha_1 + \alpha_2$$
- **Step 3: Formulate Dual Objective Function:**
  $$Q(\boldsymbol{\alpha}) = \alpha_1 + \alpha_2 + \alpha_3 - \frac{1}{2} \sum_{i=1}^3 \sum_{j=1}^3 \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j)$$
  Notice $y_1 y_1 = 1, y_2 y_2 = 1, y_3 y_3 = 1, y_1 y_2 = 1, y_1 y_3 = -1, y_2 y_3 = -1$.
  $$Q = (\alpha_1 + \alpha_2 + (\alpha_1 + \alpha_2)) - \frac{1}{2} \left[ 2\alpha_1^2 + 4\alpha_2^2 + 13\alpha_3^2 + 2(2\alpha_1\alpha_2) - 2(5\alpha_1\alpha_3) - 2(4\alpha_2\alpha_3) \right]$$
  Substitute $\alpha_3 = \alpha_1 + \alpha_2$:
  $$Q = 2\alpha_1 + 2\alpha_2 - \frac{1}{2} \left[ 2\alpha_1^2 + 4\alpha_2^2 + 13(\alpha_1+\alpha_2)^2 + 4\alpha_1\alpha_2 - 10\alpha_1(\alpha_1+\alpha_2) - 8\alpha_2(\alpha_1+\alpha_2) \right]$$
  Expand inside the brackets:
  $$\text{Bracket} = 2\alpha_1^2 + 4\alpha_2^2 + 13(\alpha_1^2 + 2\alpha_1\alpha_2 + \alpha_2^2) + 4\alpha_1\alpha_2 - 10\alpha_1^2 - 10\alpha_1\alpha_2 - 8\alpha_1\alpha_2 - 8\alpha_2^2$$
  Combine terms:
  - $\alpha_1^2 \text{ coeff: } 2 + 13 - 10 = 5$
  - $\alpha_2^2 \text{ coeff: } 4 + 13 - 8 = 9$
  - $\alpha_1\alpha_2 \text{ coeff: } 26 + 4 - 10 - 8 = 12$
  $$\text{Bracket} = 5\alpha_1^2 + 9\alpha_2^2 + 12\alpha_1\alpha_2$$
  $$Q(\alpha_1, \alpha_2) = 2\alpha_1 + 2\alpha_2 - \frac{5}{2}\alpha_1^2 - \frac{9}{2}\alpha_2^2 - 6\alpha_1\alpha_2$$
- **Step 4: Maximize $Q(\alpha_1, \alpha_2)$ via Partial Derivatives:**
  $$\frac{\partial Q}{\partial \alpha_1} = 2 - 5\alpha_1 - 6\alpha_2 = 0 \implies 5\alpha_1 + 6\alpha_2 = 2 \quad \text{--- (Eq. 1)}$$
  $$\frac{\partial Q}{\partial \alpha_2} = 2 - 9\alpha_2 - 6\alpha_1 = 0 \implies 6\alpha_1 + 9\alpha_2 = 2 \implies 2\alpha_1 + 3\alpha_2 = \frac{2}{3} \quad \text{--- (Eq. 2)}$$
  From Eq. 1: $\alpha_1 = \frac{2 - 6\alpha_2}{5}$.
  Substitute into Eq. 2:
  $$6\left(\frac{2 - 6\alpha_2}{5}\right) + 9\alpha_2 = 2 \implies \frac{12 - 36\alpha_2 + 45\alpha_2}{5} = 2 \implies 12 + 9\alpha_2 = 10 \implies 9\alpha_2 = -2 \implies \alpha_2 = -\frac{2}{9}$$
  Since $\alpha_2 < 0$, dual feasibility ($\alpha_i \ge 0$) is violated at the unconstrained stationary point! Thus, the optimum lies on the boundary $\alpha_2 = 0$.
- **Step 5: Boundary Solution ($\alpha_2 = 0$):**
  Setting $\alpha_2 = 0$:
  $$Q(\alpha_1, 0) = 2\alpha_1 - \frac{5}{2}\alpha_1^2 \implies \frac{d Q}{d \alpha_1} = 2 - 5\alpha_1 = 0 \implies \alpha_1 = \frac{2}{5} = 0.40$$
  $$\alpha_3 = \alpha_1 + \alpha_2 = 0.40 + 0 = 0.40$$
  **Optimal Multipliers:**
  $$\alpha_1 = 0.40, \quad \alpha_2 = 0.00, \quad \alpha_3 = 0.40$$
  *(Points $\mathbf{x}_1$ and $\mathbf{x}_3$ are the **Support Vectors**; $\mathbf{x}_2$ is a non-support vector).*
- **Step 6: Compute Optimal Weight Vector $\mathbf{w}$:**
  $$\mathbf{w} = \sum_{i=1}^3 \alpha_i y_i \mathbf{x}_i = \alpha_1 y_1 \mathbf{x}_1 + \alpha_3 y_3 \mathbf{x}_3 = (0.40)(-1)\begin{bmatrix} 1 \\ 1 \end{bmatrix} + (0.40)(+1)\begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
  $$\mathbf{w} = \begin{bmatrix} -0.40 \\ -0.40 \end{bmatrix} + \begin{bmatrix} 0.80 \\ 1.20 \end{bmatrix} = \begin{bmatrix} 0.40 \\ 0.80 \end{bmatrix}$$
- **Step 7: Compute Bias $b$:**
  Using Support Vector $\mathbf{x}_3 = [2, 3]^T$ with $y_3 = +1$:
  $$b = y_3 - \mathbf{w}^T \mathbf{x}_3 = 1 - \left( 0.40(2) + 0.80(3) \right) = 1 - (0.80 + 2.40) = 1 - 3.20 = -2.20$$
  *Verification with SV $\mathbf{x}_1 = [1, 1]^T$ ($y_1 = -1$):*
  $$b = y_1 - \mathbf{w}^T \mathbf{x}_1 = -1 - (0.40(1) + 0.80(1)) = -1 - 1.20 = -2.20 \quad (\text{Exact Match!})$$
- **Step 8: Hyperplane Equation & Margin Width:**
  $$\text{Optimal Hyperplane: } 0.40 x_1 + 0.80 x_2 - 2.20 = 0 \iff x_1 + 2x_2 - 5.5 = 0$$
  $$\|\mathbf{w}\| = \sqrt{0.40^2 + 0.80^2} = \sqrt{0.16 + 0.64} = \sqrt{0.80} \approx 0.8944$$
  $$\text{Geometric Margin } \gamma = \frac{2}{\|\mathbf{w}\|} = \frac{2}{\sqrt{0.80}} = \frac{2}{0.8944} \approx 2.236$$
- **Step 9: Classify Query Point $\mathbf{x}_{\text{query}} = [3, 2]^T$:**
  $$f(\mathbf{x}_{\text{query}}) = \text{sign}(\mathbf{w}^T \mathbf{x}_{\text{query}} + b) = \text{sign}(0.40(3) + 0.80(2) - 2.20) = \text{sign}(1.20 + 1.60 - 2.20) = \text{sign}(+0.60) = +1$$
  *Result:* The query point belongs to **Class $+1$**.
---

## 12.8 Problem Types Commonly Solved in Supervised Classifiers & Support Vector Machines

### Problem Type 12.1: Naive Bayes Classification with Laplace Smoothing
- **Engineering / Exam Scenario:** Given categorical sensor symptoms $x_1, x_2, \dots, x_d$, assign a fault class $C_k$.
- **MAP Rule:** $\hat{y} = \arg\max_{C_k} P(C_k) \prod_{j=1}^d P(x_j \mid C_k)$.
- **Laplace Smoothing:** $\hat{P}(x_j = v \mid C_k) = \frac{N_{kj} + 1}{N_k + V}$.

---

### Problem Type 12.2: Hard-Margin SVM Analytical Solution from 2D Coordinates
- **Step-by-Step Procedure:**
  1. Compute dot products $\mathbf{x}_i^T \mathbf{x}_j$ for all training pairs.
  2. Set up Dual: $\max \sum \alpha_i - \frac{1}{2} \sum \sum \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j)$ subject to $\sum \alpha_i y_i = 0$ and $\alpha_i \ge 0$.
  3. Substitute constraint to eliminate one variable and solve $\frac{\partial Q}{\partial \alpha} = 0$.
  4. If any $\alpha_i < 0$, set to boundary $\alpha_i = 0$ and resolve.
  5. Compute weight vector: $\mathbf{w} = \sum \alpha_i y_i \mathbf{x}_i$.
  6. Compute bias $b = y_k - \mathbf{w}^T \mathbf{x}_k$ using any Support Vector with $\alpha_k > 0$.
  7. Compute margin width $\gamma = \frac{2}{\|\mathbf{w}\|}$ and classify query points via $\text{sign}(\mathbf{w}^T \mathbf{x}_{\text{query}} + b)$.

---

### Problem Type 12.3: Non-Linear Kernel SVM Decision Rule
- **Decision Function:** $f(\mathbf{x}) = \text{sign}\left( \sum_{i \in \text{SV}} \alpha_i y_i K(\mathbf{x}_i, \mathbf{x}) + b \right)$.
- **Gaussian RBF Kernel:** $K(\mathbf{x}_i, \mathbf{x}) = \exp\left( -\gamma \|\mathbf{x}_i - \mathbf{x}\|^2 \right)$.
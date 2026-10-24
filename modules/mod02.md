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

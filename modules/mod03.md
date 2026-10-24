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

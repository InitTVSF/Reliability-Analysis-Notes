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

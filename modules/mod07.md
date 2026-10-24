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

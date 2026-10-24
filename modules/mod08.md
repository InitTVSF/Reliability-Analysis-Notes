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

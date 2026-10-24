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

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

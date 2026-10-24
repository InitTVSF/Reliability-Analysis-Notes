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

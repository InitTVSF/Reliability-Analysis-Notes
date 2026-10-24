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

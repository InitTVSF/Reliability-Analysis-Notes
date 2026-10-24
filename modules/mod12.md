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

# Block 3 Notes: Data Analysis

This revision guide covers the core concepts, statistical frameworks, and analytical techniques from **Units 7 to 12** of MMPM-006. It is designed for quick scanning and high retention on exam day.

---

## Unit 7: Hypothesis Testing

### 1. What is a Hypothesis?
A hypothesis is a **declarative, conjectural statement** about the relationship between two or more variables that can be empirically tested (proven or disproven) using valid and reliable data.
* **Role in MR:** It limits the scope of data collection, preventing the researcher from gathering vast amounts of interesting but irrelevant data. It gives the study clear direction and objectivity.
* **Characteristics of a Good Hypothesis:**
  1. **Simple, clear, and explicit:** Tests one relationship between variables at a time.
  2. **Measurable and quantifiable:** Formulated in terms of variables that can be statistically analyzed.
  3. **Theoretically grounded:** Linked to the existing body of knowledge or market expertise rather than raw intuition.

---

### 2. Null ($H_0$) vs. Alternative ($H_a$ or $H_1$) Hypotheses
* **Null Hypothesis ($H_0$):** A statement of the status quo (no difference, no effect, or equality). It is formulated with the express intention of being **rejected**.
  * *Example:* $H_0: \mu_{\text{Glass}} = \mu_{\text{Plastic}}$ (No difference in consumer packaging preferences).
* **Alternative Hypothesis ($H_a$):** The opposite of the null hypothesis; represents the difference, effect, or relationship that the researcher hopes to support.
  * *Example:* $H_a: \mu_{\text{Glass}} \neq \mu_{\text{Plastic}}$ (Or directional: $H_a: \mu_{\text{Glass}} > \mu_{\text{Plastic}}$).

---

### 3. Decision Errors: Type I and Type II
Because hypothesis testing relies on sample data, there is always a chance of drawing an incorrect conclusion:

| Decision Made | $H_0$ is True in Reality | $H_0$ is False in Reality |
| :--- | :--- | :--- |
| **Reject $H_0$** | **Type I Error ($\alpha$)** | Correct Decision |
| **Fail to Reject $H_0$** | Correct Decision | **Type II Error ($\beta$)** |

* **Type I Error ($\alpha$):** Rejecting the null hypothesis when it is actually true (e.g., launching a plastic container thinking consumers prefer it, when they actually do not).
* **Type II Error ($\beta$):** Failing to reject the null hypothesis when it is actually false (e.g., sticking with glass jars when consumers actually prefer plastic).

> [!IMPORTANT]
> **Significance Level ($\alpha$):** The probability of committing a Type I error. It is set upfront by the researcher (commonly at **5%** or **1%**). A 5% significance level means the researcher is 95% confident that the decision to reject $H_0$ is correct.

---

### 4. The 8 Steps in the Hypothesis Testing Process
1. **Identify the Broad Problem Area:** e.g., Sales of organic produce are declining.
2. **Define the Problem Statement / Research Objectives:** Define what information is needed.
3. **Develop Null and Alternative Hypotheses:** Formulate $H_0$ and $H_a$.
4. **Select an Appropriate Statistical Technique:** Choose parametric (e.g., t-test, ANOVA) or non-parametric (e.g., Chi-square) tests based on data type and assumptions.
5. **Decide the Level of Significance ($\alpha$):** Typically set to 5% or 1%.
6. **Data Collection:** Collect sample data.
7. **Data Analysis:** Run the statistical test (e.g., using SPSS) to compute the test statistic and p-value.
8. **Interpretation of Data:** If the p-value is less than $\alpha$, reject $H_0$ and accept $H_a$. Otherwise, fail to reject $H_0$. Provide recommendations to decision-makers.

---

## Unit 8 & 9: Bivariate & Multiple Regression Analysis

### 1. Differentiating Correlation and Regression
* **Correlation:** Measures the **strength and direction of the linear association** between two variables. It does not imply causation (e.g., Price vs. Sales).
  * *Karl Pearson's Coefficient ($r$):* Used for interval/ratio data. Ranges from $-1$ to $+1$.
  * *Spearman's Rank Correlation ($r_s$):* Used for ordinal (ranked) data.
* **Regression:** Models the **relationship** between a dependent variable ($Y$) and one or more independent variables ($X$) to predict or forecast outcomes.
  * *Simple Linear Regression:* $Y = \beta_0 + \beta_1 X + e$ (one predictor).
  * *Multiple Regression:* $Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_n X_n + e$ (multiple predictors).

> [!TIP]
> **Applications of Correlation:** Evaluating brand awareness vs. ad spend, price levels vs. purchase frequency, or employee responsiveness vs. customer satisfaction ratings.

---

## Unit 10: Discriminant Analysis vs. Logistic Regression

Both methods predict group membership for a categorical dependent variable based on a set of predictor variables.

* **Discriminant Analysis:** Used when the dependent variable is categorical and the population is **normally distributed** with equal variances.
* **Logistic Regression:** Used when the dependent variable is categorical, but **does not require normality** or linear assumptions.
  * *Formula:* Estimates the probability ($p$) of an event occurring: $p = \frac{e^y}{1 + e^y}$.
  * *Dependent Variable:* Binary (0 or 1) and obeys the **Bernoulli Distribution**.
  * *Estimation Method:* Uses **Maximum Likelihood Estimation (MLE)** instead of Ordinary Least Squares (OLS).

### Assumptions of Binary Logistic Regression:
1. **Binary Dependent Variable:** The outcome variable must have only two categories (e.g., Buy vs. Not Buy).
2. **No Multicollinearity:** Independent variables must be independent of one another.
3. **Linearity of Log-Odds:** The relationship between continuous independent variables and the log-odds of the dependent variable must be linear.

---

## Unit 11: Factor Analysis & Cluster Analysis

### 1. Factor Analysis (Data Reduction)
* **Purpose:** A mathematical technique used for **data reduction and summarization**. It identifies underlying, unobserved dimensions (factors) that explain the correlations among a large set of observed variables.
* **How it helps interpret results:** It groups highly correlated variables into single factors, making it easier to name the factors (e.g., grouping "friendliness," "speed," and "helpfulness" into a single factor called "Service Quality") and construct simpler statistical models.
* **Limitations:** Highly sensitive to sample changes and measurement errors. Factor naming can be highly subjective.

---

### 2. Cluster Analysis (Market Segmentation)
* **Purpose:** A grouping technique used to classify objects (consumers, brands, countries) into clusters. 
* **Core Rule:** Maximize **homogeneity (similarity) within clusters** and maximize **heterogeneity (difference) between clusters**.
* **Marketing Applications:** 
  * **Market Segmentation:** Grouping consumers based on similar needs, benefits sought, or price sensitivity (e.g., segmenting travelers into "adventure seekers," "budget families," or "luxury tourists").
  * **Targeting & Positioning:** Tailoring marketing programs to fit specific clusters or choosing a niche.
* **Approaches:** Can cluster based on demographic data (price, age) or psychographic needs (attitudes, occasions of use). Conceptual sense should guide variable selection.

---

## Unit 12: Conjoint Analysis vs. Multidimensional Scaling (MDS)

Both are advanced multivariate techniques that capture consumer trade-offs and perceptions.

### 1. Conjoint Analysis (Trade-off Analysis)
* **What it is:** A decompositional technique that measures the **joint effect of product attributes** on consumer preferences. It calculates **part-worth utilities** (importance weights) for each level of an attribute.
* **How it works:** The researcher designs hypothetical product profiles (e.g., combinations of price, brand, capacity). Consumers rate/rank the whole profile. The algorithm decomposes these rankings to show which attributes they value most and what trade-offs they will make.
* **Applications:** Optimal product design, pricing strategies, and market share simulation.

---

### 2. Multidimensional Scaling (MDS)
* **What it is:** A technique that maps consumer perceptions and preferences of competing brands in a **multidimensional perceptual space**. 
* **Key Concept:** Attribute space is divided into **objective space** (physical product specs) and **perceived space** (how consumers actually visualize the brand).
* **MDS vs. Conjoint:** In MDS, the stimuli are **existing real brands** evaluated on overall similarity. In Conjoint, the stimuli are **hypothetical profiles pre-designed by the researcher**.

---

### Key Summary: MDS vs. Conjoint Analysis

| Feature | Multidimensional Scaling (MDS) | Conjoint Analysis |
| :--- | :--- | :--- |
| **Primary Goal** | Map brand positions in the **perceptual space** of consumers to identify dimensions. | Measure the **importance and utility** of individual attributes and levels (part-worths). |
| **Stimuli Used** | Real, existing brands/products. | Hypothetical profiles constructed by varying attribute levels. |
| **Attribute Input** | Identified **post-hoc** from the derived spatial dimensions. | Selected and defined **a-priori** by the researcher. |
| **Output Type** | Visual perceptual map showing relative brand distances. | Table of part-worth utilities and relative importance weights. |

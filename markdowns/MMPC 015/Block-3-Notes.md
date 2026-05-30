# MMPC-015: Research Methodology for Management Decisions
## Block 3: Data Presentation and Analysis — Revision Notes

---

### UNIT 8: DATA PROCESSING

#### 1. Concept of Data Processing
Data processing is the transition stage between data collection and data analysis. It involves transforming raw, unorganized field data into a clean, structured, and systematic format suitable for statistical testing.

#### 2. Key Steps in Data Processing
1.  **Editing of Data:**
    *   *Purpose:* To identify and eliminate errors, omissions, inconsistencies, and illegible responses in the collected questionnaires.
    *   *Field Editing:* Done by the investigator in the field immediately after the interview to clarify vague notes or complete blank entries while the memory is fresh.
    *   *Central Editing:* Conducted in the research office. It involves exhaustive checking, correcting obvious errors (e.g., matching inconsistent answers like *"Age: 5"* and *"Occupation: Doctor"*), and discarding highly incomplete forms.
2.  **Coding of Data:**
    *   *Purpose:* Assigning numerical symbols or codes to responses so they can be processed by computers.
    *   *Closed-ended Questions:* Simple to code prior to collection (e.g., Yes = 1, No = 2).
    *   *Open-ended Questions:* Coded post-collection by reviewing a subset of forms, grouping similar qualitative answers into distinct classes, and assigning numerical codes.
3.  **Classification of Data:**
    *   *Purpose:* Sorting vast amounts of data into homogeneous groups based on common characteristics.
    *   *Types of Classification:*
        *   *Geographical (Spatial):* Sorted by location (e.g., North, South, East, West).
        *   *Chronological (Temporal):* Sorted by time sequence (e.g., monthly sales, annual profits).
        *   *Qualitative (Descriptive):* Sorted by attributes (e.g., gender, literacy, occupation).
        *   *Quantitative (Numerical):* Sorted by intervals of numerical values (e.g., income classes: $0-10k, $10k-20k).
4.  **Tabulation of Data:**
    *   *Purpose:* Arranging classified data systematically into rows and columns.
    *   *Significance:* It simplifies data comparison, saves space, facilitates mathematical calculations, and acts as the foundation for charts and graphs.
    *   *Components of a Good Table:* Title, Captions (column headings), Stubs (row headings), Body (data cells), Headnote (units of measurement), and Source Note.

#### 3. Graphical Presentation of Data
Graphs provide an immediate visual summary of trends and comparisons:
*   **Bar Charts:** Uses rectangular bars to compare discrete categories. Can be simple, multiple (comparing two series), or component/subdivided (showing internal splits).
*   **Line or Arithmetic Charts:** Plotted on coordinate axes to show changes or trends in a series over time (e.g., monthly export sales).
*   **Pie Charts:** Circles divided into sectors to represent each component's percentage contribution to a whole (e.g., cost breakdown). Angle is calculated as: $\text{Angle} = \text{Percentage} \times 3.6^\circ$.

---

### UNIT 9: STATISTICAL ANALYSIS AND INTERPRETATION OF DATA: NONPARAMETRIC TESTS

#### 1. Parametric vs. Nonparametric Tests
| Feature | Parametric Tests | Nonparametric (Distribution-Free) Tests |
| :--- | :--- | :--- |
| **Population Distribution** | Assumes the population follows a known distribution (typically a normal distribution). | Makes **no rigid assumptions** about the shape of the population distribution. |
| **Measurement Scale** | Requires high-level scales: **Interval or Ratio** (e.g., actual age, temperature). | Works perfectly with lower scales: **Nominal or Ordinal** (e.g., ranks, satisfaction ratings). |
| **Parameters** | Focuses directly on population parameters (e.g., population mean $\mu$, variance $\sigma^2$). | Tests hypotheses about overall distributions or medians rather than specific parameters. |
| **Sample Size** | Demands larger samples to ensure central limit theorem holds. | Highly effective even for **very small samples**. |
| **Statistical Power** | More powerful *if* assumptions are met (lower chance of Type II error). | Less powerful than parametric tests when parametric assumptions actually hold. |
| **Examples** | $t$-test, $F$-test (ANOVA), $Z$-test. | Sign Test, Runs Test, Chi-square Goodness-of-Fit, Mann-Whitney $U$-test. |

#### 2. Key Advantages and Limitations of Nonparametric Tests
*   **Advantages:**
    *   *Fewer Assumptions:* Highly robust and realistic for social and market research where normality is rare.
    *   *Handles Ranked/Nominal Data:* The only choice when data consists of preferences, ranks, or names.
    *   *Simple Computation:* Involves fewer mathematical operations, making them faster to calculate by hand.
    *   *Handles Incomplete Data:* Can absorb missing values through ranking adjustments.
*   **Limitations:**
    *   *Loss of Power:* Higher risk of accepting a false null hypothesis (Type II error) if parametric tests could have been used.
    *   *Vague Conclusions:* Rejection of the null hypothesis in a parametric test tells you *means are unequal*. Rejection in a nonparametric test only tells you *distributions are different*, without specifying the exact nature of the difference.

#### 3. Core Nonparametric Tests: Formulas and Step-by-Step Logic
For exam revision, here is the structured logic of the four critical nonparametric tests:

##### A. One-Sample Sign Test (Testing hypothesized median $\mu_0$)
*   *Concept:* Replaces the one-sample $t$-test when normality is violated. Tests if the sample median is equal to a hypothesized value $\mu_0$.
*   *Method:*
    1.  Subtract $\mu_0$ from each sample value.
    2.  Replace positive differences with a plus ($+$) sign and negative differences with a minus ($-$) sign. Discard zero differences.
    3.  Under $H_0$, the probability of getting a plus sign is $p = 0.5$.
    4.  *For small samples ($n \le 20$):* Use binomial expansion to find the probability of obtaining observed successes.
    5.  *For large samples ($n > 20$):* Use the normal approximation to the binomial distribution:
        $$Z = \frac{X - n/2}{\sqrt{n}/2}$$
        *(where $X$ is the number of plus signs, and $n$ is the total trials. Apply continuity correction if required).*

##### B. Runs Test for Randomness (Testing independence of sequence)
*   *Concept:* Checks if the order or sequence in which data was collected is random or biased (too many or too few runs indicate non-randomness).
*   *Run Definition:* A sequence of identical symbols followed and preceded by different symbols (e.g., $M\ M\ F\ F\ F\ M$ has 3 runs).
*   *Method:*
    1.  Count $n_1$ (number of element type 1), $n_2$ (number of element type 2), and $r$ (total runs observed).
    2.  *For large samples ($n_1$ or $n_2 > 20$):* R behaves as a normal distribution:
        $$\text{Mean } E(r) = \frac{2n_1n_2}{n_1+n_2} + 1$$
        $$\text{Standard Deviation } \sigma_r = \sqrt{\frac{2n_1n_2(2n_1n_2 - n_1 - n_2)}{(n_1+n_2)^2(n_1+n_2-1)}}$$
        $$Z = \frac{r - E(r)}{\sigma_r}$$
    3.  Compare calculated $Z$ with critical $Z$ (e.g., $1.96$ at 5% significance level).

##### C. Chi-Square ($\chi^2$) Goodness-of-Fit Test
*   *Concept:* Tests whether a significant difference exists between observed frequency distribution ($O_i$) and expected frequency distribution ($E_i$) across categories.
*   *Formula:*
    $$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$$
*   *Degrees of Freedom:* $df = k - 1$ (where $k$ is the number of categories).
*   *Decision Rule:* Reject $H_0$ if calculated $\chi^2 > \text{tabular } \chi^2$ value.

##### D. Mann-Whitney U-Test (Two independent samples)
*   *Concept:* Nonparametric alternative to the independent two-sample $t$-test. Determines if two independent groups belong to the same population.
*   *Method:*
    1.  Combine both samples and rank all observations from smallest ($1$) to largest ($n_1 + n_2$).
    2.  Sum the ranks of the first group ($R_1$) and the second group ($R_2$).
    3.  Calculate the $U$ statistic:
        $$U_1 = n_1n_2 + \frac{n_1(n_1+1)}{2} - R_1$$
        $$U_2 = n_1n_2 + \frac{n_2(n_2+1)}{2} - R_2$$
    4.  The test statistic is the smaller of $U_1$ and $U_2$. Compare it to critical values or use normal approximation for large samples.

---

### UNIT 10: MULTIVARIATE ANALYSIS OF DATA

#### 1. Regression Analysis
*   **Concept:** Used to determine the mathematical relationship between a dependent variable ($Y$) and one or more independent variables ($X$).
*   **Line of Regression of Y on X:** Represents the best-fit line predicting $Y$ based on values of $X$.
    $$Y = a + bX$$
    *   *Where:* $a$ is the intercept, and $b$ is the **regression coefficient** representing the rate of change of $Y$ per unit change in $X$.
*   **Calculation of Regression Coefficient ($b$):**
    $$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2}$$
    Once $b$ is found, the intercept $a$ is calculated as: $a = \bar{Y} - b\bar{X}$.

#### 2. Discriminant Analysis
*   **Concept:** A multivariate classification technique used when the dependent variable is categorical (e.g., Default vs. Non-default, Buyer vs. Non-buyer) and the independent variables are continuous.
*   **Objective:** To find a linear combination of predictor variables (the discriminant function) that best discriminates or separates the groups.
*   *Example:* Predict whether a bank customer will default on a loan based on their income, credit score, age, and existing debt.

#### 3. Factor Analysis
*   **Concept:** A data-reduction technique used to reduce a large number of interrelated variables into a much smaller number of unobserved latent factors.
*   **Visual Analogy:** If you have 20 variables measuring different features of a smartphone (screen size, RAM, battery life, camera megapixels, weight, processor speed, etc.), Factor Analysis might group them into 3 core latent factors:
    1.  *Performance* (RAM, Processor, RAM)
    2.  *Aesthetics* (Weight, Screen design)
    3.  *Utility* (Battery, Camera)
*   **Significance:** Simplifies subsequent statistical analysis, eliminates multicollinearity, and helps identify underlying consumer perception dimensions.

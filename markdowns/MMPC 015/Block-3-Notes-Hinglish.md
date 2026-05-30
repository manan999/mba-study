# MMPC-015: Research Methodology for Management Decisions
## Block 3: Data Presentation and Analysis — Hinglish Revision Notes

---

### UNIT 8: DATA PROCESSING

#### 1. Concept of Data Processing
Data processing data collection aur data analysis ke beech ki stage hai. Iska main objective raw, unorganized field data ko clean, error-free, aur structured format me convert karna hai taaki uspar standard statistical tests lagaye ja sakein.

#### 2. Key Steps in Data Processing
1.  **Editing of Data:**
    *   *Goal:* Questionnaires me se errors, missing details, aur inconsistencies (befizool answers) ko identify karke clean karna.
    *   *Field Editing:* Interviewer field me hi turant questionnaire check karke short notes ko details me convert karta hai aur blank fields ko fill karta hai jab tak respondents ki memory fresh ho.
    *   *Central Editing:* Research office me exhaustively kiya jata hai. Inconsistent answers (e.g., *"Age: 5"* aur *"Occupation: Bank Manager"*) ko correct kiya jata hai aur kafi zyada incomplete forms ko discard kar diya jata hai.
2.  **Coding of Data:**
    *   *Goal:* Responses ko numerical symbols/numbers dena taaki computer software unhe identify kar sake.
    *   *Closed-ended Questions:* Pre-coded hote hain collection se pehle (e.g., Male = 1, Female = 2).
    *   *Open-ended Questions:* Survey ke baad codes diye jaate hain. Ek sub-sample review karke similar qualitative answers ke distinct groups banaye jaate hain aur unhe numbers assign kiye jaate hain.
3.  **Classification of Data:**
    *   *Goal:* Pura data mass homogeneous (ek jaise) groups me segment karna.
    *   *Classification Types:*
        *   *Geographical (Spatial):* Region ke basis par divide karna (e.g., Metro cities, Rural areas).
        *   *Chronological (Temporal):* Time patterns ke basis par divide karna (e.g., annual, monthly sales).
        *   *Qualitative (Descriptive):* Attributes ke basis par divide karna (e.g., marital status, education level).
        *   *Quantitative (Numerical):* Numerical values ke ranges par divide karna (e.g., Income slabs like $0-10k, $10k-20k).
4.  **Tabulation of Data:**
    *   *Goal:* Classified data ko systematic rows aur columns me present karna.
    *   *Significance:* Data comparison ko easy banata hai, space save karta hai, math calculations me support karta hai, aur graphs/charts ka base banta hai.
    *   *Components of a Good Table:* Title, Captions (column headings), Stubs (row headings), Body (actual numbers), Headnote (units of measurement), aur Source Note.

#### 3. Graphical Presentation of Data
Graphs data trends ko eye-catching aur easy to understand banate hain:
*   **Bar Charts:** Rectangular bars ke through discrete categories ko compare karna. Simple bar chart, multiple bar chart (do series comparisons), ya component/subdivided bar chart (internal category breakdown) ho sakte hain.
*   **Line or Arithmetic Charts:** X-Y axis par trends aur patterns ko show karna over time (e.g., annual profit trend).
*   **Pie Charts:** Circular structure jahan sectors percentage contribution to a whole show karte hain. Angle calculation formula: $\text{Angle} = \text{Percentage} \times 3.6^\circ$.

---

### UNIT 9: STATISTICAL ANALYSIS AND INTERPRETATION OF DATA: NONPARAMETRIC TESTS

#### 1. Parametric vs. Nonparametric Tests
| Feature | Parametric Tests | Nonparametric (Distribution-Free) Tests |
| :--- | :--- | :--- |
| **Population Distribution** | Population ka standard distribution model assume karta hai (usually Normal Distribution). | Population distribution ka koi rigid assumption nahi hota (Distribution-Free). |
| **Measurement Scale** | Hamesha high-level scales: **Interval or Ratio** use karta hai (e.g., age, weight). | Lower-level scales: **Nominal or Ordinal** ke sath best perform karta hai (e.g., ranks, satisfaction rate). |
| **Parameters** | Population parameters ke testing par direct focus karta hai (e.g., mean $\mu$, variance $\sigma^2$). | Parameters ke bajaye overall distribution identity ya median test karta hai. |
| **Sample Size** | Central Limit Theorem ke validation ke liye badhe samples mangta hai. | **Chote samples** (small sample sizes) par bhi effectively work karta hai. |
| **Statistical Power** | Agar assumptions valid hon, toh iski statistical power sabse zyada hoti hai. | Parametric tests se statistical power thodi kam hoti hai (Type II error ka chance zyada hota hai). |
| **Examples** | $t$-test, $F$-test (ANOVA), $Z$-test. | Sign Test, Runs Test, Chi-square Goodness-of-Fit, Mann-Whitney $U$-test. |

#### 2. Key Advantages and Limitations of Nonparametric Tests
*   **Advantages (Hinglish):**
    *   *No Normality Requirement:* Social science aur management research me normally distributed data milna mushkil hota hai, wahan yeh highly robust hai.
    *   *Ranked Data Friendly:* Agar data preferences ya ranks me hai, toh parametric tests lag hi nahi sakte.
    *   *Easy Calculations:* Isme mathematical operations kam hote hain, manually fast calculate hota hai.
    *   *Handles Missing Values:* Ranks adjustments ke through gaps absorb ho jaate hain.
*   **Limitations (Hinglish):**
    *   *Statistical Power Loss:* Agar parametric assumptions valid hain, toh nonparametric test use karne se false null hypothesis accept hone ka risk badh jata hai.
    *   *Vague Conclusions:* Parametric test bata sakta hai ki *"means directly unequal hain"*. Nonparametric test sirf batata hai ki *"distributions different hain"*, par kya difference hai, yeh details me nahi batata.

#### 3. Core Nonparametric Tests: Formulas and Step-by-Step Logic

##### A. One-Sample Sign Test (Testing hypothesized median $\mu_0$)
*   *Concept:* Normality violate hone par one-sample $t$-test ko replace karta hai. Median $\mu_0$ ke test ke liye use hota hai.
*   *Method:*
    1.  Har sample element se hypothesized median value $\mu_0$ ko subtract karein.
    2.  Positive difference ko ($+$) sign aur negative difference ko ($-$) sign dein. Zero values ko drop kar dein.
    3.  Under $H_0$, plus sign aane ka probability $p = 0.5$ hota hai.
    4.  *For small samples ($n \le 20$):* Binomial probabilities chart/table check karein.
    5.  *For large samples ($n > 20$):* Normal approximation algorithm laga kar $Z$-score calculate karein:
        $$Z = \frac{X - n/2}{\sqrt{n}/2}$$
        *(jahan $X$ plus signs ka count hai, aur $n$ total trials count hai).*

##### B. Runs Test for Randomness (Testing independence of sequence)
*   *Concept:* Data collection sequence random aur unbiased hai ya nahi, yeh check karne ke liye run patterns match karta hai.
*   *Run Definition:* Identical symbols ka sequence jo different symbols se separated ho (e.g., $M\ M\ F\ F\ F\ M$ has 3 runs).
*   *Method:*
    1.  Check karein $n_1$ (element type 1 count), $n_2$ (element type 2 count), aur $r$ (total runs count).
    2.  *For large samples ($n_1$ ya $n_2 > 20$):* normal curve approximation formula lagayein:
        $$\text{Mean } E(r) = \frac{2n_1n_2}{n_1+n_2} + 1$$
        $$\text{Standard Deviation } \sigma_r = \sqrt{\frac{2n_1n_2(2n_1n_2 - n_1 - n_2)}{(n_1+n_2)^2(n_1+n_2-1)}}$$
        $$Z = \frac{r - E(r)}{\sigma_r}$$
    3.  Calculated $Z$ ko critical $Z$ value ($1.96$ at 5% significance) se compare karein.

##### C. Chi-Square ($\chi^2$) Goodness-of-Fit Test
*   *Concept:* Check karta hai ki category frequency ka observed data ($O_i$) expected frequencies ($E_i$) ke ratio se statistically deviate toh nahi kar raha.
*   *Formula:*
    $$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$$
*   *Degrees of Freedom:* $df = k - 1$ (jahan $k$ categories count hai).
*   *Decision:* Agar Calculated $\chi^2 > \text{Tabular } \chi^2$ value, toh Null Hypothesis ($H_0$) reject ho jayegi.

##### D. Mann-Whitney U-Test (Two independent samples)
*   *Concept:* Nonparametric independent two-sample $t$-test alternative. Do independent groups same population se belong karte hain ya nahi, yeh check karta hai.
*   *Method:*
    1.  Dono groups ko combine karke dynamic ranks (smallest to largest) dein.
    2.  Group 1 ranks sum ($R_1$) aur Group 2 ranks sum ($R_2$) calculate karein.
    3.  $U$ statistic calculate karein:
        $$U_1 = n_1n_2 + \frac{n_1(n_1+1)}{2} - R_1$$
        $$U_2 = n_1n_2 + \frac{n_2(n_2+1)}{2} - R_2$$
    4.  Test value $U$ smaller component ($U_1$ or $U_2$) hota hai. Large sample size par Normal curve check standard use karein.

---

### UNIT 10: MULTIVARIATE ANALYSIS OF DATA

#### 1. Regression Analysis
*   **Concept:** Ek dependent variable ($Y$) aur ek ya usse zyada independent variables ($X$) ke mathematical relationship coordinate formula se determine karta hai.
*   **Line of Regression of Y on X:** predict $Y$ coordinates based on $X$ values.
    $$Y = a + bX$$
    *   *Jahan:* $a$ vertical axis intercept hai, aur $b$ **regression coefficient** hai jo change in $Y$ per unit change in $X$ show karta hai.
*   **Calculation of Regression Coefficient ($b$):**
    $$b = \frac{n\sum XY - \sum X \sum Y}{n\sum X^2 - (\sum X)^2}$$
    Once $b$ calculate ho jaye, intercept value $a = \bar{Y} - b\bar{X}$ se nikalti hai.

#### 2. Discriminant Analysis
*   **Concept:** Multivariate classification design jahan dependent variable categorical hota hai (e.g., Default vs No-default, Buyer vs Non-buyer) aur predictor variables continuous numeric scale par hote hain.
*   **Objective:** Ek linear baseline equation banana jo categories ke separation boundary parameters mathematically divide kar sake.
*   *Example:* Predict karna ki kaun sa bank user credit card default karega based on income, debt scale, age, aur credit history variables.

#### 3. Factor Analysis
*   **Concept:** Data reduction framework jiske under inter-correlated variables ko combine karke thode latent (hidden) factors me collapse kiya jata hai.
*   **Visual Analogy (Hinglish):** Agar aapke paas mobile features ke 20 variables hain (RAM size, clock speed, display screen size, physical design weight, megapixels etc.), toh Factor Analysis algorithm unhe 3 primary factors me condense kar dega:
    1.  *Performance factor* (Processor speed, RAM capacity)
    2.  *Design aesthetics* (Body weight, screen width)
    3.  *Utility value* (Battery mAh, megapixel counts)
*   **Significance:** Multicollinearity (correlation overlap) eliminate karta hai, structural analysis easy banata hai, aur core consumer design dimensions discover karta hai.

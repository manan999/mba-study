# Block 3 Notes (Hinglish): Data Analysis

Yeh revision guide MMPM-006 ke **Units 7 se 12** ke core concepts, statistical frameworks, aur analytical techniques ko cover karti hai. Isko exam day par jaldi se scan aur revise karne ke liye design kiya gaya hai.

---

## Unit 7: Hypothesis Testing

### 1. Hypothesis kya hai?
Hypothesis ek **declarative, conjectural statement** (pehle se socha gaya bayan) hota hai jo do ya do se zyada variables ke beech ke relationship ko batata hai. Ise valid aur reliable data ke zariye empirically test (sahi ya galat prove) kiya ja sakta hai.
* **MR mein iska Role:** Yeh data collection ke scope ko limit karta hai, taaki researcher faltu ya irrelevant data gather na kare. Yeh study ko ek clear direction aur objectivity deta hai.
* **Ek acchi Hypothesis ki characteristics:**
  1. **Simple, clear, aur explicit:** Ek baar mein variables ke beech ke sirf ek relationship ko test karti hai.
  2. **Measurable aur quantifiable:** Aise variables ke terms mein bani ho jinka statistical analysis kiya ja sake.
  3. **Theoretically grounded:** Kisi existing knowledge ya market expertise par based honi chahiye, na ki sirf andaze par.

---

### 2. Null ($H_0$) vs. Alternative ($H_a$ ya $H_1$) Hypotheses
* **Null Hypothesis ($H_0$):** Status quo (koi difference nahi, koi effect nahi, ya barabari) ka statement hota hai. Ise hamesha **reject** karne ke intention se banaya jata hai.
  * *Example:* $H_0: \mu_{\text{Glass}} = \mu_{\text{Plastic}}$ (Consumer packaging preferences mein koi farq nahi hai).
* **Alternative Hypothesis ($H_a$):** Null hypothesis ka opposite hota hai; yeh us difference, effect, ya relationship ko represent karta hai jise researcher support karna chahta hai.
  * *Example:* $H_a: \mu_{\text{Glass}} \neq \mu_{\text{Plastic}}$ (Ya directional: $H_a: \mu_{\text{Glass}} > \mu_{\text{Plastic}}$).

---

### 3. Decision Errors: Type I aur Type II
Kyunki hypothesis testing sample data par depend karti hai, isliye galat conclusion nikalne ka chance hamesha rehta hai:

| Decision Made | Reality mein $H_0$ True hai | Reality mein $H_0$ False hai |
| :--- | :--- | :--- |
| **Reject $H_0$** | **Type I Error ($\alpha$)** | Correct Decision |
| **Fail to Reject $H_0$** | Correct Decision | **Type II Error ($\beta$)** |

* **Type I Error ($\alpha$):** Null hypothesis ko reject kar dena jabki woh reality mein true ho (e.g., yeh soch kar plastic container launch kar dena ki consumers use pasand karte hain, jabki real mein woh pasand nahi karte).
* **Type II Error ($\beta$):** Null hypothesis ko reject na kar paana jabki woh reality mein false ho (e.g., glass jars hi bechte rehna jabki reality mein consumers plastic prefer karte hain).

> [!IMPORTANT]
> **Significance Level ($\alpha$):** Type I error hone ki probability. Ise researcher pehle hi set karta hai (usually **5%** ya **1%**). 5% significance level ka matlab hai ki researcher 95% confident hai ki $H_0$ ko reject karne ka decision correct hai.

---

### 4. Hypothesis Testing Process ke 8 Steps
1. **Identify the Broad Problem Area:** e.g., Organic food ki sales kam ho rahi hain.
2. **Problem Statement / Research Objectives Define karna:** Pata lagana ki kaunsi information chahiye.
3. **Null aur Alternative Hypotheses banana:** $H_0$ aur $H_a$ formulate karna.
4. **Appropriate Statistical Technique select karna:** Data type aur assumptions ke basis par parametric (t-test, ANOVA) ya non-parametric (Chi-square) tests select karna.
5. **Level of Significance ($\alpha$) decide karna:** Usually 5% ya 1%.
6. **Data Collection:** Sample data collect karna.
7. **Data Analysis:** Statistical test run karna (SPSS ke zariye) aur test statistic & p-value nikalna.
8. **Interpretation of Data:** Agar p-value $\alpha$ se kam hai, toh $H_0$ ko reject karein aur $H_a$ ko accept karein. Agar p-value $\alpha$ se badi hai, toh $H_0$ ko reject na karein. Phir managers ko recommendations dein.

---

## Unit 8 & 9: Bivariate & Multiple Regression Analysis

### 1. Correlation aur Regression mein farq
* **Correlation:** Do variables ke beech ke linear association ki **strength aur direction** ko measure karta hai. Iska matlab cause-and-effect nahi hota (e.g., Price vs. Sales).
  * *Karl Pearson's Coefficient ($r$):* Interval/ratio data ke liye use hota hai. Iski range $-1$ se $+1$ hoti hai.
  * *Spearman's Rank Correlation ($r_s$):* Ordinal (ranked) data ke liye use hota hai.
* **Regression:** Dependent variable ($Y$) aur ek ya ek se zyada independent variables ($X$) ke beech ke **relationship** ko model karta hai taaki outcomes ko predict kiya ja sake.
  * *Simple Linear Regression:* $Y = \beta_0 + \beta_1 X + e$ (ek predictor).
  * *Multiple Regression:* $Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_n X_n + e$ (multiple predictors).

> [!TIP]
> **Correlation ke Applications:** Brand awareness vs. ad spend, price levels vs. purchase frequency, ya employee behavior vs. customer satisfaction ratings ko evaluate karna.

---

## Unit 10: Discriminant Analysis vs. Logistic Regression

Dono methods predictor variables ke basis par categorical dependent variable ke liye group membership ko predict karte hain.

* **Discriminant Analysis:** Tab use hota hai jab dependent variable categorical ho aur population **normally distributed** ho with equal variances.
* **Logistic Regression:** Tab use hota hai jab dependent variable categorical ho, par ismein **normality** ya linear assumptions ki zaroorat **nahi** hoti.
  * *Formula:* Event hone ki probability ($p$) estimate karta hai: $p = \frac{e^y}{1 + e^y}$.
  * *Dependent Variable:* Binary (0 ya 1) hota hai aur **Bernoulli Distribution** follow karta hai.
  * *Estimation Method:* Ordinary Least Squares (OLS) ke bajaye **Maximum Likelihood Estimation (MLE)** ka use karta hai.

### Binary Logistic Regression ke Assumptions:
1. **Binary Dependent Variable:** Outcome variable ke paas sirf do hi categories honi chahiye (e.g., Buy vs. Not Buy).
2. **No Multicollinearity:** Independent variables ek doosre se independent hone chahiye.
3. **Linearity of Log-Odds:** Continuous independent variables aur dependent variable ke log-odds ke beech ka relationship linear hona chahiye.

---

## Unit 11: Factor Analysis & Cluster Analysis

### 1. Factor Analysis (Data Reduction)
* **Purpose:** Yeh ek mathematical technique hai jo **data reduction aur summarization** ke liye use hoti hai. Yeh bade set of variables ke beech ke correlations ko samjhane ke liye underlying, unobserved dimensions (factors) ko identify karti hai.
* **Results interpret karne mein kaise help karta hai:** Yeh highly correlated variables ko single factors mein group kar deta hai, jisse factors ko name dena easy ho jata hai (jaise "friendliness," "speed," aur "helpfulness" ko "Service Quality" factor mein group karna) aur statistical models simple ho jate hain.
* **Limitations:** Sample changes aur measurement errors ke liye bohot sensitive hota hai. Factor naming subjective ho sakti hai.

---

### 2. Cluster Analysis (Market Segmentation)
* **Purpose:** Objects (consumers, brands, countries) ko groups ya clusters mein classify karne ki grouping technique hai.
* **Core Rule:** Clusters ke andar **homogeneity (similarity) maximum** honi chahiye aur clusters ke beech **heterogeneity (difference) maximum** honi chahiye.
* **Marketing Applications:**
  * **Market Segmentation:** Consumers ko unki similar needs, benefits sought, ya price sensitivity ke basis par group karna (jaise travelers ko "adventure seekers," "budget families," ya "luxury tourists" mein segment karna).
  * **Targeting & Positioning:** Specific clusters ke according marketing programs design karna.
* **Approaches:** Demographics (price, age) ya psychographics (attitudes, occasions) ke basis par clustering ki ja sakti hai. Variable selection mein conceptual sense hona zaroori hai.

---

## Unit 12: Conjoint Analysis vs. Multidimensional Scaling (MDS)

Dono hi consumer trade-offs aur perceptions ko capture karne ki advanced multivariate techniques hain.

### 1. Conjoint Analysis (Trade-off Analysis)
* **Yeh kya hai:** Ek decompositional technique hai jo consumer preferences par **product attributes ke joint effect** ko measure karti hai. Yeh har attribute level ke liye **part-worth utilities** (importance weights) calculate karti hai.
* **Yeh kaise kaam karta hai:** Researcher hypothetical product profiles design karta hai (jaise price, brand, capacity ka combination). Consumers poore profile ko rate/rank karte hain. Algorithm in rankings ko todkar batata hai ki consumers kis attribute ko sabse zyada value dete hain aur kya trade-offs karne ko taiyar hain.
* **Applications:** Optimal product design, pricing strategies, aur market share simulation.

---

### 2. Multidimensional Scaling (MDS)
* **Yeh kya hai:** Ek technique hai jo competing brands ke prati consumer perceptions aur preferences ko ek **multidimensional perceptual space** (map) mein plot karti hai.
* **Key Concept:** Attribute space ko **objective space** (physical product specs) aur **perceived space** (consumers brand ko kaise dekhte hain) mein divide kiya jata hai.
* **MDS vs. Conjoint:** MDS mein stimuli **existing real brands** hote hain jinhe similarity par evaluate kiya jata hai. Conjoint mein stimuli **hypothetical profiles** hote hain jo researcher khud design karta hai.

---

### Key Summary: MDS vs. Conjoint Analysis

| Feature | Multidimensional Scaling (MDS) | Conjoint Analysis |
| :--- | :--- | :--- |
| **Primary Goal** | Perceptions ke dimensions ko identify karne ke liye brands ko **perceptual space** mein map karna. | Individual attributes aur unke levels ki **importance aur utility** (part-worths) ko measure karna. |
| **Stimuli Used** | Real, existing brands/products. | Attribute levels ko change karke banaye gaye hypothetical profiles. |
| **Attribute Input** | Derived spatial dimensions ke basis par **post-hoc** (baad mein) identify hote hain. | Researcher dwara pehle se hi (**a-priori**) select aur define hote hain. |
| **Output Type** | Visual perceptual map jo brands ke beech ki relative distance dikhata hai. | Part-worth utilities aur relative importance weights ki table. |

# The Dual Buffer: Fiscal Credibility and Silent Stabilization in Macao's Pegged-Exchange Regime

**Authors:**

- Ihan Chang (Australian National University)
- Zeju Zhu (George Washington University)

---

## 0. Literature Review

**How Credible is Hong Kong’s Currency Peg?**

A growing body of literature examines the credibility of currency boards and pegged exchange-rate regimes. Early work by Krugman (1991) established the canonical target-zone model, where perfectly credible intervention pins the exchange rate within a band. Subsequent studies relaxed this assumption: Jeanne and Masson (2000) introduced Markov-switching models to allow regime-dependent credibility, while Blagov and Funke (2019) embedded regime shifts within a DSGE framework to study Hong Kong's Linked Exchange Rate System (LERS).

The most closely related paper is Hu and Lai (2025, NBER w34300), which develops an asset-pricing model to evaluate the credibility of Hong Kong's currency board. Their core innovation is a **target-zone framework with regime shift**: the peg survives with probability $p$ each period and, with probability $1-p$, collapses to a "fundamental" floating rate $V_t$. By deriving closed-form option-pricing formulas under this structure, they extract daily estimates of $p_t$ and $V_t$ directly from HKD option data. Their event analysis identifies notable pressure episodes—2019 (RMB depreciation), 2022 (Fed tightening), and 2025 (volatile capital flows)—and attributes credibility fluctuations to U.S. interest-rate hikes, local liquidity (Aggregate Balance), and Chinese currency dynamics.

**Contribution to Our Topic.** Hu and Lai (2025) provide a market-based credibility index ($p_t$) that quantifies investor beliefs about peg survival. This is directly relevant to Macao's MOP–HKD peg, which constitutes a "peg upon a peg." Their HKD $p_t$ series can serve as an upstream credibility shock in our empirical framework—an external financial-environment variable that transmits pressure to the MOP. More fundamentally, their finding that credibility is **not** explained by reserve stocks underscores a gap: the literature treats reserves as background rather than as an active determinant of credibility.

**Methodological Contrast.** While Hu and Lai (2025) adopt an asset-pricing identification strategy—extracting latent credibility from derivatives—we pursue a **macroeconomic-structural** approach. Our research question centers on reserve mechanisms: whether the *stock* of fiscal reserves (FMSI) passively deters speculation (Fiscal Credibility Channel) and whether *flows* from these reserves actively absorb shocks (Fiscal Dampening Channel). In their model, reserve stocks and flows do not enter the pricing equations; credibility is inferred purely from option-implied distributions. By contrast, our SVAR and OLS specifications explicitly include reserve variables as regressors, enabling us to test whether fiscal buffers **cause** reductions in exchange-market pressure.

**Implications for Our Design.** Several insights from Hu and Lai (2025) inform our methodology:

1. **External Credibility Control.** Their $p_t$ or an EMP-based proxy can be incorporated as a control or instrument in our regressions, ensuring that our FMSI effects are not confounded by upstream HKD credibility shocks.
2. **Event Windows.** The 2019, 2022, and 2025 stress episodes they identify provide natural quasi-experimental windows for testing the Fiscal Dampening Channel—periods when capital outflows were acute and fiscal rebalancing should be most visible.
3. **Complementary Channels.** Their paper shows that market-implied credibility fluctuates with interest differentials and RMB dynamics, but is silent on the role of reserve adequacy. Our contribution fills this gap by testing whether a large, liquid fiscal buffer—quantified by FMSI—independently enhances credibility and dampens required monetary contraction.

In sum, Hu and Lai (2025) establish that currency-board credibility is time-varying and can be measured from option markets; we extend this agenda by asking whether fiscal reserves, as a distinct institutional feature, shape that credibility through both stock and flow channels.



---

## 1. Research Question

Macao's reserve system exhibits three unique institutional features that are critical to understanding its stabilization mechanism. First, the Fiscal Reserve was formally separated from foreign exchange reserves in 2012 through the "Legal Framework of the Fiscal Reserve" (財政儲備法律制度), establishing it as an independent entity with its own governance structure. Second, the institution managing Macao's Fiscal Reserve naturally overlaps with the territory's monetary authority, which means that while the Fiscal Reserve officially targets investment returns, it inherently carries a mandate to maintain monetary stability—including both external balance (exchange rate stability) and internal balance (price stability). Third, foreign tourist consumption in Macao's service sector has led to substantial fiscal surpluses denominated primarily in foreign exchange, making the foreign-currency-dominated Fiscal Reserve a natural and substantial component of the government's total foreign exchange holdings.

These institutional peculiarities create a unique dual-buffer system. Macao's MOP-HKD peg operates with two distinct pools of foreign assets: the Monetary Authority of Macao's (AMCM) official reserves and this separate, massive Fiscal Reserve. While the Fiscal Reserve's official mandate is long-term investment rather than monetary policy, this paper investigates its **de facto** role as a "shadow" stabilization buffer.

We pose a two-part research question:

1. **The "Fiscal Credibility" Channel (Stock Hypothesis)**: Does the mere **existence** of a large, liquid, and deployable Fiscal Reserve (quantified as $FMSI_t$) **passively** enhance the peg's credibility and deter speculative pressure **before** it materializes?
2. **The "Fiscal Dampening" Channel (Flow Hypothesis)**: During exogenous shocks, is this reserve **actively** deployed to absorb a portion of capital flight? We test whether **flows** from this reserve ($\Delta FMSI_t$) complement AMCM operations, thereby **dampening** the required monetary contraction.

---

## 2. Contribution

This paper makes three key contributions, grounded in a granular dataset constructed from official monthly and annual reports:

### 2.1 Construct (Not Estimate) the Index

We create a high-frequency (monthly) **Liquidity-Adjusted Fiscal Buffer ($LAFB_t$)** Index by combining **observed** monthly asset class totals with **observed** annual asset and currency allocation reports. This robust, data-driven **measurement** replaces assumption-heavy interpolation methods.

### 2.2 Identify the Mechanism

We propose and test a novel **"Portfolio Rebalancing Channel"** that explains **how** a fund with an "investment" mandate can execute stabilization operations. The act of "rebalancing" its currency portfolio in response to shocks is operationally indistinguishable from sterilized intervention.

### 2.3 Test Dual Channels

We are the first to empirically disentangle and test the passive "Fiscal Credibility" (stock) channel alongside the active "Fiscal Dampening" (flow) channel, using the fund's own performance data and strategic milestone records as controls.

---

## 3. Theoretical Framework

### 3.1 Scenario A: Standard Currency Board Contraction

Under a standard currency board, a capital outflow shock ($u > 0$) forces the public to sell MOP for HKD. The AMCM acts as the sole counterparty.

- **Action**: The AMCM must sell its official FX reserves ($R_{amcm}$) to purchase the MOP.
- **Impact**: $\Delta R_{amcm} = -u$ and $\Delta MB_{mop} = -u$ (where $MB_{mop}$ is the Pataca Monetary Base).
- **Result**: The peg holds, but at the cost of a full, non-sterilized, and potentially painful monetary contraction.

### 3.2 Scenario B: Fiscal-Dampened Contraction

This is our more realistic model. The capital outflow shock ($u$) is met by **both** the AMCM and the Fiscal Reserve. The total shock is decomposed as: $u = u_m + u_f$.

- **Action**: The AMCM absorbs portion $u_m$, while the Fiscal Authority **simultaneously** absorbs $u_f$ by selling its own liquid foreign assets ($F_{fx}$).
- **Impact**:
  - AMCM: $\Delta R_{amcm} = -u_m$ and $\Delta MB_{mop} = -u_m$
  - Fiscal Reserve: $\Delta F_{fx} = -u_f$
- **Result**: The peg holds. A monetary contraction still occurs ($\Delta MB_{mop} < 0$), but its magnitude is **dampened** ($|\Delta MB_{mop}| = |u_m| < |u|$). Our central hypothesis is that $u_f > 0$, meaning the Fiscal Reserve actively intervenes.

### 3.3 The "Portfolio Rebalancing" Channel (The Mechanism)

The key question is **how** an "investment" fund can execute Scenario B without violating its mandate. We formalize the mechanism as **strategic portfolio rebalancing**. Drawing on **Black & Litterman (1992)** for equilibrium portfolios and **Froot, O'Connell, & Seasholes (2001)** for flow dynamics, we model this by contrasting the Fiscal Reserve's behavior against aggregate market flows.

#### 3.3.1 The "Neutral" Portfolio (The Mandate)

The Fiscal Reserve's mandate is to adhere to a Strategic Asset Allocation (SAA), which functions as the "Neutral Portfolio" or equilibrium in the Black-Litterman framework. Given the fund's dynamic mandate, we define the neutral portfolio ($\mathbf{w}^*_t$) as the **realized** asset allocation from the previous period ($t-1$).

Let $W_t$ be the total wealth of the Fiscal Reserve at time $t$. The fund holds $N$ assets (e.g., USD, HKD, RMB). The target weight vector defined by the mandate is $\mathbf{w}^*_t$:

$$
\mathbf{w}^*_t \equiv \mathbf{w}_{t-1}^{\text{realized}} = [w^*_{usd}, w^*_{hkd}, w^*_{rmb}]' \quad \text{subject to} \sum w_i^* = 1
$$

The fund manager minimizes the deviation (tracking error) from this neutral equilibrium:

$$
\min E [ ( \mathbf{w}_t - \mathbf{w}^*_t )' \Omega ( \mathbf{w}_t - \mathbf{w}^*_t ) ]
$$

where $\Omega$ is the covariance matrix of returns. This optimization creates a binding constraint: significant deviations from $\mathbf{w}^*_t$ caused by market movements **must** be corrected.

#### 3.3.2 The Shock and Valuation Effects

We introduce a capital outflow shock using the valuation framework from **Lane and Milesi-Ferretti (1999)**. A shock affects the portfolio through valuation changes (exchange rates and asset prices) **before** any transaction occurs.

Let $r_{i,t}$ be the return on asset $i$ at time $t$. In a crisis affecting Macao or the region (e.g., devaluation pressure on RMB or MOP), returns on risk assets (like RMB) fall relative to defensive assets (USD/HKD). The **actual** weight of asset $i$ at the end of period $t$ before rebalancing ($w_{i,t}^{pre}$) evolves as:

$$
w_{i,t}^{pre} = \frac{w_{i,t-1}(1 + r_{i,t})}{\sum_{j} w_{j,t-1}(1 + r_{j,t})}
$$

**The Shock Condition**: If capital flight occurs (private sector selling local/regional currency for USD), then $r_{rmb} < r_{usd}$. Consequently, the actual weight of the defensive asset rises above target ($w_{usd,t}^{pre} > w^*_{usd}$), and the weight of the risk asset falls ($w_{rmb,t}^{pre} < w^*_{rmb}$).

#### 3.3.3 The Rebalancing Flow (The Stabilizing Mechanism)

To return to the Black-Litterman "Neutral" equilibrium, the fund must execute a rebalancing flow $f_{i,t}$:

$$
f_{i,t} = W_t \cdot (w_i^* - w_{i,t}^{pre})
$$

Substituting the shock condition:

1. **For USD (Defensive Asset)**: Since $w_{usd,t}^{pre} > w^*_{usd}$, then $f_{usd,t} < 0$. The fund **sells** USD.
2. **For RMB (Risk Asset)**: Since $w_{rmb,t}^{pre} < w^*_{rmb}$, then $f_{rmb,t} > 0$. The fund **buys** RMB.

**Mechanism Result**: The fund effectively supplies liquidity in safe assets (USD/HKD) and absorbs risky assets (RMB/MOP), acting as a counterparty to the market.

#### 3.3.4 Fiscal Reaction Function (Testing the Hypothesis)

Since direct data on private investor positions is unavailable, we use aggregate **Net Capital Flows ($\mathit{CapFlow}_t$)** as a proxy for private market behavior. Following **Froot, O'Connell, & Seasholes (2001)**, we characterize private flows as "trend chasing" or positive feedback trading.

We define the shock $u_t$ as a negative capital flow ($\mathit{CapFlow}_t < 0$), representing capital flight. The Fiscal Reserve's rebalancing rule (derived in Section 3.3.3) creates a reaction function where the fiscal flow ($f_{fiscal}$) **opposes** the market flow:

$$
f_{fiscal, t} = -\gamma \cdot \mathit{CapFlow}_t \quad \text{where } \gamma > 0
$$

If $\mathit{CapFlow}_t$ is negative (outflow), $f_{fiscal, t}$ is positive (inflow/repatriation of foreign assets). This aligns with the "Stabilizing Speculator" behavior described by **Eichengreen & Mathieson (1998)**, where the agent buys into falling markets.

This theoretical reaction function justifies the structural identification in our **Empirical Test 2 (SVAR)**, where we expect the impulse response of $\Delta \log(FMSI_t)$ to a $\mathit{CapFlow}_t$ shock to be statistically significant and opposite in sign.

---

## 4. Data & FMSI Construction

### 4.1 Data Sources

Our dataset is constructed from official Macao SAR reports:

- **Monthly Balance Sheets (2012-2025)**: Provides $V_{\text{Deposits}, t}$, $V_{\text{Direct\_Bonds}, t}$, $V_{\text{Outsourced}, t}$.
- **Annual Asset Allocation (2014-2024)**: Provides shares ($\%\text{Equity}_Y$, etc.).
- **Annual Currency Allocation (2014-2024)**: Provides shares ($\%\text{USD}_Y$, $\%\text{HKD}_Y$, $\%\text{RMB}_Y$).
- **Performance & Milestones**: Annual returns by asset class, income breakdowns, and policy change dates.

### 4.2 Methodological Note on 2025 Data

For all monthly data points in 2025, we apply the annual asset and currency allocation percentage shares from the 2024 annual reports. This assumes the fund's strategic directive remains constant until a new annual report is issued.

### 4.3 FMSI Construction

We construct our key variable, the **Liquidity-Adjusted Fiscal Buffer ($LAFB_t$)**, in three steps:

1. **Step 1: Disaggregate Monthly Assets**. For each month $t$ in year $Y$, we disaggregate the $V_{\text{Outsourced}, t}$ "black box" using the fixed **annual** shares from $Y$:

   $$
   V_{\text{Outsourced\_Equity}, t} = V_{\text{Outsourced}, t} \times \%\text{Equity}_{Y}
   $$
2. **Step 2: Compute $LAFB_t$**. The index is the sum of all liquid, usable assets, weighted by calibrated weights $\lambda_i$ (liquidity) and $\phi_{i,t}$ (currency usability), justified in Section 4.4:

   $$
   LAFB_{t} = \sum_{i} (\lambda_{i} \times \phi_{i,t} \times V_{i,t})
   $$

   where $V_{i,t}$ is our constructed **monthly value** for each asset class $i$.
3. **Step 3: Normalize to FMSI**. We create our main index by normalizing by the Pataca Monetary Base, $MB_{mop,t}$:

   $$
   FMSI_t = \frac{LAFB_t}{MB_{mop,t}}
   $$

### 4.4 Calibration Methodology for $LAFB_t$ Weights

The construction of $LAFB_t$ depends on two calibrated parameter vectors: the Liquidity Weight ($\lambda_i$) and the Currency Usability Weight ($\phi_{i,t}$). Our calibration strategy establishes a "baseline" set of weights grounded in a conservative "stress-test" scenario, assuming peg defense occurs during periods of high financial distress where asset liquidity is compromised and currency convertibility is not guaranteed.

#### 4.4.1 Calibration of $\lambda_i$ (The "Fire-Sale" Liquidity Weight)

The $\lambda_i$ weight (0 to 1) represents the "fire-sale" value of an asset. It answers: "For every $1 of pre-crisis value, how many cents can be recovered **immediately** in a crisis to defend the peg?"

Our baseline calibration:

- **$\lambda_{\text{Deposits}} = 1.0$**: (100% usable). Cash or cash-equivalents have 1-to-1 value.
- **$\lambda_{\text{Bonds}} = 0.95$**: (95% usable). Assumes a 5% "fire-sale" discount. High-grade bonds face dramatically widened bid-ask spreads in systemic crises.
- **$\lambda_{\text{Equity}} = 0.40$**: (40% usable). Our most critical assumption, implying a 60% "fire-sale" discount.
- **$\lambda_{\text{Illiquid}} = 0.10$**: (10% usable). Applies to "Other Investments" or private equity not intended for liquidation.

**Justification for $\lambda_{\text{Equity}} = 0.40$**: This value derives from both financial literature and our dataset.

1. **Theoretical (Stress-Test)**: Academic literature on fire-sales (e.g., Shleifer & Vishny, 1992; Brunnermeier, 2009) and stress-tests (e.g., IMF, 2014) often model systemic crises as 2- or 3-standard-deviation events, corresponding to market drawdowns of 50-60%. Our $\lambda=0.4$ assumes authorities are forced to liquidate equities at the **bottom** of such a crisis.
2. **Data-Driven (VaR)**: We use annualized return rates and income breakdown data to empirically support this. For example, the "Outsourced Equity" component had returns of -15.5% (2018) and -16.9% (2022) in "bad" years. We calculate the historical standard deviation ($\sigma_{\text{equity}}$) of the fund's equity portfolio. Our 60% discount ($1-0.40$) is explicitly compared to a 2-sigma or 3-sigma tail-risk event (a standard Value-at-Risk, or VaR, calculation).

#### 4.4.2 Calibration of $\phi_{i,t}$ (The "Peg-Defense" Usability Weight)

The $\phi_{i,t}$ weight (0 to 1) concerns **usability**, not liquidity. It answers: "Is this asset denominated in a currency that can **actually be used** to defend the **MOP-HKD** peg?"

Our baseline calibration:

- **$\phi_{\text{HKD}} = 1.0$**: (100% usable). This is the intervention currency.
- **$\phi_{\text{USD}} = 0.98$**: (98% usable). A near-perfect substitute. The 2% discount accounts for transaction costs and the minor band-risk of HKD's own peg to USD (7.75-7.85).
- **$\phi_{\text{RMB/Other}} = 0.2$**: (20% usable). This highly conservative weight implies an 80% discount on all non-peg currencies.

**Justification for $\phi_{\text{RMB/Other}} = 0.2$**: This assumption is central to our paper and strongly supported by the data.

1. **Institutional**: To defend the MOP-HKD peg, the AMCM or its proxy must **sell** HKD. It cannot use RMB or AUD directly. To use RMB assets, the government must **first** sell RMB to **then** buy HKD.
2. **Market Risk (FX Loss)**: This two-step transaction is high-risk. The strategic milestones data provides a "smoking gun" justification. The 2015 and 2016 entries **explicitly** state the fund faced "significant FX losses... mainly from RMB foreign exchange revaluation losses." This proves that in a crisis (like the 2015-16 RMB depreciation), RMB holdings are a source of **loss**, not **defense**.
3. **Market Risk (Capital Controls)**: A significant portion of the fund's RMB (per currency allocation data) is "Onshore RMB," subject to PBoC capital controls. In a crisis, these controls would likely tighten, making it **impossible** to liquidate these assets and convert them to HKD.

Therefore, our $\phi=0.2$ assumes that 80% of non-peg currency value is effectively trapped by capital controls or lost to crisis-driven FX depreciation.

**Our final step**, as outlined in Section 6 (Robustness Checks), is to systematically re-run all empirical tests using different weights (e.g., $\lambda_{\text{Equity}} = 0.3, 0.5$; $\phi_{\text{RMB}} = 0.1, 0.3$). We will demonstrate that our main conclusions (the signs and statistical significance of key hypotheses) are not sensitive to these specific baseline values.

---

## 5. Empirical Methodology & Equations

Our primary dependent variable is the **Exchange Market Pressure ($EPI_t$)** Index, following Girton & Roper (1977):

$$
EPI_t = w_e (\Delta e_t) + w_i (\Delta i_t) - w_r \left( \frac{\Delta R_{amcm,t}}{MB_{mop,t-1}} \right)
$$

where:

- $\Delta e_t$: % change in MOP/HKD spot rate.
- $\Delta i_t$: Change in Macao-HK interest rate differential.
- $\Delta R_{amcm,t}$: Change in **official** AMCM reserves.
- $w_j$: Weights (inverse of rolling standard deviation of each component).

### 5.1 Test 1: The "Credibility" (Stock) Channel

We test the passive credibility hypothesis using OLS regression on the **volatility** of market pressure.

$$
\mathit{EPIVol}_t = \alpha + \beta_1 \log(FMSI_{t-1}) + \boldsymbol{\Gamma} \boldsymbol{X}_{t-1} + \epsilon_t
$$

where:

- $\mathit{EPIVol}_t$: The rolling 12-month standard deviation of $EPI_t$.
- $\log(FMSI_{t-1})$: The lagged log-level of our fiscal buffer index. **Hypothesis: $\beta_1 < 0$** (a larger buffer stock reduces future volatility).
- $\boldsymbol{X}_{t-1}$: Vector of controls (e.g., $\log(\text{GDP}_t)$, gaming revenue growth, VIX).

### 5.2 Test 2: The "Fiscal Dampening" (Flow) Channel

We test the active intervention hypothesis (Scenario B) using a Structural VAR (SVAR) with variables in first-differences. The vector of endogenous variables $Y_t$ is:

$$
Y_t = [ \mathit{CapFlow}_t, \mathit{EPI}_t, \Delta \log(FMSI_t), \Delta \log(R_{amcm,t}), \mathit{PolicyChange}_t ]'
$$

where:

- $\mathit{CapFlow}_t$: Net capital flows (from DSEC).
- $\mathit{EPI}_t$: Our exchange market pressure index.
- $\Delta \log(FMSI_t)$: The % change in our fiscal buffer.
- $\Delta \log(R_{amcm,t})$: The % change in **official** AMCM reserves.
- $\mathit{PolicyChange}_t$: A dummy variable $=1$ for months after a major policy shift (e.g., 2014 equity investment) from strategic milestone data. This precisely controls for the **evolving investment mandate**, addressing the institutional credibility question.

**Testable Hypothesis**: An impulse (shock) to $\mathit{CapFlow}_t$ will be met by a statistically significant and **offsetting** response in $\Delta \log(FMSI_t)$. This shows $u_f > 0$. We compare the relative impulse-response magnitudes of $\Delta \log(FMSI_t)$ and $\Delta \log(R_{amcm,t})$ to determine the share of the shock ($u_f$ vs $u_m$) absorbed by each buffer.

### 5.3 Test 3: The "Portfolio Rebalancing" Mechanism

We test the mechanism from Section 3.3 using two-stage least squares (2SLS).

**Stage 1:**

$$
\mathit{RMBDev}_t = \alpha_1 + \beta_1 \mathit{CapFlow}_t + \boldsymbol{\Gamma}_1 \boldsymbol{X}_t + \epsilon_t
$$

**Stage 2:**

$$
\mathit{FXLoss}_t = \alpha_2 + \beta_2 \widehat{\mathit{RMBDev}}_t + \boldsymbol{\Gamma}_2 \boldsymbol{X}_t + \nu_t
$$

where:

- $\mathit{RMBDev}_t$: The deviation of RMB holdings from the strategic target ($\%\text{RMB}_t - \text{Target}\%\text{RMB}_Y$).
- $\mathit{CapFlow}_t$: Capital outflows (our instrument for the deviation).
- $\mathit{FXLoss}_t$: The observed `FX Gains/Loss` from income breakdown data, serving as a proxy for active FX rebalancing operations.
- $\widehat{\mathit{RMBDev}}_t$: The fitted values from Stage 1.
- **Hypothesis**: We expect $\beta_1 < 0$ (capital flight causes a deviation) and $\beta_2 > 0$ (a larger deviation forces rebalancing, captured as FX losses/gains).

### 5.4 Test 4: The "Opportunity Cost" of Credibility

We use annualized return rate data to measure the **cost** of maintaining the stabilization buffer.

$$
(\mathit{Return}_t - \mathit{BenchmarkReturn}_t) = \alpha + \beta_1 \mathit{EPIVol}_{t-1} + \boldsymbol{\Gamma} \boldsymbol{X}_t + \epsilon_t
$$

where:

- $\mathit{Return}_t$: The observed overall annual return of the Fiscal Reserve.
- $\mathit{BenchmarkReturn}_t$: The return of a benchmark (e.g., 60/40 portfolio) or a peer fund.
- $\mathit{EPIVol}_{t-1}$: Lagged volatility of exchange market pressure.
- **Hypothesis: $\beta_1 < 0$**. This would show that in periods **following** high market pressure, the fund's return **underperforms** its benchmark.

---

## 6. Robustness Checks

We conduct several tests to ensure the robustness of our findings:

1. **Alternative FMSI Definitions**: Re-run all regressions using different liquidity weights ($\lambda_i$) to ensure results are not sensitive to these calibrations.
2. **Alternative EPI Definitions**: Reconstruct $EPI_t$ using alternative weighting schemes (e.g., principal components analysis).
3. **Sub-sample Analysis**: Split the sample into two periods: pre-2014 and post-2014 (using our $\mathit{PolicyChange}_t$ dummy).
4. **Alternative Lag Structures**: Test different lag-lengths in the VECM/SVAR models.

---

## 7. Expected Results

- **H1 (Credibility)**: The **level** of $FMSI_t$ will be a significant and negative predictor of future $\mathit{EPIVol}_t$.
- **H2 (Dampening)**: The SVAR impulse-responses will show that a shock to $\mathit{CapFlow}_t$ is met by a statistically significant and economically large response from $\Delta \log(FMSI_t)$, proving $u_f > 0$.
- **H3 (Mechanism)**: We will find that capital outflows predict deviations in the fund's RMB portfolio, which in turn predict FX rebalancing operations.
- **H4 (Cost)**: We will find a negative relationship between past market volatility and the fund's subsequent investment returns.

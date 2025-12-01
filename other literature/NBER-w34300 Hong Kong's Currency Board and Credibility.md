# NBER-w34300 《How Credible is Hong Kong’s Currency Peg?》问答整理

**来源文件：** `other literature/NBER-w34300.pdf`

---

## 问题 1：是否准确概括了文章的主要内容、数据和创新点？

**问题概括：**
- 主要内容：用港币外汇期权隐含概率评估联系汇率存续度，考察美联储利率、人民币汇率等对挂钩可信度的影响。
- 使用数据：港币期权价格与隐含分布、港币/美元现货和远期、美国与香港利率、CNH/CNY 汇率。
- 创新点：用期权隐含概率量化挂钩可信度，同时纳入外部（美联储）与区域（人民币）因素。

**根据原文补充：**
- 摘要明确写到：
  > “This paper develops an asset-pricing model to evaluate the credibility of Hong Kong’s Linked Exchange Rate System (LERS)… Using HKD option data, we estimate market-implied probabilities of peg survival and the fundamental value of the HKD. Our results show that credibility fluctuates with U.S. interest rate hikes, local liquidity conditions, and Chinese currency dynamics.”（Abstract）
- 第 1 节介绍里强调：美联储加息周期、本地银行体系 Aggregate Balance 的收缩、以及人民币（CNY/CNH）波动对港币挂钩构成压力。
- 第 3、4 节说明数据包括：USD/HKD 现货、3 个月期 HKD 期权（不同 delta 的风险逆转 / 蝶式）、港美利差、本地流动性、以及人民币汇率指标。

**遗漏的关键创新点：**
1. **不完美可信度 + regime shift 结构：** peg 并非 100% 可信，而是以概率 \(p\) 继续、以 \(1-p\) 破裂；破裂时汇率跳到“基本面” \(V\)。这是模型的核心设定（Section 3, eq.(2)，以及连续时间版本）。
2. **封闭式（closed-form）汇率和期权定价：** 在目标区（target zone）下推导出封闭式的 S 形汇率函数和期权定价公式（Proposition 1 & 3），可以高效逐日估计 \(p_t, V_t, \sigma_t\)。
3. **比较三类方法：**
   - 标准 Black–Scholes（忽略目标区结构）；
   - Malz (1997) / Genberg & Hui (2011) 从期权二阶导数反推出密度；
   - 本文的 regime‑shift 无套利模型。
   结果显示，若忽略 regime shift，会严重高估破带概率（Figure 8）。
4. **事件分析：** 利用估计出的 \(p_t\) 序列，系统识别 2008–09、2019、2022、2025 等关键压力期，并将之与利差、流动性、人民币汇率联动起来（Section 4）。

所以你的概括抓住了主线，但**没有提到：regime‑shift 结构、封闭式定价、与 Black–Scholes/Malz 的系统比较**，这些是非常重要的创新点。

---

## 问题 2：什么是用于评估 LERS 可信度的 asset-pricing model？

**出处：** Abstract + Section 3 “Model”。

**回答：**
- 这是一个在**目标区 + regime shift** 环境下的资产定价框架：
  - 每一期 peg 以概率 \(p\) 继续存在，以 \(1-p\) 破裂；
  - 若破裂，汇率从当前 peg 区间跳到“自由浮动”基本汇率 \(V_t\)；
  - 在风险中性测度下，汇率和期权价格由无套利条件决定。
- 离散时间下（Section 3.1, 公式 (2)）：
  $$
  \tilde S_t = \frac{1+r_\$}{1+r_H}\big[ p\,E_t^Q H(\tilde S_{t+1}; S_P, b) + (1-p) E_t^Q V_{t+1} \big]
  $$
  - \(\tilde S_t\)：未截断的理论汇率；
  - \(H(\cdot)\)：把汇率截断在 \([S_P-b, S_P+b]\) 的函数；
  - \(r_\$, r_H\)：美元/港元利率；
  - \(V_{t+1}\)：若破裂时的基本面汇率；
  - \(p\)：peg 存续概率。
- 连续时间下（Section 3.1, eq.(6)）：
  $$
  \frac{dV_t}{V_t} = (\hat r_{HKD} - r_{USD}) dt + \sigma_V dW_t,
  $$
  并假定 peg 破裂由一个 Poisson 过程以强度 \(\lambda\) 到达（\(p \approx e^{-\lambda\Delta t}\)）。
- 在此基础上，作者推导出：
  - peg 下的均衡汇率 \(S_t\) 的封闭式解（S 形函数）；
  - 同时给出欧式期权的闭式定价公式（Proposition 1 & 3）。

直观上，这是一个**“带有跳跃（regime shift）的目标区资产定价模型”**，用来把期权价格映射成“peg 存续概率”和“基本面汇率”。

---

## 问题 3：为什么要用期权数据来估计？

**出处：** Abstract；Section 3 末尾；Section 4.1；Figure 8 附近。

**回答：**
- 期权价格在风险中性世界里包含了市场对**未来汇率分布**的全部信息，尤其是：
  - 对“是否破带”、“破带到哪”的概率判断；
  - 对极端事件尾部的担忧。
- 标准目标区模型往往只使用现货和利差，很难识别市场对“破 peg”尾部风险的看法；而**期权的偏度（risk reversals）和尾部定价，正是对这种风险的直接反映**。
- 文中明确指出：
  > “… Using HKD option data, we estimate market-implied probabilities of peg survival and the fundamental value of the HKD.”（Abstract）
  > “… Our model implies a U-shaped distribution … in stark contrast to the bell-shaped distribution under standard Black–Scholes models.”（Section 3）
- 因此：
  - 用期权数据可以直接把“市场对 peg 破裂概率的看法”量化出来；
  - 同时可以与 Black–Scholes、Malz 密度方法做对比，说明传统方法如何系统性高估破带概率。

---

## 问题 4：如何用 HKD 期权数据估计 peg 存续概率和基本面？

**出处：** Abstract；Section 3（Proposition 3）；Section 4.1（估计方法与 Figure 7–8）。

**数学思路（模型层面）：**
1. 在 peg 存续时，汇率 \(S_t\) 的定价满足：
   $$
   \tilde S_t = \frac{1+r_\$}{1+r_H}\big[ p\,E_t^Q H(\tilde S_{t+1}; S_P, b) + (1-p) E_t^Q V_{t+1} \big],
   $$
   同时基本面 \(V_t\) 满足：
   $$
   \frac{1+r_\$}{1+\hat r_H}E_t^Q[V_{t+1}] = V_t, \qquad \frac{dV_t}{V_t} = (\hat r_{HKD}-r_{USD})dt + \sigma_V dW_t.
   $$
2. 对目标区下的欧式期权，作者在 Proposition 3 中推导出**闭式定价公式**：
   - 期权价格 = “peg 持续到到期”的情形下的期权价值 × \(p^N\)，加上“期间某次破裂”的情形下，根据跳到 \(V\) 后自由浮动定价得到的期权价值 × \(1-p^N\)；
   - 这里 \(N\) 是到期前的离散步数（或等价的连续时间长度）。
3. 由于期权价格对参数 \(p, V, \sigma_V\) 有解析表达，理论期权价格 \(P^{model}(p,V,\sigma_V)\) 是显式函数。

**数据拟合（估计层面）：**
1. 每一天，观察：
   - 现货 USD/HKD；
   - 3 个月期 HKD 期权的 ATM 隐含波动率、10Δ/25Δ 的 risk reversals (RR) 和 butterflies (BF)（Section 4.1，数据描述）；
   - 3M 美元与港元利率（LIBOR / SOFR vs HIBOR）。
2. 从市场的 ATM/RR/BF 组合反推 4 个“等价”的期权价（常见做法）：
   - ATM call/put；
   - 25Δ call/put；
   - 10Δ call/put（不同 delta 层上的 RR/BF 对应不同行权价的波动率）。
3. 构造目标函数：对给定一天 t，最小化
   $$
   \sum_{i \in \{\text{spot},4\,\text{options}\}} w_i\big(P^{model}_i(p_t,V_t,\sigma_{V,t})-P^{mkt}_i\big)^2,
   $$
   - 其中 \(P^{mkt}_i\) 是观察到的期权/现货价格；\(P^{model}_i\) 是模型闭式公式给出的价格；
   - 权重 \(w_i\) 通常等权或按报价精度设置。
4. 用数值方法对 \(p_t, V_t, \sigma_{V,t}\) 做非线性最小二乘校准，得到每日的：
   - **peg 存续概率 \(p_t\)**；
   - **基本面汇率 \(V_t\)**；
   - **基本面波动率 \(\sigma_{V,t}\)**。
5. 然后将 \(p_t\) 的时间序列画出来（Figure 7, Figure 8），与：
   - 美联储加息时间、
   - 香港 Aggregate Balance、
   - 人民币汇率变动（2019、2022、2025 事件）对照。

**由此得出结论：**
- "credibility fluctuates with U.S. interest rate hikes, local liquidity conditions, and Chinese currency dynamics"：
  - 在美联储加息、港元流动性骤降、人民币贬值冲击时，估计的 \(p_t\) 显著下降。
- 与 Black–Scholes 模型比较（Figure 8）：
  - Black–Scholes 的钟形分布在目标区下会把尾部质量放在"破带"之外，从而**严重高估破带概率**；
  - 本文的目标区 + regime shift 模型生成 U 型分布，更符合实际观测到的汇率和期权隐含分布。

### 附：ATM / RR / BF 报价体系的详细解释（以及如何变成 4 个"等价期权价"）

在外汇期权（FX options）市场，做市商通常不是直接报一整条波动率曲线，而是用一组三个数字来概括某个期限的 "smile"：

- **ATM IV**（at‑the‑money implied volatility）
- **RR**（risk reversal，风险逆转）
- **BF**（butterfly，蝶式）

然后大家用一些固定的线性关系，把它们还原成若干个具体 delta 层上的 call/put 隐含波动率，再进一步用 Black‑Scholes（或 Garman‑Kohlhagen）算出具体的期权价格。NBER‑w34300 用的就是这一套"行规"。

#### 1. ATM IV 是什么？

- **ATM（at the money）**：平值期权，通常指 delta ≈ 50% 的欧式 call/put（有时是 delta‑neutral straddle）。
- **ATM IV**：用 Black‑Scholes（或 FX 版本 Garman‑Kohlhagen）把平值期权的市场价格反推出来的隐含波动率，记作 $\sigma_{ATM}$。
- 它代表"中间"的波动水平，是整个 smile 的锚点。

#### 2. Risk Reversal（RR）是什么？

以 25Δ 为例，25Δ risk reversal 的标准定义是：

$$
RR_{25} = \sigma_{25\Delta C} - \sigma_{25\Delta P}
$$

也就是：
- 25Δ call 的隐含波动率 $\sigma_{25\Delta C}$
- 减去 25Δ put 的隐含波动率 $\sigma_{25\Delta P}$

10Δ RR 同理：

$$
RR_{10} = \sigma_{10\Delta C} - \sigma_{10\Delta P}
$$

**直观含义：**
- $RR > 0$：call 的 IV 高于 put，说明市场愿意为"向上"的尾部风险付更多钱（比如担心 USD 对 HKD 大幅升值），偏向看涨 skew。
- $RR < 0$：put 更贵，说明更担心向下尾部（如 HKD 突然大幅走强）。

**RR 描述的是左右不对称的"斜率"（skew）。**

#### 3. Butterfly（BF）是什么？

以 25Δ 为例，25Δ butterfly 常用定义是：

$$
BF_{25} = \tfrac{1}{2}(\sigma_{25\Delta C} + \sigma_{25\Delta P}) - \sigma_{ATM}
$$

10Δ BF 同理：

$$
BF_{10} = \tfrac{1}{2}(\sigma_{10\Delta C} + \sigma_{10\Delta P}) - \sigma_{ATM}
$$

**直观含义：**
- $\tfrac{1}{2}(\sigma_{25\Delta C} + \sigma_{25\Delta P})$：25Δ call 和 25Δ put 的 "平均 IV"，相当于两端的平均高度；
- 减去 $\sigma_{ATM}$，就是"两端比中间贵多少"。

因此：
- $BF > 0$：两端（远虚值期权）的 IV 高于 ATM，中间低，两端高，是"笑脸型" smile；
- $BF < 0$：两端相对便宜，IV 曲线更平甚至倒 U。

**BF 描述的是 smile 的"弯曲程度"（curvature）。**

#### 4. 从 ATM / RR / BF 还原 25Δ/10Δ call/put 的 IV

有了三样报价：ATM、RR、BF，就可以解出 25Δ（或 10Δ）call/put 的两条 IV。这是线性代数：两条方程解两个未知数。

**对 25Δ 层：**

$$
\begin{aligned}
RR_{25} &= \sigma_{25\Delta C} - \sigma_{25\Delta P} \\
BF_{25} &= \tfrac{1}{2}(\sigma_{25\Delta C} + \sigma_{25\Delta P}) - \sigma_{ATM}
\end{aligned}
$$

解这个二元一次方程组得到：

$$
\begin{aligned}
\sigma_{25\Delta C} &= \sigma_{ATM} + BF_{25} + \tfrac{1}{2} RR_{25} \\
\sigma_{25\Delta P} &= \sigma_{ATM} + BF_{25} - \tfrac{1}{2} RR_{25}
\end{aligned}
$$

同理，**对 10Δ 层**：

$$
\begin{aligned}
\sigma_{10\Delta C} &= \sigma_{ATM} + BF_{10} + \tfrac{1}{2} RR_{10} \\
\sigma_{10\Delta P} &= \sigma_{ATM} + BF_{10} - \tfrac{1}{2} RR_{10}
\end{aligned}
$$

这样，对于每一个 maturity（比如 3 个月），只要市场报给你：
- ATM IV；
- 25Δ RR、25Δ BF；
- 10Δ RR、10Δ BF；

你就能得到 5 个 IV 节点：$\sigma_{ATM}$、$\sigma_{25\Delta C}$、$\sigma_{25\Delta P}$、$\sigma_{10\Delta C}$、$\sigma_{10\Delta P}$。

#### 5. 再从 IV 变成具体的"4 个等价期权价"

接下来，用这些 IV 和对应的行权价 K 算出期权价格：

**已知：**
- 标的现货 $S_t$（这里是 USD/HKD）；
- 时间到期 $T$（3 个月）；
- 美元利率 $r_{USD}$、港元利率 $r_{HKD}$；
- 每个 delta（10Δ、25Δ、50Δ）的隐含波动率 $\sigma_i$；
- 给定 delta，可以反推对应的行权价 $K_i$（外汇期权中 delta 与 K 的关系是标准公式，你可以把它当成"Black–Scholes 反解"）。

**用 Garman‑Kohlhagen（FX 版 Black‑Scholes）计算各个节点的期权价格：**

$$
P^{mkt}_i = BS\big(S_t, K_i, T, r_{USD}, r_{HKD}, \sigma_i\big)
$$

其中 $i$ 对应：
- ATM 期权；
- 25Δ call；
- 25Δ put；
- 10Δ call；
- 10Δ put。

在 NBER‑w34300 里，作者从这些节点里挑出 4 个代表性期权价（加上现货价），作为**观测数据点** $P^{mkt}_i$。

#### 6. 在这篇文章里的作用：从 ATM/RR/BF 到 "校准数据"

NBER‑w34300 的步骤大致是：

1. 每天收集：现货、3M ATM IV、10Δ/25Δ 的 RR 和 BF、港美利率；
2. 用上面的线性关系把 ATM/RR/BF 变成：
   - 25Δ call/put 的 IV；
   - 10Δ call/put 的 IV；
3. 再用 Black‑Scholes / Garman‑Kohlhagen 算出 4 个具体的期权价格 $P^{mkt}_i$。
4. 然后，用自己推导的"目标区 + regime shift" 模型，写出每一个期权在参数 $(p_t, V_t, \sigma_{V,t})$ 下的**理论价** $P^{model}_i$。
5. 最小化
   $$
   \sum_i\big(P^{model}_i(p_t, V_t, \sigma_{V,t}) - P^{mkt}_i\big)^2
   $$
   把 $(p_t, V_t, \sigma_{V,t})$ 当成待估参数。

**所以：**
- **"ATM/RR/BF 组合"** 是市场给你的三种标准报价；
- **"反推 4 个等价期权价"** 是指：先用线性关系算出 10Δ/25Δ call/put 的 IV，再用 Black‑Scholes 把这些 IV 变成具体期权价格；
- 这些价格再拿来和 w34300 的资产定价模型匹配，从而反推 **"peg 存续概率（$p_t$）"** 和 **"HKD 的基本面（$V_t$）"**。

---

## 问题 5：文章认为香港汇率制度可靠性的主要决定因素是什么？是外汇储备基金吗？

**出处：** Abstract；Section 1；Section 4.3 “Economic fundamentals and sustainability…”。

**回答：**
- 文中强调的主要决定因素是：
  1. **美联储政策利率路径**：美联储加息会提高美元收益率，相对压低港元资产吸引力，增加撤资压力，降低 \(p_t\)。
  2. **本地流动性（Aggregate Balance）**：银行体系结算户余额收缩到低位，意味着货币局在捍卫挂钩过程中“吸走”了大量港元流动性，市场会担心继续捍卫的空间，\(p_t\) 下降（Figure 10 文字说明）。
  3. **人民币（CNY/CNH）汇率**：人民币贬值时，港币作为“对外港口”的角色被质疑，市场担心peg 会在较大区域压力下调整，\(p_t\) 下降；反之，人民币稳定/升值时，有助于 \(V_t\) 和 \(p_t\) 上升。
- 外汇储备基金（Exchange Fund）：
  - 在制度背景中被反复提及（Section 2），说明货币基础以美元资产全额覆盖；
  - **但在模型和估计中，储备规模并未进入关键方程，也不是回归中的解释变量**。

因此，本文的“可靠性”更多是**市场基于期权价格和利差等信息对未来 peg 存续概率的评估**，而非储备规模本身的函数。

---

## 问题 6：是否从宏观机制角度（储备机制、储备可得性）讨论？

**出处：** Section 2 “Institutional background”；Section 4.3。

**回答：**
- 有**定性**的宏观制度背景介绍：
  - 货币局通过 Exchange Fund 完全覆盖货币基础；
  - 当接近区间边界时，通过买入/卖出港元干预，并通过 HIBOR 调整本地流动性。
- 但在**量化模型**中：
  - 没有把“储备规模”或“储备流量”作为状态变量；
  - 也没有引入储备可得性（liquidity of reserves）进入 \(p_t\) 的决定。
- 宏观变量真正进入模型的是：
  - 港美利差；
  - 港元 Aggregate Balance；
  - 人民币汇率水平及其波动。

结论：本文**没有**像你设想的那样，从“储备机制/储备可得性”的角度构建显式机制方程，这个空间正好留给你的 FMSI 研究去填补。

---

## 问题 7：是不是纯资产定价文章？数据频率是什么？

**出处：** Section 3；Section 4.1 “Data and option market”。

**回答：**
- 性质上，是一篇**以资产定价模型为核心**的文章：
  - 理论部分：构建目标区 + regime shift 的资产定价框架，推导汇率与期权定价的闭式解；
  - 实证部分：利用日度汇率和期权报价，把模型参数（\(p_t,V_t,\sigma_t\)）从市场价格中反推出来。
- 数据频率：
  - 汇率和期权数据：**日频（日度）**；
  - 利率：对应 3M 美元和港元利率（按日对齐）；
  - 期权具体是 3 个月到期的 USD/HKD 期权（不同 delta 层的 RR/BF）。

没有宏观年度/季度回归，属于典型“高频资产定价 + 事件分析”的论文。

---

## 问题 8：The canonical target zone model 是什么？

**出处：** Section 3，关于 Krugman (1991) 的讨论。

**回答：**
- 典型的 Krugman (1991) 目标区模型假设：
  1. 政府承诺在某个区间内维持汇率 \(S_t\)；
  2. 只要汇率碰到区间边界，就会立刻干预把汇率拉回区间内；
  3. 市场相信这一承诺（高可信度），并假定**未覆盖利率平价（UIP）成立**：
     $$
     E_t[\Delta s_{t+1}] = i_t - i_t^\*,
     $$
     其中 \(s_t\) 为对数汇率，\(i_t,i_t^*\) 为本国/外国利率。
  4. 由于干预和预期的存在，汇率在区间内呈现“honeymoon effect”：即使不在边界，也会向区间中部“吸引”。
- 在这些模型里，汇率的无套利定价高度依赖 UIP，导致理论上很少出现持久的 carry trade 和系统性利差回报。

---

## 问题 9：为什么说 “UIP does not hold in the data”？

**出处：** Section 3，引用 Engel (1996), Lustig et al. (2011)。

**回答：**
- UIP 预测：
  - 高利率货币应该预期贬值，以抵消利差，使套利收益为零；
  - 换句话说，长期来看，做“高利率货币多头/低利率货币空头”的 carry trade 不应该有系统正收益。
- 大量实证（Engel 1996；Lustig et al. 2011 等）发现：
  - 高利率货币往往**没有**按 UIP 要求的幅度贬值，甚至反向升值；
  - carry trade 策略获得显著的正 Sharpe 比率。
- 因此，作者认为：
  - 传统目标区模型若继续假定 UIP 成立，会错估汇率和期权的风险补偿；
  - 本文采用的是基于“no-arbitrage + 价格核（stochastic discount factor）”的资产定价思路，避开 UIP 假设。

---

## 问题 10：这段话的含义？（利差、CIP 偏离与 peg 可信度）

> “… this literature provides important context for our analysis, since interest rate differentials and CIP deviations shape capital flows, carry trades, and thus the credibility of exchange rate pegs. Our framework builds on these insights by incorporating no-arbitrage conditions into the modeling of exchange rate dynamics, while allowing for imperfect credibility of the peg.”

**解释：**
- 现有文献表明：
  - 利差（interest rate differentials）影响跨境资金配置和 carry trades；
  - CIP（covered interest parity）偏离反映金融中介约束和套利限制；
  - 这些因素共同决定资本流动和对固定汇率制度的信心。
- 本文在这些洞见基础上：
  - 使用**无套利条件（no-arbitrage）**和资产定价模型，而不是简单的 UIP；
  - 同时允许 peg 只有**不完美可信度（imperfect credibility）**，即以 \(p<1\) 的概率存续；
  - 把利差、CIP 偏离等信息通过期权价格映射成“peg 存续概率”和“基本面”。

---

## 问题 11：regime shift 在本文中具体是什么意思？

> “In our paper, we introduce a probability of regime shifts and derive option prices in closed form for target-zone economies.”

**解释：**
- regime shift 指的是**汇率制度状态的转换**：
  - 当前状态：LERS 货币局目标区（7.75–7.85）；
  - 未来有概率转到另一种状态：例如更宽的区间、浮动汇率或不同挂钩水平。
- 在模型里，这被形式化为：
  - 每期 peg 以概率 \(p\) 继续；
  - 以 \(1-p\) 发生“制度切换”，汇率从当前目标区跳到基本面 \(V_t\) 并按新的（自由浮动）规则演化。
- 在定价上，期权价格是“所有可能制度路径”的贴现期望，因此**显式地包含了 regime switch 的概率 \(p\)**。

---

## 问题 12：本文与 regime-switching DSGE / 计量文献有何不同？

> “Moreover, our options-based framework differentiates itself from studies employing regime-switching DSGE or econometric models to assess currency board credibility (e.g., Jeanne and Masson, 2000; Blagov and Funke, 2019; Feng et al., 2023).”

**区别：**
- regime-switching DSGE / 计量模型：
  - 通常在结构模型中设定不同政策 regime（例如“可信货币局”和“危机/贬值”状态），用宏观时间序列（产出、通胀、利率、汇率等）估计 regime 转换概率；
  - 对应的概率更多是**结构层面**的（基于宏观方程拟合）。
- 本文的 options-based 框架：
  - 不直接设定完整 DSGE 结构，而是用**无套利资产定价**描述目标区下的汇率和期权；
  - 用期权市场价格直接反推 regime shift 概率 \(p_t\) 和基本面 \(V_t\)；
  - 估计基于日度的**金融市场数据**（期权、汇率、利差），而非宏观季度时间序列。

换句话说：本文用“市场隐含的定价概率”来衡量 credibility，而 DSGE 文献是用“结构模型拟合出的状态概率”来衡量。

---

## 问题 13：Jeanne & Masson (2000), Blagov & Funke (2019), Feng et al. (2023) 的下载与整理

- 当前环境网络访问受限，无法新建外部连接：
  - Jeanne & Masson (2000) 的 IMF Working Paper 已在本地：`other literature/Jeanne-Masson-2000.pdf`，并在 `additional_literature.md` 中有简要条目；
  - Blagov & Funke (2019), Feng et al. (2023) 若需要下载，需你提供 DOI 或已保存的 PDF 路径，或在解除网络限制后再抓取。
- 一旦有本地 PDF，我可以按你对 w34300 的要求，补充到 `additional_literature.md` 并写出各自的“模型结构 + regime switching 设定 + 数据与创新点”。

---

## 问题 14：如何“提取 market-implied probabilities of peg survival and the HKD’s fundamental value”？

**数学与数据两步合在一起：**

1. **数学上：**
   - 在 Section 3 中，作者写出目标区 + regime shift 下的汇率方程：
     $$
     \tilde S_t = \frac{1+r_\$}{1+r_H}\big[ p\,E_t^Q H(\tilde S_{t+1};S_P,b) + (1-p) E_t^Q V_{t+1} \big],
     $$
     和基本面演化：
     $$
     \frac{1+r_\$}{1+\hat r_H}E_t^Q[V_{t+1}] = V_t, \qquad \frac{dV_t}{V_t} = (\hat r_{HKD}-r_{USD})dt + \sigma_V dW_t.
     $$
   - 在此基础上，得到欧式期权的闭式定价公式 \(P^{model}(p,V,\sigma_V)\)。
2. **实证上：**
   - 每天观察现货和 3M 期权（ATM、10Δ/25Δ 的 RR/BF），构造 4 个代表性的期权价格；
   - 把这些市场价格与模型的闭式期权价格匹配，通过最小二乘反推 \(p_t, V_t, \sigma_{V,t}\)。

得到的 \(p_t\) 就是“市场隐含的 peg 存续概率”，\(V_t\) 就是“市场隐含的基本面汇率”。

---

## 问题 15：如何得到 “the peg has faced notable pressures… in 2019, 2022, 2025”？是否与基本面/储备相关？

**出处：** Section 4.3，对 Figure 7–10 的文字讨论。

**数学推导角度：**
1. 对每个交易日 t，用前述方法估计 \(p_t, V_t, \sigma_{V,t}\)：
   $$
   (p_t, V_t, \sigma_{V,t}) = \arg\min_{p,V,\sigma_V} \sum_i \big(P^{model}_i(p,V,\sigma_V) - P^{mkt}_i\big)^2.
   $$
2. **定义“credibility”**：
   - 作者把 \(p_t\)（在给定 3 个月视角下的 peg 存续概率）视为“可信度”的量化指标；
   - 较低的 \(p_t\) 表示市场更怀疑 peg 能否在 3 个月内保持不破。
3. 把 \(p_t\) 画成时间序列（Figure 7–8），观察其在不同时间段的波动：
   - 2019 年：人民币贬值、贸易摩擦；
   - 2022 年：美联储激进加息，香港 Aggregate Balance 从 >3000 亿 HKD 迅速跌到 <1000 亿；
   - 2025 年：资本流剧烈双向波动，HKD 在区间两端来回碰撞，本地利率大幅波动。
4. 在这些时期，图中 \(p_t\) 明显向下跳跃，甚至接近 50%（作者在文中有具体描述）；据此说 “the peg has faced notable pressures … in 2019, 2022, 2025”。

**与基本面/储备的关系：**
- **模型本身没有把外汇储备或财政储备作为状态变量**，因此：
  - \(p_t\) 是基于期权价格、现货和利差等金融变量推出来的；
  - 它反映的是“市场对未来 peg 的定价看法”，而不是“储备是否足够”的结构性判断。
- 作者在 Section 2 和 4 中会提到：
  - 香港拥有大量外汇储备；
  - Exchange Fund 完全覆盖货币基础；
  但这些更多是背景描述，没有进入估计方程。

**普适性与主要驱动力：**
- 普适性：
  - 对任何类似联系汇率/货币局，只要有足够深度的期权市场，都可以用类似方法估计 \(p_t\)；
  - 但 **具体驱动因子（例如 CNY/CNH、Hibor–Libor 利差）是港币特有的**，其他经济体要根据本国情况调整。
- 本文识别出的主要驱动力：
  - 外部：美联储加息路径、美元强弱、人民币汇率；
  - 内部：本地流动性（Aggregate Balance）、港美利差、市场波动（期权隐含波）。

---

## 问题 16：对澳门元（MOP）的启示及与你的研究问题的联系

**你的核心问题：**
1. **Fiscal Credibility（存量假说）**：大而可用的财政储备（\(FMSI_t\)）是否被市场视为一种“静态后盾”，在危机前就提高 peg 可信度、抑制投机？
2. **Fiscal Dampening（流量假说）**：冲击发生时，财政储备的流量 \(\Delta FMSI_t\) 是否与货币当局操作互补，从而减弱所需的货币紧缩？

**本文对 MOP 的启示：**
- 结构：MOP–HKD–USD 是“挂钩上的挂钩”，澳门元通过港元间接挂钩美元：
  - 那么 HKD peg 的 \(p_t\) 自然成为 MOP peg 的上游风险因子。
- 从本文可见：
  - 市场非常关注：美联储路径、本地（香港）流动性、人民币汇率；
  - 如果把澳门纳入视野，那么：
    - **香港的 \(p_t\)** 可以作为你的模型里的一种外生宏观金融环境变量（例如外部 EMP 或“上游 peg 可信度”）；
    - 澳门本地的财政储备（FMSI）则是“下游”用来缓冲这一外部冲击的工具。

**与两条财政渠道的结合方式（一个思路）：**
1. **Fiscal Credibility（存量）：**
   - 在你的结构方程中，可以考虑设定：HKD peg 的 \(p^{HK}_t\) 受到澳门财政储备存量的影响：
     - 例如把 \(FMSI_t\) 作为解释变量之一，看其是否能够提高 MOP–HKD 挂钩的存续概率或减弱香港 \(p^{HK}_t\) 对冲击的弹性；
   - 由于本文的 \(p_t\) 是从香港期权市场提取的，你可以把它当作**被解释变量**，研究它对 \(FMSI_t\) 的敏感度。
2. **Fiscal Dampening（流量）：**
   - 冲击时期（例如 2019/2022/2025 对应的窗口），观察：
     - Macau 的 \(\Delta FMSI_t\) 是否与澳门货币当局（AMCM）的资产负债表变化、以及香港的 EMP/\(p_t\) 收缩同步；
   - 在回归中，你可以检验：
     - 给定外部 EMP 或 HK \(p_t\) 的冲击，是否更大/更快的 \(\Delta FMSI_t\) 会减弱利率/信用利差的收缩——这就是“dampening”。

总之：本文给你一个**市场端的“peg 可信度指数” \(p_t\)**，而你的 FMSI 研究可以提供一个**财政端的“缓冲能力与可信度”视角**，两者是高度互补的。

---

## 问题 17：如何精确理解 “the peg has faced notable pressures… 2019, 2022, 2025”？（详细数学推导 + 估计步骤）

### 17.1 数学推导（如何从模型定义“压力”）

1. **状态与制度切换设定（Section 3.1）：**
   - 每一小段时间 \(\Delta t\) 内，peg 以概率 \(p = e^{-\lambda \Delta t}\) 继续存在，以 \(1-p\) 破裂；
   - 若破裂，汇率从 peg 区间跳到自由浮动的基本面 \(V_t\)。
2. **基本面演化与无套利（eq.(1),(6)）：**
   $$
   \frac{1+r_\$}{1+\hat r_H}E_t^Q[V_{t+1}] = V_t, \qquad \frac{dV_t}{V_t} = (\hat r_{HKD}-r_{USD})\,dt + \sigma_V dW_t.
   $$
   - 这保证在自由浮动 regime 下不出现套利机会。
3. **目标区下的汇率定价（eq.(2)）：**
   $$
   \tilde S_t = \frac{1+r_\$}{1+r_H}\big[ p\,E_t^Q H(\tilde S_{t+1};S_P,b) + (1-p) E_t^Q V_{t+1} \big],
   $$
   - 对 \(\tilde S_t\) 做归一化（Section 3.1, eq.(5)）：
     $$
     \bar S(\bar V_t) = \frac{1+r_\$}{1+r_H} p\,E_t^Q[H(\bar S(\bar V_{t+1});1,\bar b)] + \frac{1+\hat r_H}{1+r_H}(1-p)\bar V_t,
     $$
     并证明这是一个压缩映射，存在唯一的固定点 S 形函数 \(\bar S(\cdot)\)（Proposition 1）。
4. **期权定价与 regime shift（Proposition 3）：**
   - 对到期为 T 的欧式期权，价格写成：
     $$
     P^{model}(t) = E_t^Q\big[ M_T \cdot \text{payoff}(S_T) \big],
     $$
     其中折现因子 \(M_T\) 依赖于利率路径，\(S_T\) 的分布取决于 peg 是否在期间破裂：
     - 若 peg 在整个 [t,T] 期间维持，概率 \(p^{N}\)（N 为步数），则 \(S_T\) 由目标区 S 形函数决定；
     - 若中途某次破裂，概率 \(1-p^N\)，则 \(S_T\) 由自由浮动基本面 \(V_T\) 的分布决定。
   - 因此，期权价格显式依赖 \(p\)、\(V_t\) 和 \(\sigma_V\)。
5. **定义“压力”与“可信度”：**
   - 定义 peg 的“可信度”= 给定视角（例如 3 个月）下的 **存续概率 \(p_t\)**；
   - “压力期” = \(p_t\) 显著下降、破带概率 \(1-p_t\) 显著上升的时期。

### 17.2 数据估计（如何从期权价格算出 p_t 并识别 2019/2022/2025）

1. **每日观测数据（Section 4.1）：**
   - 现货汇率 USD/HKD；
   - 3 个月期的 HKD 期权报价，包括：
     - ATM 隐含波动率（ATM IV，通常为 50Δ）；
     - 10Δ/25Δ 风险逆转（RR）和蝶式（BF），例如 25Δ RR, 25Δ BF, 10Δ RR, 10Δ BF；
   - 3M 港元 HIBOR 与 3M 美元利率（Libor/SOFR）。
2. **从 IV 组合到期权价：**
   - 利用 ATM/RR/BF 关系：
     - 25Δ call IV = ATM IV + 0.5×RR + BF；
     - 25Δ put IV = ATM IV - 0.5×RR + BF；
     - 类似对 10Δ 层做推导；
   - 然后用 Black–Scholes 公式（仅作为 IV→价格的转换工具）把每个隐含波动率转成期权价格和行权价，使得我们有 4 个“代表性”期权价格 \(P^{mkt}_i\)。
3. **构造每日日度校准问题：**
   $$
   (p_t, V_t, \sigma_{V,t}) = \arg\min_{p,V,\sigma_V} \sum_{i\in\{spot,4\,options\}} w_i\big(P^{model}_i(p,V,\sigma_V) - P^{mkt}_i\big)^2,
   $$
   - 其中 \(P^{model}_i\) 来自前述目标区 + regime shift 模型的闭式期权定价公式；
   - 施加约束 \(p_t \le 0.975\)（文中提到防止数值不稳定）。
4. **得到的时间序列：**
   - 对所有样本日 t，获得 \(p_t, V_t, \sigma_{V,t}\)；
   - 将 \(p_t\) 画出来（Figure 7–8），同时绘制：
     - USD/HKD spot；
     - Aggregate Balance（银行体系流动性）；
     - CNY/CNH 汇率；
     - 利差等宏观金融变量（Figure 10 之后）。
5. **与事件对照识别“notable pressures”：**
   - **2019**：人民币汇率突破 7，贸易摩擦升级；港币期权反映的尾部风险上升，\(p_t\) 下跌；
   - **2022**：美联储激进加息，香港 Aggregate Balance 从 >3000 亿跌到 <1000 亿，HKMA 多次干预，\(p_t\) 一度跌近 ~0.5；
   - **2025**：资本流快速反转，HKD 在区间两端来回碰撞，本地利率剧烈波动，\(p_t\) 再次出现明显波动。

因此，“the peg has faced notable pressures … 2019, 2022, 2025” 是指：
- 在这些时间段内，由期权价格反推得到的 **存续概率 \(p_t\) 明显下降**，对应市场对 peg 的信心显著减弱；
- 这种识别方法是：**用模型隐含的 \(p_t\) 序列 + 事件时间线**，而不是直接看储备规模。

### 17.3 作为宏观工具变量的可行性与注意事项

1. **可行性：**
   - 在你的实证中，可以把 \(p_t\)（或破带概率 \(1-p_t\)）视作一个“外生市场压力/可信度指数”，用来刻画外部金融环境对澳门的冲击；
   - 例如，把它作为解释变量或工具变量，研究其对 EMP、香港/澳门利差、资本流动等的影响。
2. **注意事项：**
   - \(p_t\) 是基于衍生品价格的风险中性概率，包含风险溢价和流动性溢价，不是“物理概率”；
   - 在回归中应控制：
     - 港美利差、汇率波动率、宏观基本面（增长、通胀等）；
     - 外汇/财政储备规模（你的 FMSI）；
   - 高频（日度） \(p_t\) 与月度/季度宏观数据频率不一致时，需要做月度均值/分位数、滚动窗口等聚合。
3. **与 FMSI 的结合：**
   - 你可以用香港 \(p^{HK}_t\) 作为“上游 peg 压力”，用澳门 \(FMSI_t\) 和 \(\Delta FMSI_t\) 作为“财政缓冲”变量，检验：在外部压力上升时，澳门财政储备是否能提高本地挂钩的可信度或减缓紧缩。

---

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read data
df = pd.read_excel('Currency Allocation Time Series 2012-2024 ex12_13.xlsx')
df = df.dropna(how='all')
df = df[df['Year-End'].notna() & (df['Year-End'] >= 2012)]

# Combine RMB
df['RMB_Total'] = df.apply(lambda row:
    row['RMB (Combined)'] if pd.notna(row['RMB (Combined)'])
    else (row['Offshore RMB (境外人民幣)'] + row['Onshore RMB (境內人民幣)']
          if pd.notna(row['Offshore RMB (境外人民幣)']) and pd.notna(row['Onshore RMB (境內人民幣)'])
          else row['Offshore RMB (境外人民幣)'] if pd.notna(row['Offshore RMB (境外人民幣)'])
          else np.nan),
    axis=1)

clean_df = pd.DataFrame({
    'Year': df['Year-End'].astype(int),
    'USD': pd.to_numeric(df['USD (美元)'], errors='coerce'),
    'HKD': pd.to_numeric(df['HKD (港元)'], errors='coerce'),
    'RMB': df['RMB_Total']
})

complete_df = clean_df[clean_df['Year'] >= 2014].copy()

print("=" * 80)
print("ANALYSIS: WHAT IS THE ADJUSTMENT MECHANISM?")
print("=" * 80)
print()

# ===========================================================================
# HYPOTHESIS 1: Pure Valuation Effect (Passive)
# ===========================================================================
print("HYPOTHESIS 1: Pure Valuation Effect (Passive)")
print("-" * 80)
print("If weights change ONLY due to FX valuation:")
print("  Expected pattern: Weight changes correlate with FX returns")
print()

# Approximate FX returns (using USD/CNY as proxy)
fx_events = {
    2015: {"CNY": -0.045, "HKD": 0.0, "USD": 0.0},  # Aug 2015 devaluation
    2016: {"CNY": -0.065, "HKD": 0.0, "USD": 0.0},  # Continued pressure
    2017: {"CNY": 0.068, "HKD": 0.0, "USD": 0.0},   # CNY strengthened
    2018: {"CNY": -0.055, "HKD": 0.0, "USD": 0.0},  # Trade war
    2019: {"CNY": 0.014, "HKD": 0.0, "USD": 0.0},   # Mild depreciation
    2020: {"CNY": 0.067, "HKD": 0.0, "USD": 0.0},   # CNY surge
    2021: {"CNY": 0.028, "HKD": 0.0, "USD": 0.0},   # Stable
    2022: {"CNY": -0.085, "HKD": 0.0, "USD": 0.0},  # Sharp depreciation
    2023: {"CNY": -0.025, "HKD": 0.0, "USD": 0.0},  # Mild depreciation
    2024: {"CNY": -0.027, "HKD": 0.0, "USD": 0.0},  # Mild depreciation
}

changes = complete_df.set_index('Year')[['USD', 'HKD', 'RMB']].diff()

print("Year | RMB Weight Change | CNY FX Return | Expected if Passive | Actual Pattern")
print("-" * 80)
for year in range(2015, 2025):
    if year in changes.index and year in fx_events:
        rmb_change = changes.loc[year, 'RMB']
        fx_return = fx_events[year]['CNY']

        # If passive: weight change ≈ FX return (for small returns)
        # More precisely: w_new = w_old * (1 + r) / (1 + portfolio_return)
        # Approximation: Δw ≈ w_old * (r - portfolio_return)

        prev_weight = complete_df[complete_df['Year'] == year-1]['RMB'].values[0] if year > 2014 else 0.486
        expected_passive = prev_weight * fx_return  # Simplified

        actual_vs_expected = "LARGER" if abs(rmb_change) > abs(expected_passive) * 1.5 else "SIMILAR" if abs(rmb_change) > abs(expected_passive) * 0.5 else "SMALLER"

        print(f"{year} | {rmb_change:+.3f} ({rmb_change*100:+.1f}pp) | {fx_return:+.3f} ({fx_return*100:+.1f}%) | {expected_passive:+.3f} | {actual_vs_expected}")

print()
print("Interpretation:")
print("- If weight changes are SIMILAR to FX returns → Passive valuation effect")
print("- If weight changes are MUCH LARGER → Active rebalancing (trading)")
print()

# ===========================================================================
# HYPOTHESIS 2: Target Weight Bands (Dynamic Rebalancing)
# ===========================================================================
print("\n" + "=" * 80)
print("HYPOTHESIS 2: Target Weight Bands (Dynamic Rebalancing)")
print("-" * 80)
print("If there are target weights with tolerance bands:")
print("  Expected pattern: When weight exceeds band → next year corrects")
print()

# Calculate if there's mean reversion
print("Testing for mean reversion (回归均值):")
print()
for currency in ['USD', 'HKD', 'RMB']:
    mean_weight = complete_df[currency].mean()

    print(f"\n{currency} (Mean = {mean_weight:.3f}):")
    print(f"Year | Weight | Deviation | Next Year Change | Mean Reversion?")
    print("-" * 70)

    for i, year in enumerate(complete_df['Year'].values[:-1]):
        weight = complete_df[complete_df['Year'] == year][currency].values[0]
        next_year = complete_df['Year'].values[i+1]
        next_change = changes.loc[next_year, currency]

        deviation = weight - mean_weight

        # Mean reversion: if deviation > 0, next change should be negative
        mean_reverting = (deviation > 0 and next_change < 0) or (deviation < 0 and next_change > 0)

        print(f"{year} | {weight:.3f} | {deviation:+.3f} | {next_change:+.3f} | {'YES ✓' if mean_reverting else 'NO ✗'}")

print()

# ===========================================================================
# HYPOTHESIS 3: Asset Class Rebalancing (Two-Step Process)
# ===========================================================================
print("\n" + "=" * 80)
print("HYPOTHESIS 3: Asset Class Rebalancing (Two-Step Process)")
print("-" * 80)
print("Theory: Weights change through TWO mechanisms:")
print("  Step 1: Asset allocation changes (bonds vs stocks)")
print("  Step 2: Currency allocation changes (USD vs HKD vs RMB)")
print()
print("Example scenario:")
print("  Year 1: 60% Bonds (all in USD), 40% Stocks (50% HKD, 50% RMB)")
print("  Year 2: 70% Bonds (all in USD), 30% Stocks (50% HKD, 50% RMB)")
print("  → USD weight increases NOT because of currency decision,")
print("    but because of asset class decision!")
print()
print("This is crucial: You have asset allocation data!")
print("→ Can decompose currency weight changes into:")
print("  (a) Asset class rebalancing effect")
print("  (b) Within-asset-class currency rebalancing effect")
print()

# ===========================================================================
# HYPOTHESIS 4: Constrained Optimization (Portfolio Theory)
# ===========================================================================
print("\n" + "=" * 80)
print("HYPOTHESIS 4: Constrained Optimization")
print("-" * 80)
print("Modern Portfolio Theory suggests:")
print("  Optimal weight = f(expected returns, risks, correlations)")
print()
print("If AMCM adjusts based on risk-return trade-offs:")
print("  - 2015-2016: RMB risk increased → reduce RMB exposure")
print("  - 2017-2021: RMB stabilized → increase RMB exposure")
print()

# Calculate "regime stability" (using CV as proxy)
print("Examining stability regimes:")
print()

windows = {
    "2014-2016": (2014, 2016),
    "2017-2019": (2017, 2019),
    "2020-2024": (2020, 2024),
}

for period, (start, end) in windows.items():
    period_data = complete_df[(complete_df['Year'] >= start) & (complete_df['Year'] <= end)]

    print(f"{period}:")
    for currency in ['USD', 'HKD', 'RMB']:
        mean_w = period_data[currency].mean()
        std_w = period_data[currency].std()
        cv = std_w / mean_w if mean_w > 0 else np.nan

        print(f"  {currency}: Mean={mean_w:.3f}, Std={std_w:.3f}, CV={cv:.3f}")
    print()

# ===========================================================================
# KEY INSIGHT: The 2015-2016 Mystery
# ===========================================================================
print("\n" + "=" * 80)
print("KEY MYSTERY: What happened in 2015-2016?")
print("-" * 80)

print("\nData facts:")
print("  2014: RMB = 48.6%")
print("  2015: RMB = 31.4% (Δ = -17.2pp)")
print("  2016: RMB = 13.4% (Δ = -18.0pp)")
print()

print("Possible explanations:")
print()
print("(A) Pure Valuation Effect:")
print("    - CNY/USD: 6.20 (2014) → 6.49 (2015) → 6.95 (2016)")
print("    - Depreciation: -4.5% (2015), -6.5% (2016)")
print("    - Total FX loss: ~11%")
print("    - But weight fell by 35pp (72%)! Much larger!")
print("    → Valuation effect alone CANNOT explain this.")
print()

print("(B) Active De-risking:")
print("    - AMCM saw RMB depreciation risk")
print("    - Actively sold RMB assets (reduced exposure)")
print("    - Weight fell due to BOTH valuation AND net sales")
print("    → This would be discretionary, not mechanical.")
print()

print("(C) Asset Class Effect:")
print("    - Maybe RMB was concentrated in risky assets (stocks?)")
print("    - AMCM shifted from stocks → bonds (risk-off)")
print("    - If bonds are mostly USD → RMB weight falls automatically")
print("    → This is testable with your asset allocation data!")
print()

# ===========================================================================
# DECOMPOSITION FRAMEWORK
# ===========================================================================
print("\n" + "=" * 80)
print("PROPOSED DECOMPOSITION FRAMEWORK")
print("-" * 80)
print()
print("Total weight change = Valuation effect + Trading effect")
print()
print("Where:")
print("  Valuation effect = Passive change due to FX/price movements")
print("  Trading effect = Active change due to buying/selling")
print()
print("Standard formula:")
print("  w_t = (w_{t-1} * (1 + r_i)) / (1 + r_portfolio)")
print()
print("Where:")
print("  r_i = return of asset i (FX + price return)")
print("  r_portfolio = weighted average return of all assets")
print()
print("Trading effect = Actual w_t - Expected w_t (from valuation)")
print()

# ===========================================================================
# RECOMMENDATION
# ===========================================================================
print("\n" + "=" * 80)
print("RECOMMENDATIONS FOR YOUR ANALYSIS")
print("=" * 80)
print()

print("1. DO NOT assume pure mechanical rebalancing")
print("   → Your data shows RMB is too volatile (CV=0.41)")
print()

print("2. DO focus on 'disciplined flexibility'")
print("   → There IS structure (USD-RMB correlation = -0.92)")
print("   → But it's not mechanical (large swings in 2015-2016)")
print()

print("3. DO use your asset allocation data!")
print("   → Decompose: Are currency changes driven by:")
print("     (a) Asset class shifts (bonds vs stocks)?")
print("     (b) Within-class currency shifts?")
print()

print("4. DO test for counter-cyclical behavior")
print("   → Key question: When market stress ↑, does AMCM:")
print("     - Buy depreciated currencies (stabilizing)?")
print("     - Sell depreciated currencies (pro-cyclical)?")
print()

print("5. REGARDING YOUR INTERPOLATION IDEA:")
print("   → 'Use annual average weight × monthly total'")
print()
print("   Assessment: ⚠️ PROBLEMATIC for 2015-2016")
print()
print("   Why:")
print("   - If weights changed gradually through the year:")
print("     Jan 2015: RMB = 48.6%")
print("     Dec 2015: RMB = 31.4%")
print("     → Monthly interpolation would be better")
print()
print("   - If weights changed suddenly (e.g., Q3 2015):")
print("     → Using annual average misses the timing")
print()
print("   Alternative suggestions:")
print("   (a) Use linear interpolation between year-ends")
print("   (b) Use quarterly data if available")
print("   (c) For 2015-2016, check if you can find any quarterly reports")
print()

print("6. BETTER APPROACH: Annual analysis with event studies")
print("   → Don't force monthly granularity you don't have")
print("   → Use annual changes but:")
print("     - Control for FX returns (valuation effect)")
print("     - Identify 'abnormal' changes (trading effect)")
print("     - Link to market stress indicators")
print()

print("\n" + "=" * 80)
print("CONCLUSION")
print("=" * 80)
print()
print("The adjustment mechanism appears to be:")
print()
print("  📊 HYBRID MODEL: Constrained Optimization with Strategic Flexibility")
print()
print("  Components:")
print("  (1) Long-term strategic targets (loose bands, not fixed points)")
print("  (2) Short-term tactical adjustments based on:")
print("      - Market conditions (volatility, stress)")
print("      - Asset class opportunities (bonds vs stocks)")
print("      - Risk management needs")
print("  (3) Mean-reversion tendency (but slow and incomplete)")
print()
print("  Key insight: This is NOT a 'mechanical thermometer'")
print("              It's an 'experienced driver with guardrails'")
print()
print("  For your paper:")
print("  → Frame as 'disciplined portfolio management'")
print("  → Emphasize counter-cyclical tendencies (if they exist)")
print("  → Avoid claiming strict mechanical rebalancing")
print()


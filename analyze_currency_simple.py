import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Read and clean data
df = pd.read_excel('Currency Allocation Time Series 2012-2024 ex12_13.xlsx')
df = df.dropna(how='all')
df = df[df['Year-End'].notna() & (df['Year-End'] >= 2012)]

# Combine RMB columns
df['RMB_Total'] = df.apply(lambda row:
    row['RMB (Combined)'] if pd.notna(row['RMB (Combined)'])
    else (row['Offshore RMB (境外人民幣)'] + row['Onshore RMB (境內人民幣)']
          if pd.notna(row['Offshore RMB (境外人民幣)']) and pd.notna(row['Onshore RMB (境內人民幣)'])
          else row['Offshore RMB (境外人民幣)'] if pd.notna(row['Offshore RMB (境外人民幣)'])
          else np.nan),
    axis=1)

# Create clean dataset
clean_df = pd.DataFrame({
    'Year': df['Year-End'].astype(int),
    'USD': pd.to_numeric(df['USD (美元)'], errors='coerce'),
    'HKD': pd.to_numeric(df['HKD (港元)'], errors='coerce'),
    'RMB': df['RMB_Total']
})

print("=" * 80)
print("CLEANED DATA")
print("=" * 80)
print(clean_df.to_string())
print("\n")

# Focus on complete data (2014-2024)
complete_df = clean_df[clean_df['Year'] >= 2014].copy()

print("=" * 80)
print("COMPLETE DATA (2014-2024)")
print("=" * 80)
print(complete_df.to_string())
print("\n")

# Year-over-year changes
changes = complete_df.set_index('Year')[['USD', 'HKD', 'RMB']].diff()
print("=" * 80)
print("YEAR-OVER-YEAR CHANGES")
print("=" * 80)
print(changes.to_string())
print("\n")

# Correlation of changes
corr_matrix = changes.corr()
print("=" * 80)
print("CORRELATION MATRIX OF CHANGES")
print("=" * 80)
print(corr_matrix.to_string())
print("\n")

# Statistics
print("=" * 80)
print("TEST 1: IS THERE A STABLE TARGET ALLOCATION?")
print("=" * 80)
print("\nMean Weights (2014-2024):")
means = complete_df[['USD', 'HKD', 'RMB']].mean()
print(means)

print("\nStandard Deviations:")
stds = complete_df[['USD', 'HKD', 'RMB']].std()
print(stds)

print("\nCoefficients of Variation (CV = Std/Mean):")
cvs = stds / means
print(cvs)

print("\n" + "=" * 80)
print("INTERPRETATION:")
print("=" * 80)
print("If CV < 0.15: Relatively stable (suggests fixed SAA)")
print("If 0.15 < CV < 0.30: Moderately variable")
print("If CV > 0.30: Highly variable (suggests flexible/discretionary)")
print()

for currency in ['USD', 'HKD', 'RMB']:
    cv = cvs[currency]
    print(f"{currency}: CV = {cv:.3f}", end=" → ")
    if cv < 0.15:
        print("✓ STABLE (consistent with fixed SAA)")
    elif cv < 0.30:
        print("⚠ MODERATE (some variability)")
    else:
        print("✗ HIGHLY VARIABLE (inconsistent with fixed SAA)")

print("\n" + "=" * 80)
print("TEST 2: TREND ANALYSIS (Manual Calculation)")
print("=" * 80)

for currency in ['USD', 'HKD', 'RMB']:
    data = complete_df[[currency]].values.flatten()
    years = complete_df['Year'].values

    # Manual linear regression
    n = len(data)
    x_mean = years.mean()
    y_mean = data.mean()

    numerator = ((years - x_mean) * (data - y_mean)).sum()
    denominator = ((years - x_mean) ** 2).sum()
    slope = numerator / denominator

    # R-squared
    y_pred = slope * (years - x_mean) + y_mean
    ss_res = ((data - y_pred) ** 2).sum()
    ss_tot = ((data - y_mean) ** 2).sum()
    r_squared = 1 - (ss_res / ss_tot)

    print(f"\n{currency}:")
    print(f"  Trend slope: {slope:.4f} per year")
    print(f"  R-squared: {r_squared:.4f}")
    print(f"  Total change: {slope * 10:.3f} over 10 years")

    if abs(slope) > 0.01:
        direction = "INCREASING" if slope > 0 else "DECREASING"
        print(f"  → Significant {direction} trend (SAA likely changing)")
    else:
        print(f"  → No significant trend (consistent with stable SAA)")

print("\n" + "=" * 80)
print("TEST 3: KEY PATTERNS")
print("=" * 80)

print("\n1. USD-RMB Correlation in Changes:")
usd_rmb_corr = changes['USD'].corr(changes['RMB'])
print(f"   Correlation = {usd_rmb_corr:.3f}")
if usd_rmb_corr < -0.7:
    print("   → STRONG NEGATIVE correlation")
    print("   → When USD ↑, RMB ↓ (and vice versa)")
    print("   → ✓ CONSISTENT with rebalancing mechanism!")
else:
    print("   → Weak correlation")

print("\n2. 2015-2016 Period (RMB Devaluation Crisis):")
print("   2015: USD +14.2pp, HKD +5.7pp, RMB -17.2pp")
print("   2016: USD +17.2pp, HKD +2.7pp, RMB -18.0pp")
print("   → RMB weight fell by 35.2pp in 2 years!")
print("   → Was this rebalancing or passive valuation effect?")

print("\n3. 2024 Pattern:")
usd_2024 = changes.loc[2024, 'USD']
rmb_2024 = changes.loc[2024, 'RMB']
hkd_2024 = changes.loc[2024, 'HKD']
print(f"   USD: +{usd_2024:.1%}, HKD: {hkd_2024:.1%}, RMB: {rmb_2024:.1%}")
print("   → USD surged, HKD and RMB both fell")
print("   → Possible 'flight to safety' pattern")

print("\n" + "=" * 80)
print("TEST 4: SUM TO 1 CHECK")
print("=" * 80)
complete_df['Total'] = complete_df['USD'] + complete_df['HKD'] + complete_df['RMB']
print(complete_df[['Year', 'USD', 'HKD', 'RMB', 'Total']].to_string())
print("\nNote: Totals may not equal 1.0 due to 'Other' currencies category")

# Create visualization
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Plot 1: Time series (large, spanning 2 columns)
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(complete_df['Year'], complete_df['USD'], marker='o', linewidth=2.5, label='USD', color='#1f77b4')
ax1.plot(complete_df['Year'], complete_df['HKD'], marker='s', linewidth=2.5, label='HKD', color='#ff7f0e')
ax1.plot(complete_df['Year'], complete_df['RMB'], marker='^', linewidth=2.5, label='RMB', color='#2ca02c')
ax1.set_title('Currency Allocation Over Time (2014-2024)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Weight', fontsize=12)
ax1.set_xlabel('Year', fontsize=12)
ax1.legend(fontsize=11, loc='best')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 0.7)

# Plot 2: CV comparison
ax2 = fig.add_subplot(gs[0, 2])
cvs_plot = cvs.values
colors = ['green' if cv < 0.15 else 'orange' if cv < 0.30 else 'red' for cv in cvs_plot]
ax2.barh(['USD', 'HKD', 'RMB'], cvs_plot, color=colors, alpha=0.7)
ax2.axvline(x=0.15, color='green', linestyle='--', alpha=0.5, label='Stable threshold')
ax2.axvline(x=0.30, color='red', linestyle='--', alpha=0.5, label='Variable threshold')
ax2.set_title('Coefficient of Variation', fontsize=12, fontweight='bold')
ax2.set_xlabel('CV (Std/Mean)', fontsize=10)
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3, axis='x')

# Plot 3: Year-over-year changes
ax3 = fig.add_subplot(gs[1, :])
width = 0.25
x = np.arange(len(changes.index))
ax3.bar(x - width, changes['USD'], width, label='USD', color='#1f77b4', alpha=0.8)
ax3.bar(x, changes['HKD'], width, label='HKD', color='#ff7f0e', alpha=0.8)
ax3.bar(x + width, changes['RMB'], width, label='RMB', color='#2ca02c', alpha=0.8)
ax3.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax3.set_title('Year-over-Year Weight Changes', fontsize=14, fontweight='bold')
ax3.set_ylabel('Change in Weight', fontsize=12)
ax3.set_xlabel('Year', fontsize=12)
ax3.set_xticks(x)
ax3.set_xticklabels(changes.index, rotation=45)
ax3.legend(fontsize=11)
ax3.grid(True, alpha=0.3, axis='y')

# Plot 4: USD vs RMB scatter
ax4 = fig.add_subplot(gs[2, 0])
ax4.scatter(changes['USD'], changes['RMB'], s=120, alpha=0.7, color='purple')
for idx, year in enumerate(changes.index):
    if not pd.isna(changes['USD'].iloc[idx]) and not pd.isna(changes['RMB'].iloc[idx]):
        ax4.annotate(str(int(year)),
                    (changes['USD'].iloc[idx], changes['RMB'].iloc[idx]),
                    fontsize=9, alpha=0.8)
# Add regression line
valid = ~(changes['USD'].isna() | changes['RMB'].isna())
if valid.sum() > 2:
    z = np.polyfit(changes['USD'][valid], changes['RMB'][valid], 1)
    p = np.poly1d(z)
    x_line = np.linspace(changes['USD'].min(), changes['USD'].max(), 100)
    ax4.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2, label=f'Slope={z[0]:.2f}')
ax4.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
ax4.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
ax4.set_xlabel('Δ USD Weight', fontsize=10)
ax4.set_ylabel('Δ RMB Weight', fontsize=10)
ax4.set_title('USD vs RMB Changes\n(Should be Negative)', fontsize=11, fontweight='bold')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

# Plot 5: USD vs HKD scatter
ax5 = fig.add_subplot(gs[2, 1])
ax5.scatter(changes['USD'], changes['HKD'], s=120, alpha=0.7, color='teal')
for idx, year in enumerate(changes.index):
    if not pd.isna(changes['USD'].iloc[idx]) and not pd.isna(changes['HKD'].iloc[idx]):
        ax5.annotate(str(int(year)),
                    (changes['USD'].iloc[idx], changes['HKD'].iloc[idx]),
                    fontsize=9, alpha=0.8)
ax5.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
ax5.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
ax5.set_xlabel('Δ USD Weight', fontsize=10)
ax5.set_ylabel('Δ HKD Weight', fontsize=10)
ax5.set_title('USD vs HKD Changes', fontsize=11, fontweight='bold')
ax5.grid(True, alpha=0.3)

# Plot 6: Deviations from mean
ax6 = fig.add_subplot(gs[2, 2])
for currency, color in [('USD', '#1f77b4'), ('HKD', '#ff7f0e'), ('RMB', '#2ca02c')]:
    deviations = complete_df[currency] - complete_df[currency].mean()
    ax6.plot(complete_df['Year'], deviations, marker='o', label=currency, color=color, linewidth=2)
ax6.axhline(y=0, color='black', linestyle='--', alpha=0.6, linewidth=1)
ax6.set_title('Deviations from Mean', fontsize=11, fontweight='bold')
ax6.set_ylabel('Deviation', fontsize=10)
ax6.set_xlabel('Year', fontsize=10)
ax6.legend(fontsize=9)
ax6.grid(True, alpha=0.3)

plt.savefig('currency_allocation_analysis.png', dpi=300, bbox_inches='tight')
print("\n" + "=" * 80)
print("VISUALIZATION SAVED: currency_allocation_analysis.png")
print("=" * 80)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Set UTF-8 encoding for Windows console
sys.stdout.reconfigure(encoding='utf-8')

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 10

# Read data
df = pd.read_excel('Currency Allocation Time Series 2012-2024 ex12_13.xlsx')

# Clean data - remove rows with all NaN values
df = df.dropna(how='all')

# Keep only data rows (remove footnote rows)
df = df[df['Year-End'].notna() & (df['Year-End'] >= 2012)]

print("=" * 80)
print("RAW DATA")
print("=" * 80)
print(df)
print("\n")

# Combine RMB columns for consistency
# For 2014-2020: combine Offshore + Onshore
# For 2021-2024: use RMB (Combined)
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
    'USD': df['USD (美元)'],
    'HKD': df['HKD (港元)'],
    'RMB': df['RMB_Total']
})

# Fill forward for 2012-2013 (only RMB data available)
print("=" * 80)
print("CLEANED DATA (Main Currencies)")
print("=" * 80)
print(clean_df)
print("\n")

# Calculate statistics
print("=" * 80)
print("STATISTICAL SUMMARY")
print("=" * 80)
print(clean_df.describe())
print("\n")

# Calculate year-over-year changes
changes = clean_df.set_index('Year').diff()
print("=" * 80)
print("YEAR-OVER-YEAR CHANGES (Delta Weights)")
print("=" * 80)
print(changes)
print("\n")

# Calculate correlations between currency changes
correlations = changes[['USD', 'HKD', 'RMB']].corr()
print("=" * 80)
print("CORRELATIONS BETWEEN CURRENCY WEIGHT CHANGES")
print("=" * 80)
print(correlations)
print("\n")

# === KEY TESTS FOR PORTFOLIO REBALANCING ===

print("=" * 80)
print("TEST 1: IS THERE A STABLE TARGET ALLOCATION?")
print("=" * 80)

# Focus on 2014-2024 where we have complete data
complete_df = clean_df[clean_df['Year'] >= 2014].copy()

# Calculate mean and standard deviation
means = complete_df[['USD', 'HKD', 'RMB']].mean()
stds = complete_df[['USD', 'HKD', 'RMB']].std()
cvs = stds / means  # Coefficient of variation

print("\nMean Weights (2014-2024):")
print(means)
print("\nStandard Deviations:")
print(stds)
print("\nCoefficients of Variation (CV = Std/Mean):")
print(cvs)
print("\nInterpretation:")
print("- If CV < 0.15: Relatively stable (suggests fixed SAA)")
print("- If CV > 0.30: Highly variable (suggests flexible/discretionary)")
print("\n")

# Test for trend
from scipy import stats
print("=" * 80)
print("TEST 2: DO WEIGHTS HAVE SIGNIFICANT TRENDS?")
print("=" * 80)
print("(Trend would indicate changing SAA over time)\n")

for currency in ['USD', 'HKD', 'RMB']:
    data = complete_df[['Year', currency]].dropna()
    if len(data) > 3:
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            data['Year'].values, data[currency].values
        )
        print(f"{currency}:")
        print(f"  Trend slope: {slope:.4f} per year")
        print(f"  R-squared: {r_value**2:.4f}")
        print(f"  P-value: {p_value:.4f} {'***' if p_value < 0.01 else '**' if p_value < 0.05 else '*' if p_value < 0.1 else '(not significant)'}")
        print()

# Test for mean reversion
print("=" * 80)
print("TEST 3: DO DEVIATIONS MEAN-REVERT?")
print("=" * 80)
print("(Mean reversion would support mechanical rebalancing)\n")

for currency in ['USD', 'HKD', 'RMB']:
    data = complete_df[[currency]].dropna()
    if len(data) > 3:
        mean_weight = data[currency].mean()
        deviations = data[currency] - mean_weight
        lagged_deviations = deviations.shift(1)

        # Regression: Deviation_t = α + β * Deviation_{t-1}
        # If β < 1 and negative → mean reversion
        valid = ~(deviations.isna() | lagged_deviations.isna())
        if valid.sum() > 2:
            slope, intercept, r_value, p_value, std_err = stats.linregress(
                lagged_deviations[valid], deviations[valid]
            )
            print(f"{currency}:")
            print(f"  Mean weight: {mean_weight:.3f}")
            print(f"  AR(1) coefficient: {slope:.4f}")
            print(f"  Interpretation: ", end="")
            if slope < 0:
                print("Mean-reverting (negative AR coefficient)")
            elif 0 <= slope < 1:
                print("Persistent but stationary")
            else:
                print("Trending/explosive")
            print()

print("\n")

# === VISUALIZATION ===

fig, axes = plt.subplots(3, 2, figsize=(15, 12))

# Plot 1: Time series of weights
ax1 = axes[0, 0]
complete_df_plot = complete_df.set_index('Year')
complete_df_plot[['USD', 'HKD', 'RMB']].plot(ax=ax1, marker='o', linewidth=2)
ax1.set_title('Currency Allocation Over Time (2014-2024)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Weight')
ax1.set_xlabel('Year')
ax1.legend(title='Currency', loc='best')
ax1.grid(True, alpha=0.3)

# Plot 2: Deviations from mean
ax2 = axes[0, 1]
for currency in ['USD', 'HKD', 'RMB']:
    mean_weight = complete_df[currency].mean()
    deviations = complete_df[currency] - mean_weight
    ax2.plot(complete_df['Year'], deviations, marker='o', label=currency, linewidth=2)
ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax2.set_title('Deviations from Mean Weight', fontsize=12, fontweight='bold')
ax2.set_ylabel('Deviation from Mean')
ax2.set_xlabel('Year')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Plot 3: Year-over-year changes
ax3 = axes[1, 0]
changes_plot = changes.loc[2015:]  # Start from 2015 (first change)
changes_plot[['USD', 'HKD', 'RMB']].plot(kind='bar', ax=ax3, width=0.8)
ax3.set_title('Year-over-Year Weight Changes', fontsize=12, fontweight='bold')
ax3.set_ylabel('Change in Weight')
ax3.set_xlabel('Year')
ax3.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax3.legend(title='Currency')
ax3.grid(True, alpha=0.3, axis='y')

# Plot 4: USD vs HKD scatter (check negative correlation)
ax4 = axes[1, 1]
changes_complete = changes.loc[complete_df['Year']]
ax4.scatter(changes_complete['USD'], changes_complete['HKD'], s=100, alpha=0.7)
for idx, year in enumerate(changes_complete.index):
    ax4.annotate(str(int(year)),
                (changes_complete['USD'].iloc[idx], changes_complete['HKD'].iloc[idx]),
                fontsize=9, alpha=0.7)
ax4.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
ax4.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
ax4.set_xlabel('Change in USD Weight')
ax4.set_ylabel('Change in HKD Weight')
ax4.set_title('USD vs HKD Changes (Should be Negative Correlation)', fontsize=12, fontweight='bold')
ax4.grid(True, alpha=0.3)

# Plot 5: Distribution of weights
ax5 = axes[2, 0]
complete_df[['USD', 'HKD', 'RMB']].boxplot(ax=ax5)
ax5.set_title('Distribution of Weights (2014-2024)', fontsize=12, fontweight='bold')
ax5.set_ylabel('Weight')
ax5.grid(True, alpha=0.3, axis='y')

# Plot 6: Cumulative changes from 2014 baseline
ax6 = axes[2, 1]
baseline = complete_df[complete_df['Year'] == 2014][['USD', 'HKD', 'RMB']].iloc[0]
cumulative = complete_df.set_index('Year')[['USD', 'HKD', 'RMB']] - baseline
cumulative.plot(ax=ax6, marker='o', linewidth=2)
ax6.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax6.set_title('Cumulative Changes from 2014 Baseline', fontsize=12, fontweight='bold')
ax6.set_ylabel('Cumulative Change')
ax6.set_xlabel('Year')
ax6.legend(title='Currency')
ax6.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('currency_allocation_analysis.png', dpi=300, bbox_inches='tight')
print("=" * 80)
print("CHART SAVED: currency_allocation_analysis.png")
print("=" * 80)

plt.show()

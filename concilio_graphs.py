import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# TECHNOLOGY ASSESSMENT

# # Create DataFrame
data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'With Internet': [776401, 798760, 804667, 885119, 916765, 927525],
    'Without Internet': [161037, 141827, 141329, 89943, 76230, 65787],
    'Has Computer': [857816, 874102, 874345, 935800, 961753, 969229],
    'No Computer': [79622, 66485, 71651, 39262, 31242, 24083]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Calculate percentages
df_pct = df.div(df[['With Internet', 'Without Internet']].sum(axis=1), axis=0) * 100

# Set style
plt.style.use('seaborn-v0_8')

# GRAPH 1: Internet Subscription Trends
plt.figure(figsize=(10, 6))
ax = plt.gca()

# Plot lines
with_internet = ax.plot(df.index, df['With Internet'], 
                       marker='o', color='#ff9999', 
                       linewidth=2.5, label='With Internet')
without_internet = ax.plot(df.index, df['Without Internet'], 
                          marker='o', color='#66b3ff', 
                          linewidth=2.5, label='Without Internet')

# Add data labels
for year in df.index:
    ax.annotate(f"{df.loc[year, 'With Internet']/1000:.0f}K", 
               (year, df.loc[year, 'With Internet']), 
               textcoords="offset points", xytext=(0,10), 
               ha='center', fontsize=10, color='#ff9999')
    ax.annotate(f"{df.loc[year, 'Without Internet']/1000:.0f}K", 
               (year, df.loc[year, 'Without Internet']), 
               textcoords="offset points", xytext=(0,10), 
               ha='center', fontsize=10, color='#66b3ff')

# Formatting
plt.title('Dallas County Internet Subscription Trends (2018-2023)', 
         fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Households', fontsize=12)
plt.legend(fontsize=12, frameon=True)
plt.grid(True, alpha=0.3)
plt.xticks(df.index)

# Save and show
plt.tight_layout()
plt.savefig('Dallas_Internet_Trends.png', dpi=300, bbox_inches='tight')
plt.show()

# GRAPH 2: Computer Ownership Trends
plt.figure(figsize=(10, 6))
ax = plt.gca()

# Plot lines
has_computer = ax.plot(df.index, df['Has Computer'], 
                      marker='o', color='#3498db', 
                      linewidth=2.5, label='Has Computer')
no_computer = ax.plot(df.index, df['No Computer'], 
                     marker='o', color='#f39c12', 
                     linewidth=2.5, label='No Computer')

# Add data labels
for year in df.index:
    ax.annotate(f"{df.loc[year, 'Has Computer']/1000:.0f}K", 
               (year, df.loc[year, 'Has Computer']), 
               textcoords="offset points", xytext=(0,10), 
               ha='center', fontsize=10, color='#3498db')
    ax.annotate(f"{df.loc[year, 'No Computer']/1000:.0f}K", 
               (year, df.loc[year, 'No Computer']), 
               textcoords="offset points", xytext=(0,10), 
               ha='center', fontsize=10, color='#f39c12')

# Formatting
plt.title('Dallas County Computer Ownership Trends (2018-2023)', 
         fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Households', fontsize=12)
plt.legend(fontsize=12, frameon=True)
plt.grid(True, alpha=0.3)
plt.xticks(df.index)

# Save and show
plt.tight_layout()
plt.savefig('Dallas_Computer_Trends.png', dpi=300, bbox_inches='tight')
plt.show()


# Create DataFrame from your data
data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'With Internet': [776401, 798760, 804667, 885119, 916765, 927525],
    'Without Internet': [161037, 141827, 141329, 89943, 76230, 65787],
    'Has Computer': [857816, 874102, 874345, 935800, 961753, 969229],
    'No Computer': [79622, 66485, 71651, 39262, 31242, 24083]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Calculate percentages for annotation
df_pct = df.div(df[['With Internet', 'Without Internet']].sum(axis=1), axis=0) * 100

# Set a modern style
plt.style.use('seaborn-v0_8')

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('Dallas County Technology Adoption Trends (2018-2023)', fontsize=16, y=1.02)

# Chart 1: Internet Subscription Status
ax1.plot(df.index, df['With Internet'], marker='o', color='#2ecc71', linewidth=2.5, label='With Internet')
ax1.plot(df.index, df['Without Internet'], marker='o', color='#e74c3c', linewidth=2.5, label='Without Internet')

# Add percentage annotations
for year in df.index:
    ax1.annotate(f"{df_pct.loc[year, 'With Internet']:.1f}%", 
                (year, df.loc[year, 'With Internet']), 
                textcoords="offset points", xytext=(0,10), 
                ha='center', fontsize=10)
    ax1.annotate(f"{df_pct.loc[year, 'Without Internet']:.1f}%", 
                (year, df.loc[year, 'Without Internet']), 
                textcoords="offset points", xytext=(0,10), 
                ha='center', fontsize=10)

ax1.set_title('Internet Subscription Trends', fontsize=14, pad=15)
ax1.set_ylabel('Number of Households', fontsize=12)
ax1.legend(fontsize=12)
ax1.grid(True, alpha=0.3)
ax1.set_xticks(df.index)

# Chart 2: Computer Ownership Status
ax2.plot(df.index, df['Has Computer'], marker='o', color='#3498db', linewidth=2.5, label='Has Computer')
ax2.plot(df.index, df['No Computer'], marker='o', color='#f39c12', linewidth=2.5, label='No Computer')

# Add value annotations
for year in df.index:
    ax2.annotate(f"{df.loc[year, 'Has Computer']/1000:.1f}K", 
                (year, df.loc[year, 'Has Computer']), 
                textcoords="offset points", xytext=(0,10), 
                ha='center', fontsize=10)
    ax2.annotate(f"{df.loc[year, 'No Computer']/1000:.1f}K", 
                (year, df.loc[year, 'No Computer']), 
                textcoords="offset points", xytext=(0,10), 
                ha='center', fontsize=10)

ax2.set_title('Computer Ownership Trends', fontsize=14, pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Number of Households', fontsize=12)
ax2.legend(fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.set_xticks(df.index)

plt.tight_layout()
plt.show()


df = pd.read_excel('/Users/taylorvander/VS Code/hackathon/Concilio Raw Data.xlsx')
print(df.columns)
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

# Clean and convert Age to numeric
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df.dropna(subset=['Age'], inplace=True)

# Improved Box Plot with Seaborn
plt.figure(figsize=(8, 8))  # Increased figure height to 8 inches

# Define color to match pie charts (use the first color)
box_color = '#ff9999'

sns.boxplot(y=df['Age'], color=box_color, linewidth=1.5, fliersize=5, 
            flierprops={'marker': 'x', 'markerfacecolor': 'red'})

plt.title("Age Distribution", fontsize=16, pad=15)
plt.ylabel("Age (Years)", fontsize=12)

plt.xticks([])  # Remove x-axis ticks 

plt.grid(axis='y', linestyle='--', alpha=0.7)

sns.despine(left=True)

# Adjust y-axis limits to provide extra space
min_age = df['Age'].min()
max_age = df['Age'].max()
plt.ylim(min_age - (max_age - min_age) * 0.1, max_age + (max_age - min_age) * 0.1) 

plt.tight_layout()

plt.show()

# PIE CHART FOR # OF ADULTS

# Clean and convert to numeric
df['# of Adults in Household'] = pd.to_numeric(df['# of Adults in Household'], errors='coerce')
df.dropna(subset=['# of Adults in Household'], inplace=True)

# Convert to integers (e.g., 1.0 → 1)
df['# of Adults in Household'] = df['# of Adults in Household'].astype(int)

# Group categories: 1-5 separate, 6+ as "6+"
df['Adults Grouped'] = df['# of Adults in Household'].apply(lambda x: str(x) if x <= 5 else '6+')

# Count occurrences and sort
adults_distribution = df['Adults Grouped'].value_counts().sort_index()
adults_distribution = adults_distribution.reindex([str(i) for i in range(1, 6)] + ['6+'], fill_value=0)

# Define colors (matching previous color schemes)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 'gold'] # Adjusted colors

# Create pie chart WITHOUT percentages inside the wedges
plt.figure(figsize=(10, 10))
wedges, texts = plt.pie(
    adults_distribution,
    labels=None,  # No labels outside
    autopct=None, # No percentages inside
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 0.5},
    textprops={'fontsize': 12, 'color': 'black', 'weight': 'bold'}
)

# Create enhanced legend
legend_labels = [f"{adult} ({pct:.1f}%)" for adult, pct in
                zip(adults_distribution.index, adults_distribution / adults_distribution.sum() * 100)]
legend = plt.legend(
    legend_labels,
    title="# of Adults",
    loc="center left", # Change loc to center left
    bbox_to_anchor=(1.05, 0.5), # Adjust bbox_to_anchor
    prop={'size': 12},
    title_fontsize='14'
)


plt.title('Distribution of Adults in Household', pad=20, fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.show()


# PIE CHART FOR RACE
# Load and clean data
df['Race/Ethnicity'] = df['Race/Ethnicity'].str.strip().str.title()
df.dropna(subset=['Race/Ethnicity'], inplace=True)

# Standardize categories
df['Race/Ethnicity'] = df['Race/Ethnicity'].replace({
    'African American': 'Black Or African American',
    'Black': 'Black Or African American'
})

# Get counts and select top categories
race_counts = df['Race/Ethnicity'].value_counts()
top_n = 3  # Show top 3 categories + Other
top_races = race_counts.head(top_n)
other_count = race_counts[top_n:].sum()

# Create final distribution
final_distribution = top_races.copy()
final_distribution['Other'] = other_count

# Define colors
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create pie chart with EXTERNAL percentages
plt.figure(figsize=(12, 8))  # Wider figure for external labels

# Use labeldistance=1.1 to start labels just outside the pie
wedges, texts = plt.pie(  # removed autotexts from return values
    final_distribution,
    labels=None,  # Do not display labels inside the pie slices
    autopct=None,  # Do not display percentages inside the pie slices
    startangle=90,
    colors=colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1},
    textprops={
        'fontsize': 14,
        'weight': 'bold',
        'color': 'black'
    }
)

# Create enhanced legend
legend_labels = [f"{race} ({pct:.1f}%)" for race, pct in 
                zip(final_distribution.index, final_distribution/final_distribution.sum()*100)]
legend = plt.legend(
    legend_labels,
    title="Race/Ethnicity",
    loc="center left", # Change loc to center left
    bbox_to_anchor=(1.05, 0.5), # Adjust bbox_to_anchor
    prop={'size': 12},
    title_fontsize=14
)

plt.title('Race/Ethnicity Distribution', fontsize=16, pad=20)
plt.axis('equal')
plt.tight_layout()
plt.show()


# PIE CHART FOR GENDER
# Load and clean data
df['Gender'] = df['Gender'].str.strip().str.title()
df.dropna(subset=['Gender'], inplace=True)

# Get counts and select top categories
gender_counts = df['Gender'].value_counts()
top_n = 5  # Show top 5 categories
top_genders = gender_counts.head(top_n)

# Create final distribution (no 'Other' category)
final_distribution = top_genders.copy()

# Define colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']  # Added a 5th color

# Create pie chart with EXTERNAL percentages
plt.figure(figsize=(12, 8))

wedges, texts = plt.pie(
    final_distribution,
    labels=None,
    autopct=None,
    startangle=90,
    colors=colors,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1},
    textprops={
        'fontsize': 14,
        'weight': 'bold',
        'color': 'black'
    }
)

# Create enhanced legend
legend_labels = [f"{gender} ({pct:.1f}%)" for gender, pct in
                zip(final_distribution.index, final_distribution / final_distribution.sum() * 100)]

# Filter out "Other" from the legend labels
legend_labels = [label for label in legend_labels if "Other" not in label]

legend = plt.legend(
    legend_labels,
    title="Gender Distribution",
    loc="center left", # Change loc to center left
    bbox_to_anchor=(1.05, 0.5), # Adjust bbox_to_anchor
    prop={'size': 12},
    title_fontsize=14
)

plt.title('Gender Distribution', fontsize=16, pad=20)
plt.axis('equal')
plt.tight_layout()
plt.show()

# BAR CHART FOR ZIP CODE

# Convert to string and remove '.0'
df['Mailing Zip/Postal Code'] = df['Mailing Zip/Postal Code'].astype(str).str.replace('.0', '')

# Load and clean data
df['Mailing Zip/Postal Code'] = df['Mailing Zip/Postal Code'].str.strip()
df.dropna(subset=['Mailing Zip/Postal Code'], inplace=True)

# Get counts
zip_counts = df['Mailing Zip/Postal Code'].value_counts()

# Select top 10 (or all if there are 10 or fewer)
top_n = 10
top_zips = zip_counts.head(top_n)

# Define Colors to Match Pie Charts
pie_chart_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 'gold', '#8fbc8f', '#dda0dd', '#b0e0e6', '#fa8072'] # Extended for 10
bar_chart_colors = pie_chart_colors[:len(top_zips)] # Adjust for the actual number of bars

# Create Bar Chart with Matching Colors
plt.figure(figsize=(10, 6))
sns.barplot(x=top_zips.index, y=top_zips.values, palette=bar_chart_colors)
plt.xlabel("Zip Code")
plt.ylabel("Count")
plt.title("Top Zip Code Distribution", fontsize=16)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

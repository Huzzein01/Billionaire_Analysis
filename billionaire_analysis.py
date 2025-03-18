# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("/Users/admin88/Documents/Data_Analyst_Projects /billionaire_analysis/billionaire_csv.csv")
print(df.columns)

df.columns = df.columns.str.strip()
# Basic data cleaning (ensure correct types)
df['Age'] = df['Age'].astype(float)
df['country'] = df['country'].astype(str)
df['gender'] = df['gender'].astype(str)
df['category'] = df['category'].astype(str)

# -----------------------------------------
# 📊 1. AGE DISTRIBUTION
plt.figure(figsize=(10,6))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title("Age Distribution of Billionaires")
plt.xlabel("Age")
plt.ylabel("Number of Billionaires")
plt.tight_layout()
plt.show()

# -----------------------------------------
# 🌍 2. Billionaire Count by Country
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title("Top 10 Countries by Number of Billionaires")
plt.xlabel("Count")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# -----------------------------------------
# 🏢 3. Billionaire Count by Category
top_categories = df['category'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_categories.values, y=top_categories.index, palette='coolwarm')
plt.title("Top 10 Categories by Number of Billionaires")
plt.xlabel("Count")
plt.ylabel("Category")
plt.tight_layout()
plt.show()

# -----------------------------------------
# 🚻 4. Gender Distribution
gender_dist = df['gender'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(gender_dist, labels=gender_dist.index, autopct='%1.1f%%', colors=['lightcoral', 'lightblue'], startangle=140)
plt.title("Gender Distribution of Billionaires")
plt.axis('equal')
plt.tight_layout()
plt.show()

# -----------------------------------------
# 💰 5. Average Age & Count by Industry
industry_summary = df.groupby('industries').agg({'Age':'mean', 'personName':'count'}).rename(columns={'personName':'Billionaire Count'})
industry_summary = industry_summary.sort_values(by='Billionaire Count', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=industry_summary['Billionaire Count'], y=industry_summary.index, palette='magma')
plt.title("Top 10 Industries by Billionaire Count")
plt.xlabel("Billionaire Count")
plt.ylabel("Industry")
plt.tight_layout()
plt.show()

# -----------------------------------------
# 📈 6. Age vs. Net Worth (Estimated Net Worth not in current dataset, so simulate or replace)
# If your dataset has a 'net_worth' column, use it below. Otherwise, skip this block.

# Example: Assume df['finalWorth'] exists in billions (adjust accordingly)
sns.scatterplot(data=df, x='Age', y='finalWorth', hue='gender')
plt.title("Age vs Net Worth of Billionaires")
plt.xlabel("Age")
plt.ylabel("Net Worth (in billions)")
plt.tight_layout()
plt.show()


# 📝 7. Quick Summary Stats
print("\n📌 Summary Statistics:")
print(df.describe(include='all'))

print("\n📌 Top 10 Countries by Billionaire Count:")
print(df['country'].value_counts().head(10))

print("\n📌 Top 10 Categories by Billionaire Count:")
print(df['category'].value_counts().head(10))

print("\n📌 Gender Distribution:")
print(df['gender'].value_counts())

print("\n📌 Average Age of Billionaires:")
print(round(df['Age'].mean(), 2))

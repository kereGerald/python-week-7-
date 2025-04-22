import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv('sales_data.csv')
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: The file 'sales_data.csv' was not found. Please check the path.")
    exit()

# Display the first few rows
print("🔍 First five rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\n📊 Dataset Info:")
print(df.info())

print("\n🔎 Missing Values:")
print(df.isnull().sum())

# Handle missing values by filling numeric columns with their mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Descriptive statistics
print("\n📈 Descriptive Statistics:")
print(df.describe())

# Grouping: Average Total Sales by Region
grouped = df.groupby('Region')['Total_Sales'].mean()
print("\n📌 Average Total Sales by Region:")
print(grouped)

# Insights
print("\n💡 Insight: Highest average sales region:")
print(f"{grouped.idxmax()} with average sales of {grouped.max():.2f}")

# Convert Date to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# ====== 📊 Visualizations ======

# 1. Line Chart - Total Sales Over Time
plt.figure(figsize=(10, 5))
df_sorted = df.sort_values('Date')
plt.plot(df_sorted['Date'], df_sorted['Total_Sales'], marker='o', linestyle='-')
plt.title("📈 Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average Total Sales by Region
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped.index, y=grouped.values, palette='viridis')
plt.title("📊 Average Sales by Region")
plt.xlabel("Region")
plt.ylabel("Average Total Sales")
plt.tight_layout()
plt.show()

# 3. Histogram - Distribution of Total Sales
plt.figure(figsize=(8, 5))
plt.hist(df['Total_Sales'], bins=15, color='skyblue', edgecolor='black')
plt.title("📦 Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter Plot - Quantity vs. Total Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Quantity', y='Total_Sales', data=df, hue='Region', palette='Set2')
plt.title("🔁 Quantity vs. Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

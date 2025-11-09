# Traffic Accident Data Analysis
# Author: U Avinash Naidu

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("traffic_accidents.csv")

# Display basic info
print("First 5 rows of data:")
print(data.head(), "\n")
print("Data summary:")
print(data.info(), "\n")

# Clean and preprocess data
data['Date'] = pd.to_datetime(data['Date'])
data.fillna("Unknown", inplace=True)

# 1️⃣ Accidents by Cause
plt.figure(figsize=(8,5))
data['Cause'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Most Common Causes of Road Accidents')
plt.xlabel('Cause')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# 2️⃣ Accidents by Weather
plt.figure(figsize=(7,5))
sns.countplot(x='Weather', data=data, palette='coolwarm')
plt.title('Accidents by Weather Condition')
plt.show()

# 3️⃣ Accidents by Location
plt.figure(figsize=(8,5))
sns.countplot(y='Location', data=data, order=data['Location'].value_counts().index, palette='viridis')
plt.title('Accidents by Location')
plt.show()

# 4️⃣ Accidents by Vehicle Type
plt.figure(figsize=(7,5))
sns.countplot(x='Vehicle_Type', data=data, palette='magma')
plt.title('Accidents by Vehicle Type')
plt.show()

# Summary
print("📊 Total Accidents:", len(data))
print("💀 Total Fatalities:", data['Fatalities'].sum())
print("🤕 Total Injuries:", data['Injuries'].sum())

# Insights
print("\n🔹 Top Accident Cause:\n", data['Cause'].value_counts().head(1))
print("\n🔹 City with Most Accidents:\n", data['Location'].value_counts().head(1))

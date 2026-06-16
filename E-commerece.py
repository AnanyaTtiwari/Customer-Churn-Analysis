import pandas as pd

df = pd.read_csv("E-commerce Customer Behavior - Sheet1.csv")   # put your file name here
df.head()
df.info()
df.isnull().sum()
df = df.dropna()
df.describe()

#Churn was defined as customers inactive for more than 30 days.
df['Churn'] = df['Days Since Last Purchase'].apply(lambda x: 1 if x > 30 else 0)

#Most customers are retained, while a smaller proportion have churned.
import matplotlib.pyplot as plt

churn_counts = df['Churn'].value_counts()

plt.bar(churn_counts.index, churn_counts.values)
plt.title("Churn Distribution")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Customers")
plt.show()

#Low spenders churn more
data = [
    df[df['Churn'] == 0]['Total Spend'],
    df[df['Churn'] == 1]['Total Spend']
]

plt.boxplot(data, tick_labels=['No Churn', 'Churn'])
plt.title("Total Spend vs Churn")
plt.show()

#Low satisfaction → high churn
data = [
    df[df['Churn'] == 0]['Average Rating'],
    df[df['Churn'] == 1]['Average Rating']
]

plt.boxplot(data, tick_labels=['No Churn', 'Churn'])
plt.title("Rating vs Churn")
plt.show()

#Premium users churn less
group = df.groupby(['Membership Type', 'Churn']).size().unstack()

group.plot(kind='bar')
plt.title("Membership vs Churn")
plt.show()

#Inactive users churn more
data = [
    df[df['Churn'] == 0]['Days Since Last Purchase'],
    df[df['Churn'] == 1]['Days Since Last Purchase']
]

plt.boxplot(data, tick_labels=['No Churn', 'Churn'])
plt.title("Recency vs Churn")
plt.show()

# Younger/older customers show different churn behavior.
data = [
    df[df['Churn'] == 0]['Age'],
    df[df['Churn'] == 1]['Age']
]

plt.boxplot(data, tick_labels=['No Churn', 'Churn'])
plt.title("Age vs Churn")
plt.show()

#Customers purchasing fewer items are more likely to churn.
data = [
    df[df['Churn'] == 0]['Items Purchased'],
    df[df['Churn'] == 1]['Items Purchased']
]

plt.boxplot(data, tick_labels=['No Churn', 'Churn'])
plt.title("Items Purchased vs Churn")
plt.show()

#“Discounts help in reducing churn.”
group = df.groupby(['Discount Applied', 'Churn']).size().unstack()

group.plot(kind='bar')
plt.title("Discount vs Churn")
plt.show()

#“Days Since Last Purchase has strong positive correlation with churn.”
import numpy as np

corr = df.corr(numeric_only=True)

plt.imshow(corr)
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Heatmap")
plt.show()
df.to_csv("cleaned_data.csv", index=False)


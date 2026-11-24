import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load customer dataset
df = pd.read_csv("customers.csv")

# Display customer data
print(df)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display total customers
print("\nTotal Customers:")
print(len(df))



# Customer Spending Analysis

print("\n--- Customer Spending Analysis ---")

print("Total Sales:", df["PurchaseAmount"].sum())

print("Average Purchase:", df["PurchaseAmount"].mean())

print("Highest Purchase:", df["PurchaseAmount"].max())

print("Lowest Purchase:", df["PurchaseAmount"].min())


# Membership Analysis

print("\n--- Membership Analysis ---")

print(df["Membership"].value_counts())

# Customer Membership Chart

membership_count = df["Membership"].value_counts()

membership_count.plot(kind="bar")

plt.title("Customers by Membership Type")
plt.xlabel("Membership")
plt.ylabel("Number of Customers")

plt.savefig("membership_chart.png")

plt.show()

# Customer Analysis by City

print("\n--- Customers by City ---")

print(df["City"].value_counts())



# Customers by City Chart

city_count = df["City"].value_counts()

plt.figure()
city_count.plot(kind="bar")

plt.title("Customers by City")
plt.xlabel("City")
plt.ylabel("Number of Customers")

plt.savefig("city_chart.png")
plt.show()


# Sales by City Analysis

print("\n--- Sales by City ---")

sales_by_city = df.groupby("City")["PurchaseAmount"].sum()

print(sales_by_city)


# Sales by City Chart

plt.figure()

sales_by_city.plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.savefig("sales_by_city.png")

plt.show()

# Customer Age Analysis

print("\n--- Customer Age Analysis ---")

print("Average Customer Age:", df["Age"].mean())

print("Youngest Customer:", df["Age"].min())

print("Oldest Customer:", df["Age"].max())


# Customer Age Distribution Chart

plt.figure()

sns.histplot(df["Age"], bins=6, kde=True)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.savefig("customer_age_chart.png")

plt.show()

# Sales by Membership Analysis

print("\n--- Sales by Membership ---")

sales_by_membership = df.groupby("Membership")["PurchaseAmount"].sum()

print(sales_by_membership)

# Sales by Membership Chart

plt.figure()

sales_by_membership.plot(kind="bar")

plt.title("Sales by Membership Type")
plt.xlabel("Membership")
plt.ylabel("Total Sales")

plt.savefig("sales_by_membership.png")

plt.show()

# Business Insights

print("\n--- BUSINESS INSIGHTS ---")

print("Total Customers:", len(df))

print("Total Revenue:", df["PurchaseAmount"].sum())

print("Top Performing City:", sales_by_city.idxmax())

print("Highest Revenue Membership:", sales_by_membership.idxmax())

print("Average Customer Age:", df["Age"].mean())
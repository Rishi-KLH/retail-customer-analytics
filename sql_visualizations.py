import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. Connect to MySQL
# ----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rishi@2114",
    database="customer_analytics_project"
)

print("Connected to MySQL successfully!")

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ----------------------------
# 2. Revenue by Category
# ----------------------------
query1 = """
SELECT category, SUM(purchase_amount_usd) AS total_revenue
FROM customer_shopping
GROUP BY category
ORDER BY total_revenue DESC;
"""
df1 = pd.read_sql(query1, conn)

plt.figure()
sns.barplot(x='total_revenue', y='category', data=df1)
plt.title("Revenue by Category (SQL Analysis)")
plt.xlabel("Total Revenue")
plt.ylabel("Category")
plt.show()

# ----------------------------
# 3. Average Spending by Age Group
# ----------------------------
query2 = """
SELECT 
    CASE 
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 45 THEN '36-45'
        WHEN age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '56+'
    END AS age_group,
    ROUND(AVG(purchase_amount_usd), 2) AS avg_spending
FROM customer_shopping
GROUP BY age_group
ORDER BY avg_spending DESC;
"""
df2 = pd.read_sql(query2, conn)

plt.figure()
sns.barplot(x='age_group', y='avg_spending', data=df2)
plt.title("Average Spending by Age Group (SQL Analysis)")
plt.xlabel("Age Group")
plt.ylabel("Average Spending")
plt.show()

# ----------------------------
# 4. Discount Impact on Spending
# ----------------------------
query3 = """
SELECT discount_applied, ROUND(AVG(purchase_amount_usd), 2) AS avg_purchase
FROM customer_shopping
GROUP BY discount_applied;
"""
df3 = pd.read_sql(query3, conn)

plt.figure()
sns.barplot(x='discount_applied', y='avg_purchase', data=df3)
plt.title("Discount Impact on Purchase Amount (SQL Analysis)")
plt.xlabel("Discount Applied")
plt.ylabel("Average Purchase Amount")
plt.show()

# ----------------------------
# 5. Subscription Impact on Spending
# ----------------------------
query4 = """
SELECT subscription_status, ROUND(AVG(purchase_amount_usd), 2) AS avg_purchase
FROM customer_shopping
GROUP BY subscription_status;
"""
df4 = pd.read_sql(query4, conn)

plt.figure()
sns.barplot(x='subscription_status', y='avg_purchase', data=df4)
plt.title("Subscription Status vs Purchase Amount (SQL Analysis)")
plt.xlabel("Subscription Status")
plt.ylabel("Average Purchase Amount")
plt.show()

# ----------------------------
# 6. Payment Method Usage
# ----------------------------
query5 = """
SELECT payment_method, COUNT(*) AS usage_count
FROM customer_shopping
GROUP BY payment_method
ORDER BY usage_count DESC;
"""
df5 = pd.read_sql(query5, conn)

plt.figure()
sns.barplot(x='usage_count', y='payment_method', data=df5)
plt.title("Most Used Payment Methods (SQL Analysis)")
plt.xlabel("Usage Count")
plt.ylabel("Payment Method")
plt.show()

# ----------------------------
# 7. Sentiment Distribution
# ----------------------------
query6 = """
SELECT sentiment, COUNT(*) AS total_reviews
FROM product_reviews
GROUP BY sentiment;
"""
df6 = pd.read_sql(query6, conn)

plt.figure()
sns.barplot(x='sentiment', y='total_reviews', data=df6)
plt.title("Sentiment Distribution (SQL Analysis)")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.show()

# ----------------------------
# 8. Platform-wise Sentiment Distribution
# ----------------------------
query7 = """
SELECT window_name, sentiment, COUNT(*) AS total_reviews
FROM product_reviews
GROUP BY window_name, sentiment
ORDER BY window_name;
"""
df7 = pd.read_sql(query7, conn)

plt.figure(figsize=(10,6))
sns.barplot(x='window_name', y='total_reviews', hue='sentiment', data=df7)
plt.title("Platform-wise Sentiment Distribution (SQL Analysis)")
plt.xlabel("Platform")
plt.ylabel("Number of Reviews")
plt.show()

# ----------------------------
# 9. Close connection
# ----------------------------
conn.close()
print("All SQL visualizations generated successfully!")
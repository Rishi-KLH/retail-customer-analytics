import pandas as pd
import mysql.connector

# ----------------------------
# 1. Connect to MySQL
# ----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rishi@2114",
    database="customer_analytics_project"
)

cursor = conn.cursor()

print("Connected to MySQL successfully!")

# ----------------------------
# 2. Load cleaned CSV files
# ----------------------------
customer_df = pd.read_csv(r"C:\Users\Rishineha\Downloads\cleaned_customer_shopping_behavior.csv")
reviews_df = pd.read_csv(r"C:\Users\Rishineha\Downloads\cleaned_product_reviews_1000.csv")

print("CSV files loaded successfully!")

# ----------------------------
# 3. Insert Customer Shopping Data
# ----------------------------
customer_sql = """
INSERT INTO customer_shopping (
    customer_id, age, gender, item_purchased, category, purchase_amount_usd,
    location, size, color, season, review_rating, subscription_status,
    shipping_type, discount_applied, promo_code_used, previous_purchases,
    payment_method, frequency_of_purchases
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in customer_df.iterrows():
    cursor.execute(customer_sql, tuple(row))

print("Customer shopping data inserted successfully!")

# ----------------------------
# 4. Insert Product Reviews Data
# ----------------------------
reviews_sql = """
INSERT INTO product_reviews (
    window_name, username, user_id, review, sentiment
) VALUES (%s, %s, %s, %s, %s)
"""

for _, row in reviews_df[['window_name', 'username', 'user_id', 'review', 'sentiment']].iterrows():
    cursor.execute(reviews_sql, tuple(row))

print("Product reviews data inserted successfully!")

# ----------------------------
# 5. Save and close connection
# ----------------------------
conn.commit()
cursor.close()
conn.close()

print("All data imported successfully into MySQL!")
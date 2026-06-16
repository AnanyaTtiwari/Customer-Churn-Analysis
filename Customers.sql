create database Customer_churn_analysis;use Customer_churn_analysis;
CREATE TABLE customers (
    Customer_ID INT,
    Gender VARCHAR(10),
    Age INT,
    City VARCHAR(50),
    Membership_Type VARCHAR(20),
    Total_Spend FLOAT,
    Items_Purchased INT,
    Average_Rating FLOAT,
    Discount_Applied VARCHAR(10),
    Days_Since_Last_Purchase INT,
    Satisfaction_Level VARCHAR(20),
    Churn INT
);
SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cleaned_data.csv"
INTO TABLE customers
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

select * from customers;

-- Churn Distribution
SELECT Churn, COUNT(*) AS total
FROM customers
GROUP BY Churn;
--  Insight: Shows how many customers churned vs retained

-- Average Spend by Churn
SELECT Churn, AVG(Total_Spend) AS avg_spend
FROM customers
GROUP BY Churn;
-- Insight: Compare spending behavior

-- Membership Type vs Churn
SELECT Membership_Type, Churn, COUNT(*) AS total
FROM customers
GROUP BY Membership_Type, Churn;

-- Insight: Premium vs basic churn

-- Average Rating by Churn
SELECT Churn, AVG(Average_Rating) AS avg_rating
FROM customers
GROUP BY Churn;

-- Insight: Satisfaction impact

-- Average Days Since Last Purchase
SELECT Churn, AVG(Days_Since_Last_Purchase) AS avg_days
FROM customers
GROUP BY Churn;
-- Insight: Inactivity vs churn

-- Items Purchased vs Churn
SELECT Churn, AVG(Items_Purchased) AS avg_items
FROM customers
GROUP BY Churn;
-- Insight: Purchase behavior

-- Discount Impact
SELECT Discount_Applied, Churn, COUNT(*) AS total
FROM customers
GROUP BY Discount_Applied, Churn;
-- Insight: Do discounts reduce churn?

-- Top Cities with High Churn
SELECT City, COUNT(*) AS churn_count
FROM customers
WHERE Churn = 1
GROUP BY City
ORDER BY churn_count DESC
LIMIT 5;
-- Insight: Location-based churn








-- 

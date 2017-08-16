/**
 * Using the COUNT function to get a total amount of orders
 * from the database
 */
SELECT COUNT(amount) FROM mydb.orders;

/**
 * Using COUNT and SUM will give the total orders for
 * a person as well as the total amounts that they have
 * ordered.
 */
SELECT COUNT(amount), SUM(amount) FROM mydb.orders
WHERE person_id = 1;

/**
 * Using the AS keyword to return more readable column names
 * for the COUNT and SUM functions
 */
SELECT 
    COUNT(amount) AS total_sales,
    SUM(amount) AS total_amount_spent
FROM
    mydb.orders
WHERE
    person_id = 1;
    
/**
 * Using the AVG function to calculate the
 * average_spend from the `amount` column on the
 * `orders` table
 */
SELECT AVG (amount) AS average_spend
FROM mydb.orders WHERE person_id = 1;


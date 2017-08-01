/**
 * Select multiple columns using CONCAT
 */
SELECT CONCAT(first_name, ' ', last_name)
AS full_name FROM `mydb`.`people`;

/**
 * Using the DISTINCT keyword
 * retrieve only single instances of the values in a column (no duplicate values)
 */
SELECT DISTINCT(amount) FROM mydb.orders;
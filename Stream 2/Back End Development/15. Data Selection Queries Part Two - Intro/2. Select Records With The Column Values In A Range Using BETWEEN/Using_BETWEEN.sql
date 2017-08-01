/**
 * Create a select statement without using the BETWEEN keyword
 */
SELECT * FROM mydb.orders
WHERE
created_at >= '2015-09-08 14:48:00'
AND
created_at <= '2016-09-08 15:34:00';

/**
 * Create a select statement using the BETWEEN keyword
 */
SELECT * FROM mydb.orders
WHERE created_at
BETWEEN
'2015-01-01 00:00:00'
AND
'2017-01-31 23:59:59';
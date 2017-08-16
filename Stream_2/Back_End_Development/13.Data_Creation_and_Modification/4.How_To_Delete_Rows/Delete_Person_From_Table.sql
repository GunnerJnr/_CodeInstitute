/**
 * Delete a user from our `people` table
 */
DELETE FROM mydb.profiles
WHERE person_id = 3;
 
DELETE FROM mydb.orders
WHERE person_id = 3;
 
DELETE FROM mydb.people
WHERE id = 3;
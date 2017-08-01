/**
 * Update the address of a person in the `profiles`
 */
UPDATE `mydb`.`profiles`
SET `address` = "la New Address"
WHERE `person_id` = 2;

/**
 * Select all rows from the `people` table
 */
SELECT * FROM mydb.people;
SELECT * FROM mydb.orders;
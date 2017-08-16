/** 
 * Insert a new record into the 'people' table
 */
INSERT INTO `mydb`.`people` (
	`first_name`,
    `last_name`,
    `DOB`
) VALUES (
	'David',
    'Gunner',
    STR_TO_DATE('29/03/1984', '%d/%m/%Y')
);

/**
 * Insert a new record into the 'orders' table
 */
 INSERT INTO mydb.orders (
	amount, 
    person_id
) VALUES (
	12.02,
    1
);

/**
 * Shortened notation to Insert multiple records into our 'orders' table
 */
 INSERT INTO mydb.orders (
	amount,
    person_id
) VALUES
	(12.02, 1),
    (9.02, 1),
    (13.02, 1),
    (15.02, 1),
    (17.02, 1);
    
/**
 * Insert a new row into our `profiles` table
 */
INSERT INTO `mydb`.`profiles` (
	`person_id`,
	`address`
) VALUES (
	1,
	"25 Middle Stream Close"
)
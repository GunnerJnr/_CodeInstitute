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
    STR_TO_DATE('29/03/1984', '%d/%m/%Y'),
	'Dave',
	'Gunner Jnr',
	STR_TO_DATE('29/03/1984', '%d/%m/%Y'),
	'D',
	'Gunner Jnr',
	STR_TO_DATE('29/03/1984', '%d/%m/%Y'),
	'Davey',
	'Gunner Jnr',
	STR_TO_DATE('29/03/1984', '%d/%m/%Y'),
	'John',
	'Smith',
	STR_TO_DATE('29/03/1984', '%d/%m/%Y'),
	'Thatchers',
	'Gold',
	STR_TO_DATE('29/03/1984', '%d/%m/%Y'),
	'Bet',
	'Fred',
	STR_TO_DATE('29/03/1984', '%d/%m/%Y'),
	'Celia-Rose',
	'Gunner',
	STR_TO_DATE('29/03/1984', '%d/%m/%Y')
);
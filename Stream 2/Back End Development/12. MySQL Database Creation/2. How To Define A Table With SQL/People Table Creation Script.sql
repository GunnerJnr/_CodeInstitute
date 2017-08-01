/* tell mysql what table to use */
USE mydb;

/* create a table called people that will have the following rows:
 * id, first_name, last_name, DOB
 */

CREATE TABLE people (
	id INTEGER,
    first_name VARCHAR(50),
    last_name varchar(50),
    DOB DATE
    );
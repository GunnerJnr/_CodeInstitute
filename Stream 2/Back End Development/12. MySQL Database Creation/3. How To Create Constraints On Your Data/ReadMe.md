CHALLENGE
=========

 

### CHALLENGE A

Drop the current people table and recreate it using the new constraints version
of your table.

 

### CHALLENGE B

Using the new table definition, create the new table.

 

### HINT A

Using the **FOREIGN KEY** constraint, you can specify a related table’s primary
key:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/**
 * Create another table that references the `people` table
 * using a foreign key relationship.
 */
CREATE TABLE orders(
    id INTEGER AUTO_INCREMENT,
    amount DECIMAL(18,2) NOT NULL,
    person_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (person_id) REFERENCES people(id),
);
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This then describes the relationship between the people table and the orders
table, and shows that the **person\_id** should contain a valid ‘id’ from
the people table.

 

To take things a step further, you can also use **CHECK** to make sure the value
in the **‘amount’** column of the orders table is a positive number:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
USE my_db;
 
CREATE TABLE orders (
        id INTEGER AUTO_INCREMENT,
        amount DECIMAL(18,2) NOT NULL,
        person_id INT,
        PRIMARY KEY (id),
        FOREIGN KEY (person_id) REFERENCES people(id),
        CHECK(amount>0)
);
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

If you accidentally insert a row and the amount is

 

Finally, you want
to [record](http://codeinstitute.wpengine.com/glossary/record/) when the order
was made, so you can add a date that it was created:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
USE my_db;
 
CREATE TABLE orders (
        id INTEGER AUTO_INCREMENT,
        amount DECIMAL(18,2) NOT NULL,
        person_id INT,
        created_at datetime DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id),
        FOREIGN KEY (person_id) REFERENCES people(id),
        CHECK(amount>0)
);
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

When inserting new rows, you will not actually supply a value for this and as a
result [MySQL](http://codeinstitute.wpengine.com/glossary/mysql/) will look at
the **DEFAULT** constraint and set it using the **CURRENT\_TIMESTAMP** variable
that it maintains inside its systems. **CURRENT\_TIMESTAMP** will always equal
the time on the computer right now.

/**
 * Create a select statement using the LIKE keyword
 */
SELECT * FROM articles WHERE title LIKE '%article%';

/**
 * CHALLENGE A 
 * Use the LIKE query to select all
 * rows where the `content` column contains the
 * word 'more'
 */
SELECT * FROM articles WHERE content LIKE '%more%';

/**
 * CHALLENGE B
 * Use the LIKE query to select all
 * rows where the `content` column begins with
 * the word 'wow'
 */
SELECT * FROM articles WHERE content LIKE 'wow%';

/**
 * CHALLENGE C 
 * Select all rows where the 'title' column
 * ends with the number 4
 */
SELECT * FROM articles WHERE title LIKE '%4';
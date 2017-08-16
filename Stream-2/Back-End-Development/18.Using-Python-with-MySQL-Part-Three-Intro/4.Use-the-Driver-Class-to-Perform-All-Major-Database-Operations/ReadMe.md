CHALLENGE
=========

 

**Challenge A:**  
Using the **AVG()**, select a person from your people table and get the average
amount they spend and, at the same time, create a column that reads,
“[first_name] spends “. Then print out the columns to provide the answers in the
terminal.

**Challenge B:**  
Create a new person in the people table and add in a profile row and two orders
of random value.

**Challenge C:**  
Once you’ve added them in use select to get their full name and the minimum
amount they have spent.

**Challenge D:**  
Choose a person and update ALL of his orders to have the amount 20.02.

**Challenge E:**  
Look at this code:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Deleting a record
person = db.select('people',named_tuples=True)[0]
db.delete('orders', person_id="=%s" % person.id, id="=1")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you were to leave out the `id=”=1″` part what would happen?

 

 

HINT
====

 

**Challenge B:**  
In order to use
the `STR_TO_DATE` [function](http://lms.codeinstitute.net/glossary/function/),
you’ll need to modify the if statement in
insert [function](http://lms.codeinstitute.net/glossary/function/) to determine
if the value is a number or a date:

`if is_number(value) or arg == 'DOB':`

**Challenge C:**  
To determine the minimum amount we’ll use the
`MIN()` [function](http://lms.codeinstitute.net/glossary/function/):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SELECT MIN(amount) AS minimum_amount_spent FROM orders;
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

 

SOLUTION
========

 

In case of emergency, break the glass!

**Challenge A:**  
Find the solution to this challenge
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Two/Unit19-Using_Python_With_MySQL_pt_3/challenges/challenge-1>

**Challenge B:**  
Find the solution
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Two/Unit19-Using_Python_With_MySQL_pt_3/challenges/challenge-2>

**Challenge C:**  
Find the solution
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Two/Unit19-Using_Python_With_MySQL_pt_3/challenges/challenge-3>

**Challenge D:**  
Find the solution
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Two/Unit19-Using_Python_With_MySQL_pt_3/challenges/challenge-4>

**Challenge E:**  
Find the solution
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-Two/Unit19-Using_Python_With_MySQL_pt_3/challenges/challenge-5>

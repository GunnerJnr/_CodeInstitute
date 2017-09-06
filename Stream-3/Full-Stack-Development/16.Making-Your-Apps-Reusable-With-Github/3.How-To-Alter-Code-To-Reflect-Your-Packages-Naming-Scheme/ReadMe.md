How to Alter Code to Reflect Your Package’s Naming Scheme
=========================================================

##### In this unit the students will learn how to refactor their code to make modules reuseable

 

### HOW TO ALTER CODE TO REFLECT YOUR PACKAGE’S NAMING SCHEME

Now that we’ve configured our package, we need to alter our code to reflect the
fact that we have renamed the ‘blog’ folder to ‘reusable_blog’, to avoid any
naming conflicts in any future apps.

The main files that will need altering are the *migrations* and the *model*, as
they all reference ‘blog’ in their code. We need to edit those and replace all
instances of ‘blog’ with ‘reusable_blog’.

Fortunately, we did not specifically mention ‘blog’ in our other code files. We
used things like ‘from .models import …’ instead, so we won’t need to amend a
great deal of code.

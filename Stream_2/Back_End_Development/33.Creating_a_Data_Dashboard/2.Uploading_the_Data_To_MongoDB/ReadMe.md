### UPLOADING THE DATA TO MONGODB

As part of the **Project Assets** for this project (link at the bottom), you are
provided with a file called **opendata_projects_clean.csv** of data in csv
format. You will upload the file to an instance
of [MongoDB](http://lms.codeinstitute.net/glossary/mongodb/) running on your
machine. In doing so, the content will be converted to JSON format.

1.  Run [mongoDB](http://lms.codeinstitute.net/glossary/mongodb/) by running the
    command **mongod** in your Terminal/Command Prompt .

2.  Leave the prompt running as it is and open another Terminal/Command Prompt
    window.

3.  Copy the csv file to the same location as the directory opened in the second
    terminal window.

4.  Enter the following command:

mongoimport -d donorsUSA -c projects --type csv --file
opendata_projects_clean.csv --headerline

-   The [database](http://lms.codeinstitute.net/glossary/database/) created: `donorsUSA`

    -   The collection name: `projects`

    -   The data type to be uploaded: `csv` 

    -   The filename: `opendata_projects_clean.csv`

    -   Treat the
        first [record](http://lms.codeinstitute.net/glossary/record/) imported
        as
        the [field](http://lms.codeinstitute.net/glossary/field/) names: `--headerline`

    There are over 87,000 records in the file, so it will take a few minutes to
    upload the data. You will see a progress indicator in the terminal letting
    you know how much data has approximately been uploaded.

1.  Open Mongo Management Studio to see the uploaded data, Mongo shows it to us
    in JSON format (while internally it stores it in a related format named
    BSON).

    Take a few minutes to familiarise yourself with the data and its structure.
    We will use the following collection attributes/fields as the basis of our
    project:

    -   school\_[state](http://lms.codeinstitute.net/glossary/state/)

    -   resource_type

    -   poverty_level

    -   date_posted

    -   total_donations

    -   funding_status

Many datasets in the real world are imperfect, and may benefit from a bit
of [cleanup](https://en.wikipedia.org/wiki/Data_cleansing) before use;
donorsChoose is no exception.

One of the minor issues in this dataset is that in 3 of the records about
projects in the [state](http://lms.codeinstitute.net/glossary/state/) of
Louisiana, the
school\_[state](http://lms.codeinstitute.net/glossary/state/) [field](http://lms.codeinstitute.net/glossary/field/) was
entered as “La”, rather than the correct “LA” (both letters should be
capitalised). You can see this issue by running the following query in
Mongo: `db.projects.distinct("school_state");` .

So now you have three alternatives, all commonly used in the industry:

1.  Delete the dataset from Mongo, fix the original data in the csv (and maybe
    even further up-stream), and then reupload it to Mongo.

2.  Fix the data inside Mongo by running the following command (may take around
    a minute):

db.projects.updateMany(  
{ school_state: "La" },  
{ \$set: { school_state: "LA" } }  
);

1.  Or just ignore the issue, and accept the fact that data is generally not
    perfect, but is still very useful regardless.

<http://lms.codeinstitute.net/course-status/#>

 [Dashboard
Assets](https://www.dropbox.com/s/wbb4sva0pfbfvwu/Stream%202%20Project%20Assets%202.zip?dl=0)

Dashboard—Intro
===============

##### In this unit the students will build a dashboard using Flask, D3.js, DC.js and Crossfilter

![](http://codeinstitute.wpengine.com/wp-content/uploads/2016/02/1455038946_image1.png)

  
  
The goal of this section is to expand on the skillsets and tools for creating a
meaningful interactive data visualization learned throughout Streams 1 & 2 . To
do this, we will use a dataset from DonorsChoose.org to build a data
visualization that represents school donations broken down by different
attributes over a timeline. We will be covering a wide range of technologies:
MongoDB for storing and querying the data, Python for building a web server that
interacts with MongoDB and serves html pages, and JavaScript libraries: d3.js,
dc.js queue.js and crossfilter.js for building interactive charts.  


### BACKGROUND

[DonorsChoose.org](http://www.donorschoose.org/) is a US based nonprofit
organization that allows individuals to donate money directly to public school
classroom projects. Public school teachers post classroom project requests on
the platform, and individuals have the option to donate money directly to fund
these projects. The classroom projects range from pencils and books to computers
and other expensive equipments for classrooms. In more than 10 years of
existence, this platform helped teachers in all US states to post more than
7700,000 classroom project requests and raise more than \$280,000,000.
DonorsChoose.org has made the platform data open and available for making
discoveries and building applications.

In this project we will be using one of the available datasets for building an
interactive data visualization that represents school donations broken down by
different attributes.  


### THE COMPONENTS OF OUR DASHBOARD PROJECT AND THEIR FUNCTION:

1.  **D3.js**: A JavaScript based visualization engine, which will render
    interactive charts and graphs based on the data.

2.  **Dc.js**: A JavaScript based wrapper library for D3.js, which makes
    plotting the charts a lot easier.

3.  **Crossfilter.js**: A JavaScript based data manipulation library that
    enables two way data binding.

4.  **Queue.js**: An asynchronous helper library for JavaScript.

5.  **Mongo DB**: NoSQL Database used to convert and present our data in JSON
    format.

6.  **Flask**: A Python based  micro – framework  used to serve our data from
    the server to our web based interface.

 

### WHAT WE’LL DO:

Together we will build the core components and structure of a working Dashboard.
This will include:

1.  Creating the Python app required to server the database content to the web
    interface.

2.  Writing the HTML required to display the dashboard.

3.  Importing the JavaScript libraries and writing the code required to render
    the data to our dashboard elements.

4.  Creating core CSS used to style dashboard elements.

<http://lms.codeinstitute.net/course-status/#>

 [Dashboard
Assets](https://www.dropbox.com/s/wbb4sva0pfbfvwu/Stream%202%20Project%20Assets%202.zip?dl=0)

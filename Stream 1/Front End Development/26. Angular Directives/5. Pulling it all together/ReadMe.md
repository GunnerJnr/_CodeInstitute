See Repo on git here as required to fork for lesson ..

 

<https://github.com/GunnerJnr/mdb-nav>

 

 

### CHALLENGE A: ADDING A BOOTSTRAP MENU

Let’s add a bootstrap menu to the application for overall project level
navigation. Add the following to the **index.html** file above
the **\<div\>** element with the ng-view attribute.  The menu includes a
dropdown menu with links to the movie lists. You may want to remove the sub
menus from the individual movie list templates.

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<nav class="navbar navbar-inverse">
    <div class="container">
        <div class="nav navbar-header">
            <a class="navbar-brand" href="#/home">MoviesDB</a>
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myCollapsingList">
                <span class="sr-only">Toggle Navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
        </div>
        <div class="collapse navbar-collapse" id="myCollapsingList">
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#/home">Home</a></li>
                <li><a href="#/about">About</a></li>
                <li class="dropdown">
                    <a class="dropdown-toggle" data-toggle="dropdown" role="button"aria-haspopup="true" aria-expanded="false">Movies <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#/popular">Popular</a></li>
                        <li><a href="#/upcoming">Upcoming</a></li>
                        <li><a href="#/nowPlaying">Now Playing</a></li>
                        <li><a href="#/topRated">Top Rated</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Because we’re expanding our site our **movie-nav** directive is no longer
relevant and it makes more sense to just include those navigation links in a
single navigation bar. This means that we can now remove
the **movie-nav** element from our **movies.html** file.

   
The solution for this challenge can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-1/Unit30-Angular_Directives/pulling_it_all_together/adding_a_bootstrap_menu>

 

### CHALLENGE B: CREATING THE HOME PAGE

We now need to create some kind of home page that will be the opening page of
the application.

 

Create a homepage for our application. The steps involve:

-   adding a route to app.js a \$routeProvider for new route (‘/’);

-   adding a new home.html to templates folder

-   adding a new HomeController

 

We’ll create our new **home.html** in our templates directory:

 

*home.html*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class="container">
    <div class="home-page btn-link-hover">
        <img src="images/movies-logo-1.gif">
        <h1>{{title}}</h1>
 
        <p>Find all the latest and most popular movies out right now.</p>
        <p>See what's top rated and upcoming in the near future!</p>
        <a href="#/popular" class="btn-link">Enter Movies</a>
    </div>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Add some styling if you want to improve the look of the page. Make the ‘Enter
Movies’ link look like a button by adding some css, use the ‘btn-link’ class.
Debug the final version for ideas.

 

Example:

 

*style.css*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.btn-link {
    border: 3px solid grey;
    padding: 5px;
    margin: 60px;
    font-size: large;
    text-decoration: none;
    color: grey;
}
 
div.home-page {
    background: transparent;
    font-size: large;
    text-align: center;
}
 
div.home-page h1 {
    background: transparent;
    font-size: 300%;
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

In our **app.js** we’ll add:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
when('/', {
    templateUrl: 'templates/home.html',
    controller: 'HomeController'
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

And lastly we’ll create our **HomeController** in our **controllers.js** file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.controller('HomeController', function($scope) {
    $scope.title = "Welcome To The Movies";
});
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now when we head over to **localhost:8000**, we’ll see our brand new homepage!

   
The solution for this challenge can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-1/Unit30-Angular_Directives/pulling_it_all_together/creating_a_home_page>

 

### CHALLENGE C: ERROR HANDLING

We want to be able to elegantly handle errors when they arise. When we get an
error, we will route to an error page with appropriate messages.

 

To check that error handling works, add a typo to the url string and make sure
the catch statement handles the error elegantly. This is similar to what we did
in our previous routing lesson. We’ll do this together.

 

Add a route to app.js:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.when('/error/:message/:status' {
    templateUrl: 'templates/error.html',
    controller: ' MovieErrorController'
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We’ve added two parameters to the path ‘message’ and ‘status’. Add our
‘MovieErrorController’ to our controllers file:

 

*controller.js*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.controller('MovieErrorController', function($scope, $routeParams) {
    $scope.message = $routeParams.message;
    $scope.status = $routeParams.status;
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Now create an error.html file in the templates folder:

 

*error.html*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class='container' style='text-align: center'>
<h1>Error Encountered</h1>
<h2><span>Response:</span> {{status}}</h2>
<h3><span>Message:</span> {{message}}</h3>
<div class='btnLinkHover'>
    <a class='btnLink' href='#/home'>Return To Home</a>
</div>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

In order to test this, we can change the moviesEndpoint URL in
the **MovieNowPlayingController** to **‘/now\_paying?api\_key=’** and go
to **localhost:8000/\#/nowPlaying**  


**\$location service**

 

As part of the routing module, there is a service we can use to automatically
route to a new path using the**\$location** service. The location service has a
function we can use **path()** which takes as a parameter a path string to
re-route to. In our case, we will add a route to our new error.html template
file. So we will add to the error function of the service call as so:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.catch(
        function(error) {
          console.log('error', error);         
$location.path('/error/'+error.data.status_message+'/'+error.status)
        });
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We need to add the location service as a dependency to the controller function:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.controller('MovieNowPlayingController',function($scope, $location, 
MovieListService,myMovieConfig) {
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Leave the typo in and check that we are routing to the error template
successfully.

 

The solution for this challenge can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-1/Unit30-Angular_Directives/pulling_it_all_together/error_handling>

 

### CHALLENGE D: ADDING A DETAILS VIEW

The last major feature is to add a details view of a particular movie. The
moviesDB API provide a url for a movie as long as we have an id. The movie.id is
provided by the movie list url so we have access to this value in our movies
list.

 

We will add a link on the movie list around each poster with a link to a more
details page.

 

The url from the MoviesDB we need is:  
https://api.themoviedb.org/3/movie/[id]?api\_key=\</a\>\<your api key\>

 

**id** – the id of the movie we can obtain from the movie list

 

To the movies.html file, add an anchor link around the \<movie-info-box\>
directive so that it looks like:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class="col-md-2">
      <a href='#/movie/{{movie.id}}'>      
       <movie-info-box info="movie"></movie-info-box>  
      </a>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We are using the movie.id as a parameter to our details route. Similar to the
errors page above, we need to do the following:

 

-   add route to app.js file with templateUrl and controller

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.when('/movie/:movieId', {
                 templateUrl: 'templates/movieDetails.html',
                 controller: 'MovieDetailsController'
              })
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

-   name the new controller ‘MovieDetailsController’

-   add controller to controller.js file

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.controller('MovieDetailsController',function($scope, $location, 
$routeParams, MovieListService, myMovieConfig) {
//
   $scope.title = 'Movie Details';
   var id = $routeParams.movieId;
   var url = myMovieConfig.moviesEndpoint + '/' + id + '?api_key=' + 
myMovieConfig.apiKey;
   MovieListService.getList(url).then(
      function(result){
            $scope.movie = result.data;      
            }
      ).catch(
        function(error) {         $location.path('/error/'+error.data.status_message+'/'+error.status)
        });
})
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

-   add movieDetails.html file to the templates folder, highlighted are the data
    from the movie details returned from the url api call.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class='container'>
    <h1>{{title}}</h1>
    <div class='row'>          
      <div class="col-md-3">
        <img ng-src="http://image.tmdb.org/t/p/w370/{{movie.poster_path}}" 
class='img-responsive'>
      </div>
     <div  class="col-md-7">
        <h1 class="">{{movie.title}}</h1>
        <p> Rating: {{ movie.vote_average}} ({{movie.vote_count}})</p>
        <p>{{movie.overview}}</p>
        <h3>Tag Line</h3>
        <p>{{movie.tagline}}</p>
        <p class="" style="color: black">Released: {{movie.release_date | 
date: 'mediumDate'}}</p>
      </div>
    </div>
    <br/><br/>  
    <a href="#/popular"><button class="btn btn-primary">Return 
Movies</button></a>
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Let’s add a debug breakpoint to make sure the data we are returning is correct.

 

The solution for this challenge can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-1/Unit30-Angular_Directives/pulling_it_all_together/adding_a_details_view>

 

### CHALLENGE E: ADDING CSS TO MAKE APP PRESENTABLE

You will notice that our movies display doesn’t line up neatly on each row. To
fix this, add the following to style.css:

 

*style.css*

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
div.repeat:nth-child(6n+0):after { display: table; content: " "; clear: both}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Add the class ‘repeat’ to the repeat \<div\> in the **movies.html** file:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class='repeat' ng-repeat="movie in movieList">
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Re-run the application. Click on all options on the movie navigation menu. Does
everything work as before?

 

Try and work out what the css above is doing and why does it fix a problem we
encounter when the css is commented out. Use Google or Stackoverflow to see if
you can determine why this css fixes our problem.

 

**Adding Responsiveness**

At present we are using a col-2 layout, which results in 6 grids showing the
movie details. See what happens when you resize the width of the browser to
smaller sizes. Change this layout so that:

 

For **col-sm**    layout change to a 3 col display, i.e. use col-sm-4  
For **col-xs**     layout change to a 2 col display, i.e. use col-xs-6

 

So that we now have, in our row:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
<div class="col-md-2 col-sm-4 col-xs-6">
            .
            .
            .
</div>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

When changing the grid layout from 6 cols to 3 and 2, there will be problems
with the layout of the rows as not all the images are the same dimensions. This
was solved when there are 6 cols by introducing the css:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
div.repeat:nth-child(6n+1):{clear: both}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This will clear left and right before the 7th element is displayed (the first of
the next row).

 

When we move to col-sm-4 and col-xs-6, we need to clear the next row element as
above but for the 4th and 3rd elements respectively. To do this, we need to use
media queries.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/* Portrait tablets and small desktops  col-sm*/
@media (min-width: 768px) and (max-width: 991px) {
   div.repeat:nth-child(3n+1){ clear: both}
}
 
/* Landscape phones and portrait tablets  col-xs*/
@media (max-width: 767px) {
  div.repeat:nth-child(2n+1){ clear: both}
 
}
 
/* Portrait phones and smaller  col-xs*/
@media (max-width: 480px) {
  div.repeat:nth-child(2n+1) { clear: both}
 
}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Here’s a **hint**: Think about how we are using the bootstrap \<div
class=’row’\> – what is significant about the 6th and 7th movies in our row?  
[/tab]

 

The solution for this challenge can be found
at <https://github.com/Code-Institute-Org/full_stack_solutions/tree/master/Stream-1/Unit30-Angular_Directives/pulling_it_all_together/adding_css_to_make_app_presentable>

 

### SUMMARY

In this lesson, we looked at directives and how to create our own custom built
directives. We can see how directives can allow for the creation of reusable UI
components within an application. Directives are a powerful concept and have the
potential to make UI development and design much more productive – allowing
developers to ‘plug & play’ existing UI components into their applications and
rapidly increasing the productivity of product development.

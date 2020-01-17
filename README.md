# Recipes Book
## Data Centric Development Milestone Project 

- Heroku (https://recipe-ideas-project.herokuapp.com/get_recipe).
- Github (https://github.com/Sreniok/Recipe_Ideas)




I chose Project Example Idea 1: 

### Create an online cookbook:
 
Create a web application that allows users to store and easily access cooking recipes.
Create the backend code and frontend form(s) to allow users to add new recipes to the site, edit them and delete them.
Create the backend and frontend functionality for users to locate recipes based on the recipe's fields. You may choose to create a full search functionality or just a directory of recipes.
Provide results in a manner that is visually appealing and user-friendly.
Create a dashboard to provide some statistics about all the recipes.

#### For this project, I used MongoDB as the database.

## UX
#### User stories
1. Logo and name of website redirect you to the main page.
2. The main page display all recipes, user can search and add a new recipe from the main page. Clicking on list tab or image description will display below, where user can edit or delete the recipe. A full description is available by clicking the name of a recipe
3. On the navbar, there are four tabs:
 - search (user can search by name, cuisines and ingredients. Cuisines are pre-loaded)
 - dashboard (showing three charts. the First chart displed total cooking time per user, second how many recipes per user and third chart display map showing number recipes in-country)
 - Cuisines (user can create new cuisines, clicking on list tab or flag description will display below, where user can edit or delete the recipe. Full description is available by clicking the name of cuisines)
 - Recipes ( Clicking on list tab or image description will display below, where user can edit or delete the recipe. Full description is available by clicking the name of the recipe)
4. Any user can create, edit, or delete recipes or cuisines 
5. There is a dashboard showing three charts. The first chart displed total cooking time per user, second how many recipes per user and map displayed country of recipe 

## Database Schema

MongoDB database consists of 2 collections:

- Cuisines
- Recipes

The cuisines collection contain cuisine name, cuisine description, cuisine flag image URL
The recipes collection contain all information needed for one recipe including recipe name, user, cuisine name, ingredients, method, cooking time, recipe description, recipe image.

## Features

### Existing Features
- Simple recipe database App

### Potential future features
- User account to log in for storing, editing and deleting recipes only by the creator
- Add upvoting to recipe 
- Adding a review


## Technologies used:
##### HTML - a standardized system for tagging text files to achieve font, colour, graphic, and hyperlink effects on World Wide Web pages.
##### CSS - CSS describes how HTML elements should be displayed.
##### Javascript - client side scripting language, used for presenting statistics and animations
##### Python - Programming Language to create the backend.
##### Git Bash & GitHub -for version control and backup of code
##### Materialize - A modern responsive front-end framework based on Material Design.
##### Flask - python web framework to hold all the code and templates together as one site.
##### MongoDB - Non-relational database to store all information about the recipes, cuisines etc.
##### Google Fonts - Making the web more beautiful, fast, and open through great typography.

## Testing

#### Manual testing

All features like add, edit or delete cuisines and recipes was tested and working fine. During the test search function by cuisines is not working couldn't find the problem before submitting a project.

#### Cross-browser Testing
The site was developed on Chrome but was tested on Safari with no issues.

#### Code Validation
file run on .
- W3C for CSS.
- W3C for HTML.

#### Problems in development
Searching by cuisines currently not working showing error 404 page not found. 

## Deployment
- The project is deployed to Heroku.
- Created Procfile and requirements.txt for dependencies.
- Linked my Github and environment with Heroku
- Pushed to Heroku.
- Pushed to Github.
- A website can be found on Heroku (https://recipe-ideas-project.herokuapp.com/get_recipe).
- The repository can be found on Github (https://github.com/Sreniok/Recipe_Ideas)

## Credits
To Code Institue module Data Centric Development

### Acknowledgements
- Cuisines description and flag image was found on Wikipedia
- Recipes were found on (https://www.tasteofhome.com/recipes/)
- Recipe image was found using google search

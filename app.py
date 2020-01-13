import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 
  
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'food_recipe'

SECRET_KEY = os.environ.get('SECRET_KEY') 
app.config['MONGO_URI'] =  SECRET_KEY

mongo = PyMongo(app)

# Get recipe from MongoDB

@app.route('/get_recipe')
def get_recipe():
    return render_template("recipes.html", recipe=mongo.db.recipe.find())

# Get description from mongoDB
@app.route('/recipe_description/<recipe_id>')
def recipe_description(recipe_id):  
    return render_template('recipe_description.html', recipe=mongo.db.recipe.find({"_id": ObjectId(recipe_id)}))

# User can add recipe
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', cuisine=mongo.db.cuisine.find())

# Insert recipe to the MongoDb
@app.route('/insert_recip', methods=['POST'])
def insert_recip():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))

# Edit Recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_cuisine = mongo.db.cuisine.find()
    return render_template('edit_recipe.html', recipe=the_recipe, cuisine=all_cuisine)

# Update Recipe
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update({'_id': ObjectId(recipe_id)},
    {
    'recipe_name':request.form.get('recipe_name'),
    'user_name':request.form.get('user_name'),
    'cuisine_name':request.form.get('cuisine_name'),
    'ingredients':request.form.get('ingredients'),
    'method':request.form.get('method'),
    'prepaation_time':request.form.get('prepaation_time'),
    'recipe_description':request.form.get('recipe_description')
    })
    return redirect(url_for('get_recipe'))

# Delete recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipe'))

# Get cusine from mongoDB
@app.route('/get_cuisine')
def get_cuisine():
    return render_template("cuisine.html", cuisine=mongo.db.cuisine.find())

@app.route('/cusine/<cusines_name>')
def cusine(cusines_name): 
    cuisine=mongo.db.cuisine.find({'_id': ObjectId(cusines_name)}) 
    recipe=mongo.db.recipe.find()
    return render_template('found_recipes.html',recipe = recipe, cuisine = cuisine)

# User can add cusine
@app.route('/add_cusine')
def add_cusine():
    return render_template('add_cusine.html', cuisine=mongo.db.cuisine.find())

# Insert cuisine to MongoDB
@app.route('/insert_cusine', methods=['POST'])
def insert_cusine():
    cuisine = mongo.db.cuisine
    cuisine.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisine'))

# Edit cusine
@app.route('/edit_cuisine/<cusine_id>')
def edit_cuisine(cusine_id):
    the_cuisine = mongo.db.cuisine.find_one({"_id": ObjectId(cusine_id)})
    all_cuisine = mongo.db.recipe.find()
    return render_template('edit_cuisine.html', cuisine=the_cuisine, recipe=all_cuisine)

# Update cuisine
@app.route('/update_cuisine/<cuisine_id>', methods=["POST"])
def update_cuisine(cuisine_id):
    cuisine = mongo.db.cuisine
    cuisine.update({'_id': ObjectId(cuisine_id)},
    {
    'cuisine_name':request.form.get('cuisine_name'),
    'cuisine_description':request.form.get('cuisine_description'),
    })
    return redirect(url_for('get_cuisine'))

# Delete cuisine
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisine'))

# Search for recipes will preload options for cuisines
@app.route('/search_recipe')
def search_recipe():
    the_recipe = mongo.db.recipe.find()
    all_cuisine = mongo.db.cuisine.find()
    return render_template("search_recipe.html", cuisine=all_cuisine, recipe=the_recipe)

# search recipes
@app.route('/search_by_name', methods=['GET', 'POST'])
def search_by_name():
    search_term = []
    if request.method == 'POST':
        search_term = request.form['recipe_name']
    return render_template('found_recipes.html', recipe=mongo.db.recipe.find_one({'$text': {'$search': search_term }}))

# search cuisines
"""@app.route('/search_cuisine/<cuisine_id>')
def search_cuisine(cuisine_id):
    recipes = mongo.db.recipe.find.find({'cuisine_name' : cuisine_id})
    if recipes.count() == 0:
        return render_template("search_recipe.html")      
    return render_template("found_cuisines.html", recipes=recipes)"""

# search ingredients
"""@app.route('/search_by_ingredients', methods=['GET', 'POST'])
def search_by_ingredients():
    search_term = []
    if request.method == 'POST':
        search_term = request.form['ingredients']
        recip = mongo.db.recipe.find_one({'$text': {'$search': search_term }})
        print(recip)                 
    return render_template('found_ingredients.html', recipe=mongo.db.recipe.find_one({'$text': {'$search': search_term }}))
    """

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

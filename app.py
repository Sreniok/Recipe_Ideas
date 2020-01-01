import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'food_recipe'
app.config['MONGO_URI'] = 'mongodb+srv://Luca:sreniawski85@myfirstcluster0-3nxsy.mongodb.net/food_recipe?retryWrites=true&w=majority'

mongo = PyMongo(app)

# Get cusine from mongoDB
@app.route('/')
@app.route('/get_cuisine')
def get_cuisine():
    return render_template("cuisine.html", cuisine=mongo.db.cuisine.find())


# Get recipe from mongoDB
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

# Delete /recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipe'))

# User can add cusine
@app.route('/add_cusine')
def add_cusine():
    return render_template('add_cusine.html', cuisine=mongo.db.cuisine.find())

@app.route('/insert_cusine', methods=['POST'])
def insert_cusine():
    cuisine = mongo.db.cuisine
    cuisine.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisine'))


    






if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # port=int(os.environ.get('PORT')),
            debug=True)

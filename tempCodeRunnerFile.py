@app.route('/get_recipe')
def get_recipe():
    return render_template("recipes.html", recipe=mongo.db.recipe.find())
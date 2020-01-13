import os 
os.environ["SECRET_KEY"] = 'mongodb+srv://Luca:sreniawski85@myfirstcluster0-3nxsy.mongodb.net/food_recipe?retryWrites=true&w=majority'

SECRET_KEY = os.environ.get('SECRET_KEY') 
app.config['MONGO_URI'] =  SECRET_KEY
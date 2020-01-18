function validateFormRecipes() {
  var a = document.forms["add_recipe"]["recipe_name"].value;
  var b = document.forms["add_recipe"]["recipe_description"].value;
  var c = document.forms["add_recipe"]["user_name"].value;
  var d = document.forms["add_recipe"]["cuisine_name"].value;
  var e = document.forms["add_recipe"]["ingredients"].value;
  var f = document.forms["add_recipe"]["method"].value;
  var g = document.forms["add_recipe"]["cooking_time"].value;


  if (a == "") {
    alert("Recipe name must be filled out!!");
    return false
  }
  if (b == "") {
    alert("Recipe description must be filled out!!");
    return false
  }
  if (c == "") {
    alert("User name must be filled out!!");
    return false
  }
  if (d == "") {
    alert("Cuisines must be selected!!");
    return false
  }
  if (e == "") {
    alert("Ingredients must be filled out!!");
    return false
  }
  if (f == "") {
    alert("Method must be filled out!!");
    return false
  }
  if (g == "") {
    alert("Cooking time must be filled out!!");
    return false
  }
};

function validateFormCuisines() {
  var h = document.forms["add_cuisines"]["cuisine_name"].value;
  var i = document.forms["add_cuisines"]["cuisine_description"].value;

  if (h == "") {
    alert("Cuisine name must be filled out!!");
    return false
  }
  if (i == "") {
    alert("Cuisine description must be filled out!!");
    return false
  }
};
#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    recipevalues = []
    ingredientsvalues = []
    counter = 0
    min_value = []
    for i in recipe.items():
        recipevalues.append(i[1])
    for i in ingredients.items():
        ingredientsvalues.append(i[1])
    
    for i in range(len(recipevalues)):
        print(recipevalues[i])
        print(ingredientsvalues[i])
        number = ingredientsvalues[i] / recipevalues[i]
        if number >= 1:
            counter+=1
            min_value.append(number)
    counter -= len(recipevalues)
    if counter < 1:
        return 0
    else:
        return min(min_value)

        # ingredientsvalues


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
import requests

first_recipe = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
second_recipe = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
third_recipe = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
#gets taco recipes from API
def getrandomrecipe(url):
    try:
        cookbook = requests.get(url).json()
        for recipe in cookbook:
            base = recipe['base_layer']
            spices = recipe['seasoning']
            mix = recipe['mixin']
            additive = recipe['condiment']
            exterior = recipe['shell']
            print(f'{base}: {spices}: {mix}: {additive}: {exterior}\n')
    except:
        print('Server not found, want to taco bout it')
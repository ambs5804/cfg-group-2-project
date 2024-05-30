
# Create a dictionary to store unit conversions
unit_conversions = {  # unit1 to unit2 (1 cup = 16 tablespoons)
    ('cups', 'tbsp'): 16,
    ('tbsp', 'cups'): 1/16,
    ('cups', 'g'): 250,
    ('g', 'cups'): 1/250,
    ('cups', 'ml'): 250,
    ('ml', 'cups'): 1/250,
    ('tbsp', 'tsp'): 3,
    ('tsp', 'tbsp'): 1/3,
    ('tbsp', 'g'): 1,  # edit
    ('g', 'tbsp'): 1,  # edit
    ('tbsp', 'ml'): 3,
    ('ml', 'tbsp'): 1 / 3,
    ('oz', 'g'): 25,  # edit
    ('g', 'oz'): 1/25,  # edit
    ('fl oz', 'ml'): 25,  # edit
    ('ml', 'oz'): 1 / 25,  # edit
    ('fl oz', 'ml'): 25,  # edit
    ('ml', 'oz'): 1 / 25,  # edit
}


# Define a function that uses the dictionary to convert the units
def convert_units(amount, from_unit, to_unit):
    if (from_unit, to_unit) in unit_conversions:
        converted_amount = amount * unit_conversions[(from_unit, to_unit)]
        return converted_amount
        #print(f'{amount} {from_unit} is {converted_amount} {to_unit}')
 #   else:
  #      print('Invalid unit inputted, please try again.')


# Testing the function
# convert_units(5.5, 'cups', 'g')

# Ask the user for inputs to use as the function variables
user_from_unit = input('What unit would you like to convert from? ').lower()
user_to_unit = input('What unit would you like to convert to? ').lower()
user_amount = float(input(f'How many {user_from_unit} would you like to convert into {user_to_unit} '))

# Call the function
convert_units(user_amount, user_from_unit, user_to_unit)


# # Listing the units
# for units in unit_conversions:
#     print(units)

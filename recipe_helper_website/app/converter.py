
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
    ('tbsp', 'g'): 15,
    ('g', 'tbsp'): 1/15,
    ('tbsp', 'ml'): 3,
    ('ml', 'tbsp'): 1/3,
    ('tsp', 'g'): 5,
    ('g', 'tsp'): 1/5,
    ('tsp', 'ml'): 5,
    ('ml', 'tsp'): 1/5,
    ('oz', 'g'): 28,
    ('g', 'oz'): 1/28,
    ('fl oz', 'ml'): 30,
    ('ml', 'oz'): 1/30,
}

# Define a function that uses the dictionary to convert the units
def convert_units(amount, from_unit, to_unit):
    if (from_unit, to_unit) in unit_conversions:
        converted_amount = amount * unit_conversions[(from_unit, to_unit)]
        return f"{amount} {from_unit} is equal to {converted_amount} {to_unit}"
    else:
        return "Conversion not possible with the provided units."
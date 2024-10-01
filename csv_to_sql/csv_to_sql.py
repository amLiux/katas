import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

column_name_mapping = {
    'ID': 'id',
    'Nombres': 'ingredient_name',
    'Tipo': 'ingredient_type',
    'Cantidad': 'quantity',
    'Unidad': 'unit',
    'Precio por Unidad': 'price_per_unit',
    'Fecha de Caducidad': 'expiration_date'
}

with open(os.path.join(__location__, 'ingredientes.csv'), newline='') as csvfile:
    ingredients_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    headers, *ingredients = ingredients_reader
    # for row in ingredients_reader:
    #     print(row)
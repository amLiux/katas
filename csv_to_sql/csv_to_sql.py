import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

from os.path import split

column_name_mapping = {
    'ID': 'id',
    'Nombres': 'ingredient_name',
    'Tipo': 'ingredient_type',
    'Cantidad': 'quantity',
    'Unidad': 'unit',
    'Precio por Unidad': 'price_per_unit',
    'Fecha de Caducidad': 'expiration_date'
}


def is_float(element: any) -> bool:
    # If you expect None to be passed:
    if element is None:
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False

with open(os.path.join(__location__, 'ingredientes.csv'), newline='', encoding='utf-8') as csvfile:
    ingredients_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    headers, *ingredients = ingredients_reader
    mapped_headers = ", ".join(list(map(lambda header: column_name_mapping[header],headers)))
    final_string = ""
    for ingredient_row in ingredients:
        parsed_column_values= list(map(lambda colval: f"'{colval}'" if not is_float(colval) else colval,ingredient_row))
        final_string+= f"\n({", ".join(parsed_column_values)}),"
    statement = f"INSERT INTO Ingredients ({mapped_headers})" +'\n'  + "VALUES"  + final_string[:-1]  +';' +'\n' + "COMMIT;"
    with open("transaction.sql", "w", encoding='utf-8') as file:
        file.writelines(statement)

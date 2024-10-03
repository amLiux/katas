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

with open(os.path.join(__location__, 'ingredientes.csv'), newline='', encoding='utf-8') as csvfile:
    ingredients_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    headers, *ingredients = ingredients_reader
    mapped_headers = ", ".join(list(map(lambda header: column_name_mapping[header],headers)))
    final_string = ""
    for sub_array in ingredients:
        values_string= ""
        values_string += f"({', '.join(sub_array)})"
        final_string += values_string + ',' + '\n'
    statement = f"INSERT INTO Ingredients ({mapped_headers})" +'\n'  + "VALUES" +'\n' + final_string[:-2] +';' +'\n' + "COMMIT;"
    #print(statement)
    with open("transaction.sql", "w") as file:
      file.writelines(statement)
    # sql_statement = INSERT INTO Ingredients (CustomerName, ContactName, Address, City, PostalCode, Country)
    # VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
    # for row in ingredients_reader:
    #     print(row)
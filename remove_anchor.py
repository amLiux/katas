from utils.type_validator import validator

to_test = [
    [123, "Error"],  # Entrada no válida (int)
    [None, "Error"],  # Entrada no válida (None)
    ["www.codewars.com#about", "www.codewars.com"],
    ["www.codewars.com?page=1", "www.codewars.com?page=1"],
    ["www.codewars.com#section1", "www.codewars.com"],
    ["{'url': 'www.example.com'}", "Error"],  # Entrada como objeto (str)
    [["www.codewars.com"], "Error"],  # Entrada como lista
    ["", ""],  # Cadena vacía
    ["#onlyanchor", ""],  # Solo ancla
    ["www.test.com#query=1&sort=asc", "www.test.com"],
    ["https://example.com/path/to/resource#anchor", "https://example.com/path/to/resource"],
    ["http://example.com#part1?search=query", "http://example.com"],
    ["http://localhost:8000#debug", "http://localhost:8000"],
    ["https://example.com/path#section?param=value", "https://example.com/path"],
    ["https://example.com/path#section1&section2", "https://example.com/path"],
    [3.14, "Error"],  # Entrada no válida (float)
    ["http://example.com/valid#path", "http://example.com/valid"],
    ["test.com#anchor with spaces", "test.com"],
    [{"key": "value"}, "Error"],  # Entrada como diccionario
    ["www.codewars.com#special_characters!@#$%^&*()", "www.codewars.com"],
]

def remove_anchor(input, expected):
     if validator(input, str):
         print(input.rsplit('#')[0])
         print(f"isValid: {input.split('#')[0] == expected}")
     else:
         raise ValueError(f"{input} no es de tipo string")


for input, expected in to_test:
    try:
        remove_anchor(input, expected)
    except ValueError as e:
        print(e)
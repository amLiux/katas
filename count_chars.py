from utils.type_validator import validator
test_cases = [
    # Caso Básico listo
    ("aba", {'a': 2, 'b': 1}),
    # Cadena Vacía listo
    ("", {}),
    # Cadena con Espacios
    (" a b a ", {'a': 2, 'b': 1}),
    # Cadena con Caracteres Especiales
    ("a!b@a#", {'a': 2, 'b': 1, '!': 1, '@': 1, '#': 1}),
    # Cadena con Números
    ("123abc123", {'1': 2, '2': 2, '3': 2, 'a': 1, 'b': 1, 'c': 1}),
    # Cadena con Mayúsculas y Minúsculas
    ("aA", {'a': 1, 'A': 1}),
    # Cadena con Solo Un Carácter
    ("z", {'z': 1}),
    # Tipo de Dato Erróneo (número)
    (123, TypeError),
    # Tipo de Dato Erróneo (lista)
    (["a", "b", "a"], TypeError),
    # Tipo de Dato Erróneo (nulo)
    (None, TypeError),
    # Cadena Larga con Repeticiones
    ("ab" * 1000, {'a': 1000, 'b': 1000}),
    # Cadena con Caracteres Unicode
    ("ñáéíóú", {'ñ': 1, 'á': 1, 'é': 1, 'í': 1, 'ó': 1, 'ú': 1}),
]

def count_chars(input):
    if validator(input, str):
        dict = {}
        #https://stackoverflow.com/questions/113655/is-there-a-function-in-python-to-split-a-word-into-a-list
        for char in input:
            #https://www.geeksforgeeks.org/break-continue-and-pass-in-python/
            if char.isspace():
                continue
            # https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
            if char in dict:
                dict[char]=dict[char]+1
            else:
                # https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
                dict[char] = 1
        return dict
    else:
        raise TypeError("Dato no es tipo string")

for input, expected in test_cases:
    try:
        result = count_chars(input)
        assert result == expected
    except TypeError as e:
        print(e)

 
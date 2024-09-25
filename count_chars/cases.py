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
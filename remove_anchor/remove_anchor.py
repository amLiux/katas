from utils.type_validator import validator

def remove_anchor(input, expected):
     if validator(input, str):
         #assert input.split('#')[0] == expected
         result = input.split('#')[0] == expected
     else:
         raise ValueError(f"{input} no es de tipo string")

from utils.type_validator import validator

def remove_anchor(input):
     if validator(input, str):
         if input.isspace():
            return ''
         return input.split('#')[0]
     else:
         raise ValueError(f"{input} no es de tipo string")

from utils.type_validator import validator

def count_chars(input, expected):
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
        assert dict == expected
        return True
    else:
        raise TypeError("Dato no es tipo string")

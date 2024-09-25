import inspect
import os

from remove_anchor.cases import test_cases


class TestValidator:

    def __init__(self,fn):
        self.__fn_to_test = fn
        self.__fn_path= inspect.getfile(fn)
        self.delimiter = "\\"
        self.__test_cases_path = self.get_test_cases_path()
        self.__test_cases = []
        self.__load_test_cases()

    def get_test_cases_path(self):
        return f"{self.delimiter.join(self.__fn_path.split(self.delimiter)[:-1])}{self.delimiter}cases.py"

    def __load_test_cases(self):
        if os.path.exists(self.__test_cases_path):
            loaded_test_cases = {}
            with open(self.__test_cases_path) as file_reference:
                file_content = file_reference.read()
                #https://www.w3schools.com/python/ref_func_exec.asp
                exec(file_content, {}, loaded_test_cases)
            self.__test_cases=loaded_test_cases["test_cases"]

    def check_test_cases(self):
        print(self.__test_cases)

    def run_tests(self):
        for input, expected in self.__test_cases:
            try:
               self.__fn_to_test(input, expected)
               print("✅ Test passed")
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)

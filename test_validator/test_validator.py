import inspect
import os
from sys import platform

from remove_anchor.cases import test_cases


class TestValidator:
    def __init__(self,fn):
        self.__fn_to_test = fn
        self.__fn_path= inspect.getfile(fn)
        self.__delimiter = self.__get_delimiter_by_os()
        self.__test_cases_path = self.__get_test_cases_path()
        self.__test_cases = []
        self.__load_test_cases()

    def __get_test_cases_path(self):
        return f"{self.__delimiter.join(self.__fn_path.split(self.__delimiter)[:-1])}{self.__delimiter}cases.py"

    def __load_test_cases(self):
        if os.path.exists(self.__test_cases_path):
            loaded_test_cases = {}
            with open(self.__test_cases_path) as file_reference:
                file_content = file_reference.read()
                #https://www.w3schools.com/python/ref_func_exec.asp
                exec(file_content, {}, loaded_test_cases)
            self.__test_cases=loaded_test_cases["test_cases"]

    def __get_delimiter_by_os(self):
        if platform == "linux" or platform == "linux2":
            return "/"
        elif platform == "win32":
            return "\\"

    def run_tests(self):
        for input, expected in self.__test_cases:
            try:
               result = self.__fn_to_test(input)
               assert result == expected
               print("✅ Test passed")
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)


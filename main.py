from test_validator.test_validator import *
from remove_anchor.remove_anchor import remove_anchor
from remove_anchor.cases import test_cases


test_validator = TestValidator(remove_anchor)

test_validator.run_tests()
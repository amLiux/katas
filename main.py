from test_validator.test_validator import *
from remove_anchor.remove_anchor import remove_anchor
from remove_anchor.cases import test_cases
from count_chars.count_chars import count_chars

test_validator = TestValidator(count_chars)

test_validator.run_tests()
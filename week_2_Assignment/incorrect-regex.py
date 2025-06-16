"""incorrect-regex : regex based problem statement"""

import re

def validate_regex_patterns(patterns: list[str]):
    for pattern in patterns:
        try:
            re.compile(pattern)
            print(True)
        except re.error:
            print(False)

# Input
n = int(input())
regex_list = [input() for _ in range(n)]
validate_regex_patterns(regex_list)

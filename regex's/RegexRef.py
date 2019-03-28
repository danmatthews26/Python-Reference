"""
Exibits the use of regular expressions
"""

import re

textToSearch = '''
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1234567890.

    Meta Characters:
    !@#$%^&*(){}[]`
'''

pattern = re.compile(r'\.')
matches = pattern.finditer(textToSearch)

for match in matches:
    print(match)
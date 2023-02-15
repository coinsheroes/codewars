
# FIXME: Replace all dots Python Kata 8 kyu

#Description:

# The code provided is supposed replace all the dots . in the specified String str with dashes -

# But it's not working properly.

# Task
# Fix the bug so we can all go home early.

# Notes
# String str will never be null.






# Solution: 

import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)

import re

text = 'wood took foot food'


print(re.findall('(?:t|f)oo?', text))  # took foot food

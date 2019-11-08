import re
pattern = re.compile(r'\d{4}-\d{3}-\d{3}')
text = 'my phone doc is ironele@gmail.com'
pattern = re.compile(r'[._/\w]+@.[._/\w]+')
match = re.search(pattern, text)
print(match)
names = [ "Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]


new_name = [ name.upper() for name in names if len(name) > 5]
print(new_name)
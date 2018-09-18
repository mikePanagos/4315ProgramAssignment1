# print(isinstance("2s",int))

v="234234234234234243222222222222222444"
print(v.isdigit())
try:
    print(isinstance(int(v),int))
except ValueError:
    pass  # it was a string, not an int.

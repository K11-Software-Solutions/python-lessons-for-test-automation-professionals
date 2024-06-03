#EAFP
# Easier to ask for
# forgiveness than permission
my_dict = {
    'name': 'James'
}
try:
    x = my_dict["key"]
except KeyError:
    # handle missing key
    pass

#LBYL:
# Look before you leap
if "key" in my_dict:
    x = my_dict["key"]
else:
    # handle missing key
    pass

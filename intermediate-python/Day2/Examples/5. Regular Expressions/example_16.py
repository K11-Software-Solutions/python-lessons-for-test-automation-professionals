import re
string = '73838 847, 3778 3834'

# 4 digit number followed by space
# followed by 3 digit number
pattern = '(\d{4}) (\d{2})'
match = re.search(pattern,string)

# group() returns a part of 
# the string where there is a match
print(match.group(1))

# group() returns a part of 
# the string where there is a match
print('Group:',match.group(1,2))

# start() returns index of start of matched string
# end() returns index of end of matched string
print('Start:',match.start())
print('End:',match.end())

#span returns a tuple containing the start 
# and end of matched string
print('Span:',match.span())


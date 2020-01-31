import re
#x='[abc]'
#x='[^abc]
#x='[a-z]'
#x='[a-zA-Z]'
#x='[0-9]'
#x='[^0-9]'
#x='[a-zA-Z0-9]'
#x='[^a-zA-Z0-9]'
#x='\s'
#x='\d'
#x='\D'
#x='\w'
#x='\W'
matcher=re.finditer(x,'a7b @Ak9z')
for match in matcher:
    print("Match is available at",match.start())
    print("Group = ",match.group())

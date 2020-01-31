import re
#x='a+'
#x='a*'
#x='a?'
#x='a{2}'
#x='a{2,3}'
#x='^a'
x='a$'
matcher=re.finditer(x,'abaabaaaacaab')
for match in matcher:
    print("Match is available at",match.start())
    print("Group = ",match.group())
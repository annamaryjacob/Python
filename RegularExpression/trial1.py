import re
count=0
matcher=re.finditer('ab','abbabbabaaab')
for match in matcher:
    print("Match is available at",match.start())
    print("Group = ",match.group())
    count+=1
print("count=",count)

#re.finditer is a code in regular expression
#---.start() and ----.group() are also in regular expression
# this is used to find patterns
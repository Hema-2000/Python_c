#continue control statement

i=0
s="hemalatha"
while(i<len(s)):
    if(s[i]=='e' or s[i]=='a'):
        i+=1
        continue
    print("the current letter:",s[i])
    i+=1

#break control statement
i=0
s="hemalatha"
while(i<len(s)):
    if(s[i]=='e' or s[i]=='a'):
        i+=1
        break
    print("the current letter:",s[i])
    i+=1

#pass control statement
i = 0
s = "hemalatha"
while (i < len(s)):
    if (s[i] == 'e' or s[i] == 'a'):
        i += 1
        pass
    print("the current letter:", i)
    i += 1
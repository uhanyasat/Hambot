

bad_chars = [';', ':', '!', "*","[","]","{","}","(",")",
             "$","@","%","^","&","-","+","/","|",",","'",
             "-","—",'"',".","~","`"]
 
# initializing test string
test_string1 = '''[MULLIGAN]
Yo, I'm a tailor's apprentice
And I got y'all knuckleheads in loco parentis
I'm joining the rebellion 'cause I know it's my chance
To socially advance, instead of sewin' some pants!
I'm gonna take —'''
 
test_string=test_string1.lower()
# printing original string
#print ("Original String : " + test_string)
 
# using replace() to
# remove bad_chars
for i in bad_chars :
    test_string = test_string.replace(i, '')

 
 
# printing resultant string
print (str(test_string))
def convert(lst):
    return (lst[0].split())
 
# Driver code
lst =  [str(test_string)]

word_lst=convert(lst)
print( convert(lst))

sp=len(word_lst)
print(sp)
st_w=word_lst[0]
sp_w=word_lst[sp-1]
print(st_w,sp_w)
thisdict={}
for i in range(sp):
    
    if word_lst[i]==word_lst[sp-2]:
        break
    if sp_w==word_lst[i]:
        break
    thisdict.update({word_lst[i]: [word_lst[i+1],word_lst[i+2]]})
    

print(thisdict)


"""
distribution.py
Author: Nick Lee
Credit: stackoverflow for 2 things so far

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
# convert all text to lower case  //
# asign each char a number
# group numbers 
# sort groups
# sort groups again

import string

string1 = input("Please enter a string of text (the bigger the better): ")
print ('The distribution of characters in "', str(string1), ". is:")
string1 = list(string1)
lower =  string.ascii_lowercase
upper =  string.ascii_uppercase

for i in range(len(string1)): # string is now all lowercase
    letter = string1[i]
    for j in range(26):
        if letter == upper[j]:
            string1[i] = lower[j]
        string1[i] = str(j)
    
"""
for i in range(len(string1)):
    letter = string1[i]
    for j in range(26):
        if letter == lower[j]:
            string1[i] = str(j)
"""
string1 = ''.join(string1) # joins list back into string with the help of overflow

print(str(string1)) 













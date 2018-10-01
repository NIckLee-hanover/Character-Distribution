"""
distribution.py
Author: Nick Lee
Credit: stackoverflow for 5 things so far

Assignment: Character distrbution

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

# i tihnk it should be noted that in post i don't understand some of what i wrote.
"""
1. order of operations:
2. convert string to lower case
3. count the amount of each character
4. see what the max amount of one char is
5. add each group of the same amount to a string and print the string in order
6. decrese the max amount by one and repeat step 5
"""
import string


string1 = input("Please enter a string of text (the bigger the better): ")
print ('The distribution of characters in "' + str(string1) + '" is:')
string1 = list(string1)
lower =  string.ascii_lowercase
upper =  string.ascii_uppercase
string2 = list()
current = list()


for i in range(26): # adds 26 blank spaces to string2
    string2.append('')

for i in range(len(string1)): # converts entire string to lower case
    for j in range(26):
        if string1[i] == upper[j]:
            string1[i] = lower[j]
            

for i in range(26): # counts each letter and adds groups to string2
    amount = string1.count(lower[i])
    for j in (range(amount)):
        string2[i] = ("{0}{1}".format(string2[i], lower[i]))

maxl = 0
for i in range(26): # finds the largest amount of one character
    if len(string2[i]) > maxl:
        maxl = len(string2[i])

string2.sort(key = len) # sorts string2 by legnth

for i in range(len(string2)): # removes the blank spaces from string2... not sure why 
    if string2[0] == '':
        del string2[0]
string2 = list(reversed(string2)) # reverses order... also not sure why


numt = 0
for i in range(len(string2)): # does the rest of the stuff 
    if numt == len(string2):
        break
    del current[:]
    while len(string2[numt]) == maxl: # adds all equal amounts of one character to a list
        current.append(string2[numt])
        numt += 1
        if numt == len(string2):
            break
        
    current.sort()
    for i in range(len(current)): # prints list of each amount of character
        print(current[i])
    maxl -= 1












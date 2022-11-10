# (3).Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII
# χαρακτήρες. Αρχικά, κάντε την κατάλληλη επεξεργασία ώστε να σας μείνει
# κείμενο με μόνο γράμματα και τον κενό χαρακτήρα (space).
# Χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό και ξεκινείστε
# να αφαιρείτε ζευγάρια λέξεων αν το άθροισμα των γραμμάτων τους είναι 20.
# Βγάλτε τα στατιστικά για το μήκος των λέξεων που έμειναν, πχ. 10 λέξεις
# του ενός γράμματος, 12 λέξεις των 2 γραμμάτων, 3 λέξεις των 3 γραμμάτων
# κτλ. Τα ζεύγη δεν χρειάζεται να είναι από συνεχ όμενες λέξεις.

import string
import re
word=[]
Sts=[]
Ans=[]
Help=[]
count=0
a=0
i=1
punc = '''!()-[]{};:'"\,01235456789<>./?@#$%^&*_~'''
# Read in the file.
with open('two_cities_ascii.txt', 'r') as file :
  filedata = file.read()

#remove the numbers and punctuation.
for ele in filedata:
    if ele in punc:
         filedata= filedata.replace(ele, "")

#count the letters of any word and return it in an element.
for letter in filedata:
    if (letter!=' '):
        count=count+1
    else:
        word.append(count)
        count=0
#put the elements in ascending order
word.sort()

for x in range(0,19):
    Sts.append(word.count(x))
#the words with 10 letters will be 0 or 1
e=Sts[9]%2
Help=Sts.copy()
Help.reverse()
#find the the final answer
for i, j in zip(Sts, Help):
    Ans.append(abs(i - j))
Ans=Ans[:9]
Ans.append(e)

#print(Sts)
#print(Help)
#print(filedata)
print(Ans)
for i in range(0,10):
    print('Word with',i+1,'letters is:',Ans[i])
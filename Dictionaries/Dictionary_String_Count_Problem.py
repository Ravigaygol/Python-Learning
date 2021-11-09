# Create a new string variable with the value :

# 'I am so happy to learn python which makes my wife happy and interested in python
#  python python python' 

#Create the loop that goes though string and finds how many times each word appears, 
#and save it to dictionary

#--------------------------------------------------------------------------
#key = Word  Value = No of times the word appears

sentence = 'I am so happy to learn python which makes my wife happy and interested in python python python python'

sentence_dictionary = {}
for each_word in sentence.split(' '):
    sentence_dictionary[each_word] = sentence_dictionary.get(each_word, 0) +1

print(sentence_dictionary)    
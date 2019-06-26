vowels='aeiou' 
word=input('write a word ') 
if word[0] in vowels:
    new_word=word+'way' 
elif word[1] in vowels:
    new_word=word[1:]+word[0]+'ay' 
else:
    new_word=word[2:]+word[:2]+'ay'
print(new_word)

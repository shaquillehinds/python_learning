# Define vowels array
vowels = ['a', 'e', 'i', 'o', 'u']
# ask user for sentence
sentence = input('Please give a sentence to be translated' +
                 '\n'+"--->").strip().lower()
# Parse sentence to array
sentence_array = sentence.split(' ')
# Use List Comprehension to modify sentenceArray to pig latin array
pig_latin_array = [pig + 'yay' if (pig[0] in vowels) else pig[1:] + pig[0] + 'ay' if(len(pig) == 2) else pig[1:] + pig[0] + 'ay' if (pig[1] in vowels)
                   else pig[2:] + pig[0:2] + 'ay' if (pig[2] in vowels) else pig[1:] + pig[0] + 'ay' for pig in sentence_array]
# Join array back into a sentence. declare sentence initial string
pig_latin_sentence = ""
# Loop through each word in pig latin array
for pig in pig_latin_array:
    # Declare a new variable to be modified
    new_pig = pig
    # Check if word contains punctuation and if yes place punctuation at the end of word
    if('.' in pig):
        punctuation = '.'
        new_pig = new_pig.replace('.', '') + '.'
    elif(',' in pig):
        punctuation = ','
        new_pig = new_pig.replace(',', '') + ','
    elif('?' in pig):
        punctuation = '?'
        new_pig = new_pig.replace('?', '') + '?'
    elif('!' in pig):
        punctuation = '!'
        new_pig = new_pig.replace('!', '') + '!'
    # Add space before word and resave variable
    new_pig = ' ' + new_pig
    # Join formatted word to sentence
    pig_latin_sentence += new_pig
# remove white space at the beginning of sentence
pig_latin_sentence = pig_latin_sentence.strip()
print(pig_latin_sentence)

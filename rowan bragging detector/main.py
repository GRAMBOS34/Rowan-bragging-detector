import json

keywords = open('keywords.json')
data = json.load(keywords)

message = input("String to be used for calculation: ") #change input after finishing the code that gets the message data

words = message.lower()
sentence = words.split(" ")
sentence_arr = []

print(sentence)

def calculation(sentence, sentence_val):
    sentence_val = 0

    #Finally fixed it :D
    for x in sentence: 
        for element in data["Bragging"]:
            try: 
                word = element[x]
                if word == 1:
                    sentence_val = sentence_val + 1

                elif word == 2:
                    sentence_val = sentence_val + 2

                elif word == 3:
                    sentence_val = sentence_val + 3

                elif word == 4:
                    sentence_val = sentence_val + 4

                elif word == 5:
                    sentence_val = sentence_val + 5
            except:
                pass

    return sentence_val

total = calculation(sentence, sentence_arr)

print(total)

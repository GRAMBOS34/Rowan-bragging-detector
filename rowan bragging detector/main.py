import json

keywords = open('keywords.json')
data = json.load(keywords)

message = input("String to be used for calculation: ")

words = message.lower()
sentence = words.split(" ")
sentence_arr = []

print(sentence)

def calculation(sentence, sentence_arr):
    sentence_val = 0

    #Finally fixed it :D
    for x in sentence: 
        for element in data["Bragging"]:
            try:
                word = element[x]
                if word == 1:
                    sentence_arr.append(1)

                elif word == 2:
                    sentence_arr.append(2)

                elif word == 3:
                    sentence_arr.append(3)

                elif word == 4:
                    sentence_arr.append(4) 

                elif word == 5:
                    sentence_arr.append(5)    
            except:
                pass

    for number in sentence_arr:
        sentence_val = sentence_val + number

    sentence_arr.clear()
    return sentence_val

total = calculation(sentence, sentence_arr)

print(total)
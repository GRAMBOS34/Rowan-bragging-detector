import enum
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

    #this loop still doesnt work as intended (trying to fix)
    for i in sentence: 
        for element in data["Bragging"]:
            print(element[i])
            try:
                if element[i] == "Certainly not":
                    sentence_arr.append(-2)
                    print(element[i]) 

                elif element[i] == "Not bragging":
                    sentence_arr.append(-1)
                    print(element[i]) 

                elif element[i] == "Maybe":
                    sentence_arr.append(0)
                    print(element[i]) 

                elif element[i] == "Certainly bragging":
                    sentence_arr.append(1)
                    print(element[i])  

                elif element[i] == "Definitely bragging":
                    sentence_arr.append(2)
                    print(element[i])         
            except:
                pass

    for number in sentence_arr:
        sentence_val = sentence_val + number

    sentence_arr.clear()
    return sentence_val

total = calculation(sentence, sentence_arr)

print(total)

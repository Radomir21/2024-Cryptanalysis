#імпорти 
from collections import Counter




#Словник
alphabet='абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

#редагування тексту
text_0 = "D:\\УНИВЕР\\5 курс\\Сryptoanalyzis\\2024-Cryptanalysis\Lab_2\\text.txt"

text_1 = ''
with open(text_0, encoding='utf8') as file:
    text_1 = file.read()
text_1 =  text_1.lower() 
text_1 = text_1.replace('ґ','г').replace('\n', ' ') .replace("'","").replace('"','').replace('—','').replace('!','').replace('?','').replace('.','')


text_2=''
for letter in range(len(text_1)):
    if text_1[letter] in alphabet: text_2+=text_1[letter]

output_text_1 = "output_text_1.txt"
with open(output_text_1 ,'w',encoding="utf8") as file: 
    file.write(text_2)

#необхiдно розрахувати частоти лiтер i бiграм, а також ентропiю та iндекс вiдповiдностi.
freq_letters = Counter(text_2)

for letter in alphabet:
    if letter in freq_letters:
        print(f"'{letter}': {freq_letters[letter]}")


bigrams = [text_2[i:i+2] for i in range(len(text_2) - 1)]
bigram_counts = Counter(bigrams)

print("-----------------------------------------------------------------------")
for bigram, count in bigram_counts.most_common():
    print(f"'{bigram}': {count}")

sum = 0
for elem in freq_letters:
    sum+=freq_letters[elem]
print(sum)

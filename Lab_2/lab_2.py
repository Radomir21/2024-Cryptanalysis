#імпорти 
from collections import Counter
import math 



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

total_letters_sum = sum(freq_letters.values())

p = []
for letter in alphabet:
    if letter in freq_letters:
        count = freq_letters[letter]
        prob_letter = count / total_letters_sum
        p.append(prob_letter)
        #print(f"'{letter}': {count} (ймовірність: {prob_letter})")

#перевірка
#print(p)
print(sum(p))


#кількість біграм 
bigrams = [text_2[i:i+2] for i in range(len(text_2) - 1)]
bigram_counts = Counter(bigrams)

print("-----------------------------------------------------------------------")
#for bigram, count in bigram_counts.most_common():
 #   print(f"'{bigram}': {count}")

total_bigrams_sum = sum(bigram_counts.values())

b = []
for big in bigram_counts:
    count = bigram_counts[big]
    prob_bigram = count / total_bigrams_sum
    b.append(prob_bigram)
    #print(f"'{big}': {count} (ймовірність: {prob_bigram})")

print("-----------------------------------------------------------------------")
#перевірка
#print(b)
print(sum(b))

#ентропія літер
H_1_entropy = 0
for prob in p:
    H_1_entropy += 1/len(p)*(-1*(prob*math.log2(prob)))

print(H_1_entropy)

#ентропія біграм
H_2_entropy = 0
for prob in b:
    H_2_entropy += 1/len(b)*(-1*(prob*math.log2(prob)))

print(H_2_entropy)
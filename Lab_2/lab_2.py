#імпорти 
from collections import Counter
import math 
import random
from random import shuffle
import pickle


#Словник
alphabet='абвгдеєжзиіїйклмнопрстуфхцчшщьюя'

#редагування тексту
text_0 = "E:\\МАГИСТРАТУРА\\КРИПТА\\2024-Cryptanalysis\\Lab_2\\text.txt"

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
#print(sum(p))


#кількість біграм 
bigrams = [text_2[i:i+2] for i in range(len(text_2) - 1)]
bigram_counts = Counter(bigrams)

bigram_alphabet = [a + b for a in alphabet for b in alphabet]

for bigram in bigram_alphabet:
    bigram_counts[bigram] = bigram_counts.get(bigram, 0)

print(bigram_counts)


#for bigram, count in bigram_counts.most_common():
    #print(f"'{bigram}': {count}")

total_bigrams_sum = sum(bigram_counts.values())

b = []
for big in bigram_counts:
    count = bigram_counts[big]
    prob_bigram = count / total_bigrams_sum
    b.append(prob_bigram)
    #print(f"'{big}': {count} (ймовірність: {prob_bigram})")

#перевірка
#print(sum(b))

print("-----------------------------------------------------------------------")
#перевірка

#ентропія літер
H_1_entropy = 0
for prob in p:
    H_1_entropy += 1/len(p)*(-1*(prob*math.log2(prob)))

print(H_1_entropy)

#ентропія біграм
H_2_entropy = 0
for prob in b:
    H_2_entropy += 1/len(b) * (-1 * prob * math.log2(prob) if prob > 0 else 0)

print(H_2_entropy)

#індекс відповідності для літер 
#print(freq_letters)
IC = 0
N = sum(freq_letters.values()) 
for freq in (freq_letters.values()):
    head = freq*(freq- 1)
    IC += head / (N * (N-1))  
#print(IC)


#індекс відповідності для біграм
IC_bigrams = 0
N_bigrams = sum(bigram_counts.values())  # Загальна кількість біграм
for freq in bigram_counts.values():
    head = freq * (freq - 1) 
    IC_bigrams += head / (N_bigrams * (N_bigrams - 1))
#print(IC_bigrams)


#отримання текстів різної довжини 
def random_texts(text, L, N):
    indices = random.choices(range(len(text) - L + 1), k=N)
    return [text[i:i + L] for i in indices]

N = 10_000
L_10 = random_texts(text_2, 10, N)
L_100 = random_texts(text_2, 100, N)
L_1_000 = random_texts(text_2, 1000, N)

N = 1_000
L_10_000 = random_texts(text_2, 10_000, N)


#print(L_10[:5])  
#print(L_100[:5])  


#Віженер для могонрам
def vigenere_cipher_encrypt(text, key, alphabet):
    len_key = len(key)
    encode_text = ''
    for letter in range(len(text)):
        index_text = alphabet.index(text[letter])
        index_key = alphabet.index(key[letter % len_key])
        encoded_char = alphabet[(index_text + index_key) % len(alphabet)]
        encode_text += encoded_char
    return encode_text


def vigenere_cipher_encrypt_list(L, key, alphabet):
    return [vigenere_cipher_encrypt(text, key, alphabet) for text in L]

print('Віженер для могонрам')
key_lengths_input = input("Довжина ключа (наприклад, 1,5,10): ")
key_lengths = [int(length.strip()) for length in key_lengths_input.split(',')]
keys = {length: ''.join(random.choices(alphabet, k=length)) for length in key_lengths}


for length, key in keys.items():
    encrypted_L = vigenere_cipher_encrypt_list(L_10, key, alphabet)
    print(f'\nКлюч длиной {length}: {key}')
    print(f'Исходные строки: {L_10}')
    print(f'Зашифрованные строки: {encrypted_L}')


#Віженер для біграм
def vigenere_cipher_encrypt_bigram(text, key, bigram_alphabet):
    len_key = len(key)
    encode_text = ''
    for i in range(0, len(text)-1, 2):  
        symbol = text[i:i+2]  
        index_text = bigram_alphabet.index(symbol)
        index_key = bigram_alphabet.index(key[i % len_key:i % len_key+2])  
        encoded_char = bigram_alphabet[(index_text + index_key) % len(bigram_alphabet)]
        encode_text += encoded_char
    return encode_text


def vigenere_cipher_encrypt_bigram_list(L, key, bigram_alphabet):
    return [vigenere_cipher_encrypt_bigram(text, key, bigram_alphabet) for text in L]

#print('Віженер для біграм')
#key_lengths_input = input("Довжина ключа (наприклад, 1,5,10): ")
#key_lengths = [int(length.strip()) for length in key_lengths_input.split(',')]
#keys = {length: ''.join(random.choices(bigram_alphabet, k=length)) for length in key_lengths}

#for length, key in keys.items():
    #encrypted_L = vigenere_cipher_encrypt_bigram_list(L_10[:5], key, bigram_alphabet)
    #print(f'\nКлюч длиной {length}: {key}')
    #print(f'Исходные строки: {L_10[:5]}')
    #print(f'Зашифрованные строки: {encrypted_L}')



def affine_encrypt_mono(text, a, b, alphabet):
    if math.gcd(a, len(alphabet)) != 1:
        raise ValueError("Параметр 'a' повинен бути взаємно простим з довжиною алфавіта.")
     
    encrypted_text = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted_index = (a * index + b) % len(alphabet)
            encrypted_text += alphabet[encrypted_index]
        else:
            encrypted_text += letter  
    return encrypted_text

#a = int(input('Введите значение a : '))
#b = int(input('Введите значение b : '))
#encrypted_L = [affine_encrypt_mono(text, a, b, alphabet) for text in L_10[:5]]

#print(f'Значення a={a}')
#print(f'Значення b={b}')

#print("\nИсходные тексты:")
#print(L_10[:5])

#print("\nЗашифрованные тексты:")
#print(encrypted_L)


def affine_encrypt_bigram(text, a, b, alphabet):
    if math.gcd(a, len(alphabet) ** 2) != 1:
        raise ValueError("Параметр 'a' должен быть взаимно простым с квадратом длины алфавита.")

    bigram_alphabet = [a + b for a in alphabet for b in alphabet]  
    encrypted_text = ''
    
    for i in range(0, len(text) - 1, 2):  
        bigram = text[i:i + 2]
        if bigram in bigram_alphabet:
            index = bigram_alphabet.index(bigram)
            encrypted_index = (a * index + b) % len(bigram_alphabet)
            encrypted_text += bigram_alphabet[encrypted_index]
        else:
            encrypted_text += bigram  
    return encrypted_text


#a = int(input("Введите значение a: "))
#b = int(input("Введите значение b: "))
#encrypted_L = [affine_encrypt_bigram(text, a, b, alphabet) for text in L_10[:5]]

#print(f'Значення a={a}')
#print(f'Значення b={b}')

#print("\nИсходные тексты:")
#print(L_10[:5])

#print("\nЗашифрованные тексты:")
#print(encrypted_L)


#Рівномірно розподілений шфир для символів
key = list(alphabet)
shuffle(key)

def norm_distrib_monogram(texts, alphabet, key):
    result = []
    for text in texts:
        encrypted_text = ''.join(key[alphabet.index(letter)] for letter in text)
        result.append(encrypted_text)
    return result

#C = norm_distrib_monogram(L_10[:5], alphabet, key)
#print(f'Открытый текст: {L_10[:5]}')
#print(f'Ключ: {"".join(key)}') 
#print(f'Зашифрованный текст: {C}')



#Рівномірно розподілений шфир для біграм
key = bigram_alphabet.copy()
shuffle(key)

def norm_distrib_bigram(texts, bigram_alphabet, key):
    result = []
    for text in texts:
        encrypted_text = []
        for i in range(0, len(text) - 1, 2):  
            bigram = text[i:i+2]  
            encrypted_text.append(key[bigram_alphabet.index(bigram)]) 
        result.append(''.join(encrypted_text))  
    return result     

#C = norm_distrib_bigram(L_10[:5], bigram_alphabet, key)
#print(f'Открытый текст: {L_10[:5]}')
#print(f'Ключ: {"".join(key)}') 
#print(f'Зашифрованный текст: {C}')


#псевдорозподіл для монограм з рекурентою
def pseudo_random_mono(texts, alphabet):
    result = []
    for text in texts:
        s = [random.randint(0, 31), random.randint(0, 31)]
        encrypted_text = ''.join([alphabet[s[0]], alphabet[s[1]]])
        
        for _ in range(2, len(text)):
            next_value = (s[-1] + s[-2]) % len(alphabet)
            s.append(next_value)
            encrypted_text += alphabet[next_value]
        
        result.append(encrypted_text)
    
    return result

#C = pseudo_random_mono(L_10[:5], alphabet)
#print(f'Открытый текст: {L_10[:5]}')
#print(f'Зашифрованный текст: {C}')



def pseudo_random_bigram(texts, bigram_alphabet):
    result = []
    
    for text in texts:
        # Разбиваем текст на биграммы
        bigrams = [text[i:i+2] for i in range(0, len(text), 2)]
        encrypted_text = ''
        
        for bigram in bigrams:
            s = [random.randint(0, len(bigram_alphabet) - 1), random.randint(0, len(bigram_alphabet) - 1)]
            encrypted_text += bigram_alphabet[s[0]] + bigram_alphabet[s[1]]
            
            for _ in range(2, len(bigram)):
                next_value = (s[-1] + s[-2]) % len(bigram_alphabet)
                s.append(next_value)
                encrypted_text += bigram_alphabet[next_value]
        
        result.append(encrypted_text)
    
    return result

#C = pseudo_random_bigram(L_10[:5], alphabet)
#print(f'Открытый текст: {L_10[:5]}')
#print(f'Зашифрованный текст: {C}')




A_frq = freq_letters.most_common(3)
print(A_frq)

B_frq = bigram_counts.most_common(7)
print(B_frq)



#Критерий 2.0 для монограм
def criteria_20_monogram(L, A_frq):
    H0 = 0
    H1 = 0
    massive = {item[0] for item in A_frq}  
    for i in range(len(L)):
  
        if any(elem in L[i] for elem in massive):
            H0 += 1 
        else:
            H1 += 1  
    
    return f'H1 = {H1}, H0 = {H0}'

print(criteria_20_monogram(encrypted_L, A_frq))


#Критерий 2.0 для біграм
def criteria_20_bigram(L, B_frq):
    H0 = 0
    H1 = 0

    bigrams = {item[0] for item in B_frq} 
    print(bigrams)
    for i in range(len(L)):
        if any(elem in L[i] for elem in bigrams):
            H0 += 1  
        else:
            H1 += 1  
    
    return f'H1 = {H1}, H0 = {H0}'

print(criteria_20_bigram(encrypted_L, B_frq))


def criteria_21_monogram(L, A_frq, kf=2):
    H0 = 0
    H1 = 0
    massive = {item[0] for item in A_frq}  # Множество символов из A_frq
    
    for i in range(len(L)):
        # Множество Aaf для текущей строки
        Aaf = {char for char in L[i] if char in massive}
        
        # Проверяем условие: |Aaf ∩ A_frq| ≤ kf
        if len(Aaf & massive) <= kf:
            H1 += 1  # Принимается гипотеза H1
        else:
            H0 += 1  # Принимается гипотеза H0
    
    return f'H1 = {H1}, H0 = {H0}'




print(criteria_21_monogram(encrypted_L, A_frq))


def criteria_21_bigram(L, B_frq, kf=4):
    H0 = 0
    H1 = 0
    # Преобразуем B_frq в множество биграмм
    massive = {item[0] for item in B_frq}  # Множество биграмм из B_frq
    
    for i in range(len(L)):
        # Извлекаем биграммы из строки L[i]
        Aaf = {L[i][j:j+2] for j in range(len(L[i]) - 1) if L[i][j:j+2] in massive}
        
        # Проверяем условие: |Aaf ∩ B_frq| ≤ kf
        if len(Aaf & massive) <= kf:
            H1 += 1  # Принимается гипотеза H1
        else:
            H0 += 1  # Принимается гипотеза H0
    
    return f'H1 = {H1}, H0 = {H0}'

print(criteria_21_bigram(encrypted_L, B_frq))
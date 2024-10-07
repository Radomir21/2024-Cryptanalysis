#at first: import data
import numpy as np
import sys

P_distribution_M=[0.24,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.04]
P_distribution_K=[0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05]

encryption_table = np.array([
    [10,13,8,18,12,7,0,6,14,1,9,17,2,16,5,4,11,3,19,15],
    [14,17,11,9,10,6,13,15,5,1,8,19,4,7,12,16,18,0,2,3],
    [8,14,4,5,6,2,13,19,11,16,3,1,18,15,12,7,10,0,9,17],
    [13,5,14,11,0,15,4,17,2,19,12,10,7,16,3,8,1,18,9,6],
    [12,10,6,4,5,16,9,8,19,1,3,13,18,7,15,2,11,14,17,0],
    [15,19,9,1,8,12,2,0,10,3,16,6,17,4,13,18,7,11,5,14],
    [16,14,4,7,11,1,17,9,15,18,2,12,3,0,6,19,8,10,13,5],
    [2,5,3,11,15,19,13,9,1,6,18,4,8,16,10,7,12,14,0,17],
    [13,8,3,10,12,18,15,5,2,7,0,14,9,19,17,1,11,6,16,4],
    [7,2,18,12,10,0,16,19,5,1,15,9,4,8,6,11,17,13,14,3],
    [13,18,4,15,3,1,11,12,16,6,19,0,8,14,10,17,9,7,2,5],
    [3,16,9,12,17,11,15,19,18,4,13,6,14,8,5,1,7,10,0,2],
    [13,4,17,12,2,8,16,6,0,15,5,18,14,11,10,3,1,9,19,7],
    [2,4,1,19,3,16,11,6,15,14,13,12,17,9,0,7,8,10,5,18],
    [5,14,9,0,1,7,17,15,10,13,19,3,4,8,11,16,6,2,12,18],
    [15,8,3,1,2,13,16,9,18,0,14,7,6,11,12,19,4,10,5,17],
    [7,0,14,15,17,16,18,5,19,4,12,10,8,6,9,2,3,13,11,1],
    [18,17,7,8,3,4,1,12,15,13,2,16,11,19,9,0,14,10,6,5],
    [1,16,12,9,14,2,5,13,10,11,15,19,8,17,6,3,18,0,4,7],
    [17,0,10,19,3,6,1,13,14,15,9,4,18,5,12,11,8,16,2,7]
])


#P(C)
def calculate_P_C(P_distribution_M, P_distribution_K, encryption_table):
    P_C = np.zeros(len(encryption_table))  
    for c_value in range(len(encryption_table)):
        total_prob = 0
        for i in range(len(P_distribution_M)):
            for j in range(len(P_distribution_K)):
                if encryption_table[j][i] == c_value:
                    total_prob += P_distribution_M[i] * P_distribution_K[j]
        P_C[c_value] = total_prob
    return P_C

#P(M,C)
def calculate_P_M_C(P_distribution_M, P_distribution_K, encryption_table):
    P_M_C = np.zeros((len(P_distribution_M), len(encryption_table)))
    for i in range(len(P_distribution_M)):  
        for j in range(len(P_distribution_K)):  
            c_value = encryption_table[j][i]  
            P_M_C[i][c_value] += P_distribution_M[i] * P_distribution_K[j]  
    return P_M_C

#P(M|C)
def calculate_P_M_given_C(P_M_C, P_C):
    P_M_given_C = np.zeros((len(P_distribution_M), len(encryption_table)))
    for i in range(len(P_distribution_M)):
        for j in range(len(encryption_table)):
            if P_C[i] > 0:  
                P_M_given_C[j][i] = P_M_C[j][i] / P_C[i]
    return P_M_given_C



# Рахуємо P(M, C) и P(C)
P_M_C = calculate_P_M_C(P_distribution_M, P_distribution_K, encryption_table)
P_C = calculate_P_C(P_distribution_M, P_distribution_K, encryption_table)

#Перевірка (сума ймовірностей =1)
sum=0
for i in range(len(P_distribution_K)):
    for j in range(len(P_distribution_M)):
        sum+= P_M_C[i][j]
print(sum)

# Вычисляем P(M|C)
P_M_given_C = calculate_P_M_given_C(P_M_C, P_C)

print("\nP(M|C):")
for row in P_M_given_C:
    print([round(val, 2) for val in row])

#P(C|M)
def calculate_P_C_given_M(P_M_given_C):
    P_C_given_M= [[0]*len(P_M_given_C) for _ in range(len(P_M_given_C))]
    for i in range(len(P_distribution_M)):
        for j in range(len(encryption_table)):
            P_C_given_M[i][j] = round(P_M_given_C[j][i],3)
    return P_C_given_M

P_C_given_M=calculate_P_C_given_M(P_M_given_C)
print("\nP(C|M):")
for row in P_C_given_M:
    print([round(i,3) for i in row])

#Deterministic array
def find_deterministic_array(P_M_given_C):
    deterministic_array = [0] * len(P_M_given_C)
    for i in range(len(P_M_given_C)):  
        max_probability = max(P_M_given_C[i])  
        deterministic_array[i] = P_M_given_C[i].argmax(int(max_probability)) 
    return deterministic_array

array_final=find_deterministic_array(P_M_given_C)
print(f"\nDeterministic function:{array_final}")

#Deterministic matrix
def find_deterministic_matrix(array_final):
    matrix=[0]*len(array_final)
    for i in range(len(array_final)):
        matrix[i]= [0]*len(array_final)
    for i in range(len(array_final)):
        matrix[i][array_final[i]] = 1
    return matrix

matrix_final=find_deterministic_matrix(array_final)
print("\nDeterministic matrix:")
for row in matrix_final:
    print([i for i in row])

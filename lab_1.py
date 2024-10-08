#at first: import data
import numpy as np

P_distribution_M=[0.22,0.22,0.22,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]						
P_distribution_K=[0.22,0.22,0.22,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]

encryption_table = np.array([
    [5,3,17,18,10,1,7,14,15,13,19,4,8,6,12,16,0,11,2,9],
    [17,2,8,10,3,19,13,12,7,1,6,9,18,11,4,5,14,16,15,0],
    [8,10,4,14,5,13,18,12,15,2,0,7,16,1,17,6,9,11,19,3],
    [18,4,3,9,11,7,15,19,2,13,16,17,0,14,10,8,5,6,1,12],
    [8,12,0,14,16,18,2,4,7,13,15,19,3,17,11,6,9,1,10,5],
    [14,17,8,0,1,3,16,13,12,4,2,9,19,6,15,11,18,7,10,5],
    [15,19,4,16,3,0,13,18,14,11,8,7,9,2,12,10,1,6,17,5],
    [4,13,17,19,10,15,7,9,5,12,3,1,2,6,16,18,0,8,14,11],
    [4,3,11,17,1,14,10,0,19,18,7,13,9,5,15,16,12,8,6,2],
    [16,2,7,18,5,14,10,4,12,13,15,3,19,0,9,1,17,8,6,11],
    [7,4,5,8,13,16,3,10,18,14,15,2,6,17,0,11,12,19,1,9],
    [19,7,1,13,11,10,5,17,3,4,0,16,9,18,2,14,6,12,15,8],
    [9,13,5,18,8,12,2,10,6,19,15,14,3,7,17,0,1,4,16,11],
    [13,19,7,10,8,2,15,3,18,0,9,16,11,1,17,5,4,12,6,14],
    [17,0,9,12,6,1,11,8,3,15,19,2,14,7,5,18,4,16,10,13],
    [9,4,12,16,19,17,7,0,11,15,1,6,8,10,3,13,5,18,2,14],
    [16,15,0,6,18,3,4,5,11,19,12,2,17,10,1,7,13,9,8,14],
    [2,5,7,18,1,13,0,19,11,15,16,17,10,9,6,3,8,4,14,12],
    [4,10,9,6,8,14,16,11,3,5,19,12,15,1,18,2,7,13,17,0],
    [10,4,18,13,14,7,11,17,16,15,12,5,3,2,6,0,9,19,1,8]
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


print(f"\nP(C):\n{P_C}")

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
    print([round(i, 2) for i in row])

#P(C|M)
print("\nP(C|M):")
P_C_given_M=P_M_given_C.T
for row in P_C_given_M:
    print([round(i,2) for i in row])

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

#Loss function 1
def loss_function(P_C,P_C_given_M):
    lost_function_value = 0
    for i in range(len(P_C_given_M)):
        lost_function_value+=P_C[i]*(1 - max(P_C_given_M[i]))
    return lost_function_value

print("\nLoss function 1:")
print(loss_function(P_C,P_C_given_M))

#Stohastic function WOW!!!!(а что можна было и так???)
stohastic_matrix=P_C_given_M.copy()
stohastic_matrix[stohastic_matrix - stohastic_matrix.max(axis=1).reshape(-1,1) < -1e-8] = 0
P_distribution_M_sum = np.sum(np.where(stohastic_matrix != 0, P_distribution_M, 0), axis=1)
stochastic_matrix_final = np.where(stohastic_matrix != 0, np.round(P_distribution_M / P_distribution_M_sum[:, np.newaxis], 2), 0)
print("\nStohastic matrix:")
for row in stochastic_matrix_final:
    print([i for i in row])


#Loss function 2
average_losses = np.round(1 - stochastic_matrix_final, 1)
print("\nLoss function 2:")
print(np.sum(P_M_C.T * average_losses))

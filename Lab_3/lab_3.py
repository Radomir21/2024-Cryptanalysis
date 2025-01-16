import time
#Варіант 18
#Атака на основі КТЛ
print("------------------------------------------------------------------")
print("Атака на основі КТЛ")
print("------------------------------------------------------------------")
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def chinese_thereom(C, N):
    if len(C) != len(N):
        return False
    main_N = 1
    for elem in N:
        main_N *= elem
    modules_n_i = [main_N // elem for elem in N]
    result = sum(C[i] * modules_n_i[i] * extended_gcd(modules_n_i[i], N[i])[1] for i in range(len(C)))

    return result % main_N

def integer_nth_root(x, n):
    low, high = 0, x
    while low < high:
        mid = (low + high + 1) // 2
        if mid ** n > x:
            high = mid - 1
        else:
            low = mid
    return low


C = [
0x2c4321c14574d7a0ffbb2ad8e5f56f87a085f841bb236fcf1c352a19b833dece89b6bd6c4e6363d05dc13004962308fffbd15bab8a62c312a8d52894e2d7ce19ae0a93e250e2eba96355995d772574c0413ba0f3ee6e79507450bdda35c682ea5384a8089eaddcb5026cb4bddffe13b898353bde6a1ca106cd71f451c305a280,
0x61474ab337b37339b596f18333a065103be9087df471db7a56907a593eb195432ca9ed0199514f79d7a49493f38212eb129ff6da867871f0c4d3d004d79fcc2df8af5fea8459d67fb2b87b1a8d076546384debb122d6ae83d7f82bd373dbcbfd05752455bef80a82f106bc025d24789603c9b341bb038e41cb919ab4a180f7d6,
0x16c1b059f87785e798bda249dc18ea6d0f9316cd1923e20a58f9d635f6cceb7173b1294cf63e1b72d8b2d57de36985401b751b21dd91221833258b04973fa90ff077f59ef0fc0286944f461180a283e03a8adab144cfe6a91eb10a0d2365728729a9650874a2cbff584e2584768678fc2fb81ed40f00a786b5e92f830d1c2f7a,
0x14bd2e55dbda457a5f6c256b48ae5a244d001b7e7fbcecfea92072d745b781fb643dcc975008fe5695b9fac627140b405c6758836fa36a3a3cb801b8e6fae85aabcba0c108dfdf235a3292a693afe3524f282159525ea587dd164ab793ea3de9340bc4501d08d3c705c5885ff2d8b11177f44770380989810aa489bfcf03dece,
0x010e8d3951a5a85e1c77cf141a0ae8b57513220f9f2a31e0670eb77c779768173bcb545ceaa14622cab448405f981c262eeb0bdd9cea92f540868e25977809d5d41d89134a7f437a7eb6012095ae081bec2cb6f1710804b8ed64daf5a24b0b19b8bb55c76caa875284139836d7acc3a200f5d1e74605233cc1716562f17919dc
]
N = [
0xB6AF3639EC7EB9E120BE25FEE572EF5F3BAF2D528EDFC12F6B030268FB126807E4ADBA1F629EC070DD97B419A526F653929CA7C910D9260F7EAE09FA4119DE772C89CC597AF70C541B49B7D85F0C1CD8D8BA40085B275B66F68645896E2CBCD860AD5BFD6E5F529DF940CCC30AA530A186A3073A088939293192504B04D20EFD,
0xC2B51C056819104E4688C4817CBCF68149C287DFF47D83DED25EAAF863AC5914CD1454AC1A63C39B3CF94E248A32C83686A1287806686FC5C4F677CF0FCB50977F0A22E1C8718A46E356094790CF399E43D3DB70E49C1602BEFF90077A748967C8C58A63DB2BD78EC380B03EC6C5C19A229DE234C2D3242E8599364420B304D9,
0xC308A970B1FFF39211AFE99144743450730DD6AED975C5247643F8C1E2F0FDF243F2B4D20EAC1868C3A9AC0CF61EF3E6FF0B7575BD57DFFC0FBC04406E65E9611539E7435C60AA0F8C36563DF4FFAB901B1F6A8985AC38C3695F364B6E472F34D02C704242610FAF409DCFDC08B073A71EB92056D1058738A5157439FED476EB,
0xC518548D916F0ACC63F4153928902CA94B9FAF1BAE329D0563E6B615C4F506E5B444B1C689CE76056E5A90CC32E21FC9B94B34DD227D4B52ED005811C693102232104EE9A304E1DC3571F388BF1C4CDDB84B2B58579BE81BB839FF73B7C39A61C2646BDECB734453F4277C7372285CD7C0F7F48369909007EA29BA573FCC98A1,
0xE6A9E99BF599FB422EC5F462570FE1CC426E0179B5BCFD050CC43F6980C62B4639D3A893490C0A2A7A5B5AAA5A1E0D580B7C1F5C9B2908A44B22B8695C14388EFEDF97F8D57ADAFDBC278F38F67576B43C1219B99C26ECD71BE8CF82CB95DCD83719163F3F32FCD8DAD7AA212FBA1D0D4654DEE68F68E7EB068DDBACC35C8B27
]

E = [2,3,4,5,6,7,8]


main_C = chinese_thereom(C, N)
print(f"Шифротекст:\n {hex(main_C)}")
print("------------------------------------------------------------------")
for i in E:
    message = integer_nth_root(main_C, i)
    print(f"E= {i} Повідомлення (hex): {hex(message)}")
    print("------------------------------------------------------------------")
    print(f"Перевірка: {message ** i == main_C}")

print("------------------------------------------------------------------")
print("Атака зустріч по середині")
#Атака зустріч по середині 
C = 0xc8b6377c4dc990bae0286c4a53c3ce948f19b9d89a133da874b3cd42cb3bd76e8beb407fa0d804435b26f99934d8c7a9d8703c0bdce01dde48ad35f837f7b5114aa0b82fb5c5c79048b1907b63f3d439c54926cdc11d91b5cdc482c633c3995b0055262b3b3f1761c215ab779cb4da764f4e0419272f2a9fd8a2de223eb0ae4bc780d10e9bbb78ad33b356dbdddfbaab93b12b0c67b2761291870312b573df44b93c6c839ddd175b3a1b427c38a6235990007e378d0ea1905ed7c97a1ce3e2b5905a0afd5b3c6f49990ff75bb1c3b9b29417311b7feec6e4e4e10534abd00a9e928846941acf62f7040e91eef1abc6ecdde9dcf9add78162cb0cab4cc7697f94
N = 0xCC16EC18C48A65416682B065DA0B6C34767797B6C4A093BEBCB4873DAFA16DDBD80C0F9406C64EBEF001E4731283FCE334FD8C19EF2AFFA21EC66784B399AAD0A5AAFEBC3B56251D512B3EA1DC66A811E09471AF8DB45A8D8EB54676116D197B327E795FC91F1F63228AB101304DBE8E71CBBD74BA318F94538F722F637ECF7AB747B084094D609026F1EE6AD842C4BA302B488C70650C7C429C2317ADF3AA0082966629C7AC5FAAD9F1BFA288368512329622AF8CB09AA284DC6D6C578E50DA3B8377C6BAACA04FC965DD728125ACE0E353E12690F72938DE55006AA86FD4A64EC49C767FB156AA165A10BC7968067DD71E1C6B91C55D74EACDF9AAA9294941
l = 20
exp = 65537


X_1 = [i for i in range(1, 2 ** (l // 2) + 1)]
X_2 = [pow(i, exp, N) for i in X_1]


def mod_inverse(a, m):
    result = extended_gcd(a, m)
    g, x = result[0], result[1]  
    if g != 1:
        raise ValueError('Оберненого не існує')
    return x % m

C_s = [(C * mod_inverse(i, N)) % N for i in X_2]


def mitm_attack(C_s, X_2):
    elem_map = {value: i + 1 for i, value in enumerate(X_2)}
    for i, c in enumerate(C_s):
        if c in elem_map:
            return i + 1, elem_map[c]
    raise ValueError("Відкритий текст не було визначено")

result = mitm_attack(C_s, X_2)
print("------------------------------------------------------------------")
print(f'M1: {result[0]}, M2: {result[1]}\n M: {result[0]*result[1]}')

def verification(result, C, N, exp):
    if result != 0:
        if pow(result[0] * result[1], exp, N) == C:
            print(True)
        else:
            print(False)
    else:
        raise ValueError("Помилка")

print('Перевірка:')
verification(result, C, N, exp)


def brute_force_attack(C_s, X_2, N, exp, C):
    for open_text in range(1, len(X_2) + 1):
        if pow(open_text, exp, N) in C_s:
            return open_text  
    raise ValueError("Відкритий текст не було визначено")

print("------------------------------------------------------------------")
start_time = time.time()
result = mitm_attack(C_s, X_2)
print("Атака зустріч по середині: %s секунд" % (time.time() - start_time))

start_time = time.time()
brute_force_attack(C_s, X_2, N, exp, C)
print("Атака повного перебору: %s секунд" % (time.time() - start_time))


mitm = 0.0007166862487792969
bf = 0.06906390190124512
print(f'Атака зустріч по середині швидше у {bf/mitm}')

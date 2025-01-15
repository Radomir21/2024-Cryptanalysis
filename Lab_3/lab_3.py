#Варіант 18
#Атака на основі КТЛ
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, u_1, v_1 = extended_gcd(b % a, a)
    u = v_1 - (b // a) * u_1
    v = u_1
    return gcd, u, v

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

# values
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

for i in E:
    message = integer_nth_root(main_C, i)
    print(f"E={i} Повідомлення (hex): {hex(message)}")
    print(f"Перевірка: {message ** i == main_C}")
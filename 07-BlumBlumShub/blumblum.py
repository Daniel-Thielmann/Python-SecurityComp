# 07-BlumBlumShub/blum_blum_shub.py

import random

# Valores de p e q devem ser primos grandes ≡ 3 mod 4
p = 13687  # primo, p % 4 == 3
q = 19447  # primo, q % 4 == 3
n = p * q

# Semente s deve ser coprima com n
s = 240750636
assert 0 < s < n and pow(s, 1, p) != 0 and pow(s, 1, q) != 0


# Função de geração BBS
def blum_blum_shub(s, n, num_bits):
    bits = []
    x = (s * s) % n
    for _ in range(num_bits):
        x = pow(x, 2, n)
        bits.append(str(x % 2))
    return "".join(bits)


# Gerar 20.000 bits para o NIST
bits = blum_blum_shub(s, n, 20000)

# Salvar no formato aceito pela suíte online
with open("07-BlumBlumShub/saida_bbs.txt", "w") as f:
    for i in range(0, len(bits), 80):
        f.write(bits[i : i + 80] + "\n")

print("Sequência de 20.000 bits gerada e salva em 'saida_bbs.txt'")
print(f"p = {p}, q = {q}, s = {s}, n = {n}")

# Diffie-Hellman
def gerar_chave_publica(p, g, chave_privada):
    return pow(g, chave_privada, p)

def gerar_segredo_compartilhado(recebido, chave_privada, p):
    return pow(recebido, chave_privada, p)

# Parâmetros públicos
p = 23  # número primo
g = 5   # raiz primitiva módulo p

# Chaves privadas (devem ser secretas)
a = 6  # segredo de Alice
b = 15 # segredo de Bob

# Cálculo das chaves públicas
A = gerar_chave_publica(p, g, a)
B = gerar_chave_publica(p, g, b)

# Cálculo do segredo compartilhado
s_alice = gerar_segredo_compartilhado(B, a, p)
s_bob = gerar_segredo_compartilhado(A, b, p)

assert s_alice == s_bob

print("Parâmetros públicos:")
print(f"p = {p}, g = {g}\n")

print("Chaves privadas:")
print(f"a = {a} (Alice)")
print(f"b = {b} (Bob)\n")

print("Chaves públicas:")
print(f"A = {A} (g^a mod p)")
print(f"B = {B} (g^b mod p)\n")

print("Segredo compartilhado:")
print(f"s = {s_alice} (A^b mod p == B^a mod p)")

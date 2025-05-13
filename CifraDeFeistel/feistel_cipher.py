import random

# Garante blocos de mesmo tamanho, em bits
BLOCK_SIZE = 8  # tamanho em bits (para cada lado: L e R)
NUM_ROUNDS = 16  # número de rodadas

# Função F simples para simular confusão (poderia ser qualquer coisa)
def F(right, subkey):
    return right ^ subkey  # XOR é autorreversível

# Função de geração de subchaves aleatórias
def generate_subkeys(seed=42):
    random.seed(seed)
    return [random.randint(0, 255) for _ in range(NUM_ROUNDS)]

# Encriptação com estrutura de Feistel
def feistel_encrypt(block, subkeys):
    left = (block >> BLOCK_SIZE) & 0xFF
    right = block & 0xFF

    for i in range(NUM_ROUNDS):
        new_left = right
        new_right = left ^ F(right, subkeys[i])
        left, right = new_left, new_right

    return (right << BLOCK_SIZE) | left  # inversão final (R16L16)

# Decriptação com mesma estrutura e subchaves invertidas
def feistel_decrypt(block, subkeys):
    right = (block >> BLOCK_SIZE) & 0xFF
    left = block & 0xFF

    for i in reversed(range(NUM_ROUNDS)):
        new_right = left
        new_left = right ^ F(left, subkeys[i])
        right, left = new_right, new_left

    return (left << BLOCK_SIZE) | right  # desfaz inversão final

# Executar um exemplo
if __name__ == "__main__":
    # Mensagem de 16 bits (8 bits para L e 8 bits para R)
    plaintext = 0b1010101011110000  # 0xAAF0
    print(f"Texto original (bin): {bin(plaintext)}")

    # Gera subchaves
    keys = generate_subkeys()

    # Encripta
    ciphertext = feistel_encrypt(plaintext, keys)
    print(f"Texto cifrado  (bin): {bin(ciphertext)}")

    # Decripta
    decrypted = feistel_decrypt(ciphertext, keys)
    print(f"Texto decifrado(bin): {bin(decrypted)}")

    # Verifica se funcionou
    assert decrypted == plaintext, "Erro: a decriptação não bate com o texto original!"

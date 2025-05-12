import string
from collections import Counter
import matplotlib.pyplot as plt

# =============================
# Cifra de César com deslocamento (chave) k
# =============================


def cifra_cesar(texto, k):
    """
    Aplica a cifra de César ao texto com deslocamento k.
    Somente letras minúsculas são cifradas.
    """
    resultado = []
    alfabeto = string.ascii_lowercase

    for char in texto.lower():
        if char in alfabeto:
            idx = (alfabeto.index(char) + k) % 26
            resultado.append(alfabeto[idx])
        else:
            resultado.append(char)
    return "".join(resultado)


# =============================
# Decriptação da Cifra de César
# =============================


def decifra_cesar(texto_cifrado, k):
    """
    Reverte a cifra de César com a mesma chave k.
    """
    resultado = []
    alfabeto = string.ascii_lowercase

    for char in texto_cifrado.lower():
        if char in alfabeto:
            idx = (alfabeto.index(char) - k) % 26
            resultado.append(alfabeto[idx])
        else:
            resultado.append(char)
    return "".join(resultado)


# =============================
# Criptoanálise: Frequência de Letras
# =============================


def analisar_frequencia(texto):
    """
    Conta a frequência percentual de cada letra no texto.
    """
    texto_filtrado = [c for c in texto.lower() if c in string.ascii_lowercase]
    frequencias = Counter(texto_filtrado)
    total = sum(frequencias.values())
    porcentagens = {
        letra: round((contagem / total) * 100, 2)
        for letra, contagem in frequencias.items()
    }
    return porcentagens


def plotar_frequencias(frequencias, titulo="Frequência de Letras"):
    """
    Gera um gráfico de barras com as frequências das letras.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(frequencias.keys(), frequencias.values())
    plt.title(titulo)
    plt.xlabel("Letra")
    plt.ylabel("Frequência (%)")
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


# =============================
# Execução de Exemplo
# =============================

if __name__ == "__main__":
    mensagem_original = "a criptografia é essencial para proteger dados sensíveis em sistemas de comunicação"
    chave = 3

    # Encriptando
    mensagem_cifrada = cifra_cesar(mensagem_original, chave)
    print("\nMensagem original:")
    print(mensagem_original)

    print("\nMensagem cifrada (César k=3):")
    print(mensagem_cifrada)

    # Decriptando
    mensagem_decifrada = decifra_cesar(mensagem_cifrada, chave)
    print("\nMensagem decifrada:")
    print(mensagem_decifrada)

    # Frequência da mensagem cifrada
    freq = analisar_frequencia(mensagem_cifrada)
    print("\nFrequência de letras no texto cifrado:")
    for letra in sorted(freq):
        print(f"{letra}: {freq[letra]}%")

    # Mostrar gráfico
    plotar_frequencias(freq, titulo="Frequência de Letras na Cifra de César (k=3)")

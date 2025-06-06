# Cifra de Feistel com 16 Rodadas (Python)

**Disciplina:** DCC075 — Segurança Computacional  
**Aluno:** Daniel Alves Thielmann  
**Matrícula:** 202165020AB

## Objetivo

Este projeto implementa uma cifra de Feistel simples com:

- 16 rodadas
- Função F baseada em XOR (autorreversível)
- Encriptação e decriptação de um bloco de 16 bits
- Subchaves geradas aleatoriamente

---

## O que a atividade pedia

| Requisitos feitos:  
| Cifra de Feistel com 16 rodadas  
| Código com comentários  
| Instruções de execução  
| Encriptação  
| Decriptação usando operações reversíveis  
| Função F obrigatória (simples, baseada em XOR)

---

## Como funciona

A estrutura divide um bloco de 16 bits em dois blocos de 8 bits (L e R).  
Para cada rodada `n`:

```
Ln = Rn-1
Rn = Ln-1 XOR F(Rn-1, Kn)
```

A função F é implementada como:

```python
def F(right, subkey):
    return right ^ subkey
```

A decriptação simplesmente inverte a ordem das subchaves, já que XOR é autorreversível.

---

## Como executar

1. Instale o Python 3.
2. Baixe o arquivo `feistel_cipher.py`.
3. Execute com:

python feistel_cipher.py

Você verá:

- Texto original
- Texto cifrado após 16 rodadas
- Texto decifrado (deve bater com o original)

---

## Expansões possíveis (tópicos deixados como opcional)

- Usar **strings de texto** convertidas em blocos binários.
- Implementar **S-Boxes reais** para uma função F mais complexa.
- Suporte a **blocos de tamanho variável**.
- Gerar todas as subchaves a partir de uma chave mestre com permutações.

---

## Referências

- [Feistel Network - Wikipedia](https://en.wikipedia.org/wiki/Feistel_cipher)
- [DES Supplementary Material (S-Boxes)](https://en.wikipedia.org/wiki/DES_supplementary_material)

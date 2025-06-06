# Relatório 08 — Diffie-Hellman (DH)

**Aluno:** Daniel Thielmann  
**Disciplina:** DCC075 – Segurança em Sistemas de Computação  
**Professor:** Edelberto Franco Silva

## Objetivo

Implementar o algoritmo de troca de chaves Diffie-Hellman (DH) para estabelecer um segredo compartilhado entre duas partes. O exercício envolve:

- Definir parâmetros públicos (um número primo `p` e sua raiz primitiva `g`);
- Gerar chaves privadas `a` e `b`;
- Calcular as chaves públicas `A = g^a mod p` e `B = g^b mod p`;
- Calcular o segredo compartilhado `s` de ambos os lados.

---

## Parâmetros Escolhidos

| Parâmetro                   | Valor |
| --------------------------- | ----- |
| p (primo)                   | 23    |
| g (raiz primitiva módulo p) | 5     |
| a (secreto de Alice)        | 6     |
| b (secreto de Bob)          | 15    |
| A = g^a mod p               | 8     |
| B = g^b mod p               | 2     |
| s (segredo compartilhado)   | 13    |

## Execução

O código foi escrito em Python e simula a troca de chaves de maneira didática. Ao final, ambos os lados (Alice e Bob) calculam o mesmo valor secreto `s`, que poderá ser usado para comunicação segura.

## Conclusão

O protocolo Diffie-Hellman é uma das bases da criptografia moderna, permitindo o compartilhamento de chaves mesmo em canais inseguros. No entanto, ele não autentica as partes — o que abre espaço para ataques man-in-the-middle se não for combinado com autenticação.

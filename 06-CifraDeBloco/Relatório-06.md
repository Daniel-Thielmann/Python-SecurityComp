# 06 - Modos de Operações em Cifras de Bloco (AES)

**Disciplina:** DCC075 — Segurança Computacional  
**Aluno:** Daniel Alves Thielmann  
**Matrícula:** 202165020AB

## 1. Encriptação da imagem do Tux com diferentes modos (ECB e CBC)

Nesta prática, foi realizado um experimento de encriptação com o algoritmo **AES-128**, utilizando dois modos de operação: **ECB** e **CBC**.

A imagem utilizada foi o mascote Tux (formato `.png`), convertida para `.ppm`, com separação do cabeçalho e do corpo da imagem. A criptografia foi aplicada **apenas ao corpo da imagem**, mantendo o cabeçalho original para permitir a visualização do resultado após encriptação.

Ferramentas utilizadas:

- **OpenSSL**
- **PowerShell**
- **ImageMagick**
- **Windows 10**
- **Visual Studio Code**

### Etapas e comandos executados:

1. **Download e conversão da imagem com ImageMagick**
2. **Separação do cabeçalho e corpo da imagem**
3. **Criação manual da chave e IV**
4. **Encriptação com AES-128 nos modos ECB e CBC**
5. **Reconstrução das imagens cifradas e visualização dos resultados**

### Análise dos Resultados

- **Imagem com AES-ECB**: Ainda revela o formato do Tux, pois esse modo cifra os blocos isoladamente. Blocos iguais no conteúdo geram blocos iguais cifrados, o que compromete a privacidade de dados estruturados.

- **Imagem com AES-CBC**: Ficou completamente embaralhada, sem traços visuais do conteúdo original. O CBC encadeia os blocos e usa o IV para eliminar padrões, sendo muito mais adequado para proteger imagens e dados estruturados.

## 2. Explicação sobre o ataque Sweet32

### Visão Geral

O ataque **Sweet32** afeta cifras de bloco com blocos de apenas **64 bits**, como **3DES** e **Blowfish**. Ele já foi demonstrado na prática em conexões **HTTPS reais**, onde foi possível vazar dados sensíveis explorando repetições de blocos após grande volume de tráfego.

### Funcionamento

O ataque usa o conceito de **"birthday attack"**, que se baseia na probabilidade de colisões em espaços pequenos (como blocos de 64 bits). Quando uma sessão usa sempre a mesma chave e IV, e trafega muitos dados cifrados, essas colisões acabam revelando informações importantes, como cookies de sessão.

### Conclusão Crítica

Mesmo sendo algoritmos considerados seguros, **o uso incorreto ou ultrapassado os torna vulneráveis**. Hoje não faz mais sentido usar cifras de 64 bits em ambientes web, e protocolos modernos já abandonaram o 3DES. O ideal é usar cifras como o **AES** (com blocos de 128 bits) e modos modernos como **CBC ou GCM**, além de configurar os servidores para não aceitarem cifras antigas.

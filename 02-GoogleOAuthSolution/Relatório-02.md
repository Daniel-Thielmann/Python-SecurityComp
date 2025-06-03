# Relatório - Atividade Prática - Google OAuth2 + RBAC

**Disciplina:** DCC075 — Segurança Computacional  
**Aluno:** Daniel Alves Thielmann  
**Matrícula:** 202165020AB

## Objetivo

Implementar um sistema com autenticação via **Google OAuth2** e **controle de acesso baseado em papéis (RBAC)**.

---

## Tecnologias Utilizadas

- Node.js
- Express
- Google Auth Library
- Dotenv
- HTML + CSS

**OBS:** Não usei o [bun.sh](https://bun.sh/)

---

## Como Executar o Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/Daniel-Thielmann/Python-SecurityComp
   cd Python-SecurityComp/GoogleOAuthSolution
   ```

2. Instale as dependências:

   ```bash
   npm install
   ```

3. Crie um arquivo `.env` com os seguintes dados:

   ```env
   GOOGLE_CLIENT_ID=SEU_CLIENT_ID
   GOOGLE_CLIENT_SECRET=SUA_CLIENT_SECRET
   GOOGLE_REDIRECT_URI=http://localhost:3000/callback
   ```

4. Rode o servidor:

   ```bash
   node src/index.js
   ```

5. Acesse [http://localhost:3000](http://localhost:3000)

---

## Lógica de Autorização RBAC

Após o login, o sistema analisa o e-mail do usuário autenticado para definir o papel (**role**):

- E-mails que terminam com `@admin.com` → `admin`
- E-mails que terminam com `@estudante.ufjf.br` → `manager`
- Outros domínios → `viewer`

---

## Permissões por Papel

| Papel   | Permissões                            |
| ------- | ------------------------------------- |
| admin   | Pode criar, editar e excluir projetos |
| manager | Pode criar e editar projetos          |
| viewer  | Pode apenas visualizar projetos       |

---

## Estrutura de Pastas do Projeto

```
GoogleOAuthSolution/
├── .env
├── package.json
├── public/
│   ├── index.html
│   └── style.css
├── src/
│   └── index.js
├── screenshots/
│   ├── 1.tela-de-login.png
│   ├── 2.oauth2.png
│   ├── 3.tela-de-welcome-viewer.png
│   └── 4.tela-de-welcome-manager.png
```

---

## Observações Finais

- O sistema implementa o fluxo **Authorization Code Flow** do OAuth2.
- O papel do usuário é atribuído automaticamente com base no e-mail.
- A lógica RBAC está implementada na rota `/callback` e usada na rota `/welcome`.
- Todo o código está comentado, limpo e separado em arquivos conforme boas práticas.
- As capturas de tela estão na pasta screenshots.

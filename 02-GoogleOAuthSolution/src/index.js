import express from "express";
import { OAuth2Client } from "google-auth-library";
import dotenv from "dotenv";

dotenv.config();
const app = express();
const PORT = 3000;

const client = new OAuth2Client(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  process.env.GOOGLE_REDIRECT_URI
);

// Serve a página inicial (public/index.html)
app.use(express.static("public"));

// Rota de login que gera a URL de autenticação do Google
app.get("/login", (req, res) => {
  const url = client.generateAuthUrl({
    access_type: "offline",
    scope: ["email", "profile", "openid"],
  });
  res.redirect(url);
});

// Callback do Google após login
app.get("/callback", async (req, res) => {
  try {
    const { code } = req.query;
    const { tokens } = await client.getToken(code);
    client.setCredentials(tokens);

    const ticket = await client.verifyIdToken({
      idToken: tokens.id_token,
      audience: process.env.GOOGLE_CLIENT_ID,
    });

    const payload = ticket.getPayload();
    const name = encodeURIComponent(payload.name);
    const email = encodeURIComponent(payload.email);

    // Define o papel (role) baseado no e-mail
    let role = "viewer"; // padrão

    if (payload.email.endsWith("@admin.com")) {
      role = "admin";
    } else if (payload.email.endsWith("@estudante.ufjf.br")) {
      role = "manager";
    }

    // Redireciona para a página autenticada com dados do usuário
    res.redirect(`/welcome?name=${name}&email=${email}&role=${role}`);
  } catch (err) {
    console.error(err);
    res.status(500).send("Erro ao autenticar com o Google.");
  }
});

// Página autenticada com base no papel (RBAC)
app.get("/welcome", (req, res) => {
  const { name, email, role } = req.query;

  let mensagemPermissao = "";

  if (role === "admin") {
    mensagemPermissao =
      "Você tem permissão total para criar, editar e excluir projetos.";
  } else if (role === "manager") {
    mensagemPermissao = "Você pode criar e editar projetos.";
  } else {
    mensagemPermissao = "Você pode apenas visualizar os projetos.";
  }

  res.send(`
    <h1>Bem-vindo, ${name}!</h1>
    <p>Seu e-mail: ${email}</p>
    <p><strong>Papel:</strong> ${role}</p>
    <p>${mensagemPermissao}</p>
  `);
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});

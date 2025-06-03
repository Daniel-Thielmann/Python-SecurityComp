# Relatório - Atividade de Implementação de RBAC (Controle de Acesso Baseado em Papéis)

**Disciplina:** DCC075 — Segurança Computacional  
**Aluno:** Daniel Alves Thielmann  
**Matrícula:** 202165020AB

## Objetivo

O objetivo desta atividade é implementar um sistema de **RBAC (Role-Based Access Control)** utilizando Python. O sistema deve conter pelo menos **três papéis distintos** e um conjunto de permissões associado a cada um deles. Além disso, foi criado um **menu interativo em CLI** (Command Line Interface) para permitir que um usuário simule ações no sistema de acordo com seu papel.

---

## Papéis e Permissões

O sistema define os seguintes papéis e suas respectivas permissões:

| Papel   | Permissões                         |
| ------- | ---------------------------------- |
| ADMIN   | Criar, Editar, Excluir, Visualizar |
| MANAGER | Criar, Editar, Visualizar          |
| VIEWER  | Visualizar apenas                  |

Cada permissão corresponde a uma ação dentro do sistema de gerenciamento de projetos.

---

## Componentes do Código

### 1. Enumeração de Papéis e Permissões

O código define `Enum` para representar papéis (`Role`) e permissões (`Permission`). Isso garante que os valores são bem definidos e reduz a possibilidade de erros de digitação.

### 2. Mapeamento de Permissões

Um dicionário `roles_permissions` define quais permissões pertencem a cada papel.

### 3. Classe User

A classe `User` representa um usuário com um nome e um papel. Ela possui o método `has_permission` para verificar se o usuário possui determinada permissão.

### 4. Decorador `requires_permission`

Esse decorador é usado para proteger funções de ação do sistema. Ele verifica se o usuário tem a permissão necessária antes de executar a ação.

### 5. Funções de Ações

As ações incluem:

- `create_project`
- `edit_project`
- `delete_project`
- `view_project`

Cada função é protegida com o decorador e imprime uma mensagem de sucesso ou erro conforme o papel do usuário.

### 6. Menu Interativo (CLI)

O menu CLI permite:

- Seleção de nome e papel do usuário
- Escolha de ações
- Verificação automática das permissões com feedback adequado

---

## Como Executar

1. Salve o código como `rbac.py`.
2. Execute com Python 3:
   ```bash
   python rbac.py
   ```

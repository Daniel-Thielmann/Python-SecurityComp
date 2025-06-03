from enum import Enum, auto
from functools import wraps


# Definição de papéis
class Role(Enum):
    ADMIN = auto()
    MANAGER = auto()
    VIEWER = auto()


# Definição de permissões
class Permission(Enum):
    CREATE = auto()
    EDIT = auto()
    DELETE = auto()
    VIEW = auto()


# Mapeamento de permissões por papel
ROLE_PERMISSIONS = {
    Role.ADMIN: {
        Permission.CREATE,
        Permission.EDIT,
        Permission.DELETE,
        Permission.VIEW,
    },
    Role.MANAGER: {Permission.CREATE, Permission.EDIT, Permission.VIEW},
    Role.VIEWER: {Permission.VIEW},
}


# Representa um usuário do sistema
class User:
    def __init__(self, username: str, role: Role):
        self.username = username
        self.role = role

    def has_permission(self, permission: Permission) -> bool:
        return permission in ROLE_PERMISSIONS.get(self.role, set())


# Decorador para checar permissões
def requires_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(user: User, *args, **kwargs):
            if user.has_permission(permission):
                return func(user, *args, **kwargs)
            else:
                print(
                    f"\n[ERRO] {user.username} não tem permissão para {permission.name.lower()}."
                )

        return wrapper

    return decorator


# Ações possíveis no sistema
@requires_permission(Permission.CREATE)
def create_project(user: User):
    print(f"\n{user.username} criou um novo projeto.")


@requires_permission(Permission.EDIT)
def edit_project(user: User):
    print(f"\n{user.username} editou um projeto.")


@requires_permission(Permission.DELETE)
def delete_project(user: User):
    print(f"\n{user.username} excluiu um projeto.")


@requires_permission(Permission.VIEW)
def view_project(user: User):
    print(f"\n{user.username} está visualizando os projetos.")


# Menu interativo de CLI
def run_cli():
    print("=== Sistema de Gerenciamento de Projetos (RBAC) ===\n")
    username = input("Digite seu nome de usuário: ").strip()

    role_options = {1: Role.ADMIN, 2: Role.MANAGER, 3: Role.VIEWER}
    print("\nEscolha seu papel:")
    for num, role in role_options.items():
        print(f"{num} - {role.name.capitalize()}")

    try:
        role_input = int(input("Digite o número correspondente ao papel: ").strip())
        role = role_options[role_input]
    except (ValueError, KeyError):
        print("Papel inválido. Encerrando.")
        return

    user = User(username, role)

    actions = {
        "1": create_project,
        "2": edit_project,
        "3": delete_project,
        "4": view_project,
    }

    while True:
        print("\n--- Ações disponíveis ---")
        print("1 - Criar projeto")
        print("2 - Editar projeto")
        print("3 - Excluir projeto")
        print("4 - Visualizar projetos")
        print("0 - Sair")

        action = input("Escolha a ação: ").strip()

        if action == "0":
            print("Encerrando o sistema. Até logo!")
            break
        elif action in actions:
            actions[action](user)
        else:
            print("Ação inválida. Tente novamente.")


# Execução principal
if __name__ == "__main__":
    run_cli()

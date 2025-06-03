from enum import Enum
from functools import wraps

# Enum para papéis


class Role(Enum):
    ADMIN = 'admin'
    MANAGER = 'manager'
    VIEWER = 'viewer'

# Enum para permissões


class Permission(Enum):
    CREATE = 'create_project'
    EDIT = 'edit_project'
    DELETE = 'delete_project'
    VIEW = 'view_project'


# Mapeamento de permissões por papel
roles_permissions = {
    Role.ADMIN: {Permission.CREATE, Permission.EDIT, Permission.DELETE, Permission.VIEW},
    Role.MANAGER: {Permission.CREATE, Permission.EDIT, Permission.VIEW},
    Role.VIEWER: {Permission.VIEW}
}

# Classe que representa o usuário


class User:
    def __init__(self, username: str, role: Role):
        self.username = username
        self.role = role

    def has_permission(self, permission: Permission) -> bool:
        return permission in roles_permissions.get(self.role, set())

# Decorador para checar permissão


def requires_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(user: User, *args, **kwargs):
            if user.has_permission(permission):
                return func(user, *args, **kwargs)
            else:
                print(
                    f"\n{user.username} não tem permissão para {permission.value.replace('_', ' ')}.")
        return wrapper
    return decorator

# Ações do sistema


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

# Menu interativo


def run_cli():
    print("=== Sistema de Gerenciamento de Projetos ===\n")
    username = input("Digite seu nome: ").strip()

    print("\nEscolha seu papel:")
    print("1 - Admin\n2 - Manager\n3 - Viewer")
    role_input = input("Digite o número do papel: ").strip()

    role_map = {
        '1': Role.ADMIN,
        '2': Role.MANAGER,
        '3': Role.VIEWER
    }

    role = role_map.get(role_input)
    if not role:
        print("Papel inválido. Encerrando.")
        return

    user = User(username, role)

    while True:
        print("\nEscolha uma ação:")
        print("1 - Criar projeto")
        print("2 - Editar projeto")
        print("3 - Excluir projeto")
        print("4 - Visualizar projetos")
        print("0 - Sair")
        action = input("Digite o número da ação: ").strip()

        if action == '1':
            create_project(user)
        elif action == '2':
            edit_project(user)
        elif action == '3':
            delete_project(user)
        elif action == '4':
            view_project(user)
        elif action == '0':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Ação inválida. Tente novamente.")


# Executar CLI se for o script principal
if __name__ == "__main__":
    run_cli()

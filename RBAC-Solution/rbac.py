# Definimos os papéis do sistema e as permissões associadas a cada papel
roles_permissions = {
    'admin': {'create_project', 'edit_project', 'delete_project', 'view_project'},
    'manager': {'create_project', 'edit_project', 'view_project'},
    'viewer': {'view_project'}
}

# Classe que representa um usuário
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role.lower()  # Armazena o papel em letras minúsculas

    def has_permission(self, permission):
        """
        Verifica se o usuário tem uma determinada permissão.
        """
        # Recupera as permissões associadas ao papel do usuário
        permissions = roles_permissions.get(self.role, set())
        return permission in permissions

# Funções do sistema que dependem de permissões
def create_project(user):
    if user.has_permission('create_project'):
        print(f"{user.username} criou um novo projeto.")
    else:
        print(f"{user.username} não tem permissão para criar projetos.")

def edit_project(user):
    if user.has_permission('edit_project'):
        print(f"{user.username} editou um projeto.")
    else:
        print(f"{user.username} não tem permissão para editar projetos.")

def delete_project(user):
    if user.has_permission('delete_project'):
        print(f"{user.username} excluiu um projeto.")
    else:
        print(f"{user.username} não tem permissão para excluir projetos.")

def view_project(user):
    if user.has_permission('view_project'):
        print(f"{user.username} está visualizando os projetos.")
    else:
        print(f"{user.username} não tem permissão para visualizar projetos.")

# Exemplo de uso
if __name__ == "__main__":
    # Criamos usuários de diferentes papéis
    admin_user = User("Alice", "admin")
    manager_user = User("Bob", "manager")
    viewer_user = User("Charlie", "viewer")

    # Testamos as permissões de cada usuário
    create_project(admin_user)
    delete_project(manager_user)
    view_project(viewer_user)
    edit_project(viewer_user)

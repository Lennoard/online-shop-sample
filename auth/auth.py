class UserAuth:

    def __init__(self, usuarios=None):
        self.usuarios = usuarios or []

    def auth(self, email, senha):
        usuario = next((x for x in self.usuarios if x['email'] == email and x['senha'] == senha), None)
        return usuario

from models.concessionaria import Concessionaria
from models.cliente import Cliente
from views.cliente_view import ClienteView

class ClienteController():
    def __init__(self, model: Concessionaria):
        self.__concessionaria_model = model
        self.__cliente_view = ClienteView()

    def run(self):
        opcao = self.__cliente_view.tela_principal()
        while opcao != "0":
            if opcao == "1":
                self.cadastra()
            elif opcao == "2":
                self.lista()
            elif opcao == "3":
                self.atualiza()
            elif opcao == "4":
                self.remove()
            opcao = self.__view.tela_principal()

    def cadastra(self):
        info = self.__view.cadastra()

        if info is not None:
            for cliente in self.__concessionaria.clientes:
                if cliente.num_id == info[2]:
                    self.__view.erro()
                    return

            cliente = Cliente(info[0], info[1], info[2])
            self.__concessionaria.cadastra_objeto(cliente)
            self.__view.sucesso()

    def lista(self):
        self.__view.lista(self.__concessionaria.clientes)

    def atualiza(self):
        info = self.__view.atualiza()

        if info is not None:
            for cliente in self.__concessionaria.clientes:
                if cliente.num_id == info[2]:
                    cliente.nome = info[0]
                    cliente.telefone = info[1]

    def remove(self):
        num_id = self.__view.remove()
        for cliente in self.__concessionaria.clientes:
            if cliente.num_id == num_id:
                self.__concessionaria.remove_objeto(cliente)


    
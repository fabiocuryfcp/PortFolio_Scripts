# script.py

class DataMenu:
    def __init__(self):
        self._menu = {}  # Inicializa o dicionário vazio para armazenar pratos
        self.carregar_menu_demo()

    def criar(self, nome, vegetariano, preco):
        """Adiciona um novo prato ao menu."""
        if nome in self._menu:
            return f"Prato '{nome}' já existe no menu."
        self._menu[nome] = {
            'vegetariano': bool(int(vegetariano)),
            'preco': float(preco)
        }
        return f"Prato '{nome}' criado com sucesso."

    def ler(self, nome):
        """Lê os detalhes de um prato pelo nome."""
        if nome not in self._menu:
            return f"Prato '{nome}' não encontrado."
        detalhes = self._menu[nome]
        lucro = detalhes['preco'] * 0.25
        impostos = detalhes['preco'] * 0.15
        return (f"Nome: {nome}\n"
                f"Vegetariano: {'Sim' if detalhes['vegetariano'] else 'Não'}\n"
                f"Preço: R${detalhes['preco']:.2f}\n"
                f"Lucro aproximado: R${lucro:.2f}\n"
                f"Impostos: R${impostos:.2f}")

    def atualizar(self, nome, vegetariano=None, preco=None):
        """Atualiza os detalhes de um prato existente."""
        if nome not in self._menu:
            return f"Prato '{nome}' não encontrado."
        if vegetariano is not None:
            self._menu[nome]['vegetariano'] = bool(int(vegetariano))
        if preco is not None:
            self._menu[nome]['preco'] = float(preco)
        return f"Prato '{nome}' atualizado com sucesso."

    def deletar(self, nome):
        """Remove um prato do menu pelo nome."""
        if nome not in self._menu:
            return f"Prato '{nome}' não encontrado."
        del self._menu[nome]
        return f"Prato '{nome}' deletado com sucesso."

    def listar_pratos(self):
        """Lista todos os pratos no menu com índice numérico."""
        if not self._menu:
            return "O menu está vazio."
        return '\n'.join(
            f"{i+1}. Nome: {nome}, Vegetariano: {'Sim' if detalhes['vegetariano'] else 'Não'}, Preço: R${detalhes['preco']:.2f}"
            for i, (nome, detalhes) in enumerate(self._menu.items())
        )

    def calcular_lucro(self, nome):
        """Calcula o lucro aproximado (25% do preço) de um prato."""
        if nome not in self._menu:
            return f"Prato '{nome}' não encontrado."
        preco = self._menu[nome]['preco']
        lucro = preco * 0.25
        return f"Lucro aproximado para o prato '{nome}': R${lucro:.2f}"

    def calcular_impostos(self, nome):
        """Calcula os impostos (15% do preço) de um prato."""
        if nome not in self._menu:
            return f"Prato '{nome}' não encontrado."
        preco = self._menu[nome]['preco']
        impostos = preco * 0.15
        return f"Impostos para o prato '{nome}': R${impostos:.2f}"

    def carregar_menu_demo(self):
        """Carrega um menu de demonstração com pratos predefinidos."""
        pratos_demo = [
            ("porção de batata", 1, 5.00),
            ("noque", 0, 20.00),
            ("lanche", 0, 30.00)
        ]
        for nome, vegetariano, preco in pratos_demo:
            self.criar(nome, vegetariano, preco)

    def obter_nome_por_indice(self, indice):
        """Obtém o nome do prato pelo índice (1-based)."""
        pratos = list(self._menu.keys())
        if 1 <= indice <= len(pratos):
            return pratos[indice - 1]
        return None

    # Propriedade para acessar o menu
    @property
    def menu(self):
        return self._menu

    @menu.setter
    def menu(self, value):
        if not isinstance(value, dict):
            raise ValueError("O menu deve ser um dicionário.")
        self._menu = value

    # Propriedade para acessar um prato específico
    def get_prato(self, nome):
        if nome not in self._menu:
            return None
        return self._menu[nome]

    def set_prato(self, nome, vegetariano, preco):
        if nome not in self._menu:
            raise KeyError(f"Prato '{nome}' não encontrado.")
        self._menu[nome] = {
            'vegetariano': bool(int(vegetariano)),
            'preco': float(preco)
        }

class Interface:
    def __init__(self):
        self.data_menu = DataMenu()

    def escolher_prato(self):
        """Permite ao usuário escolher um prato a partir de uma lista numerada."""
        while True:
            print("\nPratos disponíveis:")
            print(self.data_menu.listar_pratos())
            try:
                escolha = int(input("Digite o número do prato desejado ou 0 para cancelar: ").strip())
                if escolha == 0:
                    return None
                prato = self.data_menu.obter_nome_por_indice(escolha)
                if prato:
                    return prato
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def run(self):
        """Executa a interface de linha de comando."""
        while True:
            print("\nMenu de Comandos:")
            print("1 - Criar prato")
            print("2 - Atualizar prato")
            print("3 - Deletar prato")
            print("4 - Visualizar prato")  # Atualizado para item 4
            print("5 - Calcular lucro")
            print("6 - Calcular impostos")
            print("0 - Sair")
            
            comando = input("Escolha uma opção (0-6): ").strip()  # Atualizado para 0-6

            if comando == '0':
                print("Saindo...")
                break

            elif comando == '1':
                nome = input("Digite o nome do prato: ").strip()
                vegetariano = input("O prato é vegetariano? (1 para sim, 0 para não): ").strip()
                preco = input("Digite o preço do prato: ").strip()
                print(self.data_menu.criar(nome, vegetariano, preco))

            elif comando == '2':
                prato = self.escolher_prato()
                if prato:
                    vegetariano = input("Novo valor para vegetariano? (1 para sim, 0 para não, deixe em branco para não alterar): ").strip()
                    preco = input("Novo preço do prato (deixe em branco para não alterar): ").strip()
                    print(self.data_menu.atualizar(prato, vegetariano if vegetariano else None, preco if preco else None))

            elif comando == '3':
                prato = self.escolher_prato()
                if prato:
                    print(self.data_menu.deletar(prato))

            elif comando == '4':
                prato = self.escolher_prato()
                if prato:
                    print(self.data_menu.ler(prato))

            elif comando == '5':
                prato = self.escolher_prato()
                if prato:
                    print(self.data_menu.calcular_lucro(prato))

            elif comando == '6':
                prato = self.escolher_prato()
                if prato:
                    print(self.data_menu.calcular_impostos(prato))

            else:
                print("Opção não reconhecida. Tente novamente.")

if __name__ == "__main__":
    cli = Interface()
    cli.run()


import tkinter as tk
from tkinter import messagebox


class SaborRapidoApp:
    """Classe principal da aplicação de gerenciamento de pedidos."""
    def __init__(self, root):
        # Configuração da janela principal
        self.root = root
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("800x600")

        # Dicionário de itens do menu com seus preços
        self.itens_menu = {"Hambúrguer": 10.00,
                           "Batata Frita": 5.00, "Refrigerante": 3.00}
        # Lista para armazenar os itens do pedido atual
        self.pedido = []

        # --- Frames para organizar a interface ---
        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        menu_frame = tk.LabelFrame(main_frame, text="Menu", font=("Arial", 12))
        menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        pedido_frame = tk.LabelFrame(main_frame, text="Pedido Atual", font=("Arial", 12))
        pedido_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        admin_frame = tk.LabelFrame(root, text="Adicionar Novo Item ao Menu", font=("Arial", 12))
        admin_frame.pack(padx=10, pady=5, fill="x")

        # --- Conteúdo do Frame do Menu ---
        self.listbox_menu = tk.Listbox(
            menu_frame, selectmode=tk.MULTIPLE, font=("Arial", 10), exportselection=False)
        self.atualizar_lista_menu()  # Preenche a lista com os itens iniciais
        self.listbox_menu.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        tk.Button(menu_frame, text="Adicionar ao Pedido",
                  command=self.adicionar_pedido).pack(pady=5)

        # --- Conteúdo do Frame do Pedido ---
        self.listbox_pedido = tk.Listbox(
            pedido_frame, selectmode=tk.EXTENDED, font=("Arial", 10), exportselection=False)
        self.listbox_pedido.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        
        botoes_pedido_frame = tk.Frame(pedido_frame)
        botoes_pedido_frame.pack(pady=5)
        tk.Button(botoes_pedido_frame, text="Remover Item",
                  command=self.remover_item_selecionado).pack(side=tk.LEFT, padx=5)
        tk.Button(botoes_pedido_frame, text="Finalizar Pedido",
                  command=self.finalizar_pedido).pack(side=tk.LEFT, padx=5)

        # --- Conteúdo do Frame de Administração ---
        item_frame = tk.Frame(admin_frame)
        item_frame.pack(pady=2)
        tk.Label(item_frame, text="Item:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.entry_item = tk.Entry(item_frame, font=("Arial", 10))
        self.entry_item.pack(side=tk.LEFT)

        preco_frame = tk.Frame(admin_frame)
        preco_frame.pack(pady=2)
        tk.Label(preco_frame, text="Preço:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.entry_preco = tk.Entry(preco_frame, font=("Arial", 10))
        self.entry_preco.pack(side=tk.LEFT)

        tk.Button(admin_frame, text="Adicionar Item ao Menu",
                  command=self.adicionar_item_menu).pack(pady=5)

    def atualizar_lista_menu(self):
        """Atualiza a Listbox com os itens presentes no dicionário itens_menu."""
        self.listbox_menu.delete(0, tk.END)  # Limpa a lista atual
        for item in self.itens_menu.keys():
            self.listbox_menu.insert(tk.END, item)  # Insere cada item do menu

    def adicionar_pedido(self):
        """Adiciona os itens selecionados na Listbox à lista de pedidos."""
        selecionados = self.listbox_menu.curselection()  # Obtém índices dos itens selecionados
        for index in selecionados:
            item = self.listbox_menu.get(index)
            self.pedido.append(item)
            self.listbox_pedido.insert(tk.END, item)
        messagebox.showinfo("Pedido", "Itens adicionados com sucesso!")
        self.listbox_menu.selection_clear(0, tk.END)

    def finalizar_pedido(self):
        """Calcula o total, exibe o valor e limpa o pedido."""
        if not self.pedido:
            messagebox.showinfo(
                "Pedido", "Adicione itens antes de finalizar o pedido.")
            return
        # Soma os valores dos itens baseando-se no dicionário de preços
        total = sum(self.itens_menu[item] for item in self.pedido)
        messagebox.showinfo(
            "Total", f"Total do pedido: R$ {total:.2f}\nPedido finalizado!")
        self.pedido.clear()
        self.listbox_pedido.delete(0, tk.END)

    def remover_item_selecionado(self):
        """Remove os itens selecionados do pedido atual."""
        selecionados = self.listbox_pedido.curselection()
        if not selecionados:
            messagebox.showwarning("Aviso", "Selecione um item do pedido para remover.")
            return

        # Remove da lista de pedidos e da listbox, iterando de trás para frente
        for index in reversed(selecionados):
            self.pedido.pop(index)
            self.listbox_pedido.delete(index)

    def adicionar_item_menu(self):
        """Adiciona um novo item ao menu com validação de preço."""
        item = self.entry_item.get().strip()
        preco = self.entry_preco.get().strip()
        if item and preco:
            try:
                # Converte o preço e atualiza o menu e a interface
                self.itens_menu[item] = float(preco)
                self.atualizar_lista_menu()
                self.entry_item.delete(0, tk.END)
                self.entry_preco.delete(0, tk.END)
                messagebox.showinfo(
                    "Sucesso", "Item adicionado ao menu com sucesso!")
            except ValueError:
                messagebox.showerror(
                    "Erro", "Preço inválido. Digite um valor numérico.")
        else:
            messagebox.showerror(
                "Erro", "Preencha ambos os campos corretamente.")


def iniciar_app():
    """Inicializa e executa a aplicação Tkinter."""
    root = tk.Tk()
    app = SaborRapidoApp(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_app()

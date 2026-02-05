
import tkinter as tk
from tkinter import messagebox


class SaborRapidoApp:
    """Classe principal da aplicação de gerenciamento de pedidos."""
    def __init__(self, root):
        # Configuração da janela principal
        self.root = root
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("400x500")

        # Dicionário de itens do menu com seus preços
        self.itens_menu = {"Hambúrguer": 10.00,
                           "Batata Frita": 5.00, "Refrigerante": 3.00}
        # Lista para armazenar os itens do pedido atual
        self.pedido = []

        # Rótulo de instrução
        tk.Label(root, text="Selecione os itens do pedido:",
                 font=("Arial", 12)).pack(pady=10)

        # Lista de seleção (Listbox) permitindo múltipla seleção
        self.listbox = tk.Listbox(
            root, selectmode=tk.MULTIPLE, font=("Arial", 10))
        self.atualizar_lista_menu()  # Preenche a lista com os itens iniciais
        self.listbox.pack()

        # Botões de ação para manipular o pedido
        tk.Button(root, text="Adicionar ao Pedido",
                  command=self.adicionar_pedido).pack(pady=5)
        tk.Button(root, text="Visualizar Pedido",
                  command=self.visualizar_pedido).pack(pady=5)
        tk.Button(root, text="Remover do Pedido",
                  command=self.remover_pedido).pack(pady=5)
        tk.Button(root, text="Finalizar Pedido",
        
                  command=self.finalizar_pedido).pack(pady=10)

        # Seção para cadastrar novos produtos no menu
        tk.Label(root, text="Adicionar Novo Item ao Menu:",
                 font=("Arial", 12)).pack(pady=10)
        self.entry_item = tk.Entry(root, font=("Arial", 10))
        self.entry_item.pack()
        self.entry_preco = tk.Entry(root, font=("Arial", 10))
        self.entry_preco.pack()
        tk.Button(root, text="Adicionar Item",
                  command=self.adicionar_item_menu).pack(pady=5)

    def atualizar_lista_menu(self):
        """Atualiza a Listbox com os itens presentes no dicionário itens_menu."""
        self.listbox.delete(0, tk.END)  # Limpa a lista atual
        for item in self.itens_menu.keys():
            self.listbox.insert(tk.END, item)  # Insere cada item do menu

    def adicionar_pedido(self):
        """Adiciona os itens selecionados na Listbox à lista de pedidos."""
        selecionados = self.listbox.curselection()  # Obtém índices dos itens selecionados
        for index in selecionados:
            item = self.listbox.get(index)
            self.pedido.append(item)
        messagebox.showinfo("Pedido", "Itens adicionados com sucesso!")

    def visualizar_pedido(self):
        """Exibe uma janela com a lista de itens no pedido atual."""
        if not self.pedido:
            messagebox.showinfo("Pedido", "Nenhum item no pedido.")
            return
        pedido_texto = "\n".join(self.pedido)
        messagebox.showinfo(
            "Pedido Atual", f"Itens no pedido:\n{pedido_texto}")

    def remover_pedido(self):
        """Remove o último item adicionado ao pedido (comportamento de pilha)."""
        if not self.pedido:
            messagebox.showwarning("Aviso", "O pedido está vazio.")
            return
        item = self.pedido.pop()  # Remove o último item da lista
        messagebox.showinfo("Removido", f"Item '{item}' removido do pedido.")

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
        self.pedido.clear()  # Reseta o pedido para o próximo cliente

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


if __name__ == "__main__":
    root = tk.Tk()
    app = SaborRapidoApp(root)
    root.mainloop()

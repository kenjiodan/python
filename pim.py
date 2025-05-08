import customtkinter as ctk
import tkinter.messagebox as mb
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean, median, mode
import json
import os

ARQUIVO_EXCEL = "usuarios.xlsx"
ARQUIVO_AUTH = "auth.json"

# ---------- Utilitários ----------
def criar_planilha():
    if not os.path.exists(ARQUIVO_EXCEL):
        df = pd.DataFrame(columns=["Nome", "Idade", "Email", "Curso"])
        df.to_excel(ARQUIVO_EXCEL, index=False)

def validar_login(usuario, senha):
    if not os.path.exists(ARQUIVO_AUTH):
        with open(ARQUIVO_AUTH, 'w') as f:
            json.dump({"usuario": "admin", "senha": "1234"}, f)
        mb.showinfo("Login Padrão", "Login padrão criado: admin / 1234")
    with open(ARQUIVO_AUTH, 'r') as f:
        cred = json.load(f)
    return usuario == cred["usuario"] and senha == cred["senha"]

# ---------- Interface Principal ----------
class PlataformaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IncluirTec - Plataforma de Educação Digital Segura")
        self.geometry("800x600")
        self.resizable(False, False)

        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(expand=True, fill="both", padx=20, pady=20)

        self.tab_cadastro()
        self.tab_listagem()
        self.tab_estatisticas()
        self.tab_grafico()
        self.tab_admin()

    # ---------- Aba: Cadastro de Usuários ----------
    def tab_cadastro(self):
        tab = self.tabs.add("Cadastro")

        self.nome = ctk.CTkEntry(tab, placeholder_text="Nome")
        self.nome.pack(pady=5)
        self.idade = ctk.CTkEntry(tab, placeholder_text="Idade")
        self.idade.pack(pady=5)
        self.email = ctk.CTkEntry(tab, placeholder_text="Email")
        self.email.pack(pady=5)
        self.curso = ctk.CTkEntry(tab, placeholder_text="Curso")
        self.curso.pack(pady=5)

        ctk.CTkButton(tab, text="Cadastrar", command=self.cadastrar_usuario).pack(pady=10)

    def cadastrar_usuario(self):
        nome = self.nome.get()
        idade = self.idade.get()
        email = self.email.get()
        curso = self.curso.get()

        if not nome or not idade or not email or not curso:
            mb.showwarning("Aviso", "Preencha todos os campos.")
            return
        try:
            idade = int(idade)
        except ValueError:
            mb.showerror("Erro", "Idade deve ser um número.")
            return

        df = pd.read_excel(ARQUIVO_EXCEL)
        novo = pd.DataFrame([[nome, idade, email, curso]], columns=df.columns)
        df = pd.concat([df, novo], ignore_index=True)
        df.to_excel(ARQUIVO_EXCEL, index=False)

        mb.showinfo("Sucesso", "Usuário cadastrado.")
        self.nome.delete(0, 'end')
        self.idade.delete(0, 'end')
        self.email.delete(0, 'end')
        self.curso.delete(0, 'end')

    # ---------- Aba: Lista de Usuários ----------
    def tab_listagem(self):
        tab = self.tabs.add("Listar Usuários")
        self.texto_lista = ctk.CTkTextbox(tab, width=700, height=400)
        self.texto_lista.pack(pady=10)
        ctk.CTkButton(tab, text="Carregar Lista", command=self.listar_usuarios).pack()

    def listar_usuarios(self):
        df = pd.read_excel(ARQUIVO_EXCEL)
        self.texto_lista.delete("0.0", "end")
        if df.empty:
            self.texto_lista.insert("0.0", "Nenhum usuário cadastrado.")
        else:
            self.texto_lista.insert("0.0", df.to_string(index=False))

    # ---------- Aba: Estatísticas ----------
    def tab_estatisticas(self):
        tab = self.tabs.add("Estatísticas")
        self.stats_box = ctk.CTkTextbox(tab, width=500, height=200)
        self.stats_box.pack(pady=10)
        ctk.CTkButton(tab, text="Calcular Estatísticas", command=self.calcular_estatisticas).pack()

    def calcular_estatisticas(self):
        df = pd.read_excel(ARQUIVO_EXCEL)
        self.stats_box.delete("0.0", "end")
        if df.empty:
            self.stats_box.insert("0.0", "Nenhum dado disponível.")
            return
        idades = df["Idade"].tolist()
        texto = f"Média: {mean(idades):.2f}\n"
        texto += f"Mediana: {median(idades)}\n"
        try:
            texto += f"Moda: {mode(idades)}"
        except:
            texto += "Moda: Sem valor dominante"
        self.stats_box.insert("0.0", texto)

    # ---------- Aba: Gráfico ----------
    def tab_grafico(self):
        tab = self.tabs.add("Gráfico")
        ctk.CTkButton(tab, text="Gerar Gráfico", command=self.gerar_grafico).pack(pady=20)

    def gerar_grafico(self):
        df = pd.read_excel(ARQUIVO_EXCEL)
        if df.empty:
            mb.showinfo("Info", "Nenhum dado para gerar gráfico.")
            return
        cursos = df["Curso"].value_counts()
        cursos.plot(kind='bar', title="Usuários por Curso", color="skyblue")
        plt.xlabel("Curso")
        plt.ylabel("Quantidade")
        plt.tight_layout()
        plt.savefig("grafico_cursos.png")
        plt.show()

    # ---------- Aba: Administração ----------
    def tab_admin(self):
        tab = self.tabs.add("Admin")
        ctk.CTkLabel(tab, text="Novo Usuário").pack(pady=5)
        self.novo_usuario = ctk.CTkEntry(tab, placeholder_text="Usuário")
        self.novo_usuario.pack(pady=5)
        ctk.CTkLabel(tab, text="Nova Senha").pack(pady=5)
        self.nova_senha = ctk.CTkEntry(tab, placeholder_text="Senha", show="*")
        self.nova_senha.pack(pady=5)
        ctk.CTkButton(tab, text="Salvar Novo Login", command=self.atualizar_login).pack(pady=15)

    def atualizar_login(self):
        usuario = self.novo_usuario.get()
        senha = self.nova_senha.get()
        if not usuario or not senha:
            mb.showwarning("Aviso", "Preencha usuário e senha.")
            return

        with open(ARQUIVO_AUTH, 'w') as f:
            json.dump({"usuario": usuario, "senha": senha}, f)
        mb.showinfo("Sucesso", "Login atualizado com sucesso.")
        self.novo_usuario.delete(0, 'end')
        self.nova_senha.delete(0, 'end')


# ---------- Tela de Login ----------
class LoginScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login de Administrador")
        self.geometry("400x250")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Usuário").pack(pady=5)
        self.usuario = ctk.CTkEntry(self)
        self.usuario.pack(pady=5)

        ctk.CTkLabel(self, text="Senha").pack(pady=5)
        self.senha = ctk.CTkEntry(self, show="*")
        self.senha.pack(pady=5)

        ctk.CTkButton(self, text="Entrar", command=self.login).pack(pady=20)

    def login(self):
        if validar_login(self.usuario.get(), self.senha.get()):
            self.destroy()
            app = PlataformaApp()
            app.mainloop()
        else:
            mb.showerror("Erro", "Usuário ou senha inválidos.")

# ---------- Execução ----------
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    criar_planilha()
    LoginScreen().mainloop()

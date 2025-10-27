import customtkinter as ctk
import subprocess
import psutil  # <- precisa instalar: pip install psutil

# Aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Painel de Automação")
app.geometry("400x350")

ctk.CTkLabel(app, text="MACRO BRSUPER", font=("Arial", 20)).pack(pady=20)

processo_atual = None

def rodar_macro(caminho):
    """Inicia o macro como subprocesso."""
    global processo_atual

    # Se já há um processo rodando, não inicia outro
    if processo_atual and processo_atual.poll() is None:
        print("Um macro já está sendo executado.")
        return

    processo_atual = subprocess.Popen(["python", caminho], shell=True)
    print(f"Executando: {caminho}")

def parar_macro(event=None):
    """Força o encerramento completo do macro."""
    global processo_atual
    if processo_atual and processo_atual.poll() is None:
        try:
            # Encerra todos os subprocessos filhos
            parent = psutil.Process(processo_atual.pid)
            for child in parent.children(recursive=True):
                child.kill()
            parent.kill()
            print("Macro encerrado com sucesso.")
        except Exception as e:
            print("Erro ao encerrar macro:", e)
    else:
        print("Nenhum macro em execução.")

# Botões
b1 = ctk.CTkButton(app, text="O.S LOS",
                   command=lambda: rodar_macro("C:/Users/paulo/OneDrive/Área de Trabalho/Macro/macrolos.py"))
b2 = ctk.CTkButton(app, text="O.S LENTIDÃO",
                   command=lambda: rodar_macro("C:/Users/paulo/OneDrive/Área de Trabalho/Macro/macrolentidaovisita.py"))
b3 = ctk.CTkButton(app, text="O.S LENTIDÃO SEM ACESSO",
                   command=lambda: rodar_macro("C:/Users/paulo/OneDrive/Área de Trabalho/Macro/macrolentidaosemacesso.py"))
b_parar = ctk.CTkButton(app, text="🛑 Parar Execução (ESC)",
                        fg_color="red", hover_color="#aa0000", command=parar_macro)

b1.pack(pady=10)
b2.pack(pady=10)
b3.pack(pady=10)
b_parar.pack(pady=20)

# Atalho de teclado: ESC para parar
app.bind("<Escape>", parar_macro)

ctk.CTkLabel(app, text="By. Paulo Arthur", font=("Arial", 14)).pack(pady=14)

app.mainloop()
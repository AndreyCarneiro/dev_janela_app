import tkinter as tk
from tkinter import ttk

def main():
    #Criação da janela "Pai/Raiz"
    root = tk.Tk()
    root.title("Minha Primeira Janela")
    root.geometry("400x200")
    root.resizable(True, True)

    # label simple (Etiqueta)
    label = ttk.Label(root, text="Aerials", font=("Georgia", 15,"bold"))
    label.pack(expand=True)

    # Botão para fechar a janela
    btn = ttk.Button(root, text="Fechar", command=root.destroy)
    btn.pack(anchor="s", padx=20)
    
    # Incia o loop de eventos
    root.mainloop()

if __name__ == "__main__":
    main()
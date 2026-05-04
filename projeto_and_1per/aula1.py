import tkinter as tk
from tkinter import ttk

def main():
    #Criação da janela "Pai/Raiz"
    root = tk.Tk()
    root.title("Cruelty")
    root.geometry("400x200")
    root.resizable(True, True)
    root.configure(bg="#251C1C")

    # label simple (Etiqueta)
    label = tk.Label(root, 
        text="I Love Cruelty\n🖤",
        font=("Georgia", 30,"bold"),
        fg="#8D1D1D",
        bg="#251C1C"
    )
    label.pack(expand=True)

    # Botão para fechar a janela
    btn = tk.Button(root, 
        text="Exit",
        font=("Arial", 12, "bold"),
        fg="#FFFFFF",
        bg="#8D1D1D",
        command=root.destroy)
    btn.pack(anchor="s", padx=20)
    
    # Incia o loop de eventos
    root.mainloop()

if __name__ == "__main__":
    main()
import os
import docx2txt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#000000", padx=160, pady=51)
        
        self.master = master
        self.pack()
        self.create_widgets()
            
    def create_widgets(self):
        

        self.path_label = tk.Label(self, text="Coloque o caminho da pasta:", bg="#ed145d", width=50, height=1, borderwidth=10, relief='flat')
        self.path_label.pack(side="top")

        self.path_entry = tk.Entry(self, width=50, font=("System", 16), bg="#ed145d")
        self.path_entry.pack(side="top", pady=10)

        self.run_button = tk.Button(self, text="Executar", command=self.run_script, bg="#ed145d", fg="#000000", width=50, height=1, borderwidth=5, relief='groove')
        self.run_button.pack(side="top")

        self.result_label = tk.Label(self, text="", bg="#ed145d", fg="#000000", width=80, height=20, anchor='w', justify='left', relief='groove')
        self.result_label.pack(side="top", pady=10)

        
    def browse_path(self):
        folder_path = filedialog.askdirectory()
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, folder_path)

    def run_script(self):
        folder_path = self.path_entry.get()
        if folder_path:
            nome_arquivo = "resultado.txt"
          
            with open(nome_arquivo, "w") as arquivo:
                for arquivo_docx in os.listdir(folder_path):
                    if arquivo_docx.endswith(".docx"):
                        texto = docx2txt.process(os.path.join(folder_path, arquivo_docx))
                        num_palavras = len(texto.split())
                        resultado = num_palavras // 130
                        arquivo.write(f"{arquivo_docx} - {resultado}.\n")
                        
            self.result_label.config(text=open(nome_arquivo).read())

            # ajustar la altura de la ventana principal según el tamaño de la etiqueta
            self.master.geometry(f'924x{self.result_label.winfo_reqheight()+150}')
            
            messagebox.showinfo("Concluído", "A análise foi concluída com sucesso!")
            
        else:
            messagebox.showwarning("Erro", "Por favor, informe um caminho válido para a pasta com os arquivos .docx")

root = tk.Tk()
root.geometry('1210x740')

app = Application(master=root)
app.mainloop()

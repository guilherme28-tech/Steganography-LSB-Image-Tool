import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from datetime import datetime
from core.enconder import embed_message_in_image
from core.decoder import extract_message_from_image

class SteganographyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ferramenta de Esteganografia LSB")
        self.root.geometry("920x900")
        self.root.minsize(820, 800)
        self.root.configure(bg="#071017")

        self.label_font = tkfont.Font(size=14, weight='bold')
        self.entry_font = tkfont.Font(size=14)
        self.text_font = tkfont.Font(size=14)
        self.button_font = tkfont.Font(size=13, weight='bold')
        self.title_font = tkfont.Font(size=22, weight='bold')
        self.subtitle_font = tkfont.Font(size=12)
        self.status_font = tkfont.Font(size=10)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#071017", foreground="#c1e7ff")
        style.configure("TFrame", background="#071017")
        style.configure("TEntry", fieldbackground="#0b1624", foreground="#e7f9ff")
        style.configure("TButton", background="#10223a", foreground="#e7f9ff")
        style.configure("Horizontal.TProgressbar", troughcolor="#0b1624", background="#35c3ff", thickness=16)

        menu_bar = tk.Menu(root, bg="#071017", fg="#e7f9ff")
        help_menu = tk.Menu(menu_bar, tearoff=0, bg="#071017", fg="#e7f9ff")
        help_menu.add_command(label="Sobre", command=self.show_help)
        menu_bar.add_cascade(label="Ajuda", menu=help_menu)
        root.config(menu=menu_bar)

        header_frame = tk.Frame(root, bg="#071017")
        header_frame.pack(fill='x', padx=20, pady=(16, 4))
        tk.Label(header_frame, text="guilherme28-tech", font=self.title_font, fg="#6bf0ff", bg="#071017").pack(side='left')
        tk.Label(header_frame, text="LSB", font=self.subtitle_font, fg="#8fdfff", bg="#071017").pack(side='left', padx=(8, 6), pady=(8, 0))
        tk.Label(header_frame, text="Software de Esteganografia", font=self.subtitle_font, fg="#c8ebff", bg="#071017").pack(side='left', padx=(12, 0), pady=(8, 0))

        status_frame = tk.Frame(root, bg="#071017")
        status_frame.pack(fill='x', padx=20, pady=(0, 14))
        status_items = [
            ("Fear", "The reaper"),
            ("VERSÃO", "1.0.0")
        ]
        for label, value in status_items:
            tk.Label(status_frame, text=f"{label}: {value}", font=self.status_font, fg="#8fdfff", bg="#071017").pack(side='left', padx=(0, 18))

        tk.Frame(root, height=2, bg="#35c3ff").pack(fill='x', padx=32, pady=(0, 18))

        self.content_frame = tk.Frame(root, bg="#071017")
        self.content_frame.pack(expand=1, fill='both', padx=20, pady=(0, 20))
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.columnconfigure(1, weight=1)

        self.encode_border = tk.Frame(self.content_frame, bg="#0b1624", bd=1, relief='solid')
        self.encode_border.grid(row=0, column=0, sticky='nsew', padx=(0, 10), pady=0)
        self.decode_border = tk.Frame(self.content_frame, bg="#0b1624", bd=1, relief='solid')
        self.decode_border.grid(row=0, column=1, sticky='nsew', padx=(10, 0), pady=0)

        self.encode_frame = tk.Frame(self.encode_border, bg="#071017")
        self.encode_frame.pack(expand=1, fill='both', padx=2, pady=2)
        self.decode_frame = tk.Frame(self.decode_border, bg="#071017")
        self.decode_frame.pack(expand=1, fill='both', padx=2, pady=2)

        self.setup_encode_panel()
        self.setup_decode_panel()

    def setup_encode_panel(self):
        self.encode_frame.columnconfigure(0, weight=1)

        tk.Label(self.encode_frame, text="Codificar", font=self.title_font, fg="#7c9cff", bg="#071017").grid(row=0, column=0, padx=20, pady=(20, 4), sticky='w')
        tk.Label(self.encode_frame, text="LSB STREAM", font=self.status_font, fg="#8fdfff", bg="#071017").grid(row=1, column=0, padx=20, sticky='w')

        tk.Label(self.encode_frame, text="Passo 1:", font=self.label_font, fg="#d0f4ff", bg="#071017").grid(row=2, column=0, padx=20, pady=(12, 0), sticky='w')
        tk.Label(self.encode_frame, text="Imagem de entrada:", font=self.entry_font, fg="#c8ebff", bg="#071017").grid(row=3, column=0, padx=20, pady=(2, 4), sticky='w')
        self.encode_image_entry = tk.Entry(self.encode_frame, font=self.entry_font, bg="#0b1624", fg="#e7f9ff", insertbackground="#e7f9ff", relief='flat', highlightthickness=1, highlightbackground="#2a5c90")
        self.encode_image_entry.grid(row=4, column=0, padx=20, pady=(0, 8), sticky='ew')
        tk.Button(self.encode_frame, text="Escolher imagem", command=self.select_encode_image, font=self.button_font, bg="#10223a", fg="#e7f9ff", activebackground="#1d3b5b", activeforeground="#ffffff", relief='ridge', bd=2).grid(row=5, column=0, padx=20, pady=(0, 16), sticky='ew')

        tk.Label(self.encode_frame, text="Passo 2:", font=self.label_font, fg="#d0f4ff", bg="#071017").grid(row=6, column=0, padx=20, sticky='w')
        tk.Label(self.encode_frame, text="Digite o texto a ocultar:", font=self.entry_font, fg="#c8ebff", bg="#071017").grid(row=7, column=0, padx=20, pady=(2, 8), sticky='w')
        self.message_entry = tk.Text(self.encode_frame, height=11, font=self.text_font, bg="#0b1624", fg="#dff9ff", insertbackground="#dff9ff", relief='flat', highlightthickness=1, highlightbackground="#2a5c90")
        self.message_entry.grid(row=8, column=0, padx=20, pady=(0, 16), sticky='nsew')

        self.encode_progress_label = tk.Label(self.encode_frame, text="Progresso:", font=self.label_font, fg="#d0f4ff", bg="#071017")
        self.encode_progress_label.grid(row=9, column=0, padx=20, pady=(10, 2), sticky='w')
        self.encode_progress = ttk.Progressbar(self.encode_frame, style="Horizontal.TProgressbar", length=360, mode='determinate')
        self.encode_progress.grid(row=10, column=0, padx=20, pady=(0, 16), sticky='ew')

        tk.Button(self.encode_frame, text="Codificar e Salvar", command=self.encode_message, font=self.button_font, bg="#10223a", fg="#e7f9ff", activebackground="#1d3b5b", activeforeground="#ffffff", relief='ridge', bd=2).grid(row=11, column=0, padx=20, pady=(0, 20), sticky='ew')

    def setup_decode_panel(self):
        self.decode_frame.columnconfigure(0, weight=1)

        tk.Label(self.decode_frame, text="Decodificar", font=self.title_font, fg="#7c9cff", bg="#071017").grid(row=0, column=0, padx=20, pady=(20, 4), sticky='w')
        tk.Label(self.decode_frame, text="LSB STREAM", font=self.status_font, fg="#8fdfff", bg="#071017").grid(row=1, column=0, padx=20, sticky='w')

        tk.Label(self.decode_frame, text="Passo 1:", font=self.label_font, fg="#d0f4ff", bg="#071017").grid(row=2, column=0, padx=20, pady=(12, 0), sticky='w')
        tk.Label(self.decode_frame, text="Imagem com mensagem:", font=self.entry_font, fg="#c8ebff", bg="#071017").grid(row=3, column=0, padx=20, pady=(2, 4), sticky='w')
        self.decode_image_entry = tk.Entry(self.decode_frame, font=self.entry_font, bg="#0b1624", fg="#e7f9ff", insertbackground="#e7f9ff", relief='flat', highlightthickness=1, highlightbackground="#2a5c90")
        self.decode_image_entry.grid(row=4, column=0, padx=20, pady=(0, 8), sticky='ew')
        tk.Button(self.decode_frame, text="Escolher imagem", command=self.select_decode_image, font=self.button_font, bg="#10223a", fg="#e7f9ff", activebackground="#1d3b5b", activeforeground="#ffffff", relief='ridge', bd=2).grid(row=5, column=0, padx=20, pady=(0, 16), sticky='ew')

        tk.Label(self.decode_frame, text="Passo 2:", font=self.label_font, fg="#d0f4ff", bg="#071017").grid(row=6, column=0, padx=20, sticky='w')
        tk.Button(self.decode_frame, text="Decodificar", command=self.decode_message, font=self.button_font, bg="#10223a", fg="#e7f9ff", activebackground="#1d3b5b", activeforeground="#ffffff", relief='ridge', bd=2).grid(row=7, column=0, padx=20, pady=(16, 8), sticky='ew')

        self.decode_progress_label = tk.Label(self.decode_frame, text="Progresso:", font=self.label_font, fg="#d0f4ff", bg="#071017")
        self.decode_progress_label.grid(row=8, column=0, padx=20, pady=(10, 2), sticky='w')
        self.decode_progress = ttk.Progressbar(self.decode_frame, style="Horizontal.TProgressbar", length=360, mode='determinate')
        self.decode_progress.grid(row=9, column=0, padx=20, pady=(0, 16), sticky='ew')

        tk.Label(self.decode_frame, text="Dados decodificados:", font=self.label_font, fg="#d0f4ff", bg="#071017").grid(row=10, column=0, padx=20, pady=(4, 8), sticky='w')
        self.decoded_message_text = tk.Text(self.decode_frame, height=11, font=self.text_font, bg="#0b1624", fg="#dff9ff", insertbackground="#dff9ff", relief='flat', highlightthickness=1, highlightbackground="#2a5c90")
        self.decoded_message_text.grid(row=11, column=0, padx=20, pady=(0, 20), sticky='nsew')

    def show_help(self):
        messagebox.showinfo("Ajuda", "Selecione uma imagem em cada painel (Codificar ou Decodificar) e siga os passos indicados.")

    def select_encode_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            self.encode_image_entry.delete(0, tk.END)
            self.encode_image_entry.insert(0, file_path)

    def select_decode_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            self.decode_image_entry.delete(0, tk.END)
            self.decode_image_entry.insert(0, file_path)

    def encode_message(self):
        input_path = self.encode_image_entry.get()
        message = self.message_entry.get("1.0", tk.END).strip()

        if not input_path or not message:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        try:
            downloads_path = Path.home() / "Downloads"
            downloads_path.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = downloads_path / f"imagem_criptografada_{timestamp}.png"

            self.encode_progress['value'] = 0
            embed_message_in_image(input_path, str(output_path), message)
            self.encode_progress['value'] = 100
            messagebox.showinfo("Sucesso", f"Imagem salva em:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def decode_message(self):
        input_path = self.decode_image_entry.get()

        if not input_path:
            messagebox.showerror("Erro", "Selecione uma imagem.")
            return

        try:
            message = extract_message_from_image(input_path)
            self.decoded_message_text.config(state='normal')
            self.decoded_message_text.delete("1.0", tk.END)
            self.decoded_message_text.insert(tk.END, message)
            self.decoded_message_text.config(state='disabled')
            self.decode_progress['value'] = 100
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyGUI(root)
    root.mainloop()
    
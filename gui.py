import tkinter as tk
from tkinter import ttk, messagebox
from translator_engine import OfflineTranslator

LANGUAGES = {
    "English": "eng_Latn",
    "Hindi": "hin_Deva",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Bengali": "ben_Beng",
    "Marathi": "mar_Deva",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
    "Kannada": "kan_Knda",
    "Malayalam": "mal_Mlym",
    "Odia": "ory_Orya",
    "Assamese": "asm_Beng",
    "Urdu": "urd_Arab",
    "Nepali": "npi_Deva",
    "Sanskrit": "san_Deva",
    "Maithili": "mai_Deva"
}

class TranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Indian Language Translator")
        self.root.geometry("1000x520")
        self.root.configure(bg="#f2f4f7")

        self.translator = None  # lazy loading

        # ===== TITLE =====
        tk.Label(
            root,
            text="Offline Indian Language Translation System",
            font=("Segoe UI", 18, "bold"),
            bg="#f2f4f7"
        ).pack(pady=10)

        # ===== MAIN FRAME =====
        main_frame = tk.Frame(root, bg="#f2f4f7")
        main_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # ===== LEFT (INPUT) =====
        left_frame = tk.Frame(main_frame, bg="white", bd=0)
        left_frame.grid(row=0, column=0, padx=10, sticky="nsew")

        tk.Label(left_frame, text="Source Language",
                 font=("Segoe UI", 10, "bold"),
                 bg="white").pack(pady=(10, 5))

        self.src_lang = ttk.Combobox(
            left_frame,
            values=list(LANGUAGES.keys()),
            state="readonly",
            width=25
        )
        self.src_lang.current(0)
        self.src_lang.pack(pady=5)

        self.input_text = tk.Text(
            left_frame,
            height=14,
            width=45,
            font=("Segoe UI", 11),
            bd=1,
            relief="solid"
        )
        self.input_text.pack(padx=10, pady=10)

        # ===== RIGHT (OUTPUT) =====
        right_frame = tk.Frame(main_frame, bg="white", bd=0)
        right_frame.grid(row=0, column=1, padx=10, sticky="nsew")

        tk.Label(right_frame, text="Target Language",
                 font=("Segoe UI", 10, "bold"),
                 bg="white").pack(pady=(10, 5))

        self.tgt_lang = ttk.Combobox(
            right_frame,
            values=list(LANGUAGES.keys()),
            state="readonly",
            width=25
        )
        self.tgt_lang.current(1)
        self.tgt_lang.pack(pady=5)

        self.output_text = tk.Text(
            right_frame,
            height=14,
            width=45,
            font=("Segoe UI", 11),
            bd=1,
            relief="solid",
            state="disabled"
        )
        self.output_text.pack(padx=10, pady=10)

        # ===== BUTTONS =====
        button_frame = tk.Frame(root, bg="#f2f4f7")
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Translate",
            font=("Segoe UI", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            padx=25,
            pady=8,
            command=self.translate_text
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="Copy Output",
            font=("Segoe UI", 11),
            bg="#2196F3",
            fg="white",
            relief="flat",
            padx=20,
            pady=8,
            command=self.copy_output
        ).grid(row=0, column=1, padx=10)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def translate_text(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showerror("Error", "Please enter text to translate.")
            return

        src = LANGUAGES[self.src_lang.get()]
        tgt = LANGUAGES[self.tgt_lang.get()]

        if src == tgt:
            messagebox.showerror("Error", "Source and target languages cannot be the same.")
            return

        try:
            if self.translator is None:
                messagebox.showinfo(
                    "Loading Models",
                    "Loading translation models for the first time.\nPlease wait..."
                )
                self.translator = OfflineTranslator()

            result = self.translator.translate(text, src, tgt)

            self.output_text.config(state="normal")
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, result)
            self.output_text.config(state="disabled")

        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    def copy_output(self):
        self.root.clipboard_clear()
        text = self.output_text.get("1.0", tk.END).strip()
        if text:
            self.root.clipboard_append(text)
            messagebox.showinfo("Copied", "Translated text copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorGUI(root)
    root.mainloop()

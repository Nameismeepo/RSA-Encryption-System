import tkinter as tk
from tkinter import messagebox
from rsa_core import generate_keys, encrypt_message, decrypt_message

class RSAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("سیستم رمزنگاری RSA")
        self.root.geometry("600x700")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.public_key = None
        self.private_key = None
        self.encrypted = None

        self.build_ui()

    def build_ui(self):
        # عنوان
        tk.Label(
            self.root, text="🔐 سیستم رمزنگاری RSA",
            font=("Segoe UI", 18, "bold"),
            bg="#1e1e2e", fg="#cdd6f4"
        ).pack(pady=20)

        # ورودی پیام
        tk.Label(
            self.root, text="پیام خود را وارد کنید:",
            font=("Segoe UI", 11),
            bg="#1e1e2e", fg="#89b4fa"
        ).pack()

        self.input_text = tk.Entry(
            self.root, width=50,
            font=("Segoe UI", 12),
            bg="#313244", fg="#cdd6f4",
            insertbackground="white",
            relief="flat", bd=8
        )
        self.input_text.pack(pady=8)

        # دکمه رمزنگاری
        tk.Button(
            self.root, text="🔒  رمزنگاری",
            font=("Segoe UI", 11, "bold"),
            bg="#89b4fa", fg="#1e1e2e",
            relief="flat", padx=20, pady=8,
            cursor="hand2",
            command=self.encrypt
        ).pack(pady=6)

        # نمایش کلیدها
        tk.Label(
            self.root, text="کلیدهای تولید شده:",
            font=("Segoe UI", 11),
            bg="#1e1e2e", fg="#89b4fa"
        ).pack()

        self.keys_text = tk.Text(
            self.root, width=60, height=4,
            font=("Consolas", 10),
            bg="#313244", fg="#a6e3a1",
            relief="flat", bd=8, state="disabled"
        )
        self.keys_text.pack(pady=8)

        # نمایش پیام رمزنگاری شده
        tk.Label(
            self.root, text="پیام رمزنگاری شده:",
            font=("Segoe UI", 11),
            bg="#1e1e2e", fg="#89b4fa"
        ).pack()

        self.encrypted_text = tk.Text(
            self.root, width=60, height=4,
            font=("Consolas", 10),
            bg="#313244", fg="#f38ba8",
            relief="flat", bd=8, state="disabled"
        )
        self.encrypted_text.pack(pady=8)

        # دکمه رمزگشایی
        tk.Button(
            self.root, text="🔓  رمزگشایی",
            font=("Segoe UI", 11, "bold"),
            bg="#a6e3a1", fg="#1e1e2e",
            relief="flat", padx=20, pady=8,
            cursor="hand2",
            command=self.decrypt
        ).pack(pady=6)

        # نمایش پیام رمزگشایی شده
        tk.Label(
            self.root, text="پیام رمزگشایی شده:",
            font=("Segoe UI", 11),
            bg="#1e1e2e", fg="#89b4fa"
        ).pack()

        self.decrypted_text = tk.Text(
            self.root, width=60, height=3,
            font=("Segoe UI", 12),
            bg="#313244", fg="#cdd6f4",
            relief="flat", bd=8, state="disabled"
        )
        self.decrypted_text.pack(pady=8)

        # دکمه ریست
        tk.Button(
            self.root, text="🔄  شروع مجدد",
            font=("Segoe UI", 10),
            bg="#585b70", fg="#cdd6f4",
            relief="flat", padx=15, pady=6,
            cursor="hand2",
            command=self.reset
        ).pack(pady=4)

    def set_text(self, widget, content):
        widget.config(state="normal")
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, content)
        widget.config(state="disabled")

    def encrypt(self):
        message = self.input_text.get().strip()
        if not message:
            messagebox.showwarning("خطا", "لطفاً یک پیام وارد کنید!")
            return

        self.public_key, self.private_key = generate_keys()
        self.encrypted = encrypt_message(message, self.public_key)

        self.set_text(self.keys_text,
            f"کلید عمومی  (e, n) : {self.public_key}\n"
            f"کلید خصوصی (d, n) : {self.private_key}"
        )

        self.set_text(self.encrypted_text,
            ' '.join(map(str, self.encrypted))
        )

        self.set_text(self.decrypted_text, "")

    def decrypt(self):
        if not self.encrypted:
            messagebox.showwarning("خطا", "ابتدا پیام را رمزنگاری کنید!")
            return

        result = decrypt_message(self.encrypted, self.private_key)
        self.set_text(self.decrypted_text, result)
        messagebox.showinfo("✅ موفق", "رمزگشایی با موفقیت انجام شد!")

    def reset(self):
        self.input_text.delete(0, tk.END)
        self.set_text(self.keys_text, "")
        self.set_text(self.encrypted_text, "")
        self.set_text(self.decrypted_text, "")
        self.public_key = None
        self.private_key = None
        self.encrypted = None

if __name__ == "__main__":
    root = tk.Tk()
    app = RSAApp(root)
    root.mainloop()
import tkinter as tk
from datetime import datetime, timezone, timedelta


class DigitalClock:
    def __init__(self, root, timezone_offset=0):
        self.root = root
        self.timezone_offset = timezone_offset
        self.root.title("Relógio Digital")

        self.label = tk.Label(root, font=("Arial", 80), bg="black", fg="white")
        self.label.pack(padx=20, pady=20)

        self.format_button = tk.Button(root, text="Mudar Formato", command=self.alterar_formato)
        self.format_button.pack(pady=10)

        self.formato_24h = True
        self.atualizar_hora()

    def atualizar_hora(self):
        current_time = datetime.now(timezone.utc) + timedelta(hours=self.timezone_offset)
        if self.formato_24h:
            current_time = current_time.strftime("%H:%M:%S")
        else:
            current_time = current_time.strftime("%I:%M:%S %p")
        self.label.config(text=current_time)
        self.root.after(1000, self.atualizar_hora)

    def alterar_formato(self):
        self.formato_24h = not self.formato_24h


if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
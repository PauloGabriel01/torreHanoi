import tkinter as tk
from tkinter import messagebox


class HanoiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Torre de Hanói")

        self.label = tk.Label(root, text="Insira o número de discos:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()
        self.entry.insert(0, "3")

        self.btn = tk.Button(root, text="Iniciar", command=self.start_game)
        self.btn.pack()

        self.canvas = tk.Canvas(root, width=500, height=400)
        self.canvas.pack()

        self.tower_width = 150
        self.towers = [[], [], []]

    def hanoi(self, n, origem, destino, auxiliar):
        if n == 1:
            self.move_disc(origem, destino)
        else:
            self.hanoi(n - 1, origem, auxiliar, destino)
            self.move_disc(origem, destino)
            self.hanoi(n - 1, auxiliar, destino, origem)

    def move_disc(self, origem, destino):
        disc = self.towers[origem].pop()
        move_x = (destino - origem) * self.tower_width
        self.canvas.move(disc, move_x, 0)
        self.canvas.update()
        self.canvas.after(500)
        self.towers[destino].append(disc)

    def start_game(self):
        try:
            num_discs = int(self.entry.get())
            if num_discs < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido de discos (maior que 0).")
            return

        self.canvas.delete("all")

        for i in range(3):
            self.canvas.create_line(i * self.tower_width + 100, 150, i * self.tower_width + 100, 400, width=10)

        self.towers = [[], [], []]

        for i in range(num_discs):
            disc_width = 20 + (num_discs - i) * 20
            disc = self.canvas.create_rectangle(0, 0, disc_width, 20, fill="blue")
            self.canvas.move(disc, 100 - disc_width // 2, 350 - i * 20)
            self.towers[0].append(disc)

        self.hanoi(num_discs, 0, 2, 1)


if __name__ == "__main__":
    root = tk.Tk()
    game = HanoiGame(root)
    root.mainloop()
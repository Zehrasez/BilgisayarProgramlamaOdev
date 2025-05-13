import tkinter as tk
import threading
import pygame
import snake  # snake.py dosyasındaki fonksiyonları buraya ekliyoruz
import pong
import tictactoe

def start_game(game_func):
    root.withdraw()  # Ana menüyü gizle
    def game_thread():
        game_func()  # Oyunu çalıştır
        root.deiconify()  # Oyun bitince ana menüyü geri getir
    threading.Thread(target=game_thread).start()

# Tkinter Ana Menü
root = tk.Tk()
root.title("Mini Game Hub")
root.geometry("600x700")
root.resizable(False, False)

# Arka Plan
background_label = tk.Label(root, text="🎮 Mini Game Hub 🎮", font=("Comic Sans MS", 32, "bold"))
background_label.pack(pady=30)

# Oyunun Butonları
def create_game_button(parent, text, game_func):
    btn = tk.Button(
        parent,
        text=f"  {text}",
        font=("Arial", 20),
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        padx=10,
        pady=10,
        bd=0,
        width=300,
        anchor="w",
        cursor="hand2",
        command=lambda: start_game(game_func)  # Oyunu başlat
    )
    btn.pack(pady=15)

# Butonlar
create_game_button(root, "Snake", snake.run_snake_game)
create_game_button(root, "Pong", pong.run_pong_game)
create_game_button(root, "Tic Tac Toe", tictactoe.run_tictactoe_game)

# Çıkış Butonu
exit_button = tk.Button(
    root,
    text="Çıkış",
    font=("Arial", 20),
    bg="#f44336",
    fg="white",
    activebackground="#e53935",
    padx=10,
    pady=10,
    bd=0,
    width=300,
    cursor="hand2",
    command=root.quit
)
exit_button.pack(pady=30)

root.mainloop()  # Tkinter ana döngüsü

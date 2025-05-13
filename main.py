import tkinter as tk
import threading

# Oyun modüllerini içe aktar (aynı klasörde bulunmaları gerekiyor)
import snake
import spaceshooter
import tictactoe
import pong
import breakout
import car_racing
import maze_game
import memory_card
import simon_says
import game_2048

def start_game(game_func):
    root.withdraw()  # Ana menüyü gizle
    def game_thread():
        game_func()  # Oyunu çalıştır
        root.after(100, root.deiconify)  # Oyun bitince menüyü tekrar göster
    threading.Thread(target=game_thread, daemon=True).start()

# Tkinter arayüzü
root = tk.Tk()
root.title("🎮 Mini Game Hub 🎮")
root.geometry("600x950")
root.resizable(False, False)

tk.Label(root, text="🎮 Mini Game Hub 🎮", font=("Arial", 28, "bold")).pack(pady=30)

# Oyun butonlarını oluşturan fonksiyon
def create_game_button(name, color, func):
    tk.Button(
        root, text=name, font=("Arial", 18),
        bg=color, fg="white", width=30, height=2,
        command=lambda: start_game(func)
    ).pack(pady=10)

# Oyunları menüye ekle
create_game_button("🐍 Snake", "green", snake.run_snake_game)
create_game_button("🚀 Space Shooter", "blue", spaceshooter.run_spaceshooter_game)
create_game_button("❌ Tic Tac Toe", "purple", tictactoe.run_tictactoe_game)
create_game_button("🏓 Pong", "orange", pong.run_pong_game)
create_game_button("💥 Breakout", "red", breakout.run_breakout_game)
create_game_button("🏎️ Car Racing", "darkcyan", car_racing.run_car_racing_game)
create_game_button("🧩 Maze Game", "teal", maze_game.run_maze_game)
create_game_button("🃏 Memory Card", "darkgreen", memory_card.run_memory_game)
create_game_button("🎵 Simon Says", "indigo", simon_says.run_simon_says)
create_game_button("🔢 2048", "darkred", game_2048.run_2048_game)

# Çıkış butonu
tk.Button(
    root, text="Çıkış", font=("Arial", 18),
    bg="gray", fg="white", width=30, height=2,
    command=root.quit
).pack(pady=30)

root.mainloop()

import tkinter as tk
import threading

# Oyun modülleri (aynı klasörde bulunmalılar)
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
    root.withdraw()
    def game_thread():
        game_func()
        root.after(100, root.deiconify)
    threading.Thread(target=game_thread, daemon=True).start()

root = tk.Tk()
root.title("🎮 Mini Game Hub 🎮")
root.geometry("600x700")

# Canvas + Scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Scrollbar ve Canvas yerleşimi
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Fare tekerleği desteği
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Başlık
tk.Label(scrollable_frame, text="🎮 Mini Game Hub 🎮", font=("Arial", 28, "bold")).pack(pady=30)

# Buton oluşturma fonksiyonu
def create_game_button(name, color, func):
    tk.Button(
        scrollable_frame, text=name, font=("Arial", 18),
        bg=color, fg="white", width=30, height=2,
        command=lambda: start_game(func)
    ).pack(pady=10)

# Oyun butonları
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

# Çıkış
tk.Button(
    scrollable_frame, text="Çıkış", font=("Arial", 18),
    bg="gray", fg="white", width=30, height=2,
    command=root.quit
).pack(pady=30)

root.mainloop()

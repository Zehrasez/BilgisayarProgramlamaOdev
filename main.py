import tkinter as tk
import threading
import time
import random
import math

# Oyun modülleri
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
root.configure(bg="black")

# Canvas + Scrollbar
canvas = tk.Canvas(root, bg="black", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="black")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Kalp dalga efekti
waves = []

def create_wave(x, y):
    wave = {'x': x, 'y': y, 'scale': 1.0, 'alpha': 1.0}
    waves.append(wave)

def draw_heart(canvas, x, y, size, color, tag):
    points = []
    for t in range(0, 360, 5):
        angle = math.radians(t)
        x_offset = size * 16 * (math.sin(angle) ** 3)
        y_offset = -size * (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle))
        points.append((x + x_offset, y + y_offset))
    canvas.create_polygon(points, outline=color, fill="", width=2, tags=tag)

def update_waves():
    canvas.delete("wave")
    for wave in waves[:]:
        wave['scale'] += 0.15  # Yavaş büyüme
        wave['alpha'] -= 0.03  # Hızlı şeffaflaşma
        if wave['alpha'] <= 0:
            waves.remove(wave)
            continue
        r = int(255 * wave['alpha'])
        color = f"#ff{r:02x}{r:02x}"  # Kırmızıdan açık kırmızıya geçiş
        size = 3 * wave['scale']  # Çok küçük kalp boyutu
        draw_heart(canvas, wave['x'], wave['y'], size, color, "wave")
    root.after(30, update_waves)

canvas.bind("<Button-1>", lambda e: create_wave(e.x, e.y))
update_waves()

# Başlık
tk.Label(scrollable_frame, text="🎮 Mini Game Hub 🎮", font=("Arial", 28, "bold"), bg="black", fg="white").pack(pady=30)

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

# Çıkış butonu
tk.Button(
    scrollable_frame, text="Çıkış", font=("Arial", 18),
    bg="gray", fg="white", width=30, height=2,
    command=root.quit
).pack(pady=30)

# Fare tekerleği desteği
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

root.mainloop()

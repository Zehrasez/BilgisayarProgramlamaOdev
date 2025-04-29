import tkinter as tk
from tkinter import messagebox

WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
BALL_SIZE = 20
SCORE_LIMIT = 5

def run_pong_game():
    root = tk.Toplevel()
    root.title("Pong Oyunu")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    # Raketler ve top
    left_paddle = canvas.create_rectangle(20, 160, 30, 240, fill="white")
    right_paddle = canvas.create_rectangle(570, 160, 580, 240, fill="white")
    ball = canvas.create_oval(290, 190, 310, 210, fill="white")

    # Skor
    score = {"left": 0, "right": 0}
    ball_speed = [4, 4]

    def update_score():
        canvas.delete("score_text")
        canvas.create_text(WIDTH/2 - 40, 20, text=score["left"], font=("Arial", 20), fill="white", tags="score_text")
        canvas.create_text(WIDTH/2 + 40, 20, text=score["right"], font=("Arial", 20), fill="white", tags="score_text")

    def move_ball():
        canvas.move(ball, ball_speed[0], ball_speed[1])
        bx1, by1, bx2, by2 = canvas.coords(ball)

        # Duvara çarpma
        if by1 <= 0 or by2 >= HEIGHT:
            ball_speed[1] *= -1

        # Sol raket çarpma
        if bx1 <= 30:
            if canvas.coords(left_paddle)[1] <= by1 <= canvas.coords(left_paddle)[3]:
                ball_speed[0] *= -1
            else:
                score["right"] += 1
                reset_ball()
                check_winner()

        # Sağ raket çarpma
        if bx2 >= 570:
            if canvas.coords(right_paddle)[1] <= by1 <= canvas.coords(right_paddle)[3]:
                ball_speed[0] *= -1
            else:
                score["left"] += 1
                reset_ball()
                check_winner()

        update_score()
        root.after(20, move_ball)

    def reset_ball():
        canvas.coords(ball, 290, 190, 310, 210)
        ball_speed[0] *= -1

    def move_paddle(paddle, dy):
        coords = canvas.coords(paddle)
        if coords[1] + dy >= 0 and coords[3] + dy <= HEIGHT:
            canvas.move(paddle, 0, dy)

    def key_handler(event):
        key = event.keysym
        if key == "w":
            move_paddle(left_paddle, -20)
        elif key == "s":
            move_paddle(left_paddle, 20)
        elif key == "Up":
            move_paddle(right_paddle, -20)
        elif key == "Down":
            move_paddle(right_paddle, 20)

    def check_winner():
        if score["left"] >= SCORE_LIMIT:
            messagebox.showinfo("Oyun Bitti", "Sol Oyuncu Kazandı!")
            root.destroy()
        elif score["right"] >= SCORE_LIMIT:
            messagebox.showinfo("Oyun Bitti", "Sağ Oyuncu Kazandı!")
            root.destroy()

    root.bind("<KeyPress>", key_handler)
    update_score()
    move_ball()
    root.mainloop()

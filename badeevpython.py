import tkinter as tk
from tkinter import messagebox

def solve_quadratic():
    a = float(input_a.get())
    b = float(input_b.get())
    c = float(input_c.get())

    D = b * b - 4 * a * c

    print("Дискриминант =", D)

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:
        print("Корней нет")

def show_result():
    try:
        solve_quadratic()
    except:
        messagebox.showerror("Ошибка", "Проверьте введённые числа")

window = tk.Tk()
window.title("Квадратное уравнение")
window.geometry("300x250")

tk.Label(window, text="a =").pack()
input_a = tk.Entry(window)
input_a.pack()

tk.Label(window, text="b =").pack()
input_b = tk.Entry(window)
input_b.pack()

tk.Label(window, text="c =").pack()
input_c = tk.Entry(window)
input_c.pack()

tk.Button(window, text="Решить", command=show_result).pack(pady=20)

window.mainloop()

import tkinter as tk
from tkinter import messagebox
import random


def lap_1():
    results = [
        "โจทย์: print(5 != 2)\nตอบ " + str(5 != 2),
        "โจทย์: age = 10\nprint(age > 20)\nตอบ " + str(10 > 20),
        "โจทย์: print(True and (not False))\nตอบ " + str(True and (not False)),
        "โจทย์: print((4 < 5) and ((2 > 3) or False))\nตอบ "
        + str((4 < 5) and ((2 > 3) or False)),
        "โจทย์: age = 10\nweight = 15\nprint(age > 10 and weight < 20)\nตอบ "
        + str(10 > 10 and 15 < 20),
    ]
    messagebox.showinfo("ผลลัพธ์ใบงานที่ 1", "\n\n".join(results))


def lap_2():
    def show_result():
        name = name_entry.get()
        age = age_entry.get()
        try:
            age = int(age)
            if age < 18:
                result = f"{name}, you are a minor."
            elif age <= 60:
                result = f"{name}, you are an adult."
            else:
                result = f"{name}, you are a senior."
            messagebox.showinfo("ผลลัพธ์ใบงานที่ 2", result)
        except ValueError:
            messagebox.showerror("Error", "กรุณากรอกอายุเป็นตัวเลข")

    prompt_window("รับชื่อและอายุ", show_result, ["name", "age"])


def lap_3():
    def show_result():
        username = username_entry.get()
        password = password_entry.get()
        if username == "yourname" and password == "1234":
            result = "Login successful!"
        else:
            result = "Login failed!"
        messagebox.showinfo("ผลลัพธ์ใบงานที่ 3", result)

    prompt_window("รับ username และ password", show_result, ["username", "password"])


def lap_4():
    results = []
    for i in range(2, 6):
        row = ""
        for j in range(1, 6):
            row += f"{i} x {j} = {i * j}\t"
        results.append(row.strip())
    messagebox.showinfo("ผลลัพธ์ใบงานที่ 4", "\n".join(results))


def lap_5():
    def show_result():
        try:
            rows = int(rows_entry.get())
            cols = int(cols_entry.get())
            results = "\n".join(
                [" ".join(["*" for _ in range(cols)]) for _ in range(rows)]
            )
            messagebox.showinfo("ผลลัพธ์ใบงานที่ 5", results)
        except ValueError:
            messagebox.showerror("Error", "กรุณากรอกจำนวนแถวและคอลัมน์เป็นตัวเลข")

    prompt_window("รับจำนวนแถวและคอลัมน์", show_result, ["rows", "cols"])


def lap_6():
    def show_result():
        try:
            rows = int(rows_entry.get())
            results = "\n".join(["* " * i for i in range(1, rows + 1)])
            messagebox.showinfo("ผลลัพธ์ใบงานที่ 6", results)
        except ValueError:
            messagebox.showerror("Error", "กรุณากรอกจำนวนแถวเป็นตัวเลข")

    prompt_window("รับจำนวนแถว", show_result, ["rows"])


def lap_7():
    def show_result():
        try:
            number = random.randint(1, 1000)
            attempts = 11
            for _ in range(attempts):
                guess = int(guess_entry.get())
                if guess == number:
                    result = "Congratulations! You guessed the correct number."
                    break
                elif guess < number:
                    result = "Too low!"
                else:
                    result = "Too high!"
                guess_entry.delete(0, tk.END)
            else:
                result = (
                    f"Sorry, you ran out of attempts. The correct number was {number}."
                )
            messagebox.showinfo("ผลลัพธ์ใบงานที่ 7", result)
        except ValueError:
            messagebox.showerror("Error", "กรุณากรอกตัวเลขเป็นตัวเลข")

    prompt_window("ทายตัวเลขในช่วง 1-1,000", show_result, ["guess"])


def lap_8():
    def show_result():
        total = 0
        count = 0
        while True:
            user_input = input_entry.get()
            if user_input in ("e", "E", "exit"):
                break
            try:
                number = float(user_input)
                total += number
                count += 1
            except ValueError:
                messagebox.showerror("Error", "Invalid input, please enter a number.")
            input_entry.delete(0, tk.END)
        if count > 0:
            average = total / count
            result = f"The average of the entered numbers is {average}."
        else:
            result = "No numbers were entered."
        messagebox.showinfo("ผลลัพธ์ใบงานที่ 8", result)

    prompt_window("รับตัวเลขจนกว่าจะป้อน 'e', 'E', 'exit'", show_result, ["number"])


def lap_9():
    def show_result():
        try:
            number = random.randint(1, 1000)
            while True:
                guess = int(guess_entry.get())
                if guess == number:
                    result = "Congratulations! You guessed the correct number."
                    break
                elif guess < number:
                    result = "Too low!"
                else:
                    result = "Too high!"
                guess_entry.delete(0, tk.END)
            messagebox.showinfo("ผลลัพธ์ใบงานที่ 9", result)
        except ValueError:
            messagebox.showerror("Error", "กรุณากรอกตัวเลขเป็นตัวเลข")

    prompt_window("ทายตัวเลขในช่วง 1-1,000", show_result, ["guess"])


def lap_10():
    def show_result():
        try:
            score = int(score_entry.get())
            if score >= 80:
                grade = "A"
            elif score >= 70:
                grade = "B"
            elif score >= 60:
                grade = "C"
            elif score >= 50:
                grade = "D"
            else:
                grade = "F"
            result = f"The grade is {grade}."
            messagebox.showinfo("ผลลัพธ์ใบงานที่ 10", result)
        except ValueError:
            messagebox.showerror("Error", "กรุณากรอกคะแนนเป็นตัวเลข")

    prompt_window("รับคะแนน score", show_result, ["score"])


def prompt_window(prompt, command, fields=None):
    window = tk.Toplevel()
    window.title(prompt)

    entries = {}
    if fields:
        for field in fields:
            label = tk.Label(window, text=f"Enter {field}: ")
            label.pack(pady=5)
            entry = tk.Entry(window)
            entry.pack(pady=5)
            entries[field] = entry

    def execute():
        command()
        window.destroy()

    button = tk.Button(window, text="Submit", command=execute)
    button.pack(pady=10)

    for field, entry in entries.items():
        globals()[f"{field}_entry"] = entry


def main():
    root = tk.Tk()
    root.title("โปรแกรมเลือกใบงาน")

    label = tk.Label(
        root, text="เลือกใบงานที่ต้องการ (1-10) หรือคลิก 'Exit' เพื่อออกจากโปรแกรม"
    )
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=5)

    def execute_choice():
        choice = entry.get().strip().lower()
        if choice == "exit":
            root.quit()
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 10:
                eval(f"lap_{choice}()")
            else:
                messagebox.showerror("Error", "กรุณาเลือกหมายเลขที่ถูกต้อง (1-10)")
        else:
            messagebox.showerror(
                "Error", "กรุณาใส่หมายเลขที่ถูกต้อง (1-10) หรือพิมพ์ 'exit' เพื่อออกจากโปรแกรม"
            )

    button = tk.Button(root, text="Execute", command=execute_choice)
    button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()

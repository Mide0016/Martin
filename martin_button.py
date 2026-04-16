import tkinter as tk
from tkinter import messagebox


def show_message() -> None:
    messagebox.showinfo("Martin", "HelloWorld")


def main() -> None:
    root = tk.Tk()
    root.title("Martin")
    root.geometry("240x120")

    button = tk.Button(root, text="Martin", font=("Arial", 16), width=10, command=show_message)
    button.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Martin")
    root.geometry("240x120")

    button = tk.Button(root, text="Martin", font=("Arial", 16), width=10)
    button.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()

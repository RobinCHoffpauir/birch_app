import tkinter as tk
from gui.main_window import MainWindow

def main():
    root = tk.Tk()
    root.title("Property Management App")
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()

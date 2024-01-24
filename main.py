import tkinter as tk
from gui.main_window import MainWindow
from database import Database

def main():
    # Initialize the database
    db = Database()

    # Initialize the main application window
    root = tk.Tk()
    root.title("Birch App")

    # Create an instance of the main window class
    main_window = MainWindow(root)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()

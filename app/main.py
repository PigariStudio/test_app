import tkinter as tk

def create_window():
    # Create the main window
    root = tk.Tk()
    root.title("test_app - ")

    # Create a label widget
    label = tk.Label(root, text="this is a test_app for PigarOS")
    label.pack(pady=10)

    # Create a button widget
    button = tk.Button(root, text="Exit", command=root.destroy)
    button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

create_window()

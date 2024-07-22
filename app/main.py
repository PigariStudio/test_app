import tkinter as tk

def create_window():
    # Create the main window
    root = tk.Tk()
    root.title("Simple Tkinter App")

    # Create a label widget
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=10)

    # Create a button widget
    button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked!"))
    button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

create_window()

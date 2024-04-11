import tkinter as tk
import tkinter.font as font

# Create the root window
root = tk.Tk()

# Print available font families
print(font.families())

# Continue with your Tkinter GUI code here
label = tk.Label(root, text="Hello, World!", font=("Arial", 12))
label.pack()

root.mainloop()

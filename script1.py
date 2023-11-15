import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox

def rgb_to_hex(r, g, b):
    hex_value = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex_value.upper()

def convert_rgb():
    try:
        r = int(entry_r.get())
        g = int(entry_g.get())
        b = int(entry_b.get())

        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            hex_value = rgb_to_hex(r, g, b)
            result_label.config(text=f'HEX: {hex_value}', fg='black')

            # Save the HEX value to clipboard
            window.clipboard_clear()
            window.clipboard_append(hex_value)
            window.update()
            tkinter.messagebox.showinfo("Success", "HEX value copied to clipboard.")
        else:
            result_label.config(text='Invalid RGB values', fg='red')
    except ValueError:
        result_label.config(text='Invalid input. Please enter integers.', fg='red')

# Create the main window
window = tk.Tk()
window.title("RGB to HEX Converter")

# Create and place widgets
label_r = tk.Label(window, text="Red:")
label_r.grid(row=0, column=0, padx=5, pady=5)
entry_r = tk.Entry(window)
entry_r.grid(row=0, column=1, padx=5, pady=5)

label_g = tk.Label(window, text="Green:")
label_g.grid(row=1, column=0, padx=5, pady=5)
entry_g = tk.Entry(window)
entry_g.grid(row=1, column=1, padx=5, pady=5)

label_b = tk.Label(window, text="Blue:")
label_b.grid(row=2, column=0, padx=5, pady=5)
entry_b = tk.Entry(window)
entry_b.grid(row=2, column=1, padx=5, pady=5)

convert_button = tk.Button(window, text="Convert", command=convert_rgb)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="", font=('Helvetica', 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
import tkinter as tk
from PIL import Image, ImageTk
import net
import time

class Main:
    def __init__(self, master):
        self.master = master
        self.master.title("NetLP")
        self.master.resizable(False, False)
        
        # Load the logo image with a transparent background
        self.logo_image = Image.open("res.jpg")  # Replace with the path to your transparent image
        self.logo_image = self.logo_image.resize((30, 30), Image.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(self.logo_image)

        # Top Bar with Big Text and Refresh Button (Logo)
        self.top_bar = tk.Frame(self.master, bg="#3498db")
        self.top_bar.pack(fill="x")

        self.big_text = tk.Label(self.top_bar, text="NetLP", font=("Helvetica", 24, "bold"), fg="white", bg="#3498db")
        self.big_text.pack(side="left", padx=20, pady=20)

        # Make the refresh button flat with a transparent background
        self.refresh_button = tk.Button(
            self.top_bar,
            image=self.logo_image,
            command=self.refresh_data,
            bd=0,                    # Borderwidth
            highlightthickness=0,    # Highlight thickness
            relief="flat",           # Flat appearance
            bg="#3498db",            # Set the background color to match the top bar color
            activebackground="#3498db",  # Set the background color when the button is clicked
        )
        self.refresh_button.pack(side="right", padx=20, pady=20)

        # Main Middle Area with Text
        self.main_area = tk.Frame(self.master, bg="#ecf0f1", padx=20, pady=20)
        self.main_area.pack(expand=True, fill="both")

        self.main_text = tk.Label(self.main_area, text=net.NetLP(), font=("Helvetica", 16), fg="#2c3e50", bg="#ecf0f1")
        self.main_text.pack()

        # Bind the function to adjust text size on window resize
        self.master.bind("<Configure>", self.adjust_text_size)

        # Variable to track whether the refresh is in progress
        self.refresh_in_progress = False

    def adjust_text_size(self, event):
        # Get the current width of the window
        width = event.width

        # Adjust font size based on the window width
        new_font_size = max(int(width / 20), 30)  # Adjust the divisor as needed
        self.big_text.config(font=("Helvetica", new_font_size, "bold"))
        self.main_text.config(font=("Helvetica", new_font_size - 8))  # Adjust the size difference as needed

    def refresh_data(self):
        # Check if refresh is already in progress, return if true
        if self.refresh_in_progress:
            return

        # Disable the button during refresh
        self.refresh_button.config(state=tk.DISABLED)

        # Set the flag to indicate that the refresh is in progress
        self.refresh_in_progress = True

        # Add the code to refresh your data here
        new_data = net.NetLP()
        
        # Make the text invisible for a second
        self.main_text.config(text="")
        self.master.after(1000, lambda: self.display_refreshed_data(new_data))

    def display_refreshed_data(self, new_data):
        # Display the refreshed data after a second
        self.main_text.config(text=new_data)

        # Re-enable the button after refresh is complete
        self.refresh_button.config(state=tk.NORMAL)

        # Reset the flag to indicate that the refresh is complete
        self.refresh_in_progress = False

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.geometry("1000x600")  # Set the initial size of the window
    root.mainloop()

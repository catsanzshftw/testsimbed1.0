import tkinter as tk

class EmulatorVibe:
    def __init__(self, root):
        self.root = root
        self.root.title("Deepthink PSX Core [VIBES_ONLY]")
        self.root.geometry("600x440") # Adjusted for better text fit
        self.root.resizable(False, False)
        self.root.configure(bg='black')

        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.root.after(500, self.step_1_deepthink_intro)

    def clear_canvas(self):
        self.canvas.delete("all")

    def step_1_deepthink_intro(self):
        self.clear_canvas()
        self.canvas.create_text(300, 200, text="Flames Co. R2 Deepthink [ULTRA!]", fill="#cccccc", font=("Courier", 16))
        self.canvas.create_text(300, 230, text="Initializing recursive model...", fill="#aaaaaa", font=("Courier", 12))
        self.root.after(2500, self.step_2_bios_check)

    def step_2_bios_check(self):
        self.clear_canvas()
        self.canvas.create_text(300, 200, text="PSX BIOS not found. [SKIPPING]", fill="red", font=("Courier", 12))
        self.canvas.create_text(300, 220, text="Loading VIBES_ONLY module...", fill="#00ff00", font=("Courier", 12))
        self.root.after(2000, self.step_3_sony_screen)

    def step_3_sony_screen(self):
        self.clear_canvas()
        self.canvas.create_text(300, 220, text="Sony Computer Entertainment", fill="white", font=("Courier", 20, "bold"))
        self.root.after(3000, self.step_4_ps_logo)

    def step_4_ps_logo(self):
        self.clear_canvas()
        # Drawing a simplified, text-based PS logo
        self.canvas.create_text(300, 190, text="P", fill="#ff0000", font=("Impact", 100))
        self.canvas.create_text(300, 265, text="S", fill="#0033cc", font=("Impact", 100))
        self.canvas.create_text(205, 275, text="▶", fill="#ffcc00", font=("Courier", 20))
        self.canvas.create_text(395, 275, text="◀", fill="#009900", font=("Courier", 20))
        
        self.root.after(3500, self.step_5_ready)

    def step_5_ready(self):
        self.clear_canvas()
        self.root.configure(bg='#0033cc')
        self.canvas.configure(bg='#0033cc')
        self.canvas.create_text(300, 200, text="NO GAME DATA FOUND.", fill="white", font=("Courier", 18))
        self.canvas.create_text(300, 240, text="PLEASE INSERT VIBES", fill="white", font=("Courier", 18))

if __name__ == '__main__':
    root = tk.Tk()
    app = EmulatorVibe(root)
    root.mainloop()

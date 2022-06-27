import tkinter as tk
from tkinter import ttk, filedialog
import PIL
import os
from PIL import Image, ImageTk

class App(tk.Tk):
    # logo = Image.open("/assets/logo.jpg")
    # tkLogo = ImageTk.PhotoImage(logo)


    def __init__(self):
        super().__init__()

        self.filepath = tk.StringVar()
        self.resizepercent = 0
        self.resizequality = 0
        self.w1 = tk.StringVar()
        self.w2 = 0
        self.geometry('300x150')
        self.resizable(0, 0)
        self.title('Image Compressor')

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)



        # heading
        heading = ttk.Label(self, text='Image Compressor', style='Heading.TLabel')
        heading.grid(column=1, row=0, columnspan=2, **paddings)

        # Logo
        # imageLabel = ttk.Label(self, image=App.tkLogo)
        # imageLabel.image = App.tkLogo
        # heading.grid(column=1, row=1, columnspan=2, pady=5, sticky=tk.N)

        filepath_entry = ttk.Entry(
            self, textvariable=self.filepath, **entry_font)
        filepath_entry.grid(column=0, row=2, columnspan=2, **paddings)

        # Select button
        login_button = ttk.Button(self, text="Select", command=self.select_path)
        login_button.grid(row=2, column=2, columnspan=2, **paddings)


        # Scale Quality
        qualityVar = tk.StringVar()
        w1 = tk.Scale(self, variable=qualityVar, from_=0, to=10, orient=tk.HORIZONTAL)
        w1.set(5)
        w1.grid(row=3, column=0, columnspan=2, **paddings)

        # Scale Slider
        ScaleVar = tk.StringVar()
        w2 = tk.Scale(self,variable=ScaleVar, from_=0, to=10, orient=tk.HORIZONTAL)
        w2.set(5)
        w2.grid(row=3, column=2, columnspan=2, **paddings)

        # Compress button
        login_button = ttk.Button(self, text="Compress", command=self.compress)
        login_button.grid(row=5, column=0, columnspan=4, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))



    def select_path(self):
        output_path = tk.filedialog.askdirectory()
        self.filepath.set(output_path)
        print(self.filepath)

    def compress(self):
        for file in os.listdir(self.filepath):
            f_img = self.filepath + "/" + file
            img = Image.open(f_img)
            img.resize((round(img.width * self.resizepercent), round(img.height * self.resizepercent)))
            img.save(f_img, quality=self.resizequality)

    def show_values(self):
        print(self.w1.get(), self.w2.get())



if __name__ == "__main__":
    app = App()
    app.mainloop()

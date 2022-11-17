
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

def opening_gui11():
    from pathlib import Path

    # from tkinter import *
    # Explicit imports to satisfy Flake8
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

    from gui9 import opening_gui9
    from gui8 import opening_gui8

    OUTPUT_PATH = Path(__file__).parent
    #ASSETS_PATH = OUTPUT_PATH / Path(r"/home/automatedlogos/Desktop/build/assets/frame11")
    ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/jonja/Documents/GitHub/Automated-Logos/PYTHON/build/assets/frame11") #jon's filepath

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def open_gui9():
            window.destroy()
            opening_gui9()

    def open_gui8():
            window.destroy()
            opening_gui8()

    window = Tk()

    window.geometry("800x480")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 480,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        240.0,
        image=image_image_1
    )

    #button 1 is the back button
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_gui9(),
        relief="flat"
    )
    button_1.place(
        x=595.0,
        y=380.0,
        width=161.0,
        height=75.0
    )

    canvas.create_text(
        18.0,
        0.0,
        anchor="nw",
        text="Load the [PAINTCOLOR] Paint",
        fill="#FFF9F9",
        font=("Inter ExtraBold", 40 * -1)
    )

    canvas.create_rectangle(
        18.0,
        125.0,
        343.0,
        450.0,
        fill="#D9D9D9",
        outline="")

    #button 2 is the Begin Painting button
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_gui8(),
        relief="flat"
    )
    button_2.place(
        x=595.0,
        y=184.0,
        width=161.0,
        height=150.0
    )

    canvas.create_text(
        380.0,
        110.0,
        anchor="nw",
        text="When paint is loaded...",
        fill="#FFFBFB",
        font=("Inter ExtraBold", 20 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        522.0,
        255.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()

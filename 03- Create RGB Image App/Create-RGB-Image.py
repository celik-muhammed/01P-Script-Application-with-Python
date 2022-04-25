import io
from msilib.schema import DrLocator
from select import select
import numpy as np
import tkinter as tk

from PIL import Image, ImageTk
from tkinter import CENTER, HORIZONTAL, ttk
from tkinter.font import Font
from tkinter.messagebox import showinfo


class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.rgb_name_list = ["RED", "GREEN", "BLUE"]
        self.rgb_label_list = {}
        self.rgb_label_list_sp = {}
        self.rgb_label_list_var = {}     
        
        self.frame_left = ttk.Frame(self)
        self.frame_left.pack(side=tk.LEFT, padx=10, pady=10, ipadx=0, ipady=0)

        self.frame_right = ttk.Frame(self)
        self.frame_right.pack(side=tk.LEFT, padx=10, pady=10, ipadx=0, ipady=0)

        self.__create_widgets()
        self.__create_widgets_color()
        

    def __create_widgets(self):
        # adding Label the root window
        self.msg_label = tk.Label(self.frame_left, text ="MuCe Create RGB Image", justify=CENTER, font = "50") 
        self.msg_label.pack(padx=5, pady=5)

        self.frame = ttk.Frame(self.frame_left)
        self.frame.pack()
        self.height , self.width = tk.IntVar(self, 1080), tk.IntVar(self, 1920)
        self.sp1 = tk.Spinbox(self.frame, from_= 0, to = 999999, textvariable=self.height)
        self.sp1.grid(row=0, column=0, sticky=tk.NS, padx=5, pady=5)
        self.sp2 = tk.Spinbox(self.frame, from_= 0, to = 999999, textvariable=self.width)
        self.sp2.grid(row=0, column=1, sticky=tk.NS, padx=5, pady=5)        
        # Create a Button
        btn = tk.Button(self.frame,  text = 'Save me !', bd = '5',
                          command =lambda x=None: self.save_IMG())
        btn.grid(row=0, column=3, sticky=tk.NS, padx=5, pady=5)  

        # Label olustur - Label listesini güncelle
        for i in range(3):
            self.rgb_label_list_var[self.rgb_name_list[i]] = tk.IntVar()
            self.rgb_label_list[self.rgb_name_list[i]] = tk.Label(
                                self.frame_left, 
                                text=self.rgb_name_list[i], 
                                justify=tk.CENTER,
                                font="35",
                                foreground='white',
                                background=self.rgb_name_list[i],
                                width=36, height=2)
            self.rgb_label_list[self.rgb_name_list[i]].pack(padx=5, pady=5)
            self.rgb_label_list_sp[self.rgb_name_list[i]] = tk.Scale(
                                self.frame_left,  
                                variable=self.rgb_label_list_var[self.rgb_name_list[i]],
                                label=self.rgb_name_list[i],
                                from_= 0, to = 255,
                                font=Font(family='Helvetica', size=12, weight='bold'),
                                command=lambda x=None: self.__update_scale(),
                                orient=HORIZONTAL, length=350)
            self.rgb_label_list_sp[self.rgb_name_list[i]].pack(padx=5, pady=5)


    def __update_scale(self):

        self.height, self.width = int(self.sp1.get()), int(self.sp2.get())
        self.red, self.green, self.blue = self.rgb_label_list_sp['RED'].get(), self.rgb_label_list_sp['GREEN'].get(), self.rgb_label_list_sp['BLUE'].get()

        arr = np.full((self.height, self.width, 3), [self.red, self.green, self.blue])
        arr_red = np.full((self.height, self.width, 3), [self.rgb_label_list_sp['RED'].get(), 0, 0])
        arr_green = np.full((self.height, self.width, 3), [0, self.rgb_label_list_sp['GREEN'].get(), 0])
        arr_blue = np.full((self.height, self.width, 3), [0, 0, self.rgb_label_list_sp['BLUE'].get()])

        image_red = Image.fromarray(arr_red.astype('uint8'), "RGB")
        pho_image_red = ImageTk.PhotoImage(image_red)

        image_green = Image.fromarray(arr_green.astype('uint8'), "RGB")
        pho_image_green = ImageTk.PhotoImage(image_green)

        image_blue = Image.fromarray(arr_blue.astype('uint8'), "RGB")
        pho_image_blue = ImageTk.PhotoImage(image_blue)
        
        self.image = Image.fromarray(arr.astype('uint8'), "RGB")
        self.pho_image = ImageTk.PhotoImage(self.image)

        self.rgb_label_list['RED'].configure(image=pho_image_red, width=400, height=48)
        self.rgb_label_list['GREEN'].configure(image=pho_image_green, width=400, height=48)
        self.rgb_label_list['BLUE'].configure(image=pho_image_blue, width=400, height=48)
        self.color_label.configure(image=self.pho_image, width=365, height=462)

    def save_IMG(self):
        try:
            # Raises an AttributeError
            self.image.save('./RGB_Image.png', 'png')  # save
            self.image.show()           
     
            # Prints the below statement
            # whenever an AttributeError is
            # raised
        except AttributeError:
            show = showinfo(title='Atention', message='Please Create Image Before')



    def __create_widgets_color(self):
        self.color_label = tk.Label(
                    self.frame_right, 
                    text ="Created RGB Image\n01- Firstly Select Image Size\n02- Create Your RGB Image\n03- Finally Save it \^_^/", 
                    justify= tk.CENTER,
                    font = "50",
                    foreground='white',
                    background='red',
                    width=33, height=19)
        self.color_label.pack()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("Create RGB Image")

        # set window size
        self.geometry('840x539')        
        
        #self.resizable(0, 0)
        # windows only (remove the minimize/maximize button)
        #self.attributes('-toolwindow', True)

        #set window color
        self.configure(bg='orange')

        self.__create_widgets()


    def __create_widgets(self):
        # create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(row=0, column=0, sticky=tk.NS, padx=10, pady=10, ipadx=0, ipady=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()
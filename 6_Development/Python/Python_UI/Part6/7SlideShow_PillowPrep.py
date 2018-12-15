

from tkinter import Tk, PhotoImage, Label
from itertools import cycle
from os import listdir

# using Pillow instead of PIL for Python 3.4
# Installation is: >pip install Pillow
from PIL import Image, ImageTk

class SlideShow(Tk):
    # inherit GUI framework extending tkinter
    def __init__(self, msShowTimeBetweenSlides=1500):
        # initialize tkinter super class
        Tk.__init__(self)

        # time each slide will be shown
        self.showTime = msShowTimeBetweenSlides

        # look for images in current working directory where this module lives
        listOfSlides = [slide for slide in listdir() if slide.endswith('gif')]

        # endlessly read in the slides so we can show them on the tkinter Label
        self.iterableCycle = cycle((PhotoImage(file=slide), slide) for slide in listOfSlides)

        # create tkinter Label widget which can also display images
        self.slidesLabel = Label(self)

        # create the Frame widget
        self.slidesLabel.pack()


    def slidesCallback(self):
        # get next slide from iterable cycle
        currentInstance, nameOfSlide = next(self.iterableCycle)

        # assign next slide to Label widget
        self.slidesLabel.config(image=currentInstance)

        # update Window title with current slide
        self.title(nameOfSlide)

        # recursively repeat the Show
        self.after(self.showTime, self.slidesCallback)


#=================================
# Start GUI
#=================================
win = SlideShow()
win.after(0, win.slidesCallback())
win.mainloop()

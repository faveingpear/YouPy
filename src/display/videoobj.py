import tkinter

class main():

    root = ""
    videoname = ""
    videolink = ""
    canvus = ""

    downloadbutton = ""

    def pack(self):
        self.canvus.pack()

    def download(self):
        print("Downloading: " + self.videolink)

    def __init__(self, newroot, newvideoname, newvideolink):

        self.root = newroot

        self.canvus = tkinter.Canvas(self.root)

        tkinter.Label(self.canvus,text=newvideoname).grid(row=0)

        self.downloadbutton = tkinter.Button(self.canvus,text="Download",command=self.download)
        self.downloadbutton.grid(row=1)

        self.videoname = newvideoname
        self.videolink = newvideolink
        print("test")
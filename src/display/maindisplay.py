import tkinter

import display.videoobj

class main():

    root = ""
    maincanvus = ""
    menu = ""

    videos = []

    def addVideo(self,VideoName,Videolink):

        newvideo = display.videoobj.main(self.maincanvus.scrollable_frame,VideoName,Videolink)

        self.videos.append(newvideo)

    def displayVideos(self):

        for i in range(len(self.videos)):
            print(self.videos[i])
            self.videos[i].pack()

    def exitwindow(self):
        quit()

    def refresh(self):
        print("refreshing")

    def display_download_manager(self):
        print("Download manager")

    def display_subcriptions_manager(self):
        print("Subscriptions manager")

    def display_settings_screen(self):
        print("Settomgs")

    def mainloop(self):
        self.root.mainloop()

    def __init__(self,config):
        
        self.root = tkinter.Tk()
        self.menu = tkinter.Menu()
        self.root.title("YouPy")
        self.root.config(width=config.getWidth(),height=config.getHeight(),menu=self.menu)
        self.root.geometry(str(config.getWidth()) + "x" + str(config.getHeight())) #Setting width in config doesn't work but this does

        file = tkinter.Menu(self.menu)
        file.add_command(label="Refresh",command=self.refresh)
        file.add_command(label="Exit",command=self.exitwindow)
    
        youtube = tkinter.Menu(self.menu)
        youtube.add_command(label="Downloads",command=self.display_download_manager)
        youtube.add_command(label="Subscriptions",command=self.display_subcriptions_manager)

        settings = tkinter.Menu(self.menu)
        settings.add_command(label="Edit",command=self.display_settings_screen)

        self.menu.add_cascade(label="file",menu=file)
        self.menu.add_cascade(label="Youtube",menu=youtube)
        self.menu.add_cascade(label="Settings",menu=settings)

        self.maincanvus = ScrollableFrame(self.root)

        self.maincanvus.pack(fill=tkinter.BOTH,expand=1)

        # self.container = tkinter.Frame(self.root)
        # self.maincavus = tkinter.Canvas(self.container)
        # scrollbar = tkinter.Scrollbar(self.container, orient="vertical", command=self.maincavus.yview)
        # self.scrollable_canvus = tkinter.Frame(self.maincavus)

        # self.scrollable_canvus.bind(
        #     "<Configure>",
        #     lambda e: self.maincavus.configure(
        #         scrollregion=self.maincavus.bbox("all")
        #     )
        # )

        # self.maincavus.create_window((0, 0), window=self.scrollable_canvus, anchor="nw")

        # self.maincavus.configure(yscrollcommand=scrollbar.set)

        # self.container.pack(fill=tkinter.BOTH,expand=1)
        # self.maincavus.pack(side="left", fill="both", expand=True)
        # scrollbar.pack(side="right", fill="y")

class videoobj():

    root = ""
    videoname = ""
    videolink = ""
    canvus = ""

    downloadbutton = ""

    def pack(self):
        self.canvus.pack()

    def download(self):
        print("Downloading: " + str(self.videolink))

    def __init__(self, newroot, newvideoname, newvideolink):

        self.root = newroot

        self.canvus = tkinter.Canvas(self.root)

        tkinter.Label(self.canvus,text=newvideoname).grid(row=0)

        self.downloadbutton = tkinter.Button(self.canvus,text="Download",command=self.download)
        self.downloadbutton.grid(row=1)

        self.videoname = newvideoname
        self.videolink = newvideolink
        print("test")

# Class from here https://blog.tecladocode.com/tkinter-scrollable-frames/
# This class hold the power of god... You are warned
class ScrollableFrame(tkinter.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tkinter.Canvas(self)
        scrollbar = tkinter.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tkinter.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
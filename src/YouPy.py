
from config import config
from display import configscreen,downloadmenu,downloadprompt,firstlaunch,maindisplay,subscriptionsmenu,videoplayer
from youtube import api,channel,downloader,subscriptions

try:
    import yaml
except:
    print("Could not import yaml")

try:
    import logging
except:
    print("Could not import logging")

try:
    import tkinter
except:
    print("Could not import tkinter")

try:
    import requests
except:
    print("Could not import requests")
config = config.main()
subscriptions = subscriptions.subs(config)

root = maindisplay.main(config)

root.addVideo("Matsuri",subscriptions.getSub(1))
root.addVideo("Matsuri",subscriptions.getSub(0))

root.displayVideos()
root.mainloop()


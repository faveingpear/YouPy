import yaml

class main():

    config = ""

    config_file_path = "config/config.yaml"

    width = ""
    height = ""

    downloadpath = ""

    subscriptionpath = ""

    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def getSubscriptionpath(self):
        return self.subscriptionpath
    def __init__(self):

        file = open(self.config_file_path,"r")

        self.config = yaml.load(file,Loader=yaml.FullLoader)

        file.close()

        self.width = self.config["width"]
        self.height = self.config["height"]
        self.subscriptionpath = self.config["subscriptionpath"]

        #print(self.width)
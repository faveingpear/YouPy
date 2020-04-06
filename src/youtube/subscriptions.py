import yaml

class subs():

    subs = ""

    subpath = ""

    def getSub(self,num):
        return self.subs["subscriptions"][num]

    def __init__(self, config):

        self.subpath = config.getSubscriptionpath()

        file = open(self.subpath,"r")

        self.subs = yaml.load(file,Loader=yaml.FullLoader)

        file.close()

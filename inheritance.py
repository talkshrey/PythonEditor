#example of single level inheritance
class College :
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def report(self):
        return "the math fest will start from {} to {}".format(self.start, self.end)
    #always use .format in format function

class Mathfest(College):
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def status(self):
        print("this is the annual college math fest")
        return self.report()

fest = Mathfest(start="12pm",end="6pm")
print(fest.status())


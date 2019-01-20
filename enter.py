class datastore:
    def __init__(self,filename):
        self.filename = filename
        print("in init block")

    def __enter__(self):
        self.file=open(self.filename,"a")
        print("in enter block")
        return self

    def __exit__(self,et,ev,tb):
        self.file.close()
        print("in exit block et:",et)
        print("in exit block ev:",ev)
        print("in exit block tb:",tb)

if __name__ == "__main__":
    file = None
    with datastore("log.txt") as d:
        print(d.filename)
        print("this is first line1", file=d.file)
        #print(1/0)
        print("in the with block")




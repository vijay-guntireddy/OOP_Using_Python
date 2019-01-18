class car:
    def __init__(self):
        print("class car object created")

    def __del__(self):
        print("class car object deleted")

class person:
    def __init__(self):
        print("person object created")
    def __del__(self):
        print("person object deleted")

if __name__ == '__main__':
    print("program starts")
    c =car()
    p = person()
	
    c.owns = p
    p.owner = c
	
    print("program ends")


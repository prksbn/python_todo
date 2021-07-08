class Todo :
    # 객체 생성할 때 초기화가 되는 
    def __init__(self, id, title, contents, date, done) :
        self.id = id    # int
        self.title = title  #str
        self.contents = contents    # str
        self.date = date    # str
        self.done = done    # bool (T/F)

    #def __str__ (self) :
    #    return self.id + " : " + self.title + " : " + self.contents + " : " + self.date + " : " +self.done
    
    def info(self) :
        return self.id + " : " + self.title + " : " + self.contents + " : " + self.date + " : " +self.done
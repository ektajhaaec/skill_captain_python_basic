class Counter:
    instance = None
    
    def __new__(cls):
        if cls.instance is None :
            cls.instance = super(Counter , cls).__new__(cls)
            cls.instance.count = 0
        return cls.instance

    
    @classmethod  # if we dont add this it will consider it as  normal methodd which uses self  , e dont need with inbuit function like __new__
    def get_instance(cls):
        return cls()
    
    def count_fun(self):
        self.count += 1
        return self.count




counter = Counter.get_instance()
counter2 = Counter.get_instance() # we tried creating new instance of the class .

print(counter.count_fun())  
print(counter2.count_fun())  
print(counter.count_fun()) 
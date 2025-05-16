class BorgSingleton(object):
    shared_borg_state  ={}
    def __new__(cls ,*args, **kwargs) :
        obj = super(BorgSingleton, cls) .__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.shared_borg_state
        return obj
    
borg =BorgSingleton()
borg.shared_variable = "Random Variable"
class ChildBorg(BorgSingleton):
    pass
childBorg =ChildBorg()
print(childBorg is borg)
print(childBorg.shared_variable)
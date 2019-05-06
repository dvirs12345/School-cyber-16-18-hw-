#  Dvir Sadon


class BigThing:
    def __init__(self, object):
        self.___obj = object

    def size(self):
        if type(self.___obj) == int:
            return self.___obj
        elif type(self.___obj) == str or type(self.___obj) == dict or type(self.___obj) == list:
            return len(self.___obj)

    def get_object(self):
        return self.___obj


class BigCat(BigThing):
    def __init__(self, name='chatool', weight=20):
        BigThing.__init__(self, weight)
        self.___name = name

    def size(self):
        if self.get_object() > 20:
            return 'Super Fat'
        elif self.get_object() > 15:
            return 'Meh Fat'
        else:
            return 'Not bad'


cat = BigCat()
print cat.size()

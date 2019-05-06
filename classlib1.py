class pet(object):
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
class dog(pet):
    def __init__(self, name, weight, color):
        super(dog, self).__init__(name, weight, color)
    def voice(self):
        print "bufee"
    def __repr__(self):
        print "the name: "+self.name+"the weight: "+self.weight+"the color: "+self.color

class cat(pet):
    def __init__(self, name, weight, color):
        super(cat, self).__init__(name, weight, color)
    def voice(self):
        print "hhhhhhhhhhuauuuuuuuuu"
    def __repr__(self):
        print "the name: "+self.name+"the weight: "+self.weight+"the color: "+self.color

class parrot(pet):
    def __init__(self, name, weight, color):
        super(parrot, self).__init__(name, weight, color)
    def voice(self):
        print "u ah ah ah ohoh"
    def __repr__(self):
        print "the name: "+self.name+"the weight: "+self.weight+"the color: "+self.color

pets_arr = []
for nums in range(3):
    pets_arr.append(dog(raw_input("[name], [weight],[color]").split(',')))
    pets_arr.append(cat(raw_input("[name], [weight],[color]").split(',')))
    pets_arr.append(parrot(raw_input("[name], [weight],[color]").split(',')))
pets_arr.sort(None,lambda )
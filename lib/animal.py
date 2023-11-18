class Animal:

    all = []

    def __init__(self, species, weight, nickname, zoo):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        Animal.all.append(self)

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self,new_weight):
        if isinstance(new_weight, (float or int)):
            self._weight = new_weight
        else:
            raise Exception('')

    @classmethod
    def find_by_species(cls, species):
        return [a for a in cls.all if a.species == species]
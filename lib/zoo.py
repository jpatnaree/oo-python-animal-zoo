from lib.animal import Animal

class Zoo:

    all = []
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception('Name must be a string')
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_lo):
        if isinstance(new_lo, str):
            self._location = new_lo
        else:
            raise Exception('Location must be a string')

    def animal_species(self):
        return [a.species for a in Animal.all]
    
    def find_by_species(self, species):
        return [a for a in Animal.all if a.zoo == self and a.species == species]

    def animal_nicknames(self):
        return [a.nickname for a in Animal.all if a.zoo == self]
    
    @classmethod
    def find_by_location(cls, location):
        return [z for z in Zoo.all if z.location == location]
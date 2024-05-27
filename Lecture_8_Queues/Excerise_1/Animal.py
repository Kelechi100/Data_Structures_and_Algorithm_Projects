# function that creates animal class
# I added some features to the animal class

class Animal:
    def __init__(self, name, species, gender, color, breed, order):
        self.name = name
        self.species = species
        self.gender = gender
        self.color = color
        self.breed = breed
        self.order = order
  

    def __str__(self):
       return f"{self.name} \n Species: {self.species} \n Gender: {self.gender} \n Color: {self.color} \n Breed: {self.breed}\n Order: {self.order}"
    
    
    
    
class Shelter:

    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0
    #function that take in animal input
    def intake(self, name, species, gender, color, breed):
        if species not in ['dog', 'cat']:
            print(f"Cannot intake {species}. Only dogs and cats are allowed.")
            return
        self.order += 1
        animal = Animal(name, species, gender, color, breed, self.order)
        if species == 'dog':
            self.dogs.append(animal)
        elif species == 'cat':
            self.cats.append(animal)

    # functions that adopt_dog (dequeu from the dogs queue)
    def adopt_dog(self):
        if self.dogs:
            return self.dogs.pop()
        return None
    
    # functions that adopt_cat (dequeu from the cats queue)
    def adopt_cat(self):
        if self.cats:
            return self.cats.pop()
        return None
    
    # functions that adopt_any (dequeu from any queue).
    def adopt_any(self):
        if not self.dogs and not self.cats:
            return None
        if not self.dogs:
            return self.cats.pop(0)
        if not self.cats:
            return self.dogs.pop(0)
        if self.dogs[0].species == 'dog':
            return self.dogs.pop(0)
        else:
            return self.cats.pop(0)
        
    #Function to check if the animal queue is empty
    def is_dog_queue_empty(self):
        return len(self.dogs) == 0
    
    def is_cat_queue_empty(self):
        return len(self.cats) == 0
    
    #function to check size of queue
    def dog_queue_size(self):
        return len(self.dogs)
    
    def cat_queue_size(self):
        return len(self.cats)
    
    def pet_queue_size(self):
        return len(self.dogs) + len(self.cats)
    

    def dog_names(self):
        return ', '.join([dog.name for dog in self.dogs])
    
    def cat_name(self):
        return ', '.join([cat.name for cat in self.cats])
    
 




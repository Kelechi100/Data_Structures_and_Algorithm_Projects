from Animal import Shelter
from Animal import Animal

petShop = Shelter()


#outputting the number of pet in the shelter
print("outputting the number of pet in the shelter")

print (f"Total pets in shelter: {petShop.pet_queue_size()}")
print (f"Total dogs in shelter: {petShop.dog_queue_size()}")
print (f"Total cats in shelter: {petShop.cat_queue_size()}")
print()


#Create objects of the Animals class and places them in the shelter.
petShop.intake("Bella", "cat", "female", "black", "Siamese")
petShop.intake("Abby", "dog", "female", "brown", "Labrador")
petShop.intake("Buddy", "dog", "male", "white", "Poodle")
petShop.intake("Rex", "dog", "male", "black", "German Shepherd")
petShop.intake("Mittens", "cat", "male", "white", "Persian")
petShop.intake("Whiskers", "cat", "female", "gray", "Maine Coon")
petShop.intake("Sally", "snake", "female", "green", "Python")
print("Pets available in the petShop ")
print(f"Dogs: {petShop.dog_names()}")
print(f"Cats: {petShop.cat_name()}")
print()
"""
#Creating animals and placing them in the petShop
petShop.intake(cat_bella, "Cat")
petShop.intake(dog_abby, "Dog")
petShop.intake(dog_buddy, "Dog")
petShop.intake(dog_rex, "Dog")
petShop.intake(cat_Mittens, "Cat")
petShop.intake(cat_whiskers, "Cat")

"""

 # Outputting the names and number of dogs and cats in the petShop
print("Total number of pets in the shop")
print(f"Total dogs in PetShop: {petShop.dog_queue_size()}")
print(f"Total cats in PetShop: {petShop.cat_queue_size()}")
print(f"Total pets in shelter : {petShop.pet_queue_size()}")
print()
print("Checking for pets")
# Trying to add a non-pet animal (e.g., a snake) should be ignored
petShop.intake("Sally", "snake", "female", "green", "Python") # Assuming the system doesn't handle this
print()

#Adopting a dog
print("Adopting a dog")
adopted_dog = petShop.adopt_dog()
print(f"Adopted dog: {adopted_dog}")
print()
print("After adopting a cat")
print(f"Total pets in shelter after adoptions: {petShop.pet_queue_size()}")
print()
#Adopting a cat
print("Adopiting a cat")
adopted_cat = petShop.adopt_cat()
print(f"Adopted cat: {adopted_cat}")
print()
print("After adopting a cat")
print(f"Total pets in shelter after adoptions: {petShop.pet_queue_size()}")
print()
#Adopting any pet until there are no more pets in the shelter
print("Adopting  pets untill they are finished")
while petShop.pet_queue_size() > 0:
    pet = petShop.adopt_any()
    print(f"Adopted pet: {pet}")
       
print(f"Total pets in shelter after adoptions: {petShop.pet_queue_size()}")

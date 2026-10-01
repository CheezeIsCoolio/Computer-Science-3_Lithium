class plant:
    def __init__(self, name, health, damage):
        # Attributes
        self.name = name 
        self.health = health
        self.damage = damage
        
    def attack(self, zombie):
        """Reduces health when the plant attacks."""
        zombie.health -= self.damage
        print(f"{self.name} attacked {zombie.name}! {zombie.name}'s health is now {zombie.health}.")
    
    def take_damage(self, amount):
        """Reduces health when the zombie attacks the plant."""
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health is now {self.health}.")

class zombie:
    def __init__(self, name, health, damage, distance):
        # Attributes
        self.name = name 
        self.health = health
        self.damage = damage
        self.distance = distance  # Distance from the plant
    def attack(self, plant):
        """Reduces health when the zombie attacks."""
        plant.health -= self.damage
        print(f"{self.name} attacked {plant.name}! {plant.name}'s health is now {plant.health}.")
    
    def take_damage(self, amount):
        """Reduces health when the plant attacks the zombie."""
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health is now {self.health}.")
    def move(self):
        """Moves the zombie closer to the plant."""
        self.distance -= 1
        print(f"{self.name} moved closer! Distance to plant is now {self.distance}.")

plant1 = plant("Peashooter", 50, 10)
plant2 = plant("Snow Pea", 80, 15)
zombie1 = zombie("Zombie", 100, 10, 5)

turn = 1
#----Main Program----
print("Welcome to Plants vs Zombies!")
print("A mini game made by Team Junior!")
print("Defend your house from the brain eating zombies by planting plants in your garden!")
start = input("Type Enter to start the game: ")
if start == "Enter":
    print(f"========Turn {turn}========")
    print("A zombie is approaching your house! Prepare to defend it!")
    print("Pea Shooter and Snow Pea are defending your house!")
    while plant1.health > 0 and zombie1.health > 0 and zombie1.distance>0:
        plant1.attack(zombie1)
        if zombie1.health <= 0:
            print(f"{zombie1.name} has been defeated!")
            break
        zombie1.attack(plant1)
        if plant1.health <= 0:
            print(f"{plant1.name} has been defeated!")
            break
        zombie1.move()  
elif plant1.health<=0:
        plant2.attack(zombie1)
        if zombie1.health <= 0:
            print(f"{zombie1.name} has been defeated!")
        zombie1.attack(plant2)
        turn += 1
if plant1.health <= 0 and plant2.health <= 0:
    print("All plants have been defeated! The zombies have taken over your house!")
if zombie1.health <= 0:
    print("Congratulations! You have defeated the zombie and saved your house!")
    
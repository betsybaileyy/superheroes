
# Instantiating the Hero class and defining the variables that our hero will need.
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        pass

# Adds an ability to a list of abilities.
    def add_ability(self, ability):
        self.abilities.append(ability)

# Calculates damage from a list of abilities.
    def attack(self):
        attack_total = 0
        for i in self.abilities:
            attack_damage += i.attack()
        return attack_damage

# Updates self.current_health with the damage that is passed in.
    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0
            self.deaths += 1
        return self.current_health

# Checking to see if the hero is alive or not.
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

# Running a loop to make the hero attack their opponent until one dies
    def fight(self, opponent):
        print(fighting)


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
            attack_total += i.attack()
        return attack_total

# Updates self.current_health with the damage that is passed in.
    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
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
        print("fighting")
        while self.is_alive() == True and opponent.is_alive() == True:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

            if self.is_alive() == False:
                self.deaths += 1
                opponent.kills += 1
                print("The HERO has died")
            if opponent.is_alive() == False:
                opponent.deaths += 1
                self.kills += 1
                print("the OPPONENT has died")

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())

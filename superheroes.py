import random

# Instantiating the Hero class and defining the variables that our hero will need.
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.deaths = 0
        self.damage = 0
        self.kills = 0
        pass

# Adds an ability to a list of abilities.
    def add_ability(self, ability):
        self.abilities.append(ability)

# Calculates damage from a list of abilities.
    def attack(self):
        attack_total_damage = 0
        for i in self.abilities:
            attack_total_damage += i.attack()
        return attack_total_damage

# Updates self.current_health with the damage that is passed in.
    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.damage += 1
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

class Ability:
    # Initializing the starting values.
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    # Returns an attack value between 0 and the full attack.
    def attack(self):
        attack_damage = random.randint(self.attack_strength // 2, self.attack_strength)
        return attack_damage

class Weapon(Ability):
    # Returns a random value between one half to the full attack power of the weapon .
    def attack(self):
        














if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 20)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Strength", 30)
    hero.add_ability(new_ability)
    print(hero.attack())
    hero2 = Hero("Shania Twain")
    ability2 = Ability("Smarts", 800)
    hero2.add_ability(ability2)
    hero.fight(hero2)

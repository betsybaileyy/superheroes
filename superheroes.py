import random

# Instantiating the Hero class and defining the variables that our hero will need.
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armor = list()
        self.deaths = 0
        self.damage = 0
        self.kills = 0

    # Adds an ability to a list of abilities.
    def add_ability(self, ability):
        self.abilities.append(ability)

    # Adds armor to list of armor.
    def add_armor(self, armor):
        self.armor.append(armor)

    # Runs the block method on each piece of armor and calculates the total defense.
    def defend(self):
        total_defense = 0
        if self.current_health == 0:
            return 0
        else:
            for armor in self.armors:
                total_defense += armor.defense()
                return total_defense

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
        return self.current_healths

    # Checking to see if the hero is alive or not.
    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    # Adds the number of kills to self.kills.
    def add_kill(self, num_kills):
        self.kills += num_kills

    # Running a loop to make the hero attack their opponent until one dies.
    def fight(self, opponent):
        print("fighting")
        while self.is_alive() == True and opponent.is_alive() == True:
            self.take_damage(opponent.attack())
            print("{self.name} is attacking {opponent.name}")
            opponent.take_damage(self.attack())
            print("{opponent.name} is attacking {self.name}")

            if self.is_alive() == False:
                self.deaths += 1
                opponent.kills += 1
                print("The HERO has died")
            elif opponent.is_alive() == False:
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
    # Initalizing the starting values.
    def __init__(self, name, attack_weapon_damage):
        self.name = name
        self.attack_weapon_damage = attack_weapon_damage

    # Returns a random value between one half to the full attack power of the weapon.
    def attack(self):
        attack_weapon_damage = random.randint(self.attack_weapon_damage // 2, self.attack_weapon_damage)
        return attack_weapon_damage

class Team:
    # Initate resources.
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    # Add hero objects to heroes list.
    def add_hero(self, hero):
        self.heroes.append(hero)

    # Remove hero from heroes list - if Hero not found, return 0.
    def remove_hero(self, name):
        if hero == name in self.heroes:
            self.heroes.remove(hero)
        else:
            return 0

    # Print out all heroes to console.
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    # Randomly select a living hero from each team and have them fight until one or both teams have no survivng heroes.
    def attack(self, other_team):
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            ran_hero = random.choice(self.alive_heroes())
            ran_opponent = random.choice(other_team.alive_heroes())
            ran_hero.fight(ran_opponent

    # This method should reset all heroes health to their originial starting value.
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
            return hero.current_health

class Armor:
    # Instantiating name and defense.
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    # Returns a random value between 0 and the initialized max_block strength.
    def block(self):
        return random.randint(0, self.max_block)


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

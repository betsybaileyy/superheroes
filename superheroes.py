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

    # Adds weapon object passed in as an argument to the list of abilities (that already exists.)
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    #
    # # This method will add the armor object that is passed in to this method to the list of armor objects (defined in the initalizer.)
    # def add_armor(self, armor):
    #     self.armor.append(armor)

    # Runs the block method on each piece of armor and calculates the total defense.
    def defend(self):
        total_defense = 0
        if self.current_health == 0:
            return 0
        else:
            for armor in self.armor:
                total_defense += armor.block()
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
        return self.current_health

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

    # List of team's alive heroes.
    def alive_heroes(self):
        alive_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                alive_heroes.append(hero)
        return alive_heroes

    # Randomly select a living hero from each team and have them fight until one or both teams have no survivng heroes.
    def attack(self, other_team):
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            ran_hero = random.choice(self.alive_heroes())
            ran_opponent = random.choice(other_team.alive_heroes())
            ran_hero.fight(ran_opponent)

    # Resets all heroes health to their originial starting value.
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
            return hero.current_health

    # Prints the ratio of kills/deaths for each member of the team to console.
    def stats(self):
        for hero in self.heroes:
            print("hero {hero.name} has killed {hero.kills} opponents and has {hero.deaths} deaths.")

class Armor:
    # Instantiating name and defense.
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    # Returns a random value between 0 and the initialized max_block strength.
    def block(self):
        return random.randint(0, self.max_block)

class Area:
    # Declaring Variables.
    def __init__(self):
        self.team_one = None
        self.team_two = None

    # Allows user to create an ability.
    def create_ability(self):
        ability_name = input("Name an ability for your superhero: ")
        ability_damage = int(input("How powerful is this ability? Please give a number value : "))
        return Ability(ability_name, ability_damage)

    # Allows user to create a weapon.
    def create_weapon(self):
        weapon_name = input("Give your hero a weapon to use: ")
        weapon_damage = int(input("How powerful is this weapon? Please give a number value: "))
        return Weapon(weapon_name, weapon_damage)

    # Allows user to create a piece of armor.
    def create_armor(self):
        armor_name = input("Let's give yor hero armor for protection. What armor would you like to give them? : ")
        armor_defense = int(input("How protective is this armor? Please give a numerical value: "))
        return Armor(armor_name, armor_defense)

    # Allows user to create a hero.
    def create_hero(self):
        hero_name = input("Name your mighty hero: ")
        hero = Hero(hero_name)
        hero.add_ability(self.create_ability)
        hero.add_weapon(self.create_weapon)
        hero.add_armor(self.create_armor)
        return hero

    # Allows user to create team one.
    def build_team_one(self):
        team_one_name = input("Superheroes, Unite! Give your superteam a name: ")
        team_one = Team(team_one_name)
        num_heroes_team_one = int(input("How many heroes are on your team? Please give a number value: "))
        while num_heroes_team_one > 0:
            hero = self.create_hero()
            num_heroes_team_one -= 1
            team.add_hero(hero)
        return team_one

    # Allows user to create team two.
    def build_team_two(self):
        team_two_name = input("Superheroes, Unite! Give your superteam a name: ")
        team_two = Team(team_two_name)
        num_heroes_team_two = int(input("How many heroes are on your team? Please give a number value: "))
        while num_heroes_team_two > 0:
            hero = self.create_hero()
            num_heroes_team_two -= 1
            team.add_hero(hero)
        return team_two

    # Allows user to battle teams together.
    def team_battle(self):
        while self.team_one.alive_heroes() and self.team_two.alive_heroes():
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
        if len(self.team_one.heroes) <= 0:
            print("Team {team_one} has won the battle.")
        else:
            print("Team {team_two} has won the battle.")

    # Prints battle statistics to console.
    def show_stats(self):
        print("Here are your statistics: ")
        self.team_one.stats()
        seld.team_two.stats()



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

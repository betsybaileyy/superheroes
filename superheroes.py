
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
        pass

    def attack(self):
        '''
        Calculates damage from list of abilities.
        This method should call Ability.attack()
        on every ability in self.abilities and
        return the totalself.
        '''
        pass

    def take_damage(self, damage):
        '''
        This method should update self.current_health
        with the damage that is passed in.
        '''


    coolHero = Hero("anna")

    print hero.attack()

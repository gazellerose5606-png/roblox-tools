import random

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def random_event(self):
        for player in self.players:
            if random.choice([True, False]):
                damage = random.randint(5, 20)
                player.take_damage(damage)

    def show_status(self):
        for player in self.players:
            status = 'Alive' if player.is_alive() else 'Dead'
            print(f'{player.name}: Health={player.health}, Status={status}')
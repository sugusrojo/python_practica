# Get all swords and protect the village.

def onSpawn (event):
    while True:
        item = hero.findNearestItem()
        #  The pet should fetch the item if it exists:
        if item:
            pet.fetch(item)

# Assign onSpawn function for the pet's "spawn".


while True:
    # Guard the left passage: 
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    pass

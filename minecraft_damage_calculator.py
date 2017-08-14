"""
This program is used 
to calculate damage 
in minecraft
"""

"""
To Do:
add option for missing armor pieces
make user able to input info
"""

"""
Armor grades:
First number is sword damage, 
second helmet armor bars, 
third chestplate, 
etc.
"""
LEATHER = (None, 1, 3, 2, 1)
WOOD = (5, None, None, None, None)
GOLD = (5, 2, 5, 3, 1)
CHAIN = (None, 2, 5, 4, 1)
STONE = (6, None, None, None, None)
IRON = (7, 2, 6, 5, 2)
DIAMOND = (8, 3, 8, 6, 3)

"""
Type key:
Used to direct the
program to the
proper number in each 
armor grade
"""
SWORD = 0
HELMET = 1
CHESTPLATE = 2
LEGGINGS = 3
BOOTS = 4

"""
Translation key:
Used to translate 
user input into
constants 
"""
GRADES = ({
    "leather": LEATHER,
    "wood": WOOD,
    "gold": GOLD,
    "chain": CHAIN,
    "stone": STONE,
    "iron": IRON,
    "diamond": DIAMOND
})

def calc_red(helmet, chestplate, leggings, boots):
    """
    Calculate the total 
    reduction of a suit of armor
    """
    total = 0
    count = 0
    pieces = (helmet, chestplate, leggings, boots)
    
    for piece in pieces:
        count = count + 1
        total = total + GRADES[piece][count]
        
    return total * 0.04
    
def calc_prot(helmet, chestplate, leggings, boots):
    """
    Calculate the minimum and 
    maximum damage reduction 
    from Protection enchantments
    """
    total = 0
    pieces = (helmet, chestplate, leggings, boots)
    
    for piece in pieces:
        if piece > 4:
            piece = 4
        if piece == 4:
            total = total + 5
        else:
            total = total + piece
            
    return total * 0.04

def calc_res(level):
    """
    Used to calculate
    damage reduction
    from Resistance
    """
    return level * 0.2

def calc_tot_dmg_red(armor_set, prot, res):
    """
    Calculate total 
    damage reduction
    """

    
FDG = calc_red("diamond", "diamond", "diamond", "diamond")
max_prot = calc_prot(4, 4, 4, 4)
print calc_tot_dmg_red(FDG, max_prot, 0)
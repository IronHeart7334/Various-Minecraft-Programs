"""
A damage calculator for minecraft

To do:
implement 1.9 armor system changes
add weapon data/calc
add user input
make get_reduction print armor grade properly. 3 IS NOT AN ARMOR GRADE!!!
"""

"""
Misc. data
"""


"""
reduction per shield
"""
#change for 1.9
RPS = 0.04



"""
different grades of material
"""
leather = 0
gold = 1
chain = 2
iron = 3
diamond = 4



"""
different kinds of armor
"""
helmet = 0
chestplate = 1
leggings = 2
boots = 3



"""
armor[0][1] should return leather chestplate
"""
armor_shields = ((1, 3, 2, 1), (2, 5, 3, 1), (2, 5, 4, 1), (2, 6, 5, 2), (3, 8, 6, 3))


"""
First we need to do armor calculation
"""
def get_reduction(helmet_grade, chestplate_grade, legging_grade, boot_grade, message = False):
    """
    this will calculate the total damage reduction of your armor set
    """
    total = 0
    calc_piece = 0
    your_armor = (helmet_grade, chestplate_grade, legging_grade, boot_grade)
    for piece in your_armor:
        total = total + armor_shields[piece][calc_piece] * RPS
        calc_piece = calc_piece + 1
    if message:
        print "A ", helmet_grade, " helmet, ", chestplate_grade, " chestplate, ", legging_grade, "leggings, and ", boot_grade, " boots"
        print "reduces damage taken by ", total * 100, "%"
        
        
    return total
    
    
    
print get_reduction(iron, iron, iron, iron, True)


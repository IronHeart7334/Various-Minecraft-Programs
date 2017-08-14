DAILY_QUESTS = ("Play a game", "Win a game", "Player smashes")
COSTS = (50, 125, 300, 600, 3500, 6500, 8500, 14000)
ENDERCHEST_COST = 10000

def calc_weekly_coins():
    """
    Count how many daily quests the player does.
    """
    day_quests_decided = False
    while not day_quests_decided:
        day_quests_chosen = raw_input("How many quests are you doing each day?")
        try:
            num_quests = int(day_quests_chosen)
            if num_quests <= len(DAILY_QUESTS) and num_quests >= 0:
                day_quests_decided = True
                player_day_quests = num_quests
            else:
                print "Please input a number between 0 and 3."
        except:
            print "Please input a number."
        print " "
    
    
        
    """
    Is the player doing the weekly quest?
    """
    week_quests_decided = False
    while not week_quests_decided:
        do_or_not = raw_input("Are you getting the weekly quest?")
        answer = do_or_not.lower()
        if answer[0] == "y":
            week_quests_decided = True
            player_week_quests = 1
        elif answer[0] == "n":
            week_quests_decided = True
            player_week_quests = 0
        else:
            print "Please input y or n"
            print " "    
        
        
        
    """
    calculate the coins the player gets each week
    """
    return player_week_quests * 3500 + (player_day_quests * 7) * 750


def ask_level(level_for):
    decided = False
    while not decided:
        print "What level would you like to get your ", level_for, " up to?"
        level = raw_input(" ")
        try:
            level = int(level)
            if level >= 1 and level <= len(COSTS) + 1:
                decided = True
                return level
            else:
                print "Please enter a number between 1 and 9"
        except:
            print "Please enter a number."


def calc_cost(level):
    cost = 0
    count = 0
    level = level - 2
    while count <= level:
        cost = cost + COSTS[count]
        count = count + 1        
    return cost

#print calc_weekly_coins()
print calc_cost(ask_level("Kit"))
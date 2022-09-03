import random
import time

ARMOR = 2
WEAPON = 2
SPEED = 2
MONEY = 100
TEAM_SIZE = 2
HEALTH = 25

DAY = 1

STORY_STATUS = "intro"


def get_rand_damage_taken():
    """ rand damage 5-10 minus armor level """
    rand = random.randint(5, 10)
    damage = rand - int(ARMOR)
    return damage


def roll_dice(odds):
    """
    returns true or false randomly with given odds.  the lower the odd parameter, the more likely it is to return true
    :param odds: int - will be a 1 out of odds chance of returning True
    :return: boolean
    """
    rand = random.randint(1, odds)
    return rand == 1


def p(text):
    input(text)


def display_intro():
    print("welcome to the alaskan wilderness", end="")
    input("")
    player_levels()
    input("")
    if input("press enter to begin your adventure, or type 'help' to open the tutorial. ").lower().startswith("h"):
        input("press enter to navigate through the tutorial.  this is also how you will navigate through the game")
        input("you start with level 2 armor, weapon, speed, and $100 ")
        input("these levels can change during progressing through the story")
        input("you will be prompted to make choices, typing '1' for the first choice, or '2' for the second.")
        input("the outcome of some choices are based off of your levels")
        input("make sure to keep an eye on your levels! "
              "you can check your status by typing 'levels' or 'l' during choice making")
        input("to exit the game, type 'exit' or 'e' during choice making")
    print("")


def player_levels():
    print("")
    print("your levels:")
    print("armor:", str(ARMOR), " weapon:", str(WEAPON), " speed:", str(SPEED), " money:", str(MONEY))
    print("health:", str(HEALTH))
    print("")


def player_choice():
    choice = ""

    print("what will it be?...", end=" ")
    while choice != "1" and choice != "2":
        choice = input()
        if choice != "1" and choice != "2":
            if choice.lower().startswith("l"):
                player_levels()
            elif choice.lower().startswith("e"):
                print("goodbye")
                exit()
            print("you must choose between the two...")
            print("what will it be?...", end=" ")

    return int(choice)


def level_up(level, increase):
    global ARMOR
    global WEAPON
    global SPEED
    global MONEY

    if level == "ARMOR":
        ARMOR += increase
    elif level == "WEAPON":
        WEAPON += increase
    elif level == "SPEED":
        SPEED += increase
    elif level == "MONEY":
        MONEY += increase

    print("your", str(level), "has changed by", str(increase), end="")
    input("")


def next_day(story_status):
    global DAY
    global STORY_STATUS
    global HEALTH

    for i in range(5):
        if HEALTH < 25:
            HEALTH += 1

    print("")
    time.sleep(1)
    print("day", DAY, "complete")
    player_levels()
    print("press enter to continue to day", DAY+1, end=" ")
    input("")
    print("")
    DAY += 1
    STORY_STATUS = story_status


def play_again():
    time.sleep(1)
    return input("Would you like to play again (Yes/No)? ").lower().startswith("y")


def take_damage(modifier):
    """
    reduce player health
    :param modifier: 1 is no modifier, 2 will double damage, .5 will cut damage in half
    :return:
    """
    global HEALTH
    damage_taken = round(get_rand_damage_taken() * modifier)
    HEALTH = HEALTH - damage_taken
    if HEALTH < 0:
        print("")
        p("YOU HAVE BEEN SLAIN")
    else:
        print("")
        print(str(damage_taken), "damage taken.  player health is now", str(HEALTH), end="")
    input("")
    print("")


def attack_damage(modifier):
    damage = modifier * (random.randint(5, 8) + int(WEAPON))
    return damage


def fight(boss_name, boss_moral):
    """
    mechanics of a fight
    :param boss_name: str - boss name
    :param boss_moral: int - how easy boss will give in to negotiations
    :return:
    """
    global TEAM_SIZE
    global ARMOR
    # base boss health is 25, adds 5 for each teammate helping you
    boss_health = (TEAM_SIZE*5) + 25
    print(str(boss_name).lower(), "enters fighting stance")
    while HEALTH > 0 and boss_health > 0:
        print("evade or block")
        if player_choice() == 1:
            """
            PLAYER CHOOSES TO EVADE THE ATTACK
            """
            if roll_dice(2):
                p("success")
            else:
                p("failed")
                take_damage(1)
                if HEALTH < 0:
                    break
        else:
            """
            PLAYER CHOOSES TO BLOCK THE ATTACK
            """
            if ARMOR > 0:  # only have a chance at success if player has armor
                p("your armor absorbs some of the attack")
                take_damage(.5)
                if HEALTH < 0:
                    break
                if roll_dice(4):  # 25% chance of 1 level of armor breaking during block
                    if ARMOR == 1:
                        p("armor has been completely destroyed")
                        print("")
                        ARMOR -= 1
                    else:
                        p("armor has been weakened")
                        print("")
                        ARMOR -= 1
            else:
                p("your block failed because you have no armor!")
                take_damage(1)
                if HEALTH < 0:
                    break
        print("negotiate or attack")
        if player_choice() == 1:
            """
            PLAYER CHOOSES TO NEGOTIATE
            """
            if roll_dice(boss_moral):
                # boss gives in to negotiations
                p("your diplomacy was successful!")
                print("")
                p("the fight is over.")
                break
            else:
                print(str(boss_name), "wavers but does not give in yet", end="")
                input("")
                boss_moral -= 1  # each time the player tries diplomacy, more likely it will happen
        else:
            """
            PLAYER CHOOSES TO ATTACK
            """
            damage = attack_damage(1)
            boss_health = boss_health - damage
            if boss_health < 0:
                print(str(boss_name), "has been slain.", end="")
                input("")
                print("")
                p("the fight is over.")
                break
            else:
                print("dealt", damage, str(boss_name), "now has", str(boss_health), "health", end="")
                input("")


def day_1():
    global ARMOR
    global WEAPON
    global SPEED
    global MONEY
    global DAY
    global STORY_STATUS
    global TEAM_SIZE

    input("you are in a remote alaskan village, about to start your exploration to "
          "find the ancient ruins of your ancestors")
    print("it is beginning to get late, should you begin your adventure today (1), or wait until tomorrow? (2)")
    if player_choice() == 1:
        """
        START ADVENTURE TODAY
        """
        p("you choose to begin the adventure")
        p("you are accompanied by 2 fellow explorers")
        print("the town you are in is near the ocean.  do you begin your search along the coast, or head inland?")
        if player_choice() == 1:
            """
            EXPLORE ALONG THE COAST
            """
            p("you choose to search along the coast")
            p("that night, you set up camp along the beach")
            p("on the way, your team collects coconuts")
            next_day("explore_along_coast")
        else:
            """
            EXPLORE INLAND
            """
            p("your expedition heads inland")
            p("your team finds shelter at the base of a rock outcrop")
            p("along the way, you collected rocks to use as slingshot ammunition")
            level_up("WEAPON", 1)
            next_day("explore_inland")
    else:
        """
        START ADVENTURE TOMORROW
        """
        p("you decide to wait until tomorrow")
        p("the tavern charges you $10 for staying an extra night")
        level_up("MONEY", -10)
        next_day("in_town")


def day_2():
    global ARMOR
    global WEAPON
    global SPEED
    global MONEY
    global DAY
    global STORY_STATUS
    global TEAM_SIZE

    if STORY_STATUS == "explore_along_coast":
        """
        CONTINUE EXPLORING ALONG COAST
        """
        p("your team eats the coconuts for breakfast")
        level_up("SPEED", 1)
        p("your team is able to cover more ground today")
        p("you come to a river coming down from the mountains into the ocean.  the current looks strong.")
        print("you can see a shipwreck on the other side.  "
              "should you try to cross the river or follow the river upstream?")
        if player_choice() == 1:
            """
            TRY TO CROSS THE RIVER
            """
            p("you and your team attempt to cross the river")
            if roll_dice(2):
                """
                LOSE AN EXPLORER
                """
                TEAM_SIZE -= 1
                p("one of your explorers gets swept away by the current")
                p("only you and one other explorer make it across")
            else:
                """
                EVERYONE MAKES IT ACROSS SAFELY
                """
                p("everyone crosses the river safely")
            p("you continue towards the shipwreck")
            p("searching through the shipwreck, you find crates full of military supplies")
            level_up("ARMOR", 1)
            if roll_dice(3):
                level_up("WEAPONS", 2)
            else:
                level_up("WEAPONS", 1)
            p("nightfall approaches, you decide to set up camp at the edge of the forest")
            next_day("camp_near_shipwreck")
        else:
            """
            FOLLOW THE RIVER UPSTREAM
            """
            p("you and your follow the river upstream through the forest")
            p("you come across a lost hiker. "
              "they seem disgruntled, you are unsure if they are friendly or not")
            print("you have power in numbers, do you decide to approach him?")
            if player_choice() == 1:
                """
                APPROACH THE HIKER
                """
                p("the hiker turns towards you as you approach")
                if roll_dice(2):  # 50% chance the hiker attacks you
                    """
                    HIKER ATTACKS YOU
                    """
                    fight("disgruntled hiker", 6)
                    p("you are worn out from your fight with the hiker")
                    p("you continue a little farther and set up camp for the night")
                    next_day("upstream_after_hiker")
                else:
                    """
                    HIKER IS FRIENDLY
                    """
                    p("the hiker is friendly")
                    p("you convince him to join your expedition")
                    TEAM_SIZE += 1
                    p("you continue a little farther and set up camp for the night")
                    next_day("upstream_after_hiker")

            else:
                """
                WALK PAST THE HIKER
                """
                if roll_dice(3):  # 33% chance the hiker attacks you
                    """
                    HIKER ATTACKS YOU
                    """
                    fight("disgruntled hiker", 6)
                    p("you are worn out from your fight with the hiker")
                    p("you continue a little farther and set up camp for the night")
                    next_day("upstream_after_hiker")
                else:
                    """
                    HIKER IS FRIENDLY
                    """
                    p("you walk right past the hiker without him noticing you")
                    p("you continue a little farther and set up camp for the night")
                    next_day("upstream_after_hiker")
    elif STORY_STATUS == "explore_inland":
        """
        CONTINUE EXPLORING INLAND
        """
        pass
    elif STORY_STATUS == "in_town":
        """
        BEGIN YOUR ADVENTURE
        """
        pass


def main():
    global DAY
    while True:
        DAY = 1
        display_intro()
        day_1()
        day_2()
        if not play_again():
            return


if __name__ == "__main__":
    main()

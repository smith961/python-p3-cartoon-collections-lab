def roll_call_dwarves(names):
    i = 1
    for name in names:
        print(f"{i}. {name}")
        i += 1

# def roll_call_dwarves(names):
#     for i, name in enumerate(names, start=1):
#         print(f"{i}. {name}")
        


def summon_captain_planet(planeteer_calls):
    new_list = []
    for call in planeteer_calls:
        new_list.append(call.capitalize() + "!")
    return new_list


def long_planeteer_calls(words):
    for word in words:
        if len(word) > 4:
            return True
    return False


def find_the_cheese(foods):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheese_types:
            return food
    return None





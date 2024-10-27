CHESSE = ["cheddar", "gouda", "camembert"]


def roll_call_dwarves(staff):

    for index in range(len(staff)):
        print(f'{index+1}. {staff[index]}')


def summon_captain_planet(calls):

    call_list = []
    for call in calls: 
        calls_string = f'{call.capitalize()}' + '!'
        call_list.append(calls_string)

    return call_list

def long_planeteer_calls(calls):
    
    for call in calls:
        if len(call) > 4:
            return True
        
    return False


def find_the_cheese(foods):
    
    for food in foods: 
        if food in CHESSE:
            return food
    
    return None
    

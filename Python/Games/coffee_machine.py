# A coffee machine simulator

# Menu and resources from https://replit.com/@appbrewery/coffee-machine-start
menu = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}


def report():
    print(f"Water status: {resources['water']} ml")
    print(f"Milk status: {resources['milk']} ml")
    print(f"Coffee status: {resources['coffee']} g")
    print(f"Money status: {resources['money']} PLN")


def take_money():
    print(f'That will cost you {coffee['cost']:.2f}zł')
    print('We accept 10gr, 20gr, 50gr, 1zł, 2zł, 5zł coins.')

    paid = 0.1 * int(input('How many 10gr coins? '))
    paid += 0.2 * int(input('How many 20gr coins? '))
    paid += 0.5 * int(input('How many 50gr coins? '))
    paid += 1 * int(input('How many 1zł coins? '))
    paid += 2 * int(input('How many 2zł coins? '))
    paid += 5 * int(input('How many 5zł coins? '))
    return paid
    #return float(input('Give me the money: '))


def is_craftable(item):
    global ran_out
    for i in item['ingredients']:
        if resources[i] - item['ingredients'][i] < 0:
            ran_out.append(i)
    if not ran_out: return True
    else: return


def is_enough_money(item, money):
    if money - item['cost'] < 0: return
    else: return True


while True:
    ran_out = []

    choice = input('What do you want? I ain`t giving you any coffee (definitely not espresso/latte/cappuccino): ')
    if choice == 'off': break
    elif choice == 'report':
        report()
        continue
    elif choice not in list(menu.keys()): continue
    else:
        coffee = menu[choice]

    if is_craftable(coffee):
        user_money = take_money()
        if is_enough_money(coffee, user_money):
            resources['money'] += coffee['cost']
            remainder = user_money - coffee['cost']
        else:
            print('Sorry, you can`t afford this. Money refunded.')
            break

        # make coffee
        for ingredient in menu[choice]['ingredients']:
            resources[ingredient] -= menu[choice]['ingredients'][ingredient]
        print(f'Thank you, here`s your coffee: [{choice} coffee cup]\nand the change: {remainder:.2f}zł')
    else:
        print(f'Sorry, we ran out of {' and '.join(ran_out)}. Come back another lifetime.')

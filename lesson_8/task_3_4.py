import string
import random


ATTR_POINTS_COUNT = 5
ATTR_POINTS_COSTS = {
    'damage': 0.5,
    'health': 10,
    'armor': 0.11,
}
ATTR_POINTS_KEYS = {
    'damage': '1',
    'health': '2',
    'armor': '3',
}
ATTR_INIT_STATE = {
    'damage': 5,
    'health': 100,
    'armor': 1,
}


# Info prints
def print_attr_points_costs():
    print(
        f'Распределение очков. Доступно: {ATTR_POINTS_COUNT}\n'
        f'1. +{ATTR_POINTS_COSTS["damage"]} к урону\n'
        f'2. +{ATTR_POINTS_COSTS["health"]} к здоровью\n'
        f'3. +{ATTR_POINTS_COSTS["armor"]} к броне\n'
    )


def print_enemies(_player, _enemy):
    print(f'{_player["name"]:>7}  против    {_enemy["name"]:<7}')
    print(f'{_player["damage"]:>7.2f}  урон      {_enemy["damage"]:<7.2f}')
    print(f'{_player["health"]:>7.2f}  здоровье  {_enemy["health"]:<7.2f}')
    print(f'{_player["armor"]:>7.2f}  броня     {_enemy["armor"]:<7.2f}')
    print()


def print_state(_player, _enemy):
    print(f'{_player["name"]:>7}  против    {_enemy["name"]:<7}')
    print(f'{_player["health"]:>7.2f}  здоровье  {_enemy["health"]:<7.2f}')
    print()
# END Info prints


# Preparation
def generate_enemy():
    def generate_string(choices, length):
        letters = random.choices(choices, k=length)
        return ''.join(letters)

    unit = {
        'name': generate_string(
            choices=string.ascii_lowercase,
            length=4
        ).capitalize(),
        **ATTR_INIT_STATE
    }
    choice = generate_string(
        choices=list(ATTR_POINTS_KEYS.values()),
        length=ATTR_POINTS_COUNT
    )
    return apply_choice(unit, choice)


def apply_choice(unit, choice_string):
    _string = choice_string[:ATTR_POINTS_COUNT]
    for attr, key in ATTR_POINTS_KEYS.items():
        unit[attr] += ATTR_POINTS_COSTS[attr] * _string.count(key)
    return unit
# END Preparation


# Calculations
def calculate_damage(initiator, aim):
    bonus = random.randint(0, 1) * (initiator['damage'] / 20)
    return (initiator['damage'] / aim['armor']) + bonus


def attack(initiator, aim):
    aim['health'] -= calculate_damage(initiator, aim)
# END Calculations


# User sets a unit
player = {'name': input('Введи имя: '), **ATTR_INIT_STATE}

print_attr_points_costs()

user_choice = list(input('Введите строку распределения очков: '))
player_char = apply_choice(player, user_choice)

# Battle starts
is_ready = True
print()

stats = {'battles': 0, 'wins': 0, 'loses': 0}
while is_ready:
    player = player_char.copy()
    enemy = generate_enemy()

    stats['battles'] += 1

    print_enemies(player, enemy)
    while player['health'] > 0 and enemy['health'] > 0:
        attack(player, enemy)
        attack(enemy, player)

        print_state(player, enemy)

    if player['health'] <= 0 and enemy['health'] <= 0:
        print('Никого не осталось')
    elif player['health'] > 0:
        print(f'Поздравляем, {player["name"]}')
        stats['wins'] += 1
    else:
        print(f'Поздравляем, {enemy["name"]}')
        stats['loses'] += 1

    print('')
    print(
        f'Матчей: {stats["battles"]}; '
        f'Побед: {stats["wins"]}; '
        f'Поражений: {stats["loses"]}.'
    )
    is_ready = bool(int(input('Сразиться снова? [1 - в бой!, 0 - домой...] : ')))

print('\nУдачи!')

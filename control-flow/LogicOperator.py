is_magician = True
is_expert = True
gamer1 = {
    'user_id': 'gamer1',
    'is_magician': is_magician,
    'is_expert': is_expert,
}
if gamer1['is_magician'] and gamer1['is_expert']:
    print(f'{gamer1["user_id"]} is a master magician')
elif gamer1['is_magician']:
    print(f'{gamer1["user_id"]} is a magician')
elif gamer1['is_expert']:
    print(f'{gamer1["user_id"]} is not a magician, but expert at something else')
else:
    print(f'{gamer1["user_id"]} is not a magician, nor a expert neither')

# another writing
# ternary operator
print(f'{gamer1["user_id"]} is a master magician' if gamer1['is_magician'] and gamer1["is_expert"] else f'{gamer1["user_id"]} not a magician nor a expert')


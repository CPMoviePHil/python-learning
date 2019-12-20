# user1's tesla driving permission
finger_prints = ['123456789', '23456789']
toxic_status = ['drunken', 'alcohol-free']
user1 = {
    'finger_print': '123456789',
    'name': 'Donald Trump',
    'age': 18,
    'toxic_status': 'drunken',
    'license': 'pass',
}
tesla1 = {
    'autopilot': True,
    'finger_print': '123456789',
    'model': 'model_3',
    'driven_times': 23,
    'battery_status': 'full',
}
if user1['finger_print'] is tesla1['finger_print']:
    print(f'{user1["name"]} is tesla1\'s owner')
    if user1['age'] > 18:
        print(f'{user1["name"]} is old enough to drive the car')
        if user1['toxic_status'] is toxic_status[1]:
            print(f'{user1["name"]} doesn\'t have any alcohol')
            if user1['license'] is 'pass':
                print(f'{user1["name"]}, now you can drive the tesla1')
            elif tesla1['autopilot'] and tesla1['battery_status'] is 'full':
                print(f'{user1["name"]} is not licenced, will start autopilot immediately')
        else:
            print(f'{user1["name"]} can\'t drive right now')
            if tesla1['autopilot'] and tesla1['battery_status'] is 'full':
                print('tesla1\'s autopilot system is on')
    elif 1 < user1['age'] < 18:
        print(f'{user1["name"]} not enough age to drive the car')
    elif user1['age'] < 0:
        print('what the hell?')
else:
    print(f'finger print is not correct, you are not the owner of tesla1')

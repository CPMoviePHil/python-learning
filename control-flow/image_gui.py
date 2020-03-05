picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
print('---------for-loop---------')
for value in picture:
    final_gui = ''
    for value_2 in value:
        if value_2 == 0:
            final_gui += ' '
        if value_2 == 1:
            final_gui += '*'
    print(final_gui)

print('---------while-loop---------')
counter = 0
fill = '*'
empty_space = ' '
while counter < len(picture):
    inside_counter = 0
    while inside_counter < len(picture[counter]):
        if picture[counter][inside_counter]:
            print(fill, end='')
        else:
            print(empty_space, end='')
        inside_counter += 1
    print('')
    counter += 1



team = [
    'A', 100,
    'B', 200,
    'C', 300
]

new_member = ['D', 400]

team += new_member

del(team[2])

print(team)

del(team[2])

print(team)

del(team[:])

print(team)
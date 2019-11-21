# MATH199 CHP Project 2
#
# Program that determines which pitch types are likliest to hit
#
# Kenneth Tochihara


import csv #import library

with open('data/pitches.csv', mode = 'r') as csv_file:
    pitches = csv.DictReader(csv_file)
    pitch = 0

    fastballs = 0
    offspeeds = 0


    #swinging strike, called strike, foul, hit out, hit on
    data_fastball = {'count': 0, 'STW': 0, 'C': 0, 'F': 0, 'X': 0, 'DE': 0}
    data_offspeed = {'count': 0, 'STW': 0, 'C': 0, 'F': 0, 'X': 0, 'DE': 0}

    for row in pitches:

        if row['Is Fastball'] == 'True':
            data_fastball['count'] += 1

            if (row['Call'] == 'S') | (row['Call'] == 'T') | (row['Call'] == 'W'):
                data_fastball['STW'] += 1

            if row['Call'] == 'C':
                data_fastball['C'] += 1

            if row['Call'] == 'F':
                data_fastball['F'] += 1

            if row['Call'] == 'X':
                data_fastball['X'] += 1

            if (row['Call'] == 'D') | (row['Call'] == 'E'):
                data_fastball['DE'] += 1

        elif row['Is Fastball'] == 'False':
            pitch += 1
            data_offspeed['count'] += 1

            if (row['Call'] == 'S') | (row['Call'] == 'T') | (row['Call'] == 'W'):
                data_offspeed['STW'] += 1

            if row['Call'] == 'C':
                data_offspeed['C'] += 1

            if row['Call'] == 'F':
                data_offspeed['F'] += 1

            if row['Call'] == 'X':
                data_offspeed['X'] += 1

            if (row['Call'] == 'D') | (row['Call'] == 'E'):
                data_offspeed['DE'] += 1

print(pitch)
print("~Results~\n")
print("Fastballs: " + str(data_fastball['STW']) + ' ' + str(data_fastball['C']) + ' ' + str(data_fastball['F']) + ' ' + str(data_fastball['X']) + ' ' + str(data_fastball['DE']))
print("Offspeeds: " + str(data_offspeed['STW']) + ' ' + str(data_offspeed['C']) + ' ' + str(data_offspeed['F']) + ' ' + str(data_offspeed['X']) + ' ' + str(data_offspeed['DE']))

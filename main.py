#Phelisa Ntayiya 2022/08/08

def addpoints():
    game1()
    game2()
    game3()
    game4()
    game5()
    print('\nOUTPUT')

    lions = (Lions_game1_points + Lions_game2_points + Lions_game3_points)
    fc_awesome = (FC_Awesome_game1_points + FC_Awesome_game2_points)
    snakes = (Snakes_game1_points + Snakes_game2_points)
    tarantulas = (Tarantulas_game1_points + Tarantulas_game2_points)
    grouches = Grouches_game_points

    values = [("Lions", lions, "pts"), ('Snakes', snakes, 'pts'), ('Tarantulas', tarantulas, 'pts'),
              ('FC_Awesome', fc_awesome, 'pts'),
              ('Grouches', grouches, 'pts')]
    data = sorted(values)
    #def Sort_Descending(value):
       # for i in range(len(value) - 1):
         #   minimum = i
          #  for j in range(len(value) - 1, i, -1):
            #    if (value[j] > value[minimum]):
             #       minimum = j
           # if (minimum != i):
            #    value[i], value[minimum] = value[minimum], value[i]
       # return value

    # print('Sorted List Descending:', Sort_Descending(values))
    def sort_key(data):
        return data[1]
    data.sort(key=sort_key, reverse=True)
    print(data)


def game1():
    print("#Lions VS Snakes#")
    Lions_game1 = int(input('Lions : '))
    Snakes_game1 = int(input('Snakes :'))
    global Lions_game1_points
    global Snakes_game1_points
    if Lions_game1 > Snakes_game1:
        Lions_game1_points = 3
        Snakes_game1_points = 0
        return Lions_game1_points, Snakes_game1_points
    elif Snakes_game1 > Lions_game1:
        Snakes_game1_points = 3
        Lions_game1_points = 0
        return Snakes_game1_points, Lions_game1_points
    elif Lions_game1 == Snakes_game1:
        print("Its a DRAW")
        Lions_game1_points = 1
        Snakes_game1_points = 1
        return Snakes_game1_points, Lions_game1_points


def game2():
    print("#Tarantulas VS FC Awesome#")
    global Tarantulas_game1_points
    global FC_Awesome_game1_points
    Tarantulas_game1 = int(input('Tarantulas : '))
    FC_Awesome_game1 = int(input('FC_Awesome :'))
    if Tarantulas_game1 > FC_Awesome_game1:
        Tarantulas_game1_points = 3
        FC_Awesome_game1_points = 0
        return Tarantulas_game1_points, FC_Awesome_game1_points

    elif FC_Awesome_game1 > Tarantulas_game1:
        FC_Awesome_game1_points = 3
        Tarantulas_game1_points = 0
        return FC_Awesome_game1_points
    elif FC_Awesome_game1 == Tarantulas_game1:
        print("Its a DRAW")
        Tarantulas_game1_points = 1
        FC_Awesome_game1_points = 1
        return Tarantulas_game1_points, FC_Awesome_game1_points


def game3():
    print("#Lions VS FC Awesome#")
    global Lions_game2_points
    global FC_Awesome_game2_points
    Lions_game2 = int(input('Lions : '))
    FC_Awesome_game2 = int(input('FC_Awesome :'))
    if Lions_game2 > FC_Awesome_game2:
        Lions_game2_points = 3
        FC_Awesome_game2_points = 0
        return Lions_game2_points, FC_Awesome_game2_points

    elif FC_Awesome_game2 > Lions_game2:
        FC_Awesome_game2_points = 3
        Lions_game2_points = 0
        return FC_Awesome_game2_points, Lions_game2_points
    elif FC_Awesome_game2 == Lions_game2:
        print("Its a DRAW")
        Lions_game2_points = 1
        FC_Awesome_game2_points = 1
        return Lions_game2_points, FC_Awesome_game2_points


def game4():
    print("#Tarantulas VS Snakes#")
    global Tarantulas_game2_points
    global Snakes_game2_points
    Tarantulas_game2 = int(input('Tarantulas : '))
    Snakes_game2 = int(input('Snakes :'))
    if Tarantulas_game2 > Snakes_game2:
        Tarantulas_game2_points = 3
        Snakes_game2_points = 0
        return Tarantulas_game2_points, Snakes_game2_points

    elif Snakes_game2 > Tarantulas_game2:
        Snakes_game2_points = 3
        Tarantulas_game2_points = 0
        return Snakes_game2_points, Tarantulas_game2_points
    elif Tarantulas_game2 == Snakes_game2:
        print("Its a DRAW")
        Tarantulas_game2_points = 1
        Snakes_game2_points = 1
        return Tarantulas_game2_points, Snakes_game2_points


def game5():
    print("#Lions VS Grouches#")
    global Lions_game3_points
    global Grouches_game_points
    Lions_game3 = int(input('Lions : '))
    Grouches_game = int(input('Grouches :'))
    if Lions_game3 > Grouches_game:
        Lions_game3_points = 3
        Grouches_game_points = 0
        return Lions_game3_points, Grouches_game_points

    elif Grouches_game > Lions_game3:
        Grouches_game_points = 3
        Lions_game3_points = 0
        return Grouches_game_points, Lions_game3_points
    elif Lions_game3 == Grouches_game:
        print("Its a DRAW")
        Lions_game3_points = 1
        Grouches_game_points = 1
        return Lions_game3_points, Grouches_game_points


# main function
print("LEAGUE")
print("#Please Enter Fulltime Score for each team for each game#\n")
addpoints()

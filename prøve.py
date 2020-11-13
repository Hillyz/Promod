#Oppgave 3

#Konstaner
c = 3 * 1E8
lambda0 = [278, 490, 687, 856, 954, 399]
lambda_obs = [280, 520, 675, 810, 990, 400]


def stjernefart(lst1, lst2):
    v_lst = [] #Unødvendig liste nå, kan være fin til senere hvis vi vil sammenlikne farten på stjernene

    for i in range(len(lst1)):
        v = round((lst1[i]-lst2[i])/ lst2[i] * c, 2) #regner ut farten og runder av til to desimaler
        if v < 0:
            print(f"Stjerne nummer {i+1} er blåforskjøvet med farten {v} m/s")
        else:
            print(f"Stjerne nummer {i+1} er rødforkjøvet med farten {v} m/s")

        v_lst.append(v) #igjen unødvening, men kanskje interessant

    return v_lst

#programmet blir utført
stjernefart(lambda0, lambda_obs)

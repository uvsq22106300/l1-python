def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre
    de seconde passé en argument"""
    jours = seconde // 86400
    heures = (seconde - jours * 86400) // 3600
    minutes = (seconde - jours * 86400 - heures * 3600) // 60
    secondes = seconde - jours * 86400 - heures * 3600 - minutes * 60
    return (jours, heures, minutes, secondes)


temps = secondeEnTemps(100000)
# print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3],
#       "secondes")


def afficheTemps(temps):
    # affichage des jours
    if temps[0] == 1:
        print(temps[0], "jour", end=" ")
    elif temps[0] > 1:
        print(temps[0], "jours", end=" ")
    else:
        pass

    # affichage des heures
    if temps[1] == 1:
        print(temps[1], "heure", end=" ")
    elif temps[1] > 1:
        print(temps[1], "heures", end=" ")
    else:
        pass

    # affichage des minutes
    if temps[2] == 1:
        print(temps[2], "minute", end=" ")
    elif temps[2] > 1:
        print(temps[2], "minutes", end=" ")
    else:
        pass

    # affichage des heures
    if temps[3] == 1:
        print(temps[3], "seconde", end=" ")
    elif temps[3] > 1:
        print(temps[3], "secondes", end=" ")
    else:
        pass


# afficheTemps((1, 0, 14, 23))


def demandeTemps():
    """Affiche proprement le temps entré"""
    tempsDemandeJours = int(input("Entrer un nombre de jours. "))
    tempsDemandeHeures = int(input("Entrer un nombre d'heures. "))
    tempsDemandeMinutes = int(input("Entrer un nombre de minutes. "))
    tempsDemandeSecondes = int(input("Entrer un nombre de secondes. "))
    temps = (tempsDemandeJours, tempsDemandeHeures, tempsDemandeMinutes,
             tempsDemandeSecondes)
    return temps

#afficheTemps(demandeTemps())

def sommeTemps(temps1, temps2):
    """Affiche la somme de deux tuples temps (j/h/m/s)"""
    tempsTotale = []
    tempsTotale.append(temps1[0]+temps2[0])
    tempsTotale.append(temps1[1]+temps2[1])
    tempsTotale.append(temps1[2]+temps2[2])
    tempsTotale.append(temps1[3]+temps2[3])
    tempsTotale = tuple(tempsTotale)
    return tempsTotale


# afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))


def proportionTemps(temps, proportion):
    """Calcule le pourcentage d'un temps"""
    temps = tempsEnSeconde(temps) * proportion
    temps = secondeEnTemps(temps)
    return temps


# afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))


def tempsEnDate(temps):
    """Donne la date sous la forme (année/j/h/m/s)"""
    if temps[0] >= 365:
        année = temps[0] // 365
        jours = temps[0]
    temps = list(temps)
    temps.insert(0, année)
    temps[1] = jours - année * 365
    temps = tuple(temps)
    return temps


def afficheDate(date=-1):
    return "année", (1970 + date[0])
    pass


# temps = secondeEnTemps(1000000000)
# afficheTemps(temps)
# print(afficheDate(tempsEnDate(temps)))


def bisextile(jours):
    années = jours // 365
    année = 2020 + années
    is_bisextile = False
    if année % 4 == 0:
        if année % 100 == 0:
            if année % 400 == 0:
                is_bisextile = True
            else:
                is_bisextile = False
        else:
            is_bisextile = True
    if is_bisextile:
        return "l'année", année, "est bisextile"
    else:
        return "l'année", année, "n'est pas bisextile"


# print(bisextile(19300))


def nombreBisextile(jour):
    if jour<365:
        print("année non bisextile")
    else:
        print("année bisextil")
    
def tempsEnDateBisextile(temps):
    
   
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))


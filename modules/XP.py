
XP = 0

def X_P(xp_, status=None):
    global XP

    if status == "add":
        XP += xp_

    elif status == "sub":
        XP -= xp_

    return XP
    






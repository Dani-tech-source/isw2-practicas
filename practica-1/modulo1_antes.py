d = {}  # inventario


def proc(c, l, t):
    # calcula
    tot = 0
    for x in l:
        p = d[x[0]]
        if p["s"] < x[1]:
            print("no hay")
            return -1
        tot = tot + p["p"] * x[1]
    if t == 1:
        tot = tot - tot * 0.10
    elif t == 2:
        tot = tot - tot * 0.20
    # isv
    tot = tot + tot * 0.15
    for x in l:
        d[x[0]]["s"] = d[x[0]]["s"] - x[1]
    print("Correo a " + c + ": su total es " + str(tot))
    return tot


if __name__ == "__main__":
    d["FIL-001"] = {"n": "Filtro de aceite", "p": 450, "s": 10}
    d["PAS-002"] = {"n": "Pastillas de freno", "p": 1500, "s": 4}
    proc("dani@correo.com", [("FIL-001", 2), ("PAS-002", 1)], 1)
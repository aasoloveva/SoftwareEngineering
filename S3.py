s="111235930184619"

def create_dict(string):
    d = {x: string.count(str(x)) for x in range(10)}
    res = {}
    mass = sorted(d, key=d.get)[::-1]
    mass = mass[0:3]
    mass = sorted(mass)[::-1]
    for i in mass:
        res.update({i:string.count(str(i))})
    return res
print(create_dict(s))
def intocm():
    ms=input("What is it? (inch-in or centimeter-cm): ")
    am=float(input("How many of it: "))
    intocm=2.54
    global inch
    global cm
    if ms=="inch" or ms=="in":
        cm=am*intocm
        inch=am
    elif ms=="centimeter" or ms=="cm":
        cm=am
        inch=cm/intocm
    print(f'inch: {inch}, centimeter: {cm}')
def kgtopd():
    ms=input("What is it? (kilogram-kg or pound-pd): ")
    am=float(input("How many of it: "))
    kgtopd=2.205
    global kg
    global pd
    if ms=="kilogram" or ms=="kg":
        kg=am
        pd=kg*kgtopd
    elif ms=="pound" or ms=="pd":
        pd=am
        kg=pd/kgtopd
    print(f'pound: {pd}, kilogram: {kg}')
calc=input("What do you want to calculate? (kilogram-kg into pound-pd == kgtopd or inch-in into centimeter-cm == intocm): ")
if calc=="kgtopd":
    kgtopd()
elif calc=="intocm":
    intocm()

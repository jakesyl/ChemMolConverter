#Adding Elements Weights
H=1
He=4
Li=6.9
Be=9
B=10.8
C=12
N=14
O=16
F=19
Ne=20.2
Na=23
Mg=24.3
Al=27
Si=28.1
P=31
S=32.1
Cl=35.5
Ar=39.9
K=39.1
Ca=40
Sc=44
Ti=47.9
V=50.9
Cr=52
Mn=54.9
Fe=55.8
Co=58.9
Ni=58.7
Cu=63.5
Zn=65.4
Ga=69.7
Ge=72.6
As=74.9
Se=79
Br=80
Kr=83.8
Rb=85.5
Sr=87.6
Y=88.9
Zr=91.2
Nb=92.9
Mo=96
Tc=98
Ru=101.1
Rh=102.9
Pd=106.4
Ag=107.9
Cd=112.4
In=114.8
Sn=118.7
Sb=121.8
Te=127.6
I=126.9
Xe=131.3
Cs=132.9
Ba=137.3
La=138.9
Ce=140.1
Pr=140.9
Nd=144.2
Pm=145
Sm=150.4
Eu=152
Gd=157.3
Tb=158.9
Dy=162.5
Ho=164.9
Er=167.3
Tm=168.9
Yb=173.1
Lu=175
Hf=178.5
Ta=180.9
W=183.8
Re=186.2
Os=190.2
Ir=192.2
Pt=195.1
Au=197
Hg=201
Tl=204.4
Pb=207.2
Bi=209
Po=209
At=210
Rn=222
Fr=223
Ra=226
Ac=227
Th=232
Pa=231
U=238
Np=237
Pu=244
Am=243
Cm=247
Bk=247
Cf=251
Es=252
Fm=257
Md=258
No=259
Lr=262
Rf=267
Db=268
Sg=271
Bh=272
Hs=270
Mt=276
Ds=281
Rg=280
Cn=285
Uut=284
Fl=289
Uup=288
Lv=293
Uus=294
Uuo=294

#Introduction
print("Welcome to the Chemistry Mole Converter by Zach Panzarino.")
print("Make sure to use just the element symbol (Not the Name) with the correct capitalization.")
print("Conversions can be done between grams, moles, and number of molecules.")

#Func for different types
def g2mol(g, weight):
    result=g/weight
    return (result)
def mol2g(mol, weight):
    result=mol*weight
    return (result)
def mol2molec(mol):
    result=mol*6.022*10^23
    return(result)
def molec2mol(molec):
    result=molec/(6.022*10^23)
    return(result)
def g2molec(g, weight):
    result=(g*6.022*10^23)/weight
    return(result)
def molec2g(molec, weight):
    result=(molec*weight)/(6.022*10^23)
    return(result)

#Program
go=True
convfrom=None
convto=None
convweight=None
elementnum=None
while go:
    end = None
    convweight = 0
    convfrom=input("What do you want to convert from? (Write out the full name)").lower()
    convto=input("What do you want to convert to? (Write out the full name)").lower()
    elementnum=int(input("How many different elements are in the molecule?"))
    for x in range(elementnum):
        element=eval(input("What is one of the elements?"))
        sgelementnum=int(input("How many of this element?"))
        convweight+=element*sgelementnum
    if convfrom == "grams" and convto == "mole":
        grams = int(input("How many grams?"))
        end = g2mol(grams, convweight)
        print(end + "mol")
    if convfrom == "mole" and convto == "grams":
        moles = int(input("How many moles?"))
        end = mol2g(moles, convweight)
        print(end + "g")
    if convfrom == "mole" and convto == "molecules":
        moles = int(input("How many moles?"))
        end = mol2molec(moles)
        print(end + "molec")
    if convfrom == "molecules" and convto == "moles":
        molecules = int(input("How many molecules?"))
        end = molec2mol(molecules)
        print(end + "mol")
    if convfrom == "grams" and convto == "molecules":
        grams = int(input("How many grams?"))
        end = g2molec(grams, convweight)
        print(end + "molec")
    if convfrom == "molecules" and convto == "grams":
        molecules = int(input("How many molecules?"))
        end = molec2g(molecules, convweight)
        print(end + "g")
    #End
    again = input("Do you need to do another calculation?").lower()
    if again == "yes":
        go = True
    elif again == "no":
        go = False
    else:
        go = False
print("Looks like we are done here.")

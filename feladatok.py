import math

def feladat1(a:str):
    i:int=0
    semmi:int=0
    while i<len(a):
        if a[i]==" ":
            semmi+=1
        i+=1
    return semmi

def feladat2(a:str):
    i:int=0
    nelkul:str=" "
    while i<len(a):
        if not(a[i]==" "):
            nelkul+=a[i]
        i+=1
    return nelkul

def feladat3(a:str):
    a=a.lower()
    a=a.replace("é","e")
    a=a.replace("á","a")
    a=a.replace("ó","o")
    a=a.replace("ő","o")
    a=a.replace("ö","o")
    a=a.replace("ü","u")
    a=a.replace("ű","u")
    a=a.replace("ú","u")
    a=a.replace("í","i")

    i=len(a)-1
    while i>=0:
        print(a[i], end=" ")
        i-=1


    
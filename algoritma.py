def compBasic(num):
    return 1-num

def compSugeno(num, a):
    comp = (1-num)/(1+(a*num))
    return comp

def compYager(num, a):
    comp = (1-num**a)(1/a)
    return comp

def tNormBasic(num1, num2):
    return min(num1,num2)

def tNormDubois(num1, num2, a):
    t = (num1*num2)
    tdiv = max(num1, num2, a)
    return t/tdiv


def tNormDombi(num1, num2, a):
    t = (1/num1 - 1)**a + (1/num2 - 1)**a
    tres = t**(1/a)
    return 1/(tres+1)

def tNormYager(num1, num2, a):
    t = ((1-num1)**a)+((1-num2)**a)
    tres = min(1, t**(1/a))
    return 1-tres

def tNormEinstein(num1, num2):
    t = (num1*num2)
    tdiv = 2-(num1+num2-t)
    return t/tdiv

def tNormDrastic(num1, num2):
    if num1 == 1:
        return num2
    elif num2 == 1:
        return num1
    else:
        return 0

def tNormAlgebraic(num1, num2):
    return num1*num2

def sNormBasic(num1,num2):
    return max(num1, num2)

def sNormDubois(num1, num2, a):
    s = (num1 + num2 - (num1 * num2)-(min(num1, num2, (1-a))))
    sMax = max((1-num1),(1-num2), a)
    return s/sMax

def sNormDombi(num1, num2, a):
    s = ((1/num1)-1)**(0-a)+((1/num2)-1)**(0-a)
    sres = s**(0-(1/a))
    return 1/(1+sres)

def sNormYager(num1, num2, a):
    s = num1**a+num2**a
    sres = min(1, s**(1/a))
    return sres

def sNormDrastic(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return 1

def sNormEinstein(num1, num2):
    s = (num1+num2)/(1+(num1*num2))
    return s

def sNormAlgebraic(num1, num2):
    s = num1+num2-(num1*num2)
    return s


while True:
    x=eval(input("Masukan nilai x yang di uji: "))
    y=eval(input("Masukan nilai y  yang di uji: "))
    if ( x > 1 or x < 0 or y > 1 or y < 0):
        print("Masukan angka yang sesuai")
    else:
        print ("Complement: \n   1. Basic \n   2. Sugeno Class \n   3. Yagger Class")
        pilih1 = int(input("Masukan Complement: "))
        if pilih1 == 1:
            hasil = compBasic(x)
            


        elif pilih1 == 2 :
            a = eval(input("Masukan konstanta: "))
            hasil= compSugeno(x, a)
        

        elif pilih1 == 3:
            a = eval(input("Masukan konstanta: "))
            hasil = compYager(x, a)
            
        print ("T-Norm: \n   1. Basic Minimum \n   2. Dombi Class\n   3. Dubois Prade Class\n   4. Yager Class\n   5. Drastic Product\n   6. Einstein Product\n   7. Algebraic Product")
        pilih2 = int(input("Masukan T-Norm: "))
        if pilih2 == 1:
            hasil2 = tNormBasic(x, y)
             
           

        elif pilih2 == 2:
            a = eval(input("Masukan nilai konstanta: "))
            hasil2 = tNormDombi(x, y, a)
             
            

        elif pilih2 == 3:
            a = eval(input("Masukan nilai konstanta: "))
            hasil2 = tNormDubois(x, y, a)
             
            

        elif pilih2 == 4:
            a = eval(input("Masukan nilai konstanta: "))
            hasil2 = tNormYager(x, y, a)
             
            

        elif pilih2 == 5:
            hasil2 = tNormDrastic(x, y)
            
            

        elif pilih2 == 6:
            hasil2 = tNormEinstein(x, y)
            
            

        elif pilih2 == 7:
            hasil2 = tNormAlgebraic(x, y)
             
        print ("S-Norm: \n   1. Basic Maximum \n   2. Dombi Class\n   3. Dubois Prade Class\n   4. Yager Class\n   5. Drastic Product\n   6. Einstein Product\n   7. Algebraic Product")
        pilih3 = int(input("Masukan S-Norm: "))
        if pilih3 == 1:
            hasil3 = sNormBasic(x, y)
            
            
        elif pilih3 == 2:
            z = eval(input("Masukan nilai konstanta: "))
            hasil3 = sNormDombi(x, y, z)
            
            

        elif pilih3 == 3:
            a = eval(input("Masukan nilai konstanta: "))
            hasil3 = sNormDubois(x, y, a)
            
            

        elif pilih3 == 4:
            a = eval(input("Masukan nilai konstanta: "))
            hasil3 = sNormYager(x, y, a)
            
            

        elif pilih3 == 5:
            hasil3 = sNormDrastic(x, y)
            
           

        elif pilih3 == 6:
            hasil3 = sNormEinstein(x, y)
            
            

        elif pilih3 == 7:
            hasil3 = sNormAlgebraic(x, y)
        min1= min(a,hasil)
        max1 = max(hasil2,min1)
        max2 = max (max1,hasil)
        print ("Hasil   : ",max2)
        

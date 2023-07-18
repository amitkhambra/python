#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp
#
# Created:     05/07/2023
# Copyright:   (c) hp 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
''' a=6
b=4
c=a+b
print(c)

a=6
b=4
c=a-b
print(c)


a=34
b=4
print(a+b)


a=34
b=4
print(a%b)


a=45
b=5
print(45/ 5)
print(45// 5)
print(45+5)
print(45-5)

a=34
b=4
print(a+b)

a=31
b=34
print(a//b)
print(a/b)

a=23
b=23
print(a+b)

a=67
b=3
print(a+b)


a=8
b=6
print(a==b)

a=8
b=4
print(a>b)

a=45
b=40
print(a>b)

a=45
b=40
print(a<b)

a=45
b=34
print(a<=b)

a=45
b=45
print(a<=b)

a=45
b=45
print(a>=b)

a=5
b=6
print(a>b and a<b)

a=45
b=34
print(a>b and a<b)

a=45
b=40
print(a<b or a>b)

a=34
b=34
print(a<b or a>b)

a=2
b=3
print(a<b or a>b)

a=45
b=65
print(a<b or a>b)

a=34
b=45
print(a+b)

a=45
b=45
print(a==b)

a=45
b=35
print(a==b)

a=56
b=56
print(a<b and a>b)

a=56
b=54
print(a<b and a>b)

a=56
b=54
print(a<b  or a>b)

a=78
b=69
print(a<b  or a>b) '''

#a=int(input("enter a value"))
#b=int(input("enter 2nd  value"))
#c=a+b
#print(c)



#p=100
#r=2
#t=2
#print(100*2*2/100)

#p=int(input("enter a value"))
#r=int(input("enter 2nd value"))
#t=int(input("enter 3rd value"))
#s=(p*r*t)/100
#print(s)


#arthimatic  operator

''''a=54
b=45
print(a+b)

a=54
b=45
print(a-b)

a=54
b=45
print(a/b)

a=54
b=45
print(a//b)

a=54
b=45
print(a%b)

a=54
b=45
print(a*b)


a=54
b=45
print(a+b)

#comparison operator
a=54
b=45
print(a==b)

a=55
b=55
print(a==b)

a=54
b=45
print(a>b)


b=54
a=45
print(a>b)

a=54
b=45
print(a>=b)



#logical operator

a=54
b=45
print(a<b and a>b)

a=54
b=45
print(a>b or a<b)

#bitwise

a=54
b=45
print(a  & b)

a=54
b=45
print(a  | b)


#left shift
a=54
b=45
print(a<<2)
print(b<<2)

#right shift

a=54
b=45
print(a>>  2)
print(b>>  2)

#xor

a=54
b=45
print(a^b)

a=5
b=6
print(a^b)

#membership operator
a="amit"
print("m" in a)

#input function
a= input("")
b=input("")
c=a+b
print(c)



a=int( input("1st "))
b=int(input("2nd"))
c=a+b
print(c)

#compound interset
p=200
r=4
t=2
s=(p*r*t)/100
print(s)


p=1000
r=40
t=4
s=(p*r*t)/100
print(s)


#xor
a=65
b=75
print(a^b)

a=99
b=69
print(a^b)



#bitwise
a=89
b=97
print(a&b)


a=89
b=97
print(a| b)

a=int(input("1st "))
b=int(input("2nd"))
c=a+b
print(c)


#input  function

a=input("6")
b=input("8")
print(a+b)'''''


#membership operator

#a="khambra "
#print("v" in a)

#a="dazzling"
#print("zz" in a)

#xor

#a=6
#b=9
#print(a^b)

#print(2**3)





#a=51
#b=6
#if a>b:
 #   print("a is greater")
  #else:
   # print("b is greater")



#a=int(input("1st"))
#if a>0:
 #  print(" no. is positive")
#else :
 #   print(" no is negative ")


'''a=int(input("1st"))
if a % 2 == 0:
    print("no. is   even")

else:
    print(" no. is odd ")

a=5
b=6
print("before swap",a,b)
c=a
a=b
b=c
print("after swap",a,b)

a=7
b=5
print("before swap", a,b)
b=b-a
a=a+b
b=a-b
print(" after swap", a, b)

a=9
b=3
print("before swap",  a, b)
b=b-a
a=a+b
b=a-b

print("after swap", a, b)






a=47
b=34
print("before swap",  a, b)
a=a-b
b=a+b
a=b-a
print("after swap", a, b)

a=99
b=89
print("before swap",  a, b)
b=a-b
a=a-b
b=a+b
print("after swap", a, b)



#if and else
a=int(input("enter the age"))
b=input("enter the gender")
if a>18 and b=='male'  :
    print("  eligible ")

else:
    print(" not eligible")





a=int(input("enter the age "))
b=input("enter  the gender")
if a>18 or  b== 'male' or 'female'  :
    print(" eligible")
else:
    print("  not eligible")


a=int(input("enter the salary"))
if a>15000:
    print(a/5*100)

else:
    print(" not eligible")


#Calculater
num=input("""  enter any  number
    press 1 for addition
    press 2 for mutiplication
    press 3 for substration
    press 4 for division


""")
if num=='1':
    print("  addition")
    a=int(input("enter 1st no"))
    b=int(input("enter 2nd no"))
    c=a+b
    print(c)
if num=='2':
    print(" multiplication")
    a=int(input("enter 1st  no"))
    b=int(input("enter 2nd  no"))
    c=a*b
    print(c)
if  num=='3':
    print("substraction")
    a=int(input("enter 1st  no"))
    b=int(input("enter 2nd  no"))
    c=a-b
    print(C)
if num=='4':
    print("division")
    a=int(input("enter 1st  no"))
    b=int(input("enter 2nd  no"))
    c=a/b
    print(c)




a=int(input("enter your percentage"))
if a>80:
    print("A+ grade")
elif a<=80 and a>= 70:
    print("A grade")
elif a<=   70 and a>=60:
    print(" B grade")
elif a<=60 and a>=50:
    print("C grade")
elif a<=50:
    print("FAIL")





a=int(input("n. in maths subject"))
b=int(input("n. in  science subject"))
c=int(input("n. in hindi subject"))
d=int(input("n. in english subject"))
e=int(input("n. in social science subject"))
h=(a+b+c+d+e)/5*100
print(h)
if a>80:
    print("A+ grade")
elif a<=80 and a>= 70:
    print("A grade")
elif a<=   70 and a>=60:
    print(" B grade")
elif a<=60 and a>=50:
    print("C grade")
elif a<=50:
    print("FAIL")




num= input("""enter a number
          press 1 for multiplication
          press 2 for addition
          press  3 for division
          press 4 for substraction
""")
if num== '1':
    print(" multiplication")
    a= int(input("enter a 1st number"))
    b= int(input("enter a 2nd number"))
    c=a*b
    print(c)

if num=='2':
    print("addition")
    a= int(input("enter a 1st number"))
    b= int(input("enter a 2nd number"))
    c=a+b
    print(c)

if num== '3':
    print("division")
    a= int(input("enter a 1st number"))
    b= int(input("enter a 2nd number"))
    c=a/b
    print(c)

if num =='4':
    print("substraction")
    a= int(input("enter a 1st number"))
    b= int(input("enter a 2nd number"))
    c=a-b
    print(c)






n=int(input(" enter  a number"))
b=n%10
n=n//10
c=n%10
n=n//10
d=n%10
n=n//10

r=b*100+c*10+d*1

b=r%10
r=r//10
if(b==1):
       print("One ",end="")

b=r%10
r=r//10
if(b==2):
        print("Two ",end="")

b=r%10
r=r//10
if(b==3):
        print("Three",end="")

    if(b==1):
        print("One ",end="")


    elif(b==2):
                    print("Two ",end="")
    elif(b==3):
                    print("Three ",end="")
    elif(b==4):
                    print("Four ",end="")
    elif(b==5):
                    print("Five ",end="")
    elif(b==6):
                    print("Six ",end="")
    elif(b==7):
                    print("Seven ",end="")
    elif(b==8):
                    print("Eight ",end="")
    elif(b==9):
                    print("Nine ",end="")
    elif(b==0):
                    print("Zero ",end="")









a=int(input("enter  the marks in mathematics"))
b=int(input("enter the marks in science"))
c=int(input("enter the marks in english"))
d=int(input("enter the marks in hindi"))
e=int(input("enter the marks in social science"))
h=(a+b+c+d+e)/5*100
print(h)
if a>80:
    print("A+ Grade")
elif a<=80 and a>= 70:
    print("   A Grade ")
elif   a<=70 and  a>=60:
    print(" B Grade")
elif a<=60 and a>=50:
    print(" C Grade ")
elif a<=50:
    print("FAIL")




a= int(input("enter your age"))
b= input(" enter your gender")
c=int(input(" enter your mobile no."))
if a>18 and  b=='male  ':
    print(" eligible")

else:
    print("not eligible")






a=5
b=6
print("before swap",a,b)
c=a
a=b
b=c
print("after swap",a,b)


a=int(input("enter your salary"))
if a>25000 :
    print(" 5% tdx is  eligible")
    b= (a)*5/100
    print(b)

else:
    print(" not eligible")


a= int(input(' enter   your roll no.'))
b= int(input(" enter your marks in  previous sem."))
if b >80 :
    print("  your fees is 5000")
else :
    print("your fees is 78000")




a= 5
b= 4

print(" before swap", a , b)
c=a
a=b
b=c

print("  after swap", a , b)





a= input("enter your name")
b=int(input(" enter your roll number"))
c=int(input(" enter your marks in    previous sem."))
if a== 'amit khambra' and  b== 210230440004 and  c>=70:

    print(" welcome")
    print(" eligible for entrance exam")
else:
    print(" wrong")
    print(" not  eligible")





a=input(" 1st no.")
b=input(" 2nd  no.")
print(a+b)



a=input("enter your name")
b=int(input("enter  your age"))
c=input(' enter your gender')
if b>= 18 and c== 'male' :
    print ("eligible for licience")

else :
    print(" not eligible for licience ")




#arithmatic operators

a=7
b=4
print(a+b)


a=7
b=4
print(a-b)



a=10
b=5
print(a/b)

a=10
b=5
print(a*b)



a=10
b=5
print(a%b)

a=10
b=5
print(a//b)


#logical operator

a=8
b=6
print(a==b)

a=8
b=4
print(a>b)

a=45
b=40
print(a>b)

a=45
b=40
print(a<b)

a=45
b=34
print(a<=b)

a=45
b=45
print(a<=b)

a=45
b=45
print(a>=b)

a=5
b=6
print(a>b and a<b)



#membership operator

a="amit"
print("m" in a)



#input  operator

a=int(input("enter a number"))
print(a)



# if and else

a=int(input("enter your age"))
b=input("enter your gender")
if    a>= 18 and b== 'male':
    print(" eligible")
else:
    print(" eligible")




# for loop
a=int(input(" enter a no."))
for i in range(1,11):

    a=34
    print(a,"*",i ,'=', i*a)
    print(a,"*",i ,'=', i*a)
    print(a,"*",i ,'=', i*a)
    print(a,"*",i ,'=', i*a)




a=int(input(" enter a marks in science"))
b=int(input(" enter a marks in  mathmathics"))
c=int(input(" enter a marks in hindi"))
d=int(input(" enter a marks in social science"))
e=int(input(" enter a marks in English"))
h=(a+b++c+d+e)/5*100
print(h)
if h>=80:
    print(" A+ Grade")

if  h<=80 and h>=70:
    print(" A Grade")

if h<=70 and h>=60:
    print(" B Grade")

if h<=50:
    print(" FAIL")'''





# code for sum of (1,10)
temp=0
for i in  range(1,11):
    temp=temp+i
print(temp)

# print for odd number
for i in range (1,21):
  if  i%2==1:
    print(i)



# print for even number
for i in range (1,21):
  if  i%2==0:
    print(i)

















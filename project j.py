print ("line 1")
mylist = [ 1 ,3 , 4 , 'b']
for a in mylist :
    print (a)
    print (f"{a}x2 = {a*2}")
    
print ("end")
print ('\n')
print ("line 2")
for _ in 'batman is dead' :
    print (_)
print ('\n')
print ("line 3")
mytuple = (1 ,2 , 3.14 , 'Mmz')
for b in mytuple :
    print (b)
print ('\n')
print ("line 4")
peoples = (('Mmz', 19 ) , ('maryam', 12))
for person in peoples :
    print (person)
print ('\n')
print ("line 5")
for person in peoples :
    name , sen = person
    print (f"{name} is {sen} years old")
print ('\n')
print ("line 6")
for name , sen in peoples :
    print (f"{name} is {sen} years old")
print ('\n')
print ("line 7")
people = {
        'Mmz' : (19 , 172) , 'maryam' : (12 , 143)
    }
for person in people :
    print (person)
print ('\n')
print ("line 8")
for person in people :
    print (person , people[person])
print ('\n')
print ("line 9")
for person in people :
    print (person , people[person][0])
print ('\n')
print ("line 10")
for person in people.items() :
    print (person)
print ('\n')
print ("line 11")
for person , data in people.items():
    print (f"{person} -> {data}")
print ('\n')
print ("line 12")
for person in people.keys() :
    print (f"{person}")
print ('\n')
print ("line 13")
for person in people.values() :
    print (f"{person}")
print ('\n')
print ("line 14")
a = 0
while a <= 5 :
    print (f"a is {a} ")
    a += 1
print ('\n')
print ("line 15")
for a in [1,2,3] :
    pass
print ("hich kari nemikone yani az dastoor rad mishe")
print ('\n')
print ("line 16")
for a in [1, 2, 3 ,4 ,5] :
    if a == 3 :
        break 
    print (a)
print ("dastoor break halghe ro mishkane")
print ('\n')
print ("line 17")
for a in [1, 2 ,3 ,4 , 5]:
    print ("start of an around loop")
    if a == 3 :
        continue
    print (a)
    print ("end of an around loop")
print ("dastoor continue baes mishe dar on dor dastoor haye bad az continue ejra nashavad va halghe be dor bad beravad")
print ('\n')
print ("line 18")
b = 0 
while b < 20 :
    b +=1
    if b % 3 == 0 and b % 5 ==0 :
        print ("hiphop")
        continue
    if b % 3 == 0 :
        print ("hip")
        continue
    if b % 5 == 0 :
        print ("hop")
        continue
    print (b)
print ('\n')
print ("line 19")
q = [1 , 3.14 , 19 , 5]
new = []
for n in q :
    new.append(n*2)
print (new)
print ('\n')
print ("line 20")
new = [ x*2 for x in q]
print (new)
print ('\n')
print ('line 21')
a = 5 
if a % 2 == 0 :
    res = 'zoj'
else :
    res = 'fard'
print (res)
print ('\n')
print ('line 22')
a = 5
rees = 'zoj' if a % 2 == 0 else 'fard'
print (rees)
print ('\n')
print ('line 23')
w = [1 ,2 ,4 ,5 , 6]
new = [a for a in w if a % 2 ==0]
print (new)
print ('\n')
print ('line 24')
new = ['zoj' if a % 2 == 0 else 'fard' for a in w]
print (new)
print ('\n')
print ('line 25')
new = ['hop' if a % 3 == 0 else a for a in range(1 ,20)]
print (new)
print ('\n')
print ('line 26')
for i in range(3) :
    for j in range(3) :
        print (i , j , i*j)
print ('\n')
print ('line 27')
for i in range(6) :
    for j in range(6):
        print (i*j , end = '\t')
    print ()
print ('\n')
print ('line 28')
for i in range(1, 6) :
    for j in range(1, 6) :
        print (i*j, end = '\t')
    print ()
print ('\n')
print ('line 29')
for i in range(2, 20, 2):
    print (i , end = ' ')
print ('\n')
print ('line 30')
for i in range(13, 1 , -2):
    print (i , end = ' ')
print ('\n')
print ('line 31')
l = 'maryam'
for i in range(len(l)) :
    print ( i , l[i])
print ('az len baraye andaze tool estefade mishe')
print ('\n')
print ('line 32')
l = ['sara','Mmz', 'maryam']
print (enumerate(l))
print ('\n')
print ('line 33')
for i , a in enumerate(l):
    print (i , a)
print ('enumerate jofti az 0 va sara / 1 va Mmz / 2 va maryam misazad')
print ('\n') 
print ('line 34')
esm = ['Mmz' , 'sara' , ' maryam']
famil = ['ziba' , 'razi' , 'zeabai']
sen = ['19' , '40' , '12']
for a in zip(esm , famil , sen) :
    print (a)
print ('zip mitavanad hkane haye yeksan chand list ra be ham vasl konad va dar ghaleb tuple dar khrooji neshan dahad')
print ('\n')
print ('line 35')
print ('mmz' in esm)
print ('az <in> baraye check kardane mojood boodan yek string dar list ya dictionary estefade mishe')
print ('\n')
print ('line 36')
s = 'abcd'
if 'm' in s :
    print ('yes')
else :
    print ('nah')
print ('\n')
print ('line 37')
names = ['Mmz' , 'sara' , 'maryam']
people = {
    'Mmz' : {'sen' : 19 , 'ghad' : 172},
    'maryam' : {'sen' : 12 , 'ghad' : 145}
    }
for name in names :
    if name in people :
        print (f"I have {name} and sen is {people[name]['sen']}")
    else :
        print (f"I don't have {name}")
print ('\n')
print ('line 38')
print (max(1, 2,6 ,4,8 ))
print ('bozorg tarin')
print ('\n')
print ('line 39')
print (min(1, 2, 3 ,5))
print ('koochak tarin')
print ('\n')
print ('line 40')
a = input("ye adad bede : ")
print (type(a) , a)
print ('\n')
print ('line 41')
a = input('ye adad bede: ')
a = int(a)
print (a*2)
print ('\n')
print ('line 42')
from random import randint
javab = randint(1, 6)
i = input('hads bezan : ')
i = int(i)
if i==javab:
    print ('dorost hads zadi')
else:
    print (f"try again! mal man {javab} bood!")
print ('\n')
print ('line 43')
l = [1 ,2 ,3]
l.pop()
print (l)
print ('<pop> onsor akhar list ro az list hazf mikone')
print ('\n')
print ('line 44')
l = [1,2,3,4]
akhari = l.pop(2)
print (akhari)
print (l)
print ('dar () pop agar index mored nazar dar list ro benevisim , chizi ke dar index vojood darad az list hazf mishavad')
print ('\n')
print ('line 45')
def hello() :
    print ('hello world!')
hello()
print ('\n')
print ('line 46')
def hello (name) :
    for i in range(2):
        print (f"hello {name}")
hello('Mmz')
print ('\n')
print ('line 47')
def say_hello (name) :
    '''
    this function print hello to you 
    '''
    for i in range(len(name)):
        print (f"hello {name}")
say_hello ('Mmz')
print ('be tedad horoof chap mikone')
print ("neveshte bein <'''> tozih amal kard tabe hast")
print ('braye esm haye tabe ya list ya... hamishe bein do kalame az <_> estefade kon')
print ('\n')
print ('line 48')
def say_hello_n_times(name, n):
    '''
    function print hello to you n times
    '''
    for i in range (n):
        print (f"hello {name}")
say_hello_n_times('Mmz', 2)
print ('\n')
print ('line 49')
def sum_of_numbers(a, b):
    res = a + b
    return res
print (f"sum of your numbers is {sum_of_numbers(3, 5)}")
print (sum_of_numbers('mohammad', 'mahdi'))
print (sum_of_numbers('mohammad', '19'))
print ('\n')
print ('line 50')
def chanta_tooshe (s, c) :
    '''
    function give to you how many of any chracter in your string
    '''
    counter = 0
    for your_character in s :
        if your_character == c :
            counter += 1
    return (counter)
name = 'mohammad'
chan = chanta_tooshe (name, "m")
print (f"the {name} has {chan} in the name")
print ('\n')
print ('line 51')
def tavan (n , t=2):
    javab = 1
    for i in range (t):
        javab *= n
    return javab
print (tavan ( 6 ))
print (tavan (3, 4))
print ('\n')
print ('line 52')
def numbers_of_even (numb):
    def is_even (n):
        return (n % 2 == 0)
    counter = 0
    for n in numb:
        if is_even(n) :
            counter += 1
    return counter 
counter = numbers_of_even ([2,3,4,5,6,7,8,9])
print (f"you have {counter} even numbers")
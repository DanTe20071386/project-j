print ("line 1")
mylist = [ 1 ,3 , 4 , 'b']
for a in mylist :
    print (a)
    print (f"{a}x2 = {a*2}")
    
print ("end")

print ("\nline 2")
for _ in 'batman is dead' :
    print (_)

print ("\nline 3")
mytuple = (1 ,2 , 3.14 , 'Mmz')
for b in mytuple :
    print (b)

print ("\nline 4")
peoples = (('Mmz', 19 ) , ('maryam', 12))
for person in peoples :
    print (person)

print ("\nline 5")
for person in peoples :
    name , sen = person
    print (f"{name} is {sen} years old")

print ("\nline 6")
for name , sen in peoples :
    print (f"{name} is {sen} years old")

print ("\nline 7")
people = {
        'Mmz' : (19 , 172) , 'maryam' : (12 , 143)
    }
for person in people :
    print (person)

print ("\nline 8")
for person in people :
    print (person , people[person])

print ("\nline 9")
for person in people :
    print (person , people[person][0])

print ("\nline 10")
for person in people.items() :
    print (person)

print ("\nline 11")
for person , data in people.items():
    print (f"{person} -> {data}")

print ("\nline 12")
for person in people.keys() :
    print (f"{person}")

print ("\nline 13")
for person in people.values() :
    print (f"{person}")

print ("\nline 14")
a = 0
while a <= 5 :
    print (f"a is {a} ")
    a += 1

print ("\nline 15")
for a in [1,2,3] :
    pass
print ("hich kari nemikone yani az dastoor rad mishe")

print ("\nline 16")
for a in [1, 2, 3 ,4 ,5] :
    if a == 3 :
        break 
    print (a)
print ("dastoor break halghe ro mishkane")

print ("\nline 17")
for a in [1, 2 ,3 ,4 , 5]:
    print ("start of an around loop")
    if a == 3 :
        continue
    print (a)
    print ("end of an around loop")
print ("dastoor continue baes mishe dar on dor dastoor haye bad az continue ejra nashavad va halghe be dor bad beravad")

print ("\nline 18")
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

print ("\nline 19")
q = [1 , 3.14 , 19 , 5]
new = []
for n in q :
    new.append(n*2)
print (new)

print ("\nline 20")
new = [ x*2 for x in q]
print (new)

print ('\nline 21')
a = 5 
if a % 2 == 0 :
    res = 'zoj'
else :
    res = 'fard'
print (res)

print ('\nline 22')
a = 5
rees = 'zoj' if a % 2 == 0 else 'fard'
print (rees)

print ('\nline 23')
w = [1 ,2 ,4 ,5 , 6]
new = [a for a in w if a % 2 ==0]
print (new)

print ('\nline 24')
new = ['zoj' if a % 2 == 0 else 'fard' for a in w]
print (new)

print ('\nline 25')
new = ['hop' if a % 3 == 0 else a for a in range(1 ,20)]
print (new)

print ('\nline 26')
for i in range(3) :
    for j in range(3) :
        print (i , j , i*j)

print ('\nline 27')
for i in range(6) :
    for j in range(6):
        print (i*j , end = '\t')
    print ()

print ('\nline 28')
for i in range(1, 6) :
    for j in range(1, 6) :
        print (i*j, end = '\t')
    print ()

print ('\nline 29')
for i in range(2, 20, 2):
    print (i , end = ' ')

print ('\nline 30')
for i in range(13, 1 , -2):
    print (i , end = ' ')

print ('\nline 31')
l = 'maryam'
for i in range(len(l)) :
    print ( i , l[i])
print ('az len baraye andaze tool estefade mishe')

print ('\nline 32')
l = ['sara','Mmz', 'maryam']
print (enumerate(l))

print ('\nline 33')
for i , a in enumerate(l):
    print (i , a)
print ('enumerate jofti az 0 va sara / 1 va Mmz / 2 va maryam misazad')
 
print ('\nline 34')
esm = ['Mmz' , 'sara' , ' maryam']
famil = ['ziba' , 'razi' , 'zeabai']
sen = ['19' , '40' , '12']
for a in zip(esm , famil , sen) :
    print (a)
print ('zip mitavanad hkane haye yeksan chand list ra be ham vasl konad va dar ghaleb tuple dar khrooji neshan dahad')

print ('\nline 35')
print ('mmz' in esm)
print ('az <in> baraye check kardane mojood boodan yek string dar list ya dictionary estefade mishe')

print ('\nline 36')
s = 'abcd'
if 'm' in s :
    print ('yes')
else :
    print ('nah')

print ('\nline 37')
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

print ('\nline 38')
print (max(1, 2,6 ,4,8 ))
print ('bozorg tarin')

print ('\nline 39')
print (min(1, 2, 3 ,5))
print ('koochak tarin')

print ('\nline 40')
a = input("ye adad bede : ")
print (type(a) , a)

print ('\nline 41')
a = input('ye adad bede: ')
a = int(a)
print (a*2)

print ('\nline 42')
from random import randint
javab = randint(1, 6)
i = input('hads bezan : ')
i = int(i)
if i==javab:
    print ('dorost hads zadi')
else:
    print (f"try again! mal man {javab} bood!")

print ('\nline 43')
l = [1 ,2 ,3]
l.pop()
print (l)
print ('<pop> onsor akhar list ro az list hazf mikone')

print ('\nline 44')
l = [1,2,3,4]
akhari = l.pop(2)
print (akhari)
print (l)
print ('dar () pop agar index mored nazar dar list ro benevisim , chizi ke dar index vojood darad az list hazf mishavad')

print ('\nline 45')
def hello() :
    print ('hello world!')
hello()

print ('\nline 46')
def hello (name) :
    for i in range(2):
        print (f"hello {name}")
hello('Mmz')

print ('\nline 47')
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

print ('\nline 48')
def say_hello_n_times(name, n):
    '''
    function print hello to you n times
    '''
    for i in range (n):
        print (f"hello {name}")
say_hello_n_times('Mmz', 2)

print ('\nline 49')
def sum_of_numbers(a, b):
    res = a + b
    return res
print (f"sum of your numbers is {sum_of_numbers(3, 5)}")
print (sum_of_numbers('mohammad', 'mahdi'))
print (sum_of_numbers('mohammad', '19'))

print ('\nline 50')
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
print (f"the {name} has {chan} {'m'} in the name")

print ('\nline 51')
def tavan (n , t=2):
    javab = 1
    for i in range (t):
        javab *= n
    return javab
print (tavan ( 6 ))
print (tavan (3, 4))

print ('\nline 52')
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

print ('\nline 53')
def is_even (n):
    return (n % 2 == 0)
def any_numbers_in_my_list(numb):
    '''
    if have any even number return true
    '''
    have_even = False
    for n in numb :
        if is_even(n) :
            have_even = True
    return have_even
my_numbers=[1, 2, 4, 5, 7]
print (any_numbers_in_my_list(my_numbers))

print ('\nline 54')
def any_numbers_in_my_list(numb):
    '''
    if have any even number return true
    '''
    for n in numb :
        if is_even(n) :
            return True
    return False
my_numbers=[1, 2, 4, 5, 7]
print (any_numbers_in_my_list(my_numbers))

print ('\nline 55')
def largest (numb):
    largest_number = numb[0]
    for n in numb :
        if largest_number < n :
            largest_number = n
    return largest_number
my_numbers = [1, 5, 3, 12, 6, 8]
largest_numbers = largest (my_numbers)
print (largest_numbers)
print ('bozorg tarin adad ro aval , avalin adad list gharar mide va bad be tartib ba baghie adad haye list moghayese mikone')

print ('\nline 56')
def get_odds(numb):
    odds = []
    for n in numb :
        if not is_even(n) :
            odds.append(n)
    return odds
my_list = [1, 4, 5, 6, 7, 8 ,13]
odds = get_odds(my_list)
print (odds)
print ('tabe (append) har adadi ke zoj nabashad ro be array odds ezafe mikone')

print ('\nline 57')
def get_odds(numb):
    odds = []
    for n in numb :
        if not is_even(n) :
            odds.append(n)
    return odds
my_list = [1, 4, 5, 6, 7, 8 ,13]
odds = get_odds(my_list)
print (len(odds))

print ('\nline 58')
def get_odds(numb):
    '''
    answer as a tuple
    '''
    odds = []
    count = 0
    for n in numb :
        if not is_even(n) :
            odds.append(n)
            count += 1
    return count , odds
my_list = [1, 4, 5, 6, 7, 8]
count , odds = get_odds(my_list)
print (count, odds, sep=':')
print ('tabe javab ro be soorat (tuple) bar migardoone')

print ('\nline 59')
def jam_zarb (n1 , n2) :
    jam = n1 + n2
    zarb = n1 * n2
    return jam, zarb
print (jam_zarb (5, 7))

print ('\nline 60')
scores = {
    'mohammad' : 19 ,
    'ali' : 17 ,
    'saman' : 18.5 ,
    'kasra' : 12.75
}
def scores_analysis(s):
    person = ''
    total = 0
    count = 0
    max_score = -1
    for name , score in s.items() : 
        total += score
        count += 1
        if score > max_score :
            person = name
            max_score = score
    avg = total / count
    return total , avg , person
total , avg , max_score = scores_analysis(scores)
print (f'total scores = {total}')
print (f'average scores = {avg}')
print (f'score A+ for {max_score}')

print ('\nline 61')
import random
def welcome () :
    print ('welcome to the my first game')
    print ('you are my first player ,I hope you enjoy to playing')
    print ('are you readyyyyy?')
    print ("let's gooooooooo!\n")

def finish (number, count) :
    print ('thanks for your playing :)\n')
    if count >= 10 :
        return f"my number is {number} and you found it in {count} guesses and that's prove you're so fool!"
    elif 4 <= count < 10 :
        print (f"my number is {number} and you found it in {count} guesses and that's prove you're as like riddler")
    elif 0 < count < 4 : 
        print (f"my number is {number} and you found it in {count} guesses and that's prove your mind is genius and you're as like sherlock holmes")
    answer = input ('do you want play again ? (y/n)  ')
    if answer.upper() == 'Y' :
        return True
    else :
        return False

def win (computer_number, guess) :
    return computer_number == guess

def answer (computer, user) :
    if computer > user :
        return "my number is bigger\n"
    if computer < user : 
        return "my number is smaller\n" 
    
    return 'ache...! you can defeated me!\n'

def get_a_guess () :
    ans = input ("what's your guess!? ")
    return int(ans)

welcome()
continue_playing = True
while (continue_playing) :
    computer_number = random.randint(1, 19)
    guess = 0
    count = 0
    while (not win(computer_number, guess)) :
        guess = get_a_guess()
        count += 1
        print (answer(computer_number, guess))
    continue_playing = finish(computer_number, count)
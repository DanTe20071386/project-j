print("\nline 1")


def zarb(*args):
    res = 1
    for i in args:
        res *= i
    return res


a = zarb(1, 4, 5, 7, 8, 11)
print(a)

print("\nline 2")


def masahat(**kwargs):
    print(kwargs)


masahat(tool=3, arz=9)

print("\nline 3")


def calculate_masahat(**kwargs):
    print(f"kwargs is : {kwargs}")
    if "tool" in kwargs:
        return kwargs["tool"] * kwargs["arz"]
    if "shoa" in kwargs:
        return kwargs["shoa"] * kwargs["shoa"] * 3.1415


print(calculate_masahat(shoa=2))
print(calculate_masahat(tool=9, arz=3))

print("\nline 3")


def tavan_2(x):
    return x**2


a = [2, 4, 6, 7]
for i in range(len(a)):
    a[i] = tavan_2(a[i])
print(a)

print("\nline 4")


def tavan_2(x):
    return x**2


a = [2, 4, 6, 7]
tavan_a = map(tavan_2, a)
print(tavan_a)
print(list(tavan_a))

print("\nline 5")
a = [2, 4, 6, 7]
tavan_a = map(lambda x: x**2, a)
print(list(tavan_a))
print(
    "baraye estefade az tavabe nashenas az (lambda) estefade mikonim dar zamani ke be yek tabe koochack niaz bashad"
)

print("\nline 6")


def is_ashari(x):
    return not x == int(x)


a = [1.2, 3, 4.5, 6, 7, 8.9, 0]
print(list(filter(is_ashari, a)))

print("\nline 7")
a = [1.2, 3, 4.5, 6, 7, 8.9, 0]
print(list(filter(lambda x: x != int(x), a)))

print("\nline 8")
names = ["Moahammad", "sadi", "arad", "hassan", "mahdi", "hafez", "hossien"]
short_names = tuple(filter(lambda s: len(s) <= 5, names))
print(short_names)

print("\nline 9")


def hello():
    name = "mahdi"
    print(f"in function name is {name}")


name = "mohammad"
print(f"first , real name is {name}")
hello()
print(f"second , real name is {name}")
print("tartib estefade az (variables{moteghaier ha}) bar asas mafhoom (legb) hast")
print("avalin tartib (local) hast")
print("dovomin tartib (enclosing function local) hast")
print("sevomin tartib (global) hast")
print("chaharomin tartib (build-in) hast ke yani baraye khode python bashe")
print(
    "\ndar code line 9 (mohammad) <global> tarif shode va (mahdi) <enclosing function local> tarif shode"
)

print("\nline 10")


def hello():
    global name
    name = "mahdi"
    print(f"in function name is {name}")


name = "mohammad"
print(f"first , real name is {name}")
hello()
print(f"second , real name is {name}")
print("ba neveshtan (global) dar tabe , name daroon tabe global tarif mishavad")
print("estefade az in ravesh pishnahad nemishe!!!")

print("\nline 11")


class classname:
    def __init__(self, param1):
        self.param1 = param1
        print("object created")

    def say_hello(self):
        print(f"hello")


t = classname(19)
print(t)
print(t.param1)
t.say_hello()
print(type(t))

print("\nline 12")


class book:
    def __init__(self, page):
        self.pages = page


my_book = book(325)
print(my_book.pages)
print(type(my_book))

print("\nline 13")


class book:
    def __init__(self, page):
        self.pages = page

    def open(self):
        print(f"open the book on page {self.pages}")


mybook = book(123)
mybook.open()

print("\nline 14")


class book:
    book_type = "sadness"

    def __init__(self, page):
        self.pages = page

    def open(self):
        print(f"open the book on page {self.pages}")


b1 = book(123)
print(b1.book_type)
b2 = book(321)
print(b2.book_type)
b1.book_type = "horror"
print(b1.book_type)
book.book_type = "fun"
b3 = book(12)
print(b3.book_type)

print("\nline 15")


class circle:
    pi = 3.1415

    def __init__(self, r):
        self.r = r

    def masahat(self):
        m = self.r * self.r * circle.pi
        return m

    def mohit(self):
        mo = 2 * self.r * self.pi
        return mo


c = circle(3)
print(c.masahat())
print(c.mohit())

print("\nline 16")


class book:
    def __init__(self, page, name):
        self.pages = page
        self.name = name

    def open(self):
        print(f"open the {self.name} book on page {self.pages}")


class darsi(book):
    def __init__(self, pages, name, reshte, paye):
        book.__init__(self, name, pages)
        print("a new book was added")
        self.reshte = reshte
        self.paye = paye

    def open(self):
        print(f"open the {self.name} book of {self.reshte} for paye {self.paye}")


d = darsi("gossaste", 123, "ryazi", 12)
print(type(d))
print(d.pages), print(d.name), print(d.reshte), d.open()
print("mozoo line 16 (ers bari) hast")

print("\nline 17")


class runner:
    def __init__(self, name):
        self.name = name

    def action(self):
        print(f"{self.name} is running")


class cyclist:
    def __init__(self, name):
        self.name = name

    def action(self):
        print(f"{self.name} is biking")


mohammad = runner("mohammad")
mohammad.action()
mahdi = cyclist("mahdi")
mahdi.action()
for person in [mohammad, mahdi]:
    person.action()


def show(p):
    p.action()


show(mahdi)
show(mohammad)

print("\nline 18")


class Human:
    def __init__(self, name):
        pass

    def sit():
        raise NotImplementedError("implement the sit")


class programmmer(Human):
    pass

    def sit(self):
        print("sit on the chair")


mahdi = programmmer("mahdi")
mahdi.sit()
print(
    "mozoo line 18 ==> (class) ie ke khodesh kari nemikone vali majboor mikone kassaie ke azash be ers mibaran ro ke yek kari bokonan"
)

print("\nline 19")


class book:
    def __init__(self, name, page):
        self.pages = page
        self.name = name

    def open(self):
        print(f"open the {self.name} book on page {self.pages}")

    def __len__(self):
        return self.pages

    def __str__(self):
        r = f"{self.name}, {self.pages}"
        return r


book1 = book("cruel prince", 254)
book2 = book("fallen king", 345)
book3 = book("midnight", 125)
print(book1)
print(len(book1))
print(str(book2))
print("mozoo line 19 ==> dunder method (double under __)")

print("\nline 20")
import zackage.mymod as mymod

mymod.hello()

print("\nline 21")
from zackage.mymod import hello

hello()
print(f"there is a {mymod.a} world")

print("\nline 22")
from zackage import mymod

mymod.hello()
print(f"in main project, the name is {__name__}")

print("\nline 23")
try:
    print(gajdj)
except:
    print("error!")

print("\nline 24")


def divzero(a, b):
    try:
        return a / b
    except:
        print("error!")
        return None


print(divzero(4, 2))
print(divzero(2, 0))

print("\nline 25")


def divzero(a, b):
    try:
        return a / b
    except Exception as E:
        print(f"error!, error in {E}")
        return None


print(divzero(4, 2))
print(divzero(2, 0))

print("\nline 26")


def divzero(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("b can't be a zero")
        return None
    except Exception as E:
        print(f"error!, error in {E}")
        return None


print(divzero(4, 2))
print(divzero(2, 0))
print(divzero("a", 2))

print("\nline 27")
try:
    f = open("/temp/nothing")
except FileNotFoundError:
    print("file nist!")
except Exception as E:
    print(f"error in {E} ")

print("\nline 28")


def divz(a, b):
    try:
        # try this
        r = a / b
    except Exception as E:
        # show exceptions
        print(f"error in {E}")
        r = None
    else:
        # will run if no exception happens
        print(r)
    finally:
        # will be done in any case
        return r


divz(2, 0), divz(2, 5)

print("\nline 29")


def countm(s, m):
    count = 0
    for i in range(len(s)):
        if s[i] == m:
            count += 1
    return count


print(countm("mohammad", "m"))

print("\nline 30")


def hello():
    print("hello mahdi")


hello()
print(hello)
heee = hello
print(heee)
heee()
print(heee is hello)
print("ebarat <is> barabary do object ro check mikone")

print("\nline 31")


def add(a, b):
    return a + b


def calculate(a, b, f):
    return f(a, b)


print(calculate(3, 5, add))

print("\nline 32")


def hello():
    print("hello mahdi")


def do_anytime(hell):
    hell()
    hell()


do_anytime(hello)

print("\nline 33")


def calculator(a, b, dooo):
    def sum(a, b):
        return a + b

    def zarb(a, b):
        return a * b

    if dooo == "sum":
        return sum(a, b)
    if dooo == "zarb":
        return zarb(a, b)


res = calculator(3, 5, "zarb")
print(res)

print("\nline 34")


def time_zoj(f):
    import datetime

    now = datetime.datetime.now()
    minute = now.minute
    if minute % 2 == 0:
        f()
    else:
        print("tik tok")


def hello():
    print("hello mahdi")


def bye():
    print("bye mahdi")


time_zoj(hello)
time_zoj(bye)

print("\nline 35")
print('decorator')

def time_zoj(f):
    def wrapper():
        import datetime

        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 0:
            f()
        else:
            print("tik tok")

    return wrapper


@time_zoj
def hello():
    print("hello mahdi")


@time_zoj
def bye():
    print("bye mahdi")


hello()
bye()

print ('\nline 36')
import random
import pickle
data = []
for i in range(10_000) :
    this = (random.randint(1, 6), random.randint(1, 6))
    data.append(this)
taas_out = open ("secret.taas", "wb")
pickle.dump(data, taas_out)
taas_out.close()

print ('\nline 37')
import pickle
def get_taas () :
    with open('secret.taas', 'rb') as data_file :
        data = pickle.load(data_file)
    for taas in data :
        yield taas


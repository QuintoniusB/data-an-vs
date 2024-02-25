import random
name = random.choice(['Meera','Ben','John','Anand'])
score = random.randint(0,100)

if score >=70:
    print(f' {name} perfomed really well in the test and got a score of {score}')
elif score >= 50 and score < 70:
    print(f'{name} passed the test and got a score of {score}')
else:
    print(f'{name} failed the test with a score of {score}')


x = [1,2,{'car':'Ford'},'Hello']

x[2]['car']

x = [1,2,3,(1,2,[1,2,3,4,5],3,2,1,[1,2])]

x[3][2][1:4]


codes = ['826GBR','840USA','276DEU','818EGY','250FRA']
codetjes = []

for element in codes:
    x = element
    codetjes.append(x[3:])
print(codetjes)


names=['Sophie', 'Mark','Susan','Jerome','Roger','Sunita','Boris','Steve']

upper = [x.upper() for x in names]
print(upper)


list_1 = [1,2,3,4,'Helena',9,2.8724,4,2,'Rick',{'name':'John'}]

whole_numbers = [list(filter(lambda x: isinstance(x,(int,float)) ,list_1))]
print(whole_numbers)


def function(x):
    if type(x) is list:
        y = sorted(x)
        x = y
    elif type(x) is tuple:
        x= len(x)
    elif type(x) is str:
        y = x.upper()
        x = y
    else:
        x = 'This is not a string, tuple or list'
    return x

test = [5555,555,55,5555,5]
print(function(test))


def num_check(x):
    return any(char.isdigit() for char in x)

test = 'hallo 5 yhaerhgieaiuhgr 88 aerhugfbea'
num_check(test)


person = [('Andrew',39,'Blue'),('Ross',48,'Red'),('Sarah',19,'Yellow'),('Meena',42,'Orange'),('Sophue',28,'Blue')]

def dinges1(dinges):
    dinges2 = []
    for element in dinges:
        if element[2] == 'Blue':
            dinges2.append(element)
    return dinges2

print(dinges1(person))
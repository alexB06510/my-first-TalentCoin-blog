print(2+3)

if 3>2:
    print("ça marche")

if 5>2:
    print("5 est effectivement plus grand que 2")
else:
    print("n'est pas plus grand que")

name = "Alexandra"

if name == "Alexandra":
    print ("hey Alexandra")
elif name == "Daphné":
    print ("hey Daphné!")
else: 
    print ("hey anonymous!")

volume = 60

if volume < 20:
    print("it is kinda quiet.")
elif 20 <= volume <40:
    print("it's nice for a background music.") 
elif 40 <= volume <60:
    print("Perfect, I can hear all the details.")
elif 60 <= volume <80:
    print('Nice for parties.')
elif 80 <= volume <100:
    print("My god it is too loud!")
else:
    print("My ears are crying!!:")

# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    print("That's better!")

def hi():
    print("hi there!")
    print("how are you?")

hi()

def hi(name):
    if name == 'Alexandra':
        print('Hi Alexandra!')
    elif name == 'Daphné':
        print('Hi Daphné!')
    else:
        print('Hi anonymous!')

hi("Alexandra")

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Daphné', 'Alexandra', 'You']

for name in girls:
    hi(name)
    print("newt girls")
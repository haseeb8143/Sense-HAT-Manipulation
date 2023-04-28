from sense_hat import SenseHat
import time
import sys

s = SenseHat()
s.low_light = True

o = (0, 0, 0)
c2 = (255, 255, 255)
c1 = (220, 220, 220)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)
pink = (255, 105, 180)


def trinket_logo(G, Y, B, O):
    logo = [
        O, O, O, O, O, O, O, O,
        O, Y, Y, Y, B, G, O, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        O, Y, Y, Y, B, G, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def raspi_logo(G, R, O):
    logo = [
        O, G, G, O, O, G, G, O,
        O, O, G, G, G, G, O, O,
        O, O, R, R, R, R, O, O,
        O, R, R, R, R, R, R, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, R, R, R, R, R, R, O,
        O, O, R, R, R, R, O, O,
    ]
    return logo


def plus(W, O):
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def equals(W, O):
    logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def heart(P, O):
    logo = [
        O, O, O, O, O, O, O, O,
        O, P, P, O, P, P, O, O,
        P, P, P, P, P, P, P, O,
        P, P, P, P, P, P, P, O,
        O, P, P, P, P, P, O, O,
        O, O, P, P, P, O, O, O,
        O, O, O, P, O, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def elephant(o, c2, c1):
    logo = [
        o, o, c1, c1, o, o, o, o,
        o, c1, c1, c1, c1, c1, c1, o,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, c1, c1, c1, c1, c1, c1, c1,
        c1, c2, c2, c1, c1, c1, c1, c1,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, o, c1, c1, o, c1, c1, o,
        c1, o, c2, c1, o, c2, c1, o,
    ]
    return logo


images = [trinket_logo(green, yellow, blue, nothing), plus(white, nothing), raspi_logo(green, red, nothing),
          equals(white, nothing), heart(pink, nothing),
          elephant(o, c2, c1)]

exitCode = 1

count = 0
def getUserChoice():
  done = False
  while done == False:
    try:
        print('1. Logo')
        print('2. Plus sign')
        print('3. Equal sign')
        print('4. Raspberry')
        print('5. Heart')
        print('6. Elephant')
        print('0. Exit')
        choice = int(input('What do you want to display?'))
        if choice > 0:
          s.set_pixels(images[choice-1])
        elif choice > 6:
            print('Please provide a valid number')
        elif choice == 0:
            exitCode = 0
            done=True
    except:
        print("please use a correct value")
if exitCode == 1:
  getUserChoice()

print('exiting')
exit()

import os
from time import sleep, time, ctime
from random import randint, choice, uniform, random, seed
from colorsys import hsv_to_rgb as htr, rgb_to_hsv as rth
from math import pi, sin, cos, sqrt

#just a bunch of functions

os.system("color")

chc = {"tao":(92, 51, 117) , "yri":(163, 157, 229), "sur":(207, 86, 77), "sen":(216, 161, 161), "yun":(56, 33, 135), "rin":(89, 109, 181), "lis":(200, 60, 85), "iu":(145, 140, 171), "kud":(189, 191, 209), "nik":(10, 206, 222)}

rpc = {"do":(163, 163, 163), "th":(95, 133, 125), "sp":(255, 255, 255), "wh":(174, 108, 140), "yl":(255, 200, 0)}

rgb = lambda hexc: tuple(int(hexc.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

hexc = lambda color: "%02x%02x%02x" % (*color,)

def hsv(array):
    array = tuple(i / 255 for i in array)
    result = int(rth(*array)[0] * 360),  int(rth(*array)[1] * 100),  int(rth(*array)[2] * 100)
    return result

def hgb(array):
    array = array[0] / 360, array[1] / 100, array[2] / 100
    result = tuple(int(i * 255) for i in htr(*array))
    return result

cs = lambda: os.system("cls")

bg = lambda color: "\x1b[48;2;{};{};{}m".format(*color)

fg = lambda color: "\x1b[38;2;{};{};{}m".format(*color)

def bgn(text, color = (255, 255, 255), array = False):
    if array:
        result = list(text)
        result[0] = bg(color) + result[0]
        result[-1] = result[-1] + "\x1b[49m"
        return tuple(result)
    else:
        return bg(color) + text + "\x1b[49m"

def fgn(text, color = (255, 255, 255), array = False):
    if array:
        result = list(text)
        result[0] = fg(color) + result[0]
        result[-1] = result[-1] + "\x1b[39m"
        return tuple(result)
    else:
        return fg(color) + text + "\x1b[39m"

rs  = "\x1b[0m"

smartint = lambda *numRange: randint(min(numRange), max(numRange))

def picture(array, char = "██"):
    result = ""
    for i in array:
        for j in i:
            result += fg(j) + char
        result += "\n"
    return result + rs

def convert(array):
    dict = {}
    for i in array:
        dict[i[0]] = i[1]
    return dict

def globalscreate(**kwargs): #is not working, use it inside main file
    for k, v in kwargs.items(): globals().update(kwargs)

def localscreate(**kwargs): #is not working, use it inside main file
    for k, v in kwargs.items(): locals().update(kwargs)

mean = lambda array: sum(array) / len(array)

colormean = lambda array: tuple(sum(i) // len(i) for i in zip(*array))

percent = lambda num, perc: (num / 100) * perc

part = lambda num1, num2: (num2 / num1) * 100

clamp = lambda num, minNum, maxNum:  max(min(num, minNum), maxNum)

def cira(num, minNum, maxNum):
    rangeSize = maxNum - minNum + 1
    result = (num - minNum) % rangeSize
    return result + minNum

def stepoffset(array, step = 10):
    result = []
    step_num = (array[1] - array[0]) / (step - 1)
    for i in range(step):
        result.append(int(array[0] + step_num * i))
    return tuple(result)

def arraytinate(array, char = ""):
    result = ""
    for i in range(len(array)):
        result += str(array[i])
        if i == len(array) - 1:
            break
        result += char
    return result

equivalent = lambda *args, **kwargs: (args, kwargs)

def randchar(array, num):
    result = ""
    for i in range(num):
        result += choice(array)
    return result

def similar(replaceble, replacer):
    min_str = min([len(replaceble), len(replacer)])
    max_str = max([len(replaceble), len(replacer)])
    length = 100 / max_str
    result = 0
    for i in range(min_str):
        if replacer[i] == replaceble[i]:
            result += length
    return result

def caesar(word, num = 1, key = False):
    if key: return ("".join((chr(ord(i) + num) for i in word)), -key)
    else: return "".join((chr(ord(i) + num) for i in word))

def lavenshtain(replaceble, replacer):
    def recursive(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        elif replaceble[i - 1] == replacer[j - 1]:
            return recursive(i - 1, j - 1)
        else:
            return 1 + min(recursive(i, j - 1), recursive(i - 1, j), recursive(i - 1, j - 1))
    return recursive(len(replaceble), len(replacer))

fibonacci = lambda num: 1 if num in (0, 1, 2) else fibonacci(num - 1) + fibonacci(num - 2)

inv = lambda args: tuple(not i for i in args)

transistor = lambda emitter, base: emitter if base else False

factorial = lambda num: 1 if num == 1 else num * factorial(num - 1)

def row(lower, upper, expression, type = 1):
    result = eval(expression.replace("i", str(lower))) 
    match type:
        case 1:
            for i in range(lower + 1, upper + 1):
                result += eval(expression)
        case 2:
            for i in range(lower + 1, upper + 1):
                result *= eval(expression)
        case _:

            for i in range(lower + 1, upper + 1):
                result += eval(expression)
    return result

def notation(num, first_notation, second_notation, is_upper = False):
    if isinstance(num, int) or isinstance(num, float):
        num = str(num)
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    decimal = 0
    for i in range(len(num)):
        digit = num[-(i+1)]
        if digit.isalpha():
            digit = digit.upper()
            value = ord(digit) - ord('A') + 10
        else:
            value = int(digit)
        decimal += value * (first_notation ** i)
    result = ""
    while decimal > 0:
        remainder = decimal % second_notation
        if remainder >= 10:
            result = digits[remainder] + result
        else:
            result = str(remainder) + result
        decimal //= second_notation
    return result if not is_upper else result.upper()

def listshift(array, offset = 1):
    for i in range(abs(offset)):
        if offset > 0:
            array = list(array)[1:] + [array[0]]
        elif offset < 0:
            array = [list(array)[-1]] + array[:-1]
    return tuple(array)

def multireplace(text, dict):
    for i in list(dict):
        text = text.replace(i, dict[i])
    return text

def allowed(char, array, replacer):
    if char in array: return char
    else: return replacer

def chance(dict):
    result = []
    for i in list(dict):
        result += [i] * dict[i]
    return tuple(result)

def revertchance(tuple):
    result = {}
    for i in tuple:
        if i in list(result):
            result[i] += 1
        else:
            result[i] = 1
    return result

def diapason(*args):
    match len(args):
        case 1: return tuple(range(args[0] + 1))
        case 2: return tuple(range(args[0], args[1] + 1))
        case 3: return tuple(range(args[0], args[1] + 1, args[2]))
        case _: raise TypeError(f"diapason expected at most 3 arguments, got {len(args)}")

def lerp(min, max, delta, deltamin = 0, deltamax = 1): return min + (max - min) * (delta - deltamin) / (deltamax - deltamin)

def easing(num, type = "easeInSine", add1 = 2, add2 = 1):
    match type:
        case "easeInSine": return 1 - cos((num * pi) / 2)
        case "easeOutSine": return sin((num * pi) / 2) 
        case "easeInOutSine": return -(cos(num * pi) - 1) / 2
        case "easeInQuad": return num ** 2
        case "easeOutQuad": return 1 - (1 - num) ** 2
        case "easeInOutQuad": return 2 * (num ** 2) if num < 0.5 else 1 - (-2 * num + 2) ** 2 / 2
        case "easeInCubic": return num ** 3
        case "easeOutCubic": return 1 - (1 - num) ** 3
        case "easeInOutCubic": return 4 * (num ** 3) if num < 0.5 else 1 - (-2 * num + 2) ** 3 / 2
        case "easeInQuart": return num ** 4
        case "easeOutQuart": return 1 - (1 - num) ** 4
        case "easeInOutQuart": return 8 * (num ** 4) if num < 0.5 else 1 - (-2 * num + 2) ** 4 / 2
        case "easeInQuint": return num ** 5
        case "easeOutQuint": return 1 - (1 - num) ** 5
        case "easeInOutQuint": return 16 * (num ** 5) if num < 0.5 else 1 - (-2 * num + 2) ** 5 / 2
        case "easeInCustom": return num ** add1
        case "easeOutCustom": return 1 - (1 - num) ** add1
        case "easeInOutCustom": return 2 ** (add1 - 1) * (num ** add1) if num < 0.5 else 1 - (-2 * num + 2) ** add1 / 2
        case "easeInExpo": return 0 if num == 0 else 2 ** (10 * num - 10)
        case "easeOutExpo": return 1 if num == 1 else 1 - 2 ** (-10 * num)
        case "easeInOutExpo":
            if num == 0:
                return 0
            elif num == 1:
                return 1
            elif num < 0.5:
                return pow(2, 20 * num - 10) / 2
            else:
                return (2 - pow(2, -20 * num + 10)) / 2
        case "easeInCirc": return 1 - sqrt(1 - num ** 2)
        case "easeOutCirc": return sqrt(1 - (num - 1) ** 2)
        case "easeInOutCirc": return (1 - sqrt(1 - (2 * num) ** 2)) / 2 if num < 0.5 else (sqrt(1 - (-2 * num + 2) ** 2) + 1) / 2
        case "easeInBack": return (add2 * 2.70158) * num ** 3 - (add1 * 0.85079) * num ** 2
        case "easeOutBack": return 1 + (add2 * 2.70158) * (num - 1) ** 3 + (add1 * 0.85079) * (num - 1) ** 2
        case "easeInOutBack": return ((2 * num) ** 2 * (((add1 * 1.29745475) + 1) * 2 * num - (add1 * 1.29745475))) / 2 if num < 0.5 else ((2 * num - 2) ** 2 * (((add1 * 1.29745475) + 1) * (2 * num - 2) + (add1 * 1.29745475)) + 2) / 2
        case "easeInElastic": return 0 if num == 0 else 1 if num == 1 else -(2 ** (10 * num - (10 * 10))) * sin((num * 10 - 10.75) * (add1 * pi / 3)) 
        case "easeOutElastic": return 0 if num == 0 else 1 if num == 1 else 2 ** (-10 * num) * sin((num * 10 - .75) * (add1 * pi / 3)) + 1
        case "easeInOutElastic": return 0 if num == 0 else 1 if num == 1 else -(2 ** (20 * num - 10) * sin(20 * num - 11.125) * (add1 * pi / 4.5)) / 2 if num < 0.5 else (2 ** (-20 * num + 10) * sin(20 * num - 11.125) * (add1 * pi / 4.5)) / 2 + 1
        case "easeInBounce": return 1 - easing(1 - num, "easeOutBounce", add1, add2)
        case "easeOutBounce":
            if num < 1 / (add2 * 2.75):
                return (add1 * 3.78125) * num ** 2
            elif num < 2 / (add2 * 2.75):
                return (add1 * 3.78125) * (num - 1.5 / add2) * num + 0.75
            elif num < 2.5 / (add2 * 2.75):
                return (add1 * 3.78125) * (num - 2.25 / (add2 * 2.75)) * num + 0.9375
            else:
                return (add1 * 3.78125) * (num - 2.625 / (add2 * 2.75)) * num + 0.984375
        case "easeInOutBounce": return (1 - easing(1 - 2 * num, "easeOutBounce", add1, add2)) / 2 if num < 0.5 else (1 + easing(2 * num - 1, "easeOutBounce", add1, add2)) / 2
        case _: return easing(num, "easeInSine", add1, add2)

def colorshift(array, num, type = "h", set = False):
    if set:
        match type:
            case "h":
                return hgb((cira(num, 0, 360), hsv(array)[1], hsv(array)[2]))
            case "s":
                return hgb((hsv(array)[0], clamp(num, 0, 100), hsv(array)[2]))
            case "l":
                return hgb((hsv(array)[0], hsv(array)[1], clamp(num, 0, 100)))
            case _:
                return tuple(array)
    else:
        match type:
            case "h":
                return hgb((cira(hsv(array)[0] + num, 0, 360), hsv(array)[1], hsv(array)[2]))
            case "s":
                return hgb((hsv(array)[0], clamp(hsv(array)[1] + num, 0, 100), hsv(array)[2]))
            case "l":
                return hgb((hsv(array)[0], hsv(array)[1], clamp(hsv(array)[2] + num, 0, 100)))
            case _:
                return tuple(array)

def rainbow(num, offset = 0):
    rainlist = []
    for i in range(num):
        hue = ((i / num) * 360) + offset
        rgb = hgb((hue, 100, 100))
        rainlist.append(rgb)
    return tuple(rainlist)

def randcoord(latRange = (-90, 90), longRange = (0, 180)): return uniform(latRange[0], latRange[1]), uniform(longRange[0], longRange[1])

def randip(ipRange = ((0, 255), (0, 255), (0, 255), (0,255))):
    result = []
    for i in ipRange:
        result.append(randint(*i))
    return tuple(result)

def sections(text, start_marker, end_marker, markers = True):
    result = []
    start_index = 0
    while True:
        start = text.find(start_marker, start_index)
        if start == -1:
            break
        end = text.find(end_marker, start + len(start_marker))
        if end == -1:
            break
        section = text[start + len(start_marker):end]
        if markers:
            result.append(start_marker + section + end_marker)
        else:
            result.append(section)
        start_index = end + len(end_marker)
    return tuple(result)

def reduce(array, num, offset = 0): return tuple(array[offset::num])

def timequence(num):
    result = []
    days = round(num // 86400)
    hours = round((num - (days * 86400)) // 3600)
    minutes = round((num - ((days * 86400) + (hours * 3600))) // 60)
    seconds = float("{:.2f}".format(num - ((days * 86400) + (hours * 3600) + (minutes * 60))))
    for i in [days, hours, minutes, seconds]:
        result.append(i)
    return tuple(result)

def pinput(prompt = "", default = ""):
    print(prompt, end = "")
    temp = input()
    if temp != "":
        return temp
    else:
        return default
    del temp

def randcolor(colorRange = ((0, 0, 0), (255, 255, 255))): return randint(colorRange[0][0], colorRange[1][0]), randint(colorRange[0][1], colorRange[1][1]), randint(colorRange[0][2], colorRange[1][2])

def ef(text, effect):
    effects = {"bold":["\x1b[1m", "\x1b[2m"], "dim":["\x1b[2m", "\x1b[1m"], "italic":["\x1b[3m", "\x1b[23m"], "underline":["\x1b[4m", "\x1b[24m"], "blink":["\x1b[5m", "\x1b[25m"], "inverse":["\x1b[7m", "\x1b[27m"], "hidden":["\x1b[8m", "\x1b[28m"]}
    return effects[effect][0] + text + effects[effect][1]

invertcolor = lambda array: tuple(255 - i for i in array)

desatcolor = lambda array: tuple(hgb((0, 0, hsv(array)[2])))

performance = lambda speed, horsepower, acceleration, weight: (speed * horsepower) / (weight  * acceleration)

def gradient(array, num = 10): return tuple(zip(stepoffset((array[0][0], array[1][0]), num), stepoffset((array[0][1], array[1][1]), num), stepoffset((array[0][2], array[1][2]), num)))

def gradients(array, num = 5):
    gradations = []
    num_gradients = len(array) - 1
    for i in range(num_gradients):
        colors = array[i], array[i + 1]
        gradation = gradient(colors, num)
        gradations.extend(gradation)
    return tuple(gradations)

def accugrad(dict):
    gradation = []
    for i in list(dict):
        gradation.extend(gradient((i[0], i[1]), dict[i]))
    return tuple(gradation)

def foregrad(text, color_list, array = False):
    gradation = gradient(color_list, len(text))
    if array:
        result = []
        for i in range(len(text)):
            result.append(fg(gradation[i]) + text[i])
        result[-1] += rs
    else:
        result = ""
        for i in range(len(text)):
            result += fg(gradation[i]) + text[i]
        result += rs
    return result

def backgrad(text, color_list, array = False):
    gradation = gradient(color_list, len(text))
    if array:
        result = []
        for i in range(len(text)):
            result.append(bg(gradation[i]) + text[i])
        result[-1] += rs
    else:
        result = ""
        for i in range(len(text)):
            result += bg(gradation[i]) + text[i]
        result += rs
    return result

def forerain(text, offset = 0, array = False):
    gradation = rainbow(len(text), offset)
    if array:
        result = []
        for i in range(len(text)):
            result.append(fg(gradation[i]) + text[i])
        result[-1] += rs
    else:
        result = ""
        for i in range(len(text)):
            result += fg(gradation[i]) + text[i]
        result += rs
    return result

def backrain(text, offset = 0, array = False):
    gradation = rainbow(len(text), offset)
    if array:
        result = []
        for i in range(len(text)):
            result.append(bg(gradation[i]) + text[i])
        result[-1] += rs
    else:
        result = ""
        for i in range(len(text)):
            result += bg(gradation[i]) + text[i]
        result += rs
    return result

def colorfamily(array = (randcolor(), randcolor()), num = 5, quality = 100):
    result = []
    for i in range(num): result.append(choice(gradient((array[0], array[1]), quality)))
    return tuple(result)

def flush(array, time = .1, samestring = False):
    for i in array:
        print(i, end = "", flush = True)
        sleep(time)
    if not samestring:
        print()

def play(text, effect, speed = .1, times = 1):
    for time in range(times):
        for color in effect:
            print(fgn(text, color))
            sleep(speed)
            cs()

class Bulbs_Network:
    def __init__(self):
        self.__bulbs = {}

    def create_bulb(self, new_id):
        self.__bulbs[new_id] = (False, (255, 255, 255))

    def delete_bulb(self, id):
        del self.__bulbs[id]

    def set_id(self, old_id, new_id):
        self.__bulbs[new_id] = self.__bulbs[old_id].copy()
        del self.__bulbs[old_id]

    def set_state(self, id, state):
        self.__bulbs[id] = list(self.__bulbs[id])
        self.__bulbs[id][0] = state
        self.__bulbs[id] = tuple(self.__bulbs[id])

    def get_state(self, id):
        return self.__bulbs[id][0]

    def set_color(self, id, color):
        self.__bulbs[id] = list(self.__bulbs[id])
        self.__bulbs[id][1] = color
        self.__bulbs[id] = tuple(self.__bulbs[id])

    def get_color(self, id):
        return self.__bulbs[id][1]
        
    def get_color_real(self, id):
        if self.__bulbs[id][0]:
            return self.__bulbs[id][1]
        else:
            return (0, 0, 0)

class Case:
    def __init__(self, items = {}):
        self.__items = items

    def set_items(self, items = {}):
        self.__items = items

    def get_info(self):
        return {"amount":len(self.__items), "items":tuple(self.__items), "chances":self.__items}

    def open(self):
        return choice(chance(self.__items))

class Inventory:
    def __init__(self, items):
        self.__items = items

    def set(self, items):
        self.__items = items

    def add(self, items):
        for i in list(items):
            if i in list(self.__items):
                self.__items[i] += items[i]
            else:
                self.__items[i] = items[i]

    def delete(self, items):
        for i in list(items):
            if i in list(self.__items):
                if self.__items[i] > items[i]:
                    self.__items[i] -= items[i]
                else:
                    del self.__items[i]

    def clear(self):
        self.__items = {}

    def show(self):
        return self.__items

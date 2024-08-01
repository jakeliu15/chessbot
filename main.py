import pyautogui
import time
import random
from stockfish import Stockfish
from stockfish import StockfishException

stockfish = Stockfish(path="/opt/homebrew/bin/stockfish")

time.sleep(4)

#region

#images for each piece for matching
LS = '/Users/jakeliu/Desktop/chess-pieces/LS.png'
DS = '/Users/jakeliu/Desktop/chess-pieces/DS.png'

WPLS = '/Users/jakeliu/Desktop/chess-pieces/WPLS.png'
WPDS = '/Users/jakeliu/Desktop/chess-pieces/WPDS.png'
WBLS = '/Users/jakeliu/Desktop/chess-pieces/WBLS.png'
WBDS = '/Users/jakeliu/Desktop/chess-pieces/WBDS.png'
WNLS = '/Users/jakeliu/Desktop/chess-pieces/WNLS.png'
WNDS = '/Users/jakeliu/Desktop/chess-pieces/WNDS.png'
WRLS = '/Users/jakeliu/Desktop/chess-pieces/WRLS.png'
WRDS = '/Users/jakeliu/Desktop/chess-pieces/WRDS.png'
WQLS = '/Users/jakeliu/Desktop/chess-pieces/WQLS.png'
WQDS = '/Users/jakeliu/Desktop/chess-pieces/WQDS.png'
WKLS = '/Users/jakeliu/Desktop/chess-pieces/WKLS.png'
WKDS = '/Users/jakeliu/Desktop/chess-pieces/WKDS.png'

BPLS = '/Users/jakeliu/Desktop/chess-pieces/BPLS.png'
BPDS = '/Users/jakeliu/Desktop/chess-pieces/BPDS.png'
BBLS = '/Users/jakeliu/Desktop/chess-pieces/BBLS.png'
BBDS = '/Users/jakeliu/Desktop/chess-pieces/BBDS.png'
BNLS = '/Users/jakeliu/Desktop/chess-pieces/BNLS.png'
BNDS = '/Users/jakeliu/Desktop/chess-pieces/BNDS.png'
BRLS = '/Users/jakeliu/Desktop/chess-pieces/BRLS.png'
BRDS = '/Users/jakeliu/Desktop/chess-pieces/BRDS.png'
BQLS = '/Users/jakeliu/Desktop/chess-pieces/BQLS.png'
BQDS = '/Users/jakeliu/Desktop/chess-pieces/BQDS.png'
BKLS = '/Users/jakeliu/Desktop/chess-pieces/BKLS.png'
BKDS = '/Users/jakeliu/Desktop/chess-pieces/BKDS.png'

#coordinates of board square corners 
a8_xmin = 207
a8_ymin = 188
a8_xmax = 286
a8_ymax = 265

b8_xmin = 296
b8_ymin = 188
b8_xmax = 376
b8_ymax = 265

c8_xmin = 384
c8_ymin = 188
c8_xmax = 464
c8_ymax = 265

d8_xmin = 472
d8_ymin = 188
d8_xmax = 552
d8_ymax = 265

e8_xmin = 560
e8_ymin = 188
e8_xmax = 640
e8_ymax = 265

f8_xmin = 648
f8_ymin = 188
f8_xmax = 728
f8_ymax = 265

g8_xmin = 736
g8_ymin = 188
g8_xmax = 816
g8_ymax = 265

h8_xmin = 824
h8_ymin = 188
h8_xmax = 904
h8_ymax = 265

a7_xmin = 207
a7_ymin = 276
a7_xmax = 286
a7_ymax = 353

b7_xmin = 296
b7_ymin = 276
b7_xmax = 376
b7_ymax = 353

c7_xmin = 384
c7_ymin = 276
c7_xmax = 464
c7_ymax = 353

d7_xmin = 472
d7_ymin = 276
d7_xmax = 552
d7_ymax = 353

e7_xmin = 560
e7_ymin = 276
e7_xmax = 640
e7_ymax = 353

f7_xmin = 648
f7_ymin = 276
f7_xmax = 728
f7_ymax = 353

g7_xmin = 736
g7_ymin = 276
g7_xmax = 816
g7_ymax = 353

h7_xmin = 824
h7_ymin = 276
h7_xmax = 904
h7_ymax = 353

a6_xmin = 207
a6_ymin = 364
a6_xmax = 286
a6_ymax = 441

b6_xmin = 296
b6_ymin = 364
b6_xmax = 376
b6_ymax = 441

c6_xmin = 384
c6_ymin = 364
c6_xmax = 464
c6_ymax = 441

d6_xmin = 472
d6_ymin = 364
d6_xmax = 552
d6_ymax = 441

e6_xmin = 560
e6_ymin = 364
e6_xmax = 640
e6_ymax = 441

f6_xmin = 648
f6_ymin = 364
f6_xmax = 728
f6_ymax = 441

g6_xmin = 736
g6_ymin = 364
g6_xmax = 816
g6_ymax = 441

h6_xmin = 824
h6_ymin = 364
h6_xmax = 904
h6_ymax = 441

a5_xmin = 207
a5_ymin = 452
a5_xmax = 286
a5_ymax = 529

b5_xmin = 296
b5_ymin = 452
b5_xmax = 376
b5_ymax = 529

c5_xmin = 384
c5_ymin = 452
c5_xmax = 464
c5_ymax = 529

d5_xmin = 472
d5_ymin = 452
d5_xmax = 552
d5_ymax = 529

e5_xmin = 560
e5_ymin = 452
e5_xmax = 640
e5_ymax = 529

f5_xmin = 648
f5_ymin = 452
f5_xmax = 728
f5_ymax = 529

g5_xmin = 736
g5_ymin = 452
g5_xmax = 816
g5_ymax = 529

h5_xmin = 824
h5_ymin = 452
h5_xmax = 904
h5_ymax = 529

a4_xmin = 207
a4_ymin = 540
a4_xmax = 286
a4_ymax = 617

b4_xmin = 296
b4_ymin = 540
b4_xmax = 376
b4_ymax = 617

c4_xmin = 384
c4_ymin = 540
c4_xmax = 464
c4_ymax = 617

d4_xmin = 472
d4_ymin = 540
d4_xmax = 552
d4_ymax = 617

e4_xmin = 560
e4_ymin = 540
e4_xmax = 640
e4_ymax = 617

f4_xmin = 648
f4_ymin = 540
f4_xmax = 728
f4_ymax = 617

g4_xmin = 736
g4_ymin = 540
g4_xmax = 816
g4_ymax = 617

h4_xmin = 824
h4_ymin = 540
h4_xmax = 904
h4_ymax = 617

a3_xmin = 207
a3_ymin = 628
a3_xmax = 286
a3_ymax = 705

b3_xmin = 296
b3_ymin = 628
b3_xmax = 376
b3_ymax = 705

c3_xmin = 384
c3_ymin = 628
c3_xmax = 464
c3_ymax = 705

d3_xmin = 472
d3_ymin = 628
d3_xmax = 552
d3_ymax = 705

e3_xmin = 560
e3_ymin = 628
e3_xmax = 640
e3_ymax = 705

f3_xmin = 648
f3_ymin = 628
f3_xmax = 728
f3_ymax = 705

g3_xmin = 736
g3_ymin = 628
g3_xmax = 816
g3_ymax = 705

h3_xmin = 824
h3_ymin = 628
h3_xmax = 904
h3_ymax = 705

a2_xmin = 207
a2_ymin = 716
a2_xmax = 286
a2_ymax = 793

b2_xmin = 296
b2_ymin = 716
b2_xmax = 376
b2_ymax = 793

c2_xmin = 384
c2_ymin = 716
c2_xmax = 464
c2_ymax = 793

d2_xmin = 472
d2_ymin = 716
d2_xmax = 552
d2_ymax = 793

e2_xmin = 560
e2_ymin = 716
e2_xmax = 640
e2_ymax = 793

f2_xmin = 648
f2_ymin = 716
f2_xmax = 728
f2_ymax = 793

g2_xmin = 736
g2_ymin = 716
g2_xmax = 816
g2_ymax = 793

h2_xmin = 824
h2_ymin = 716
h2_xmax = 904
h2_ymax = 793

a1_xmin = 207
a1_ymin = 804
a1_xmax = 286
a1_ymax = 881

b1_xmin = 296
b1_ymin = 804
b1_xmax = 376
b1_ymax = 881

c1_xmin = 384
c1_ymin = 804
c1_xmax = 464
c1_ymax = 881

d1_xmin = 472
d1_ymin = 804
d1_xmax = 552
d1_ymax = 881

e1_xmin = 560
e1_ymin = 804
e1_xmax = 640
e1_ymax = 881

f1_xmin = 648
f1_ymin = 804
f1_xmax = 728
f1_ymax = 881

g1_xmin = 736
g1_ymin = 804
g1_xmax = 816
g1_ymax = 881

h1_xmin = 824
h1_ymin = 804
h1_xmax = 904
h1_ymax = 881



coordinates = {
    'a1': (a1_xmin, a1_ymin, a1_xmax, a1_ymax),
    'b1': (b1_xmin, b1_ymin, b1_xmax, b1_ymax),
    'c1': (c1_xmin, c1_ymin, c1_xmax, c1_ymax),
    'd1': (d1_xmin, d1_ymin, d1_xmax, d1_ymax),
    'e1': (e1_xmin, e1_ymin, e1_xmax, e1_ymax),
    'f1': (f1_xmin, f1_ymin, f1_xmax, f1_ymax),
    'g1': (g1_xmin, g1_ymin, g1_xmax, g1_ymax),
    'h1': (h1_xmin, h1_ymin, h1_xmax, h1_ymax),
    'a2': (a2_xmin, a2_ymin, a2_xmax, a2_ymax),
    'b2': (b2_xmin, b2_ymin, b2_xmax, b2_ymax),
    'c2': (c2_xmin, c2_ymin, c2_xmax, c2_ymax),
    'd2': (d2_xmin, d2_ymin, d2_xmax, d2_ymax),
    'e2': (e2_xmin, e2_ymin, e2_xmax, e2_ymax),
    'f2': (f2_xmin, f2_ymin, f2_xmax, f2_ymax),
    'g2': (g2_xmin, g2_ymin, g2_xmax, g2_ymax),
    'h2': (h2_xmin, h2_ymin, h2_xmax, h2_ymax),
    'a3': (a3_xmin, a3_ymin, a3_xmax, a3_ymax),
    'b3': (b3_xmin, b3_ymin, b3_xmax, b3_ymax),
    'c3': (c3_xmin, c3_ymin, c3_xmax, c3_ymax),
    'd3': (d3_xmin, d3_ymin, d3_xmax, d3_ymax),
    'e3': (e3_xmin, e3_ymin, e3_xmax, e3_ymax),
    'f3': (f3_xmin, f3_ymin, f3_xmax, f3_ymax),
    'g3': (g3_xmin, g3_ymin, g3_xmax, g3_ymax),
    'h3': (h3_xmin, h3_ymin, h3_xmax, h3_ymax),
    'a4': (a4_xmin, a4_ymin, a4_xmax, a4_ymax),
    'b4': (b4_xmin, b4_ymin, b4_xmax, b4_ymax),
    'c4': (c4_xmin, c4_ymin, c4_xmax, c4_ymax),
    'd4': (d4_xmin, d4_ymin, d4_xmax, d4_ymax),
    'e4': (e4_xmin, e4_ymin, e4_xmax, e4_ymax),
    'f4': (f4_xmin, f4_ymin, f4_xmax, f4_ymax),
    'g4': (g4_xmin, g4_ymin, g4_xmax, g4_ymax),
    'h4': (h4_xmin, h4_ymin, h4_xmax, h4_ymax),
    'a5': (a5_xmin, a5_ymin, a5_xmax, a5_ymax),
    'b5': (b5_xmin, b5_ymin, b5_xmax, b5_ymax),
    'c5': (c5_xmin, c5_ymin, c5_xmax, c5_ymax),
    'd5': (d5_xmin, d5_ymin, d5_xmax, d5_ymax),
    'e5': (e5_xmin, e5_ymin, e5_xmax, e5_ymax),
    'f5': (f5_xmin, f5_ymin, f5_xmax, f5_ymax),
    'g5': (g5_xmin, g5_ymin, g5_xmax, g5_ymax),
    'h5': (h5_xmin, h5_ymin, h5_xmax, h5_ymax),
    'a6': (a6_xmin, a6_ymin, a6_xmax, a6_ymax),
    'b6': (b6_xmin, b6_ymin, b6_xmax, b6_ymax),
    'c6': (c6_xmin, c6_ymin, c6_xmax, c6_ymax),
    'd6': (d6_xmin, d6_ymin, d6_xmax, d6_ymax),
    'e6': (e6_xmin, e6_ymin, e6_xmax, e6_ymax),
    'f6': (f6_xmin, f6_ymin, f6_xmax, f6_ymax),
    'g6': (g6_xmin, g6_ymin, g6_xmax, g6_ymax),
    'h6': (h6_xmin, h6_ymin, h6_xmax, h6_ymax),
    'a7': (a7_xmin, a7_ymin, a7_xmax, a7_ymax),
    'b7': (b7_xmin, b7_ymin, b7_xmax, b7_ymax),
    'c7': (c7_xmin, c7_ymin, c7_xmax, c7_ymax),
    'd7': (d7_xmin, d7_ymin, d7_xmax, d7_ymax),
    'e7': (e7_xmin, e7_ymin, e7_xmax, e7_ymax),
    'f7': (f7_xmin, f7_ymin, f7_xmax, f7_ymax),
    'g7': (g7_xmin, g7_ymin, g7_xmax, g7_ymax),
    'h7': (h7_xmin, h7_ymin, h7_xmax, h7_ymax),
    'a8': (a8_xmin, a8_ymin, a8_xmax, a8_ymax),
    'b8': (b8_xmin, b8_ymin, b8_xmax, b8_ymax),
    'c8': (c8_xmin, c8_ymin, c8_xmax, c8_ymax),
    'd8': (d8_xmin, d8_ymin, d8_xmax, d8_ymax),
    'e8': (e8_xmin, e8_ymin, e8_xmax, e8_ymax),
    'f8': (f8_xmin, f8_ymin, f8_xmax, f8_ymax),
    'g8': (g8_xmin, g8_ymin, g8_xmax, g8_ymax),
    'h8': (h8_xmin, h8_ymin, h8_xmax, h8_ymax),
}

def concat_values(*args):
        result = ""
        current_sum = 0
        for arg in args:
            if isinstance(arg, int):
                current_sum += arg
            else:
                if current_sum:
                    result += str(current_sum)
                    current_sum = 0
                result += arg

        # In case the last set of values are integers
        if current_sum:
            result += str(current_sum)

        return result

def image_in_range(piece, square):
        match = None

        # Look for the image in the cropped screenshot
        match = pyautogui.locate(piece, square, confidence=.99, grayscale=True)

        # Return True if the image was found, otherwise False
        return match 


def move(start_xmin, start_ymin, start_xmax, start_ymax, end_xmin, end_ymin, end_xmax, end_ymax):
        
    startx = start_xmin + ((start_xmax - start_xmin) / 2)   #calculations must be divided by two due to mac having double the expected display size
    starty = start_ymin + ((start_ymax - start_ymin) / 2)
    endx = end_xmin + ((end_xmax - end_xmin) / 2)
    endy = end_ymin + ((end_ymax - end_ymin) / 2)

    pyautogui.click(startx, starty)
    time.sleep(.5)
    pyautogui.click(endx, endy)
        
#retrieve current board position using FEN notation
def getFen():    
    screenshot = pyautogui.screenshot()

    a1 = 1
    b1 = 1
    c1 = 1
    d1 = 1
    e1 = 1
    f1 = 1
    g1 = 1
    h1 = 1

    a2 = 1
    b2 = 1
    c2 = 1
    d2 = 1
    e2 = 1
    f2 = 1
    g2 = 1
    h2 = 1

    a3 = 1
    b3 = 1
    c3 = 1
    d3 = 1
    e3 = 1
    f3 = 1
    g3 = 1
    h3 = 1

    a4 = 1
    b4 = 1
    c4 = 1
    d4 = 1
    e4 = 1
    f4 = 1
    g4 = 1
    h4 = 1

    a5 = 1
    b5 = 1
    c5 = 1
    d5 = 1
    e5 = 1
    f5 = 1
    g5 = 1
    h5 = 1

    a6 = 1
    b6 = 1
    c6 = 1
    d6 = 1
    e6 = 1
    f6 = 1
    g6 = 1
    h6 = 1

    a7 = 1
    b7 = 1
    c7 = 1
    d7 = 1
    e7 = 1
    f7 = 1
    g7 = 1
    h7 = 1

    a8 = 1
    b8 = 1
    c8 = 1
    d8 = 1
    e8 = 1
    f8 = 1
    g8 = 1
    h8 = 1

    region = (a1_xmin*2, a1_ymin*2, a1_xmax*2, a1_ymax*2)
    imga1 = screenshot.crop(region)

    region = (b1_xmin*2, b1_ymin*2, b1_xmax*2, b1_ymax*2)
    imgb1 = screenshot.crop(region)

    region = (c1_xmin*2, c1_ymin*2, c1_xmax*2, c1_ymax*2)
    imgc1 = screenshot.crop(region)

    region = (d1_xmin*2, d1_ymin*2, d1_xmax*2, d1_ymax*2)
    imgd1 = screenshot.crop(region)

    region = (e1_xmin*2, e1_ymin*2, e1_xmax*2, e1_ymax*2)
    imge1 = screenshot.crop(region)

    region = (f1_xmin*2, f1_ymin*2, f1_xmax*2, f1_ymax*2)
    imgf1 = screenshot.crop(region)

    region = (g1_xmin*2, g1_ymin*2, g1_xmax*2, g1_ymax*2)
    imgg1 = screenshot.crop(region)

    region = (h1_xmin*2, h1_ymin*2, h1_xmax*2, h1_ymax*2)
    imgh1 = screenshot.crop(region)

    region = (a2_xmin*2, a2_ymin*2, a2_xmax*2, a2_ymax*2)
    imga2 = screenshot.crop(region)

    region = (b2_xmin*2, b2_ymin*2, b2_xmax*2, b2_ymax*2)
    imgb2 = screenshot.crop(region)

    region = (c2_xmin*2, c2_ymin*2, c2_xmax*2, c2_ymax*2)
    imgc2 = screenshot.crop(region)

    region = (d2_xmin*2, d2_ymin*2, d2_xmax*2, d2_ymax*2)
    imgd2 = screenshot.crop(region)

    region = (e2_xmin*2, e2_ymin*2, e2_xmax*2, e2_ymax*2)
    imge2 = screenshot.crop(region)

    region = (f2_xmin*2, f2_ymin*2, f2_xmax*2, f2_ymax*2)
    imgf2 = screenshot.crop(region)

    region = (g2_xmin*2, g2_ymin*2, g2_xmax*2, g2_ymax*2)
    imgg2 = screenshot.crop(region)

    region = (h2_xmin*2, h2_ymin*2, h2_xmax*2, h2_ymax*2)
    imgh2 = screenshot.crop(region)

    region = (a3_xmin*2, a3_ymin*2, a3_xmax*2, a3_ymax*2)
    imga3 = screenshot.crop(region)

    region = (b3_xmin*2, b3_ymin*2, b3_xmax*2, b3_ymax*2)
    imgb3 = screenshot.crop(region)

    region = (c3_xmin*2, c3_ymin*2, c3_xmax*2, c3_ymax*2)
    imgc3 = screenshot.crop(region)

    region = (d3_xmin*2, d3_ymin*2, d3_xmax*2, d3_ymax*2)
    imgd3 = screenshot.crop(region)

    region = (e3_xmin*2, e3_ymin*2, e3_xmax*2, e3_ymax*2)
    imge3 = screenshot.crop(region)

    region = (f3_xmin*2, f3_ymin*2, f3_xmax*2, f3_ymax*2)
    imgf3 = screenshot.crop(region)

    region = (g3_xmin*2, g3_ymin*2, g3_xmax*2, g3_ymax*2)
    imgg3 = screenshot.crop(region)

    region = (h3_xmin*2, h3_ymin*2, h3_xmax*2, h3_ymax*2)
    imgh3 = screenshot.crop(region)

    region = (a4_xmin*2, a4_ymin*2, a4_xmax*2, a4_ymax*2)
    imga4 = screenshot.crop(region)

    region = (b4_xmin*2, b4_ymin*2, b4_xmax*2, b4_ymax*2)
    imgb4 = screenshot.crop(region)

    region = (c4_xmin*2, c4_ymin*2, c4_xmax*2, c4_ymax*2)
    imgc4 = screenshot.crop(region)

    region = (d4_xmin*2, d4_ymin*2, d4_xmax*2, d4_ymax*2)
    imgd4 = screenshot.crop(region)

    region = (e4_xmin*2, e4_ymin*2, e4_xmax*2, e4_ymax*2)
    imge4 = screenshot.crop(region)

    region = (f4_xmin*2, f4_ymin*2, f4_xmax*2, f4_ymax*2)
    imgf4 = screenshot.crop(region)

    region = (g4_xmin*2, g4_ymin*2, g4_xmax*2, g4_ymax*2)
    imgg4 = screenshot.crop(region)

    region = (h4_xmin*2, h4_ymin*2, h4_xmax*2, h4_ymax*2)
    imgh4 = screenshot.crop(region)

    region = (a5_xmin*2, a5_ymin*2, a5_xmax*2, a5_ymax*2)
    imga5 = screenshot.crop(region)

    region = (b5_xmin*2, b5_ymin*2, b5_xmax*2, b5_ymax*2)
    imgb5 = screenshot.crop(region)

    region = (c5_xmin*2, c5_ymin*2, c5_xmax*2, c5_ymax*2)
    imgc5 = screenshot.crop(region)

    region = (d5_xmin*2, d5_ymin*2, d5_xmax*2, d5_ymax*2)
    imgd5 = screenshot.crop(region)

    region = (e5_xmin*2, e5_ymin*2, e5_xmax*2, e5_ymax*2)
    imge5 = screenshot.crop(region)

    region = (f5_xmin*2, f5_ymin*2, f5_xmax*2, f5_ymax*2)
    imgf5 = screenshot.crop(region)

    region = (g5_xmin*2, g5_ymin*2, g5_xmax*2, g5_ymax*2)
    imgg5 = screenshot.crop(region)

    region = (h5_xmin*2, h5_ymin*2, h5_xmax*2, h5_ymax*2)
    imgh5 = screenshot.crop(region)

    region = (a6_xmin*2, a6_ymin*2, a6_xmax*2, a6_ymax*2)
    imga6 = screenshot.crop(region)

    region = (b6_xmin*2, b6_ymin*2, b6_xmax*2, b6_ymax*2)
    imgb6 = screenshot.crop(region)

    region = (c6_xmin*2, c6_ymin*2, c6_xmax*2, c6_ymax*2)
    imgc6 = screenshot.crop(region)

    region = (d6_xmin*2, d6_ymin*2, d6_xmax*2, d6_ymax*2)
    imgd6 = screenshot.crop(region)

    region = (e6_xmin*2, e6_ymin*2, e6_xmax*2, e6_ymax*2)
    imge6 = screenshot.crop(region)

    region = (f6_xmin*2, f6_ymin*2, f6_xmax*2, f6_ymax*2)
    imgf6 = screenshot.crop(region)

    region = (g6_xmin*2, g6_ymin*2, g6_xmax*2, g6_ymax*2)
    imgg6 = screenshot.crop(region)

    region = (h6_xmin*2, h6_ymin*2, h6_xmax*2, h6_ymax*2)
    imgh6 = screenshot.crop(region)

    region = (a7_xmin*2, a7_ymin*2, a7_xmax*2, a7_ymax*2)
    imga7 = screenshot.crop(region)

    region = (b7_xmin*2, b7_ymin*2, b7_xmax*2, b7_ymax*2)
    imgb7 = screenshot.crop(region)

    region = (c7_xmin*2, c7_ymin*2, c7_xmax*2, c7_ymax*2)
    imgc7 = screenshot.crop(region)

    region = (d7_xmin*2, d7_ymin*2, d7_xmax*2, d7_ymax*2)
    imgd7 = screenshot.crop(region)

    region = (e7_xmin*2, e7_ymin*2, e7_xmax*2, e7_ymax*2)
    imge7 = screenshot.crop(region)

    region = (f7_xmin*2, f7_ymin*2, f7_xmax*2, f7_ymax*2)
    imgf7 = screenshot.crop(region)

    region = (g7_xmin*2, g7_ymin*2, g7_xmax*2, g7_ymax*2)
    imgg7 = screenshot.crop(region)

    region = (h7_xmin*2, h7_ymin*2, h7_xmax*2, h7_ymax*2)
    imgh7 = screenshot.crop(region)

    region = (a8_xmin*2, a8_ymin*2, a8_xmax*2, a8_ymax*2)
    imga8 = screenshot.crop(region)

    region = (b8_xmin*2, b8_ymin*2, b8_xmax*2, b8_ymax*2)
    imgb8 = screenshot.crop(region)

    region = (c8_xmin*2, c8_ymin*2, c8_xmax*2, c8_ymax*2)
    imgc8 = screenshot.crop(region)

    region = (d8_xmin*2, d8_ymin*2, d8_xmax*2, d8_ymax*2)
    imgd8 = screenshot.crop(region)

    region = (e8_xmin*2, e8_ymin*2, e8_xmax*2, e8_ymax*2)
    imge8 = screenshot.crop(region)

    region = (f8_xmin*2, f8_ymin*2, f8_xmax*2, f8_ymax*2)
    imgf8 = screenshot.crop(region)

    region = (g8_xmin*2, g8_ymin*2, g8_xmax*2, g8_ymax*2)
    imgg8 = screenshot.crop(region)

    region = (h8_xmin*2, h8_ymin*2, h8_xmax*2, h8_ymax*2)
    imgh8 = screenshot.crop(region)    

    if (image_in_range(LS, imga1) is not None or image_in_range(DS, imga1) is not None):
        a1 = 1

    elif (image_in_range(WPLS, imga1) is not None or image_in_range(WPDS, imga1) is not None):
        a1 = 'P'

    elif (image_in_range(BPLS, imga1) is not None or image_in_range(BPDS, imga1) is not None):
        a1 = 'p'

    elif (image_in_range(WBLS, imga1) is not None or image_in_range(WBDS, imga1) is not None):
        a1 = 'B'

    elif (image_in_range(BBLS, imga1) is not None or image_in_range(BBDS, imga1) is not None):
        a1 = 'b'

    elif (image_in_range(WNLS, imga1) is not None or image_in_range(WNDS, imga1) is not None):
        a1 = 'N'

    elif (image_in_range(BNLS, imga1) is not None or image_in_range(BNDS, imga1) is not None):
        a1 = 'n'

    elif (image_in_range(WRLS, imga1) is not None or image_in_range(WRDS, imga1) is not None):
        a1 = 'R'

    elif (image_in_range(BRLS, imga1) is not None or image_in_range(BRDS, imga1) is not None):
        a1 = 'r'

    elif (image_in_range(WQLS, imga1) is not None or image_in_range(WQDS, imga1) is not None):
        a1 = 'Q'

    elif (image_in_range(BQLS, imga1) is not None or image_in_range(BQDS, imga1) is not None):
        a1 = 'q'

    elif (image_in_range(WKLS, imga1) is not None or image_in_range(WKDS, imga1) is not None):
        a1 = 'K'

    elif (image_in_range(BKLS, imga1) is not None or image_in_range(BKDS, imga1) is not None):
        a1 = 'k'

    if (image_in_range(LS, imgb1) is not None or image_in_range(DS, imgb1) is not None):
        b1 = 1

    elif (image_in_range(WPLS, imgb1) is not None or image_in_range(WPDS, imgb1) is not None):
        b1 = 'P'

    elif (image_in_range(BPLS, imgb1) is not None or image_in_range(BPDS, imgb1) is not None):
        b1 = 'p'

    elif (image_in_range(WBLS, imgb1) is not None or image_in_range(WBDS, imgb1) is not None):
        b1 = 'B'

    elif (image_in_range(BBLS, imgb1) is not None or image_in_range(BBDS, imgb1) is not None):
        b1 = 'b'

    elif (image_in_range(WNLS, imgb1) is not None or image_in_range(WNDS, imgb1) is not None):
        b1 = 'N'

    elif (image_in_range(BNLS, imgb1) is not None or image_in_range(BNDS, imgb1) is not None):
        b1 = 'n'

    elif (image_in_range(WRLS, imgb1) is not None or image_in_range(WRDS, imgb1) is not None):
        b1 = 'R'

    elif (image_in_range(BRLS, imgb1) is not None or image_in_range(BRDS, imgb1) is not None):
        b1 = 'r'

    elif (image_in_range(WQLS, imgb1) is not None or image_in_range(WQDS, imgb1) is not None):
        b1 = 'Q'

    elif (image_in_range(BQLS, imgb1) is not None or image_in_range(BQDS, imgb1) is not None):
        b1 = 'q'

    elif (image_in_range(WKLS, imgb1) is not None or image_in_range(WKDS, imgb1) is not None):
        b1 = 'K'

    elif (image_in_range(BKLS, imgb1) is not None or image_in_range(BKDS, imgb1) is not None):
        b1 = 'k'

    if (image_in_range(LS, imgc1) is not None or image_in_range(DS, imgc1) is not None):
        c1 = 1

    elif (image_in_range(WPLS, imgc1) is not None or image_in_range(WPDS, imgc1) is not None):
        c1 = 'P'

    elif (image_in_range(BPLS, imgc1) is not None or image_in_range(BPDS, imgc1) is not None):
        c1 = 'p'

    elif (image_in_range(WBLS, imgc1) is not None or image_in_range(WBDS, imgc1) is not None):
        c1 = 'B'

    elif (image_in_range(BBLS, imgc1) is not None or image_in_range(BBDS, imgc1) is not None):
        c1 = 'b'

    elif (image_in_range(WNLS, imgc1) is not None or image_in_range(WNDS, imgc1) is not None):
        c1 = 'N'

    elif (image_in_range(BNLS, imgc1) is not None or image_in_range(BNDS, imgc1) is not None):
        c1 = 'n'

    elif (image_in_range(WRLS, imgc1) is not None or image_in_range(WRDS, imgc1) is not None):
        c1 = 'R'

    elif (image_in_range(BRLS, imgc1) is not None or image_in_range(BRDS, imgc1) is not None):
        c1 = 'r'

    elif (image_in_range(WQLS, imgc1) is not None or image_in_range(WQDS, imgc1) is not None):
        c1 = 'Q'

    elif (image_in_range(BQLS, imgc1) is not None or image_in_range(BQDS, imgc1) is not None):
        c1 = 'q'

    elif (image_in_range(WKLS, imgc1) is not None or image_in_range(WKDS, imgc1) is not None):
        c1 = 'K'

    elif (image_in_range(BKLS, imgc1) is not None or image_in_range(BKDS, imgc1) is not None):
        c1 = 'k'

    if (image_in_range(LS, imgd1) is not None or image_in_range(DS, imgd1) is not None):
        d1 = 1

    elif (image_in_range(WPLS, imgd1) is not None or image_in_range(WPDS, imgd1) is not None):
        d1 = 'P'

    elif (image_in_range(BPLS, imgd1) is not None or image_in_range(BPDS, imgd1) is not None):
        d1 = 'p'

    elif (image_in_range(WBLS, imgd1) is not None or image_in_range(WBDS, imgd1) is not None):
        d1 = 'B'

    elif (image_in_range(BBLS, imgd1) is not None or image_in_range(BBDS, imgd1) is not None):
        d1 = 'b'

    elif (image_in_range(WNLS, imgd1) is not None or image_in_range(WNDS, imgd1) is not None):
        d1 = 'N'

    elif (image_in_range(BNLS, imgd1) is not None or image_in_range(BNDS, imgd1) is not None):
        d1 = 'n'

    elif (image_in_range(WRLS, imgd1) is not None or image_in_range(WRDS, imgd1) is not None):
        d1 = 'R'

    elif (image_in_range(BRLS, imgd1) is not None or image_in_range(BRDS, imgd1) is not None):
        d1 = 'r'

    elif (image_in_range(WQLS, imgd1) is not None or image_in_range(WQDS, imgd1) is not None):
        d1 = 'Q'

    elif (image_in_range(BQLS, imgd1) is not None or image_in_range(BQDS, imgd1) is not None):
        d1 = 'q'

    elif (image_in_range(WKLS, imgd1) is not None or image_in_range(WKDS, imgd1) is not None):
        d1 = 'K'

    elif (image_in_range(BKLS, imgd1) is not None or image_in_range(BKDS, imgd1) is not None):
        d1 = 'k'

    if (image_in_range(LS, imge1) is not None or image_in_range(DS, imge1) is not None):
        e1 = 1

    elif (image_in_range(WPLS, imge1) is not None or image_in_range(WPDS, imge1) is not None):
        e1 = 'P'

    elif (image_in_range(BPLS, imge1) is not None or image_in_range(BPDS, imge1) is not None):
        e1 = 'p'

    elif (image_in_range(WBLS, imge1) is not None or image_in_range(WBDS, imge1) is not None):
        e1 = 'B'

    elif (image_in_range(BBLS, imge1) is not None or image_in_range(BBDS, imge1) is not None):
        e1 = 'b'

    elif (image_in_range(WNLS, imge1) is not None or image_in_range(WNDS, imge1) is not None):
        e1 = 'N'

    elif (image_in_range(BNLS, imge1) is not None or image_in_range(BNDS, imge1) is not None):
        e1 = 'n'

    elif (image_in_range(WRLS, imge1) is not None or image_in_range(WRDS, imge1) is not None):
        e1 = 'R'

    elif (image_in_range(BRLS, imge1) is not None or image_in_range(BRDS, imge1) is not None):
        e1 = 'r'

    elif (image_in_range(WQLS, imge1) is not None or image_in_range(WQDS, imge1) is not None):
        e1 = 'Q'

    elif (image_in_range(BQLS, imge1) is not None or image_in_range(BQDS, imge1) is not None):
        e1 = 'q'

    elif (image_in_range(WKLS, imge1) is not None or image_in_range(WKDS, imge1) is not None):
        e1 = 'K'

    elif (image_in_range(BKLS, imge1) is not None or image_in_range(BKDS, imge1) is not None):
        e1 = 'k'

    if (image_in_range(LS, imgf1) is not None or image_in_range(DS, imgf1) is not None):
        f1 = 1

    elif (image_in_range(WPLS, imgf1) is not None or image_in_range(WPDS, imgf1) is not None):
        f1 = 'P'

    elif (image_in_range(BPLS, imgf1) is not None or image_in_range(BPDS, imgf1) is not None):
        f1 = 'p'

    elif (image_in_range(WBLS, imgf1) is not None or image_in_range(WBDS, imgf1) is not None):
        f1 = 'B'

    elif (image_in_range(BBLS, imgf1) is not None or image_in_range(BBDS, imgf1) is not None):
        f1 = 'b'

    elif (image_in_range(WNLS, imgf1) is not None or image_in_range(WNDS, imgf1) is not None):
        f1 = 'N'

    elif (image_in_range(BNLS, imgf1) is not None or image_in_range(BNDS, imgf1) is not None):
        f1 = 'n'

    elif (image_in_range(WRLS, imgf1) is not None or image_in_range(WRDS, imgf1) is not None):
        f1 = 'R'

    elif (image_in_range(BRLS, imgf1) is not None or image_in_range(BRDS, imgf1) is not None):
        f1 = 'r'

    elif (image_in_range(WQLS, imgf1) is not None or image_in_range(WQDS, imgf1) is not None):
        f1 = 'Q'

    elif (image_in_range(BQLS, imgf1) is not None or image_in_range(BQDS, imgf1) is not None):
        f1 = 'q'

    elif (image_in_range(WKLS, imgf1) is not None or image_in_range(WKDS, imgf1) is not None):
        f1 = 'K'

    elif (image_in_range(BKLS, imgf1) is not None or image_in_range(BKDS, imgf1) is not None):
        f1 = 'k'

    if (image_in_range(LS, imgg1) is not None or image_in_range(DS, imgg1) is not None):
        g1 = 1

    elif (image_in_range(WPLS, imgg1) is not None or image_in_range(WPDS, imgg1) is not None):
        g1 = 'P'

    elif (image_in_range(BPLS, imgg1) is not None or image_in_range(BPDS, imgg1) is not None):
        g1 = 'p'

    elif (image_in_range(WBLS, imgg1) is not None or image_in_range(WBDS, imgg1) is not None):
        g1 = 'B'

    elif (image_in_range(BBLS, imgg1) is not None or image_in_range(BBDS, imgg1) is not None):
        g1 = 'b'

    elif (image_in_range(WNLS, imgg1) is not None or image_in_range(WNDS, imgg1) is not None):
        g1 = 'N'

    elif (image_in_range(BNLS, imgg1) is not None or image_in_range(BNDS, imgg1) is not None):
        g1 = 'n'

    elif (image_in_range(WRLS, imgg1) is not None or image_in_range(WRDS, imgg1) is not None):
        g1 = 'R'

    elif (image_in_range(BRLS, imgg1) is not None or image_in_range(BRDS, imgg1) is not None):
        g1 = 'r'

    elif (image_in_range(WQLS, imgg1) is not None or image_in_range(WQDS, imgg1) is not None):
        g1 = 'Q'

    elif (image_in_range(BQLS, imgg1) is not None or image_in_range(BQDS, imgg1) is not None):
        g1 = 'q'

    elif (image_in_range(WKLS, imgg1) is not None or image_in_range(WKDS, imgg1) is not None):
        g1 = 'K'

    elif (image_in_range(BKLS, imgg1) is not None or image_in_range(BKDS, imgg1) is not None):
        g1 = 'k'

    if (image_in_range(LS, imgh1) is not None or image_in_range(DS, imgh1) is not None):
        h1 = 1

    elif (image_in_range(WPLS, imgh1) is not None or image_in_range(WPDS, imgh1) is not None):
        h1 = 'P'

    elif (image_in_range(BPLS, imgh1) is not None or image_in_range(BPDS, imgh1) is not None):
        h1 = 'p'

    elif (image_in_range(WBLS, imgh1) is not None or image_in_range(WBDS, imgh1) is not None):
        h1 = 'B'

    elif (image_in_range(BBLS, imgh1) is not None or image_in_range(BBDS, imgh1) is not None):
        h1 = 'b'

    elif (image_in_range(WNLS, imgh1) is not None or image_in_range(WNDS, imgh1) is not None):
        h1 = 'N'

    elif (image_in_range(BNLS, imgh1) is not None or image_in_range(BNDS, imgh1) is not None):
        h1 = 'n'

    elif (image_in_range(WRLS, imgh1) is not None or image_in_range(WRDS, imgh1) is not None):
        h1 = 'R'

    elif (image_in_range(BRLS, imgh1) is not None or image_in_range(BRDS, imgh1) is not None):
        h1 = 'r'

    elif (image_in_range(WQLS, imgh1) is not None or image_in_range(WQDS, imgh1) is not None):
        h1 = 'Q'

    elif (image_in_range(BQLS, imgh1) is not None or image_in_range(BQDS, imgh1) is not None):
        h1 = 'q'

    elif (image_in_range(WKLS, imgh1) is not None or image_in_range(WKDS, imgh1) is not None):
        h1 = 'K'

    elif (image_in_range(BKLS, imgh1) is not None or image_in_range(BKDS, imgh1) is not None):
        h1 = 'k'

    if (image_in_range(LS, imga2) is not None or image_in_range(DS, imga2) is not None):
        a2 = 1

    elif (image_in_range(WPLS, imga2) is not None or image_in_range(WPDS, imga2) is not None):
        a2 = 'P'

    elif (image_in_range(BPLS, imga2) is not None or image_in_range(BPDS, imga2) is not None):
        a2 = 'p'

    elif (image_in_range(WBLS, imga2) is not None or image_in_range(WBDS, imga2) is not None):
        a2 = 'B'

    elif (image_in_range(BBLS, imga2) is not None or image_in_range(BBDS, imga2) is not None):
        a2 = 'b'

    elif (image_in_range(WNLS, imga2) is not None or image_in_range(WNDS, imga2) is not None):
        a2 = 'N'

    elif (image_in_range(BNLS, imga2) is not None or image_in_range(BNDS, imga2) is not None):
        a2 = 'n'

    elif (image_in_range(WRLS, imga2) is not None or image_in_range(WRDS, imga2) is not None):
        a2 = 'R'

    elif (image_in_range(BRLS, imga2) is not None or image_in_range(BRDS, imga2) is not None):
        a2 = 'r'

    elif (image_in_range(WQLS, imga2) is not None or image_in_range(WQDS, imga2) is not None):
        a2 = 'Q'

    elif (image_in_range(BQLS, imga2) is not None or image_in_range(BQDS, imga2) is not None):
        a2 = 'q'

    elif (image_in_range(WKLS, imga2) is not None or image_in_range(WKDS, imga2) is not None):
        a2 = 'K'

    elif (image_in_range(BKLS, imga2) is not None or image_in_range(BKDS, imga2) is not None):
        a2 = 'k'

    if (image_in_range(LS, imgb2) is not None or image_in_range(DS, imgb2) is not None):
        b2 = 1

    elif (image_in_range(WPLS, imgb2) is not None or image_in_range(WPDS, imgb2) is not None):
        b2 = 'P'

    elif (image_in_range(BPLS, imgb2) is not None or image_in_range(BPDS, imgb2) is not None):
        b2 = 'p'

    elif (image_in_range(WBLS, imgb2) is not None or image_in_range(WBDS, imgb2) is not None):
        b2 = 'B'

    elif (image_in_range(BBLS, imgb2) is not None or image_in_range(BBDS, imgb2) is not None):
        b2 = 'b'

    elif (image_in_range(WNLS, imgb2) is not None or image_in_range(WNDS, imgb2) is not None):
        b2 = 'N'

    elif (image_in_range(BNLS, imgb2) is not None or image_in_range(BNDS, imgb2) is not None):
        b2 = 'n'

    elif (image_in_range(WRLS, imgb2) is not None or image_in_range(WRDS, imgb2) is not None):
        b2 = 'R'

    elif (image_in_range(BRLS, imgb2) is not None or image_in_range(BRDS, imgb2) is not None):
        b2 = 'r'

    elif (image_in_range(WQLS, imgb2) is not None or image_in_range(WQDS, imgb2) is not None):
        b2 = 'Q'

    elif (image_in_range(BQLS, imgb2) is not None or image_in_range(BQDS, imgb2) is not None):
        b2 = 'q'

    elif (image_in_range(WKLS, imgb2) is not None or image_in_range(WKDS, imgb2) is not None):
        b2 = 'K'

    elif (image_in_range(BKLS, imgb2) is not None or image_in_range(BKDS, imgb2) is not None):
        b2 = 'k'

    if (image_in_range(LS, imgc2) is not None or image_in_range(DS, imgc2) is not None):
        c2 = 1

    elif (image_in_range(WPLS, imgc2) is not None or image_in_range(WPDS, imgc2) is not None):
        c2 = 'P'

    elif (image_in_range(BPLS, imgc2) is not None or image_in_range(BPDS, imgc2) is not None):
        c2 = 'p'

    elif (image_in_range(WBLS, imgc2) is not None or image_in_range(WBDS, imgc2) is not None):
        c2 = 'B'

    elif (image_in_range(BBLS, imgc2) is not None or image_in_range(BBDS, imgc2) is not None):
        c2 = 'b'

    elif (image_in_range(WNLS, imgc2) is not None or image_in_range(WNDS, imgc2) is not None):
        c2 = 'N'

    elif (image_in_range(BNLS, imgc2) is not None or image_in_range(BNDS, imgc2) is not None):
        c2 = 'n'

    elif (image_in_range(WRLS, imgc2) is not None or image_in_range(WRDS, imgc2) is not None):
        c2 = 'R'

    elif (image_in_range(BRLS, imgc2) is not None or image_in_range(BRDS, imgc2) is not None):
        c2 = 'r'

    elif (image_in_range(WQLS, imgc2) is not None or image_in_range(WQDS, imgc2) is not None):
        c2 = 'Q'

    elif (image_in_range(BQLS, imgc2) is not None or image_in_range(BQDS, imgc2) is not None):
        c2 = 'q'

    elif (image_in_range(WKLS, imgc2) is not None or image_in_range(WKDS, imgc2) is not None):
        c2 = 'K'

    elif (image_in_range(BKLS, imgc2) is not None or image_in_range(BKDS, imgc2) is not None):
        c2 = 'k'

    if (image_in_range(LS, imgd2) is not None or image_in_range(DS, imgd2) is not None):
        d2 = 1

    elif (image_in_range(WPLS, imgd2) is not None or image_in_range(WPDS, imgd2) is not None):
        d2 = 'P'

    elif (image_in_range(BPLS, imgd2) is not None or image_in_range(BPDS, imgd2) is not None):
        d2 = 'p'

    elif (image_in_range(WBLS, imgd2) is not None or image_in_range(WBDS, imgd2) is not None):
        d2 = 'B'

    elif (image_in_range(BBLS, imgd2) is not None or image_in_range(BBDS, imgd2) is not None):
        d2 = 'b'

    elif (image_in_range(WNLS, imgd2) is not None or image_in_range(WNDS, imgd2) is not None):
        d2 = 'N'

    elif (image_in_range(BNLS, imgd2) is not None or image_in_range(BNDS, imgd2) is not None):
        d2 = 'n'

    elif (image_in_range(WRLS, imgd2) is not None or image_in_range(WRDS, imgd2) is not None):
        d2 = 'R'

    elif (image_in_range(BRLS, imgd2) is not None or image_in_range(BRDS, imgd2) is not None):
        d2 = 'r'

    elif (image_in_range(WQLS, imgd2) is not None or image_in_range(WQDS, imgd2) is not None):
        d2 = 'Q'

    elif (image_in_range(BQLS, imgd2) is not None or image_in_range(BQDS, imgd2) is not None):
        d2 = 'q'

    elif (image_in_range(WKLS, imgd2) is not None or image_in_range(WKDS, imgd2) is not None):
        d2 = 'K'

    elif (image_in_range(BKLS, imgd2) is not None or image_in_range(BKDS, imgd2) is not None):
        d2 = 'k'

    if (image_in_range(LS, imge2) is not None or image_in_range(DS, imge2) is not None):
        e2 = 1

    elif (image_in_range(WPLS, imge2) is not None or image_in_range(WPDS, imge2) is not None):
        e2 = 'P'

    elif (image_in_range(BPLS, imge2) is not None or image_in_range(BPDS, imge2) is not None):
        e2 = 'p'

    elif (image_in_range(WBLS, imge2) is not None or image_in_range(WBDS, imge2) is not None):
        e2 = 'B'

    elif (image_in_range(BBLS, imge2) is not None or image_in_range(BBDS, imge2) is not None):
        e2 = 'b'

    elif (image_in_range(WNLS, imge2) is not None or image_in_range(WNDS, imge2) is not None):
        e2 = 'N'

    elif (image_in_range(BNLS, imge2) is not None or image_in_range(BNDS, imge2) is not None):
        e2 = 'n'

    elif (image_in_range(WRLS, imge2) is not None or image_in_range(WRDS, imge2) is not None):
        e2 = 'R'

    elif (image_in_range(BRLS, imge2) is not None or image_in_range(BRDS, imge2) is not None):
        e2 = 'r'

    elif (image_in_range(WQLS, imge2) is not None or image_in_range(WQDS, imge2) is not None):
        e2 = 'Q'

    elif (image_in_range(BQLS, imge2) is not None or image_in_range(BQDS, imge2) is not None):
        e2 = 'q'

    elif (image_in_range(WKLS, imge2) is not None or image_in_range(WKDS, imge2) is not None):
        e2 = 'K'

    elif (image_in_range(BKLS, imge2) is not None or image_in_range(BKDS, imge2) is not None):
        e2 = 'k'

    if (image_in_range(LS, imgf2) is not None or image_in_range(DS, imgf2) is not None):
        f2 = 1

    elif (image_in_range(WPLS, imgf2) is not None or image_in_range(WPDS, imgf2) is not None):
        f2 = 'P'

    elif (image_in_range(BPLS, imgf2) is not None or image_in_range(BPDS, imgf2) is not None):
        f2 = 'p'

    elif (image_in_range(WBLS, imgf2) is not None or image_in_range(WBDS, imgf2) is not None):
        f2 = 'B'

    elif (image_in_range(BBLS, imgf2) is not None or image_in_range(BBDS, imgf2) is not None):
        f2 = 'b'

    elif (image_in_range(WNLS, imgf2) is not None or image_in_range(WNDS, imgf2) is not None):
        f2 = 'N'

    elif (image_in_range(BNLS, imgf2) is not None or image_in_range(BNDS, imgf2) is not None):
        f2 = 'n'

    elif (image_in_range(WRLS, imgf2) is not None or image_in_range(WRDS, imgf2) is not None):
        f2 = 'R'

    elif (image_in_range(BRLS, imgf2) is not None or image_in_range(BRDS, imgf2) is not None):
        f2 = 'r'

    elif (image_in_range(WQLS, imgf2) is not None or image_in_range(WQDS, imgf2) is not None):
        f2 = 'Q'

    elif (image_in_range(BQLS, imgf2) is not None or image_in_range(BQDS, imgf2) is not None):
        f2 = 'q'

    elif (image_in_range(WKLS, imgf2) is not None or image_in_range(WKDS, imgf2) is not None):
        f2 = 'K'

    elif (image_in_range(BKLS, imgf2) is not None or image_in_range(BKDS, imgf2) is not None):
        f2 = 'k'

    if (image_in_range(LS, imgg2) is not None or image_in_range(DS, imgg2) is not None):
        g2 = 1

    elif (image_in_range(WPLS, imgg2) is not None or image_in_range(WPDS, imgg2) is not None):
        g2 = 'P'

    elif (image_in_range(BPLS, imgg2) is not None or image_in_range(BPDS, imgg2) is not None):
        g2 = 'p'

    elif (image_in_range(WBLS, imgg2) is not None or image_in_range(WBDS, imgg2) is not None):
        g2 = 'B'

    elif (image_in_range(BBLS, imgg2) is not None or image_in_range(BBDS, imgg2) is not None):
        g2 = 'b'

    elif (image_in_range(WNLS, imgg2) is not None or image_in_range(WNDS, imgg2) is not None):
        g2 = 'N'

    elif (image_in_range(BNLS, imgg2) is not None or image_in_range(BNDS, imgg2) is not None):
        g2 = 'n'

    elif (image_in_range(WRLS, imgg2) is not None or image_in_range(WRDS, imgg2) is not None):
        g2 = 'R'

    elif (image_in_range(BRLS, imgg2) is not None or image_in_range(BRDS, imgg2) is not None):
        g2 = 'r'

    elif (image_in_range(WQLS, imgg2) is not None or image_in_range(WQDS, imgg2) is not None):
        g2 = 'Q'

    elif (image_in_range(BQLS, imgg2) is not None or image_in_range(BQDS, imgg2) is not None):
        g2 = 'q'

    elif (image_in_range(WKLS, imgg2) is not None or image_in_range(WKDS, imgg2) is not None):
        g2 = 'K'

    elif (image_in_range(BKLS, imgg2) is not None or image_in_range(BKDS, imgg2) is not None):
        g2 = 'k'

    if (image_in_range(LS, imgh2) is not None or image_in_range(DS, imgh2) is not None):
        h2 = 1

    elif (image_in_range(WPLS, imgh2) is not None or image_in_range(WPDS, imgh2) is not None):
        h2 = 'P'

    elif (image_in_range(BPLS, imgh2) is not None or image_in_range(BPDS, imgh2) is not None):
        h2 = 'p'

    elif (image_in_range(WBLS, imgh2) is not None or image_in_range(WBDS, imgh2) is not None):
        h2 = 'B'

    elif (image_in_range(BBLS, imgh2) is not None or image_in_range(BBDS, imgh2) is not None):
        h2 = 'b'

    elif (image_in_range(WNLS, imgh2) is not None or image_in_range(WNDS, imgh2) is not None):
        h2 = 'N'

    elif (image_in_range(BNLS, imgh2) is not None or image_in_range(BNDS, imgh2) is not None):
        h2 = 'n'

    elif (image_in_range(WRLS, imgh2) is not None or image_in_range(WRDS, imgh2) is not None):
        h2 = 'R'

    elif (image_in_range(BRLS, imgh2) is not None or image_in_range(BRDS, imgh2) is not None):
        h2 = 'r'

    elif (image_in_range(WQLS, imgh2) is not None or image_in_range(WQDS, imgh2) is not None):
        h2 = 'Q'

    elif (image_in_range(BQLS, imgh2) is not None or image_in_range(BQDS, imgh2) is not None):
        h2 = 'q'

    elif (image_in_range(WKLS, imgh2) is not None or image_in_range(WKDS, imgh2) is not None):
        h2 = 'K'

    elif (image_in_range(BKLS, imgh2) is not None or image_in_range(BKDS, imgh2) is not None):
        h2 = 'k'

    if (image_in_range(LS, imga3) is not None or image_in_range(DS, imga3) is not None):
        a3 = 1

    elif (image_in_range(WPLS, imga3) is not None or image_in_range(WPDS, imga3) is not None):
        a3 = 'P'

    elif (image_in_range(BPLS, imga3) is not None or image_in_range(BPDS, imga3) is not None):
        a3 = 'p'

    elif (image_in_range(WBLS, imga3) is not None or image_in_range(WBDS, imga3) is not None):
        a3 = 'B'

    elif (image_in_range(BBLS, imga3) is not None or image_in_range(BBDS, imga3) is not None):
        a3 = 'b'

    elif (image_in_range(WNLS, imga3) is not None or image_in_range(WNDS, imga3) is not None):
        a3 = 'N'

    elif (image_in_range(BNLS, imga3) is not None or image_in_range(BNDS, imga3) is not None):
        a3 = 'n'

    elif (image_in_range(WRLS, imga3) is not None or image_in_range(WRDS, imga3) is not None):
        a3 = 'R'

    elif (image_in_range(BRLS, imga3) is not None or image_in_range(BRDS, imga3) is not None):
        a3 = 'r'

    elif (image_in_range(WQLS, imga3) is not None or image_in_range(WQDS, imga3) is not None):
        a3 = 'Q'

    elif (image_in_range(BQLS, imga3) is not None or image_in_range(BQDS, imga3) is not None):
        a3 = 'q'

    elif (image_in_range(WKLS, imga3) is not None or image_in_range(WKDS, imga3) is not None):
        a3 = 'K'

    elif (image_in_range(BKLS, imga3) is not None or image_in_range(BKDS, imga3) is not None):
        a3 = 'k'

    if (image_in_range(LS, imgb3) is not None or image_in_range(DS, imgb3) is not None):
        b3 = 1

    elif (image_in_range(WPLS, imgb3) is not None or image_in_range(WPDS, imgb3) is not None):
        b3 = 'P'

    elif (image_in_range(BPLS, imgb3) is not None or image_in_range(BPDS, imgb3) is not None):
        b3 = 'p'

    elif (image_in_range(WBLS, imgb3) is not None or image_in_range(WBDS, imgb3) is not None):
        b3 = 'B'

    elif (image_in_range(BBLS, imgb3) is not None or image_in_range(BBDS, imgb3) is not None):
        b3 = 'b'

    elif (image_in_range(WNLS, imgb3) is not None or image_in_range(WNDS, imgb3) is not None):
        b3 = 'N'

    elif (image_in_range(BNLS, imgb3) is not None or image_in_range(BNDS, imgb3) is not None):
        b3 = 'n'

    elif (image_in_range(WRLS, imgb3) is not None or image_in_range(WRDS, imgb3) is not None):
        b3 = 'R'

    elif (image_in_range(BRLS, imgb3) is not None or image_in_range(BRDS, imgb3) is not None):
        b3 = 'r'

    elif (image_in_range(WQLS, imgb3) is not None or image_in_range(WQDS, imgb3) is not None):
        b3 = 'Q'

    elif (image_in_range(BQLS, imgb3) is not None or image_in_range(BQDS, imgb3) is not None):
        b3 = 'q'

    elif (image_in_range(WKLS, imgb3) is not None or image_in_range(WKDS, imgb3) is not None):
        b3 = 'K'

    elif (image_in_range(BKLS, imgb3) is not None or image_in_range(BKDS, imgb3) is not None):
        b3 = 'k'

    if (image_in_range(LS, imgc3) is not None or image_in_range(DS, imgc3) is not None):
        c3 = 1

    elif (image_in_range(WPLS, imgc3) is not None or image_in_range(WPDS, imgc3) is not None):
        c3 = 'P'

    elif (image_in_range(BPLS, imgc3) is not None or image_in_range(BPDS, imgc3) is not None):
        c3 = 'p'

    elif (image_in_range(WBLS, imgc3) is not None or image_in_range(WBDS, imgc3) is not None):
        c3 = 'B'

    elif (image_in_range(BBLS, imgc3) is not None or image_in_range(BBDS, imgc3) is not None):
        c3 = 'b'

    elif (image_in_range(WNLS, imgc3) is not None or image_in_range(WNDS, imgc3) is not None):
        c3 = 'N'

    elif (image_in_range(BNLS, imgc3) is not None or image_in_range(BNDS, imgc3) is not None):
        c3 = 'n'

    elif (image_in_range(WRLS, imgc3) is not None or image_in_range(WRDS, imgc3) is not None):
        c3 = 'R'

    elif (image_in_range(BRLS, imgc3) is not None or image_in_range(BRDS, imgc3) is not None):
        c3 = 'r'

    elif (image_in_range(WQLS, imgc3) is not None or image_in_range(WQDS, imgc3) is not None):
        c3 = 'Q'

    elif (image_in_range(BQLS, imgc3) is not None or image_in_range(BQDS, imgc3) is not None):
        c3 = 'q'

    elif (image_in_range(WKLS, imgc3) is not None or image_in_range(WKDS, imgc3) is not None):
        c3 = 'K'

    elif (image_in_range(BKLS, imgc3) is not None or image_in_range(BKDS, imgc3) is not None):
        c3 = 'k'

    if (image_in_range(LS, imgd3) is not None or image_in_range(DS, imgd3) is not None):
        d3 = 1

    elif (image_in_range(WPLS, imgd3) is not None or image_in_range(WPDS, imgd3) is not None):
        d3 = 'P'

    elif (image_in_range(BPLS, imgd3) is not None or image_in_range(BPDS, imgd3) is not None):
        d3 = 'p'

    elif (image_in_range(WBLS, imgd3) is not None or image_in_range(WBDS, imgd3) is not None):
        d3 = 'B'

    elif (image_in_range(BBLS, imgd3) is not None or image_in_range(BBDS, imgd3) is not None):
        d3 = 'b'

    elif (image_in_range(WNLS, imgd3) is not None or image_in_range(WNDS, imgd3) is not None):
        d3 = 'N'

    elif (image_in_range(BNLS, imgd3) is not None or image_in_range(BNDS, imgd3) is not None):
        d3 = 'n'

    elif (image_in_range(WRLS, imgd3) is not None or image_in_range(WRDS, imgd3) is not None):
        d3 = 'R'

    elif (image_in_range(BRLS, imgd3) is not None or image_in_range(BRDS, imgd3) is not None):
        d3 = 'r'

    elif (image_in_range(WQLS, imgd3) is not None or image_in_range(WQDS, imgd3) is not None):
        d3 = 'Q'

    elif (image_in_range(BQLS, imgd3) is not None or image_in_range(BQDS, imgd3) is not None):
        d3 = 'q'

    elif (image_in_range(WKLS, imgd3) is not None or image_in_range(WKDS, imgd3) is not None):
        d3 = 'K'

    elif (image_in_range(BKLS, imgd3) is not None or image_in_range(BKDS, imgd3) is not None):
        d3 = 'k'

    if (image_in_range(LS, imge3) is not None or image_in_range(DS, imge3) is not None):
        e3 = 1

    elif (image_in_range(WPLS, imge3) is not None or image_in_range(WPDS, imge3) is not None):
        e3 = 'P'

    elif (image_in_range(BPLS, imge3) is not None or image_in_range(BPDS, imge3) is not None):
        e3 = 'p'

    elif (image_in_range(WBLS, imge3) is not None or image_in_range(WBDS, imge3) is not None):
        e3 = 'B'

    elif (image_in_range(BBLS, imge3) is not None or image_in_range(BBDS, imge3) is not None):
        e3 = 'b'

    elif (image_in_range(WNLS, imge3) is not None or image_in_range(WNDS, imge3) is not None):
        e3 = 'N'

    elif (image_in_range(BNLS, imge3) is not None or image_in_range(BNDS, imge3) is not None):
        e3 = 'n'

    elif (image_in_range(WRLS, imge3) is not None or image_in_range(WRDS, imge3) is not None):
        e3 = 'R'

    elif (image_in_range(BRLS, imge3) is not None or image_in_range(BRDS, imge3) is not None):
        e3 = 'r'

    elif (image_in_range(WQLS, imge3) is not None or image_in_range(WQDS, imge3) is not None):
        e3 = 'Q'

    elif (image_in_range(BQLS, imge3) is not None or image_in_range(BQDS, imge3) is not None):
        e3 = 'q'

    elif (image_in_range(WKLS, imge3) is not None or image_in_range(WKDS, imge3) is not None):
        e3 = 'K'

    elif (image_in_range(BKLS, imge3) is not None or image_in_range(BKDS, imge3) is not None):
        e3 = 'k'

    if (image_in_range(LS, imgf3) is not None or image_in_range(DS, imgf3) is not None):
        f3 = 1

    elif (image_in_range(WPLS, imgf3) is not None or image_in_range(WPDS, imgf3) is not None):
        f3 = 'P'

    elif (image_in_range(BPLS, imgf3) is not None or image_in_range(BPDS, imgf3) is not None):
        f3 = 'p'

    elif (image_in_range(WBLS, imgf3) is not None or image_in_range(WBDS, imgf3) is not None):
        f3 = 'B'

    elif (image_in_range(BBLS, imgf3) is not None or image_in_range(BBDS, imgf3) is not None):
        f3 = 'b'

    elif (image_in_range(WNLS, imgf3) is not None or image_in_range(WNDS, imgf3) is not None):
        f3 = 'N'

    elif (image_in_range(BNLS, imgf3) is not None or image_in_range(BNDS, imgf3) is not None):
        f3 = 'n'

    elif (image_in_range(WRLS, imgf3) is not None or image_in_range(WRDS, imgf3) is not None):
        f3 = 'R'

    elif (image_in_range(BRLS, imgf3) is not None or image_in_range(BRDS, imgf3) is not None):
        f3 = 'r'

    elif (image_in_range(WQLS, imgf3) is not None or image_in_range(WQDS, imgf3) is not None):
        f3 = 'Q'

    elif (image_in_range(BQLS, imgf3) is not None or image_in_range(BQDS, imgf3) is not None):
        f3 = 'q'

    elif (image_in_range(WKLS, imgf3) is not None or image_in_range(WKDS, imgf3) is not None):
        f3 = 'K'

    elif (image_in_range(BKLS, imgf3) is not None or image_in_range(BKDS, imgf3) is not None):
        f3 = 'k'

    if (image_in_range(LS, imgg3) is not None or image_in_range(DS, imgg3) is not None):
        g3 = 1

    elif (image_in_range(WPLS, imgg3) is not None or image_in_range(WPDS, imgg3) is not None):
        g3 = 'P'

    elif (image_in_range(BPLS, imgg3) is not None or image_in_range(BPDS, imgg3) is not None):
        g3 = 'p'

    elif (image_in_range(WBLS, imgg3) is not None or image_in_range(WBDS, imgg3) is not None):
        g3 = 'B'

    elif (image_in_range(BBLS, imgg3) is not None or image_in_range(BBDS, imgg3) is not None):
        g3 = 'b'

    elif (image_in_range(WNLS, imgg3) is not None or image_in_range(WNDS, imgg3) is not None):
        g3 = 'N'

    elif (image_in_range(BNLS, imgg3) is not None or image_in_range(BNDS, imgg3) is not None):
        g3 = 'n'

    elif (image_in_range(WRLS, imgg3) is not None or image_in_range(WRDS, imgg3) is not None):
        g3 = 'R'

    elif (image_in_range(BRLS, imgg3) is not None or image_in_range(BRDS, imgg3) is not None):
        g3 = 'r'

    elif (image_in_range(WQLS, imgg3) is not None or image_in_range(WQDS, imgg3) is not None):
        g3 = 'Q'

    elif (image_in_range(BQLS, imgg3) is not None or image_in_range(BQDS, imgg3) is not None):
        g3 = 'q'

    elif (image_in_range(WKLS, imgg3) is not None or image_in_range(WKDS, imgg3) is not None):
        g3 = 'K'

    elif (image_in_range(BKLS, imgg3) is not None or image_in_range(BKDS, imgg3) is not None):
        g3 = 'k'

    if (image_in_range(LS, imgh3) is not None or image_in_range(DS, imgh3) is not None):
        h3 = 1

    elif (image_in_range(WPLS, imgh3) is not None or image_in_range(WPDS, imgh3) is not None):
        h3 = 'P'

    elif (image_in_range(BPLS, imgh3) is not None or image_in_range(BPDS, imgh3) is not None):
        h3 = 'p'

    elif (image_in_range(WBLS, imgh3) is not None or image_in_range(WBDS, imgh3) is not None):
        h3 = 'B'

    elif (image_in_range(BBLS, imgh3) is not None or image_in_range(BBDS, imgh3) is not None):
        h3 = 'b'

    elif (image_in_range(WNLS, imgh3) is not None or image_in_range(WNDS, imgh3) is not None):
        h3 = 'N'

    elif (image_in_range(BNLS, imgh3) is not None or image_in_range(BNDS, imgh3) is not None):
        h3 = 'n'

    elif (image_in_range(WRLS, imgh3) is not None or image_in_range(WRDS, imgh3) is not None):
        h3 = 'R'

    elif (image_in_range(BRLS, imgh3) is not None or image_in_range(BRDS, imgh3) is not None):
        h3 = 'r'

    elif (image_in_range(WQLS, imgh3) is not None or image_in_range(WQDS, imgh3) is not None):
        h3 = 'Q'

    elif (image_in_range(BQLS, imgh3) is not None or image_in_range(BQDS, imgh3) is not None):
        h3 = 'q'

    elif (image_in_range(WKLS, imgh3) is not None or image_in_range(WKDS, imgh3) is not None):
        h3 = 'K'

    elif (image_in_range(BKLS, imgh3) is not None or image_in_range(BKDS, imgh3) is not None):
        h3 = 'k'

    if (image_in_range(LS, imga4) is not None or image_in_range(DS, imga4) is not None):
        a4 = 1

    elif (image_in_range(WPLS, imga4) is not None or image_in_range(WPDS, imga4) is not None):
        a4 = 'P'

    elif (image_in_range(BPLS, imga4) is not None or image_in_range(BPDS, imga4) is not None):
        a4 = 'p'

    elif (image_in_range(WBLS, imga4) is not None or image_in_range(WBDS, imga4) is not None):
        a4 = 'B'

    elif (image_in_range(BBLS, imga4) is not None or image_in_range(BBDS, imga4) is not None):
        a4 = 'b'

    elif (image_in_range(WNLS, imga4) is not None or image_in_range(WNDS, imga4) is not None):
        a4 = 'N'

    elif (image_in_range(BNLS, imga4) is not None or image_in_range(BNDS, imga4) is not None):
        a4 = 'n'

    elif (image_in_range(WRLS, imga4) is not None or image_in_range(WRDS, imga4) is not None):
        a4 = 'R'

    elif (image_in_range(BRLS, imga4) is not None or image_in_range(BRDS, imga4) is not None):
        a4 = 'r'

    elif (image_in_range(WQLS, imga4) is not None or image_in_range(WQDS, imga4) is not None):
        a4 = 'Q'

    elif (image_in_range(BQLS, imga4) is not None or image_in_range(BQDS, imga4) is not None):
        a4 = 'q'

    elif (image_in_range(WKLS, imga4) is not None or image_in_range(WKDS, imga4) is not None):
        a4 = 'K'

    elif (image_in_range(BKLS, imga4) is not None or image_in_range(BKDS, imga4) is not None):
        a4 = 'k'

    if (image_in_range(LS, imgb4) is not None or image_in_range(DS, imgb4) is not None):
        b4 = 1

    elif (image_in_range(WPLS, imgb4) is not None or image_in_range(WPDS, imgb4) is not None):
        b4 = 'P'

    elif (image_in_range(BPLS, imgb4) is not None or image_in_range(BPDS, imgb4) is not None):
        b4 = 'p'

    elif (image_in_range(WBLS, imgb4) is not None or image_in_range(WBDS, imgb4) is not None):
        b4 = 'B'

    elif (image_in_range(BBLS, imgb4) is not None or image_in_range(BBDS, imgb4) is not None):
        b4 = 'b'

    elif (image_in_range(WNLS, imgb4) is not None or image_in_range(WNDS, imgb4) is not None):
        b4 = 'N'

    elif (image_in_range(BNLS, imgb4) is not None or image_in_range(BNDS, imgb4) is not None):
        b4 = 'n'

    elif (image_in_range(WRLS, imgb4) is not None or image_in_range(WRDS, imgb4) is not None):
        b4 = 'R'

    elif (image_in_range(BRLS, imgb4) is not None or image_in_range(BRDS, imgb4) is not None):
        b4 = 'r'

    elif (image_in_range(WQLS, imgb4) is not None or image_in_range(WQDS, imgb4) is not None):
        b4 = 'Q'

    elif (image_in_range(BQLS, imgb4) is not None or image_in_range(BQDS, imgb4) is not None):
        b4 = 'q'

    elif (image_in_range(WKLS, imgb4) is not None or image_in_range(WKDS, imgb4) is not None):
        b4 = 'K'

    elif (image_in_range(BKLS, imgb4) is not None or image_in_range(BKDS, imgb4) is not None):
        b4 = 'k'

    if (image_in_range(LS, imgc4) is not None or image_in_range(DS, imgc4) is not None):
        c4 = 1

    elif (image_in_range(WPLS, imgc4) is not None or image_in_range(WPDS, imgc4) is not None):
        c4 = 'P'

    elif (image_in_range(BPLS, imgc4) is not None or image_in_range(BPDS, imgc4) is not None):
        c4 = 'p'

    elif (image_in_range(WBLS, imgc4) is not None or image_in_range(WBDS, imgc4) is not None):
        c4 = 'B'

    elif (image_in_range(BBLS, imgc4) is not None or image_in_range(BBDS, imgc4) is not None):
        c4 = 'b'

    elif (image_in_range(WNLS, imgc4) is not None or image_in_range(WNDS, imgc4) is not None):
        c4 = 'N'

    elif (image_in_range(BNLS, imgc4) is not None or image_in_range(BNDS, imgc4) is not None):
        c4 = 'n'

    elif (image_in_range(WRLS, imgc4) is not None or image_in_range(WRDS, imgc4) is not None):
        c4 = 'R'

    elif (image_in_range(BRLS, imgc4) is not None or image_in_range(BRDS, imgc4) is not None):
        c4 = 'r'

    elif (image_in_range(WQLS, imgc4) is not None or image_in_range(WQDS, imgc4) is not None):
        c4 = 'Q'

    elif (image_in_range(BQLS, imgc4) is not None or image_in_range(BQDS, imgc4) is not None):
        c4 = 'q'

    elif (image_in_range(WKLS, imgc4) is not None or image_in_range(WKDS, imgc4) is not None):
        c4 = 'K'

    elif (image_in_range(BKLS, imgc4) is not None or image_in_range(BKDS, imgc4) is not None):
        c4 = 'k'

    if (image_in_range(LS, imgd4) is not None or image_in_range(DS, imgd4) is not None):
        d4 = 1

    elif (image_in_range(WPLS, imgd4) is not None or image_in_range(WPDS, imgd4) is not None):
        d4 = 'P'

    elif (image_in_range(BPLS, imgd4) is not None or image_in_range(BPDS, imgd4) is not None):
        d4 = 'p'

    elif (image_in_range(WBLS, imgd4) is not None or image_in_range(WBDS, imgd4) is not None):
        d4 = 'B'

    elif (image_in_range(BBLS, imgd4) is not None or image_in_range(BBDS, imgd4) is not None):
        d4 = 'b'

    elif (image_in_range(WNLS, imgd4) is not None or image_in_range(WNDS, imgd4) is not None):
        d4 = 'N'

    elif (image_in_range(BNLS, imgd4) is not None or image_in_range(BNDS, imgd4) is not None):
        d4 = 'n'

    elif (image_in_range(WRLS, imgd4) is not None or image_in_range(WRDS, imgd4) is not None):
        d4 = 'R'

    elif (image_in_range(BRLS, imgd4) is not None or image_in_range(BRDS, imgd4) is not None):
        d4 = 'r'

    elif (image_in_range(WQLS, imgd4) is not None or image_in_range(WQDS, imgd4) is not None):
        d4 = 'Q'

    elif (image_in_range(BQLS, imgd4) is not None or image_in_range(BQDS, imgd4) is not None):
        d4 = 'q'

    elif (image_in_range(WKLS, imgd4) is not None or image_in_range(WKDS, imgd4) is not None):
        d4 = 'K'

    elif (image_in_range(BKLS, imgd4) is not None or image_in_range(BKDS, imgd4) is not None):
        d4 = 'k'

    if (image_in_range(LS, imge4) is not None or image_in_range(DS, imge4) is not None):
        e4 = 1

    elif (image_in_range(WPLS, imge4) is not None or image_in_range(WPDS, imge4) is not None):
        e4 = 'P'

    elif (image_in_range(BPLS, imge4) is not None or image_in_range(BPDS, imge4) is not None):
        e4 = 'p'

    elif (image_in_range(WBLS, imge4) is not None or image_in_range(WBDS, imge4) is not None):
        e4 = 'B'

    elif (image_in_range(BBLS, imge4) is not None or image_in_range(BBDS, imge4) is not None):
        e4 = 'b'

    elif (image_in_range(WNLS, imge4) is not None or image_in_range(WNDS, imge4) is not None):
        e4 = 'N'

    elif (image_in_range(BNLS, imge4) is not None or image_in_range(BNDS, imge4) is not None):
        e4 = 'n'

    elif (image_in_range(WRLS, imge4) is not None or image_in_range(WRDS, imge4) is not None):
        e4 = 'R'

    elif (image_in_range(BRLS, imge4) is not None or image_in_range(BRDS, imge4) is not None):
        e4 = 'r'

    elif (image_in_range(WQLS, imge4) is not None or image_in_range(WQDS, imge4) is not None):
        e4 = 'Q'

    elif (image_in_range(BQLS, imge4) is not None or image_in_range(BQDS, imge4) is not None):
        e4 = 'q'

    elif (image_in_range(WKLS, imge4) is not None or image_in_range(WKDS, imge4) is not None):
        e4 = 'K'

    elif (image_in_range(BKLS, imge4) is not None or image_in_range(BKDS, imge4) is not None):
        e4 = 'k'

    if (image_in_range(LS, imgf4) is not None or image_in_range(DS, imgf4) is not None):
        f4 = 1

    elif (image_in_range(WPLS, imgf4) is not None or image_in_range(WPDS, imgf4) is not None):
        f4 = 'P'

    elif (image_in_range(BPLS, imgf4) is not None or image_in_range(BPDS, imgf4) is not None):
        f4 = 'p'

    elif (image_in_range(WBLS, imgf4) is not None or image_in_range(WBDS, imgf4) is not None):
        f4 = 'B'

    elif (image_in_range(BBLS, imgf4) is not None or image_in_range(BBDS, imgf4) is not None):
        f4 = 'b'

    elif (image_in_range(WNLS, imgf4) is not None or image_in_range(WNDS, imgf4) is not None):
        f4 = 'N'

    elif (image_in_range(BNLS, imgf4) is not None or image_in_range(BNDS, imgf4) is not None):
        f4 = 'n'

    elif (image_in_range(WRLS, imgf4) is not None or image_in_range(WRDS, imgf4) is not None):
        f4 = 'R'

    elif (image_in_range(BRLS, imgf4) is not None or image_in_range(BRDS, imgf4) is not None):
        f4 = 'r'

    elif (image_in_range(WQLS, imgf4) is not None or image_in_range(WQDS, imgf4) is not None):
        f4 = 'Q'

    elif (image_in_range(BQLS, imgf4) is not None or image_in_range(BQDS, imgf4) is not None):
        f4 = 'q'

    elif (image_in_range(WKLS, imgf4) is not None or image_in_range(WKDS, imgf4) is not None):
        f4 = 'K'

    elif (image_in_range(BKLS, imgf4) is not None or image_in_range(BKDS, imgf4) is not None):
        f4 = 'k'

    if (image_in_range(LS, imgg4) is not None or image_in_range(DS, imgg4) is not None):
        g4 = 1

    elif (image_in_range(WPLS, imgg4) is not None or image_in_range(WPDS, imgg4) is not None):
        g4 = 'P'

    elif (image_in_range(BPLS, imgg4) is not None or image_in_range(BPDS, imgg4) is not None):
        g4 = 'p'

    elif (image_in_range(WBLS, imgg4) is not None or image_in_range(WBDS, imgg4) is not None):
        g4 = 'B'

    elif (image_in_range(BBLS, imgg4) is not None or image_in_range(BBDS, imgg4) is not None):
        g4 = 'b'

    elif (image_in_range(WNLS, imgg4) is not None or image_in_range(WNDS, imgg4) is not None):
        g4 = 'N'

    elif (image_in_range(BNLS, imgg4) is not None or image_in_range(BNDS, imgg4) is not None):
        g4 = 'n'

    elif (image_in_range(WRLS, imgg4) is not None or image_in_range(WRDS, imgg4) is not None):
        g4 = 'R'

    elif (image_in_range(BRLS, imgg4) is not None or image_in_range(BRDS, imgg4) is not None):
        g4 = 'r'

    elif (image_in_range(WQLS, imgg4) is not None or image_in_range(WQDS, imgg4) is not None):
        g4 = 'Q'

    elif (image_in_range(BQLS, imgg4) is not None or image_in_range(BQDS, imgg4) is not None):
        g4 = 'q'

    elif (image_in_range(WKLS, imgg4) is not None or image_in_range(WKDS, imgg4) is not None):
        g4 = 'K'

    elif (image_in_range(BKLS, imgg4) is not None or image_in_range(BKDS, imgg4) is not None):
        g4 = 'k'

    if (image_in_range(LS, imgh4) is not None or image_in_range(DS, imgh4) is not None):
        h4 = 1

    elif (image_in_range(WPLS, imgh4) is not None or image_in_range(WPDS, imgh4) is not None):
        h4 = 'P'

    elif (image_in_range(BPLS, imgh4) is not None or image_in_range(BPDS, imgh4) is not None):
        h4 = 'p'

    elif (image_in_range(WBLS, imgh4) is not None or image_in_range(WBDS, imgh4) is not None):
        h4 = 'B'

    elif (image_in_range(BBLS, imgh4) is not None or image_in_range(BBDS, imgh4) is not None):
        h4 = 'b'

    elif (image_in_range(WNLS, imgh4) is not None or image_in_range(WNDS, imgh4) is not None):
        h4 = 'N'

    elif (image_in_range(BNLS, imgh4) is not None or image_in_range(BNDS, imgh4) is not None):
        h4 = 'n'

    elif (image_in_range(WRLS, imgh4) is not None or image_in_range(WRDS, imgh4) is not None):
        h4 = 'R'

    elif (image_in_range(BRLS, imgh4) is not None or image_in_range(BRDS, imgh4) is not None):
        h4 = 'r'

    elif (image_in_range(WQLS, imgh4) is not None or image_in_range(WQDS, imgh4) is not None):
        h4 = 'Q'

    elif (image_in_range(BQLS, imgh4) is not None or image_in_range(BQDS, imgh4) is not None):
        h4 = 'q'

    elif (image_in_range(WKLS, imgh4) is not None or image_in_range(WKDS, imgh4) is not None):
        h4 = 'K'

    elif (image_in_range(BKLS, imgh4) is not None or image_in_range(BKDS, imgh4) is not None):
        h4 = 'k'

    if (image_in_range(LS, imga5) is not None or image_in_range(DS, imga5) is not None):
        a5 = 1

    elif (image_in_range(WPLS, imga5) is not None or image_in_range(WPDS, imga5) is not None):
        a5 = 'P'

    elif (image_in_range(BPLS, imga5) is not None or image_in_range(BPDS, imga5) is not None):
        a5 = 'p'

    elif (image_in_range(WBLS, imga5) is not None or image_in_range(WBDS, imga5) is not None):
        a5 = 'B'

    elif (image_in_range(BBLS, imga5) is not None or image_in_range(BBDS, imga5) is not None):
        a5 = 'b'

    elif (image_in_range(WNLS, imga5) is not None or image_in_range(WNDS, imga5) is not None):
        a5 = 'N'

    elif (image_in_range(BNLS, imga5) is not None or image_in_range(BNDS, imga5) is not None):
        a5 = 'n'

    elif (image_in_range(WRLS, imga5) is not None or image_in_range(WRDS, imga5) is not None):
        a5 = 'R'

    elif (image_in_range(BRLS, imga5) is not None or image_in_range(BRDS, imga5) is not None):
        a5 = 'r'

    elif (image_in_range(WQLS, imga5) is not None or image_in_range(WQDS, imga5) is not None):
        a5 = 'Q'

    elif (image_in_range(BQLS, imga5) is not None or image_in_range(BQDS, imga5) is not None):
        a5 = 'q'

    elif (image_in_range(WKLS, imga5) is not None or image_in_range(WKDS, imga5) is not None):
        a5 = 'K'

    elif (image_in_range(BKLS, imga5) is not None or image_in_range(BKDS, imga5) is not None):
        a5 = 'k'

    if (image_in_range(LS, imgb5) is not None or image_in_range(DS, imgb5) is not None):
        b5 = 1

    elif (image_in_range(WPLS, imgb5) is not None or image_in_range(WPDS, imgb5) is not None):
        b5 = 'P'

    elif (image_in_range(BPLS, imgb5) is not None or image_in_range(BPDS, imgb5) is not None):
        b5 = 'p'

    elif (image_in_range(WBLS, imgb5) is not None or image_in_range(WBDS, imgb5) is not None):
        b5 = 'B'

    elif (image_in_range(BBLS, imgb5) is not None or image_in_range(BBDS, imgb5) is not None):
        b5 = 'b'

    elif (image_in_range(WNLS, imgb5) is not None or image_in_range(WNDS, imgb5) is not None):
        b5 = 'N'

    elif (image_in_range(BNLS, imgb5) is not None or image_in_range(BNDS, imgb5) is not None):
        b5 = 'n'

    elif (image_in_range(WRLS, imgb5) is not None or image_in_range(WRDS, imgb5) is not None):
        b5 = 'R'

    elif (image_in_range(BRLS, imgb5) is not None or image_in_range(BRDS, imgb5) is not None):
        b5 = 'r'

    elif (image_in_range(WQLS, imgb5) is not None or image_in_range(WQDS, imgb5) is not None):
        b5 = 'Q'

    elif (image_in_range(BQLS, imgb5) is not None or image_in_range(BQDS, imgb5) is not None):
        b5 = 'q'

    elif (image_in_range(WKLS, imgb5) is not None or image_in_range(WKDS, imgb5) is not None):
        b5 = 'K'

    elif (image_in_range(BKLS, imgb5) is not None or image_in_range(BKDS, imgb5) is not None):
        b5 = 'k'

    if (image_in_range(LS, imgc5) is not None or image_in_range(DS, imgc5) is not None):
        c5 = 1

    elif (image_in_range(WPLS, imgc5) is not None or image_in_range(WPDS, imgc5) is not None):
        c5 = 'P'

    elif (image_in_range(BPLS, imgc5) is not None or image_in_range(BPDS, imgc5) is not None):
        c5 = 'p'

    elif (image_in_range(WBLS, imgc5) is not None or image_in_range(WBDS, imgc5) is not None):
        c5 = 'B'

    elif (image_in_range(BBLS, imgc5) is not None or image_in_range(BBDS, imgc5) is not None):
        c5 = 'b'

    elif (image_in_range(WNLS, imgc5) is not None or image_in_range(WNDS, imgc5) is not None):
        c5 = 'N'

    elif (image_in_range(BNLS, imgc5) is not None or image_in_range(BNDS, imgc5) is not None):
        c5 = 'n'

    elif (image_in_range(WRLS, imgc5) is not None or image_in_range(WRDS, imgc5) is not None):
        c5 = 'R'

    elif (image_in_range(BRLS, imgc5) is not None or image_in_range(BRDS, imgc5) is not None):
        c5 = 'r'

    elif (image_in_range(WQLS, imgc5) is not None or image_in_range(WQDS, imgc5) is not None):
        c5 = 'Q'

    elif (image_in_range(BQLS, imgc5) is not None or image_in_range(BQDS, imgc5) is not None):
        c5 = 'q'

    elif (image_in_range(WKLS, imgc5) is not None or image_in_range(WKDS, imgc5) is not None):
        c5 = 'K'

    elif (image_in_range(BKLS, imgc5) is not None or image_in_range(BKDS, imgc5) is not None):
        c5 = 'k'

    if (image_in_range(LS, imgd5) is not None or image_in_range(DS, imgd5) is not None):
        d5 = 1

    elif (image_in_range(WPLS, imgd5) is not None or image_in_range(WPDS, imgd5) is not None):
        d5 = 'P'

    elif (image_in_range(BPLS, imgd5) is not None or image_in_range(BPDS, imgd5) is not None):
        d5 = 'p'

    elif (image_in_range(WBLS, imgd5) is not None or image_in_range(WBDS, imgd5) is not None):
        d5 = 'B'

    elif (image_in_range(BBLS, imgd5) is not None or image_in_range(BBDS, imgd5) is not None):
        d5 = 'b'

    elif (image_in_range(WNLS, imgd5) is not None or image_in_range(WNDS, imgd5) is not None):
        d5 = 'N'

    elif (image_in_range(BNLS, imgd5) is not None or image_in_range(BNDS, imgd5) is not None):
        d5 = 'n'

    elif (image_in_range(WRLS, imgd5) is not None or image_in_range(WRDS, imgd5) is not None):
        d5 = 'R'

    elif (image_in_range(BRLS, imgd5) is not None or image_in_range(BRDS, imgd5) is not None):
        d5 = 'r'

    elif (image_in_range(WQLS, imgd5) is not None or image_in_range(WQDS, imgd5) is not None):
        d5 = 'Q'

    elif (image_in_range(BQLS, imgd5) is not None or image_in_range(BQDS, imgd5) is not None):
        d5 = 'q'

    elif (image_in_range(WKLS, imgd5) is not None or image_in_range(WKDS, imgd5) is not None):
        d5 = 'K'

    elif (image_in_range(BKLS, imgd5) is not None or image_in_range(BKDS, imgd5) is not None):
        d5 = 'k'

    if (image_in_range(LS, imge5) is not None or image_in_range(DS, imge5) is not None):
        e5 = 1

    elif (image_in_range(WPLS, imge5) is not None or image_in_range(WPDS, imge5) is not None):
        e5 = 'P'

    elif (image_in_range(BPLS, imge5) is not None or image_in_range(BPDS, imge5) is not None):
        e5 = 'p'

    elif (image_in_range(WBLS, imge5) is not None or image_in_range(WBDS, imge5) is not None):
        e5 = 'B'

    elif (image_in_range(BBLS, imge5) is not None or image_in_range(BBDS, imge5) is not None):
        e5 = 'b'

    elif (image_in_range(WNLS, imge5) is not None or image_in_range(WNDS, imge5) is not None):
        e5 = 'N'

    elif (image_in_range(BNLS, imge5) is not None or image_in_range(BNDS, imge5) is not None):
        e5 = 'n'

    elif (image_in_range(WRLS, imge5) is not None or image_in_range(WRDS, imge5) is not None):
        e5 = 'R'

    elif (image_in_range(BRLS, imge5) is not None or image_in_range(BRDS, imge5) is not None):
        e5 = 'r'

    elif (image_in_range(WQLS, imge5) is not None or image_in_range(WQDS, imge5) is not None):
        e5 = 'Q'

    elif (image_in_range(BQLS, imge5) is not None or image_in_range(BQDS, imge5) is not None):
        e5 = 'q'

    elif (image_in_range(WKLS, imge5) is not None or image_in_range(WKDS, imge5) is not None):
        e5 = 'K'

    elif (image_in_range(BKLS, imge5) is not None or image_in_range(BKDS, imge5) is not None):
        e5 = 'k'

    if (image_in_range(LS, imgf5) is not None or image_in_range(DS, imgf5) is not None):
        f5 = 1

    elif (image_in_range(WPLS, imgf5) is not None or image_in_range(WPDS, imgf5) is not None):
        f5 = 'P'

    elif (image_in_range(BPLS, imgf5) is not None or image_in_range(BPDS, imgf5) is not None):
        f5 = 'p'

    elif (image_in_range(WBLS, imgf5) is not None or image_in_range(WBDS, imgf5) is not None):
        f5 = 'B'

    elif (image_in_range(BBLS, imgf5) is not None or image_in_range(BBDS, imgf5) is not None):
        f5 = 'b'

    elif (image_in_range(WNLS, imgf5) is not None or image_in_range(WNDS, imgf5) is not None):
        f5 = 'N'

    elif (image_in_range(BNLS, imgf5) is not None or image_in_range(BNDS, imgf5) is not None):
        f5 = 'n'

    elif (image_in_range(WRLS, imgf5) is not None or image_in_range(WRDS, imgf5) is not None):
        f5 = 'R'

    elif (image_in_range(BRLS, imgf5) is not None or image_in_range(BRDS, imgf5) is not None):
        f5 = 'r'

    elif (image_in_range(WQLS, imgf5) is not None or image_in_range(WQDS, imgf5) is not None):
        f5 = 'Q'

    elif (image_in_range(BQLS, imgf5) is not None or image_in_range(BQDS, imgf5) is not None):
        f5 = 'q'

    elif (image_in_range(WKLS, imgf5) is not None or image_in_range(WKDS, imgf5) is not None):
        f5 = 'K'

    elif (image_in_range(BKLS, imgf5) is not None or image_in_range(BKDS, imgf5) is not None):
        f5 = 'k'

    if (image_in_range(LS, imgg5) is not None or image_in_range(DS, imgg5) is not None):
        g5 = 1

    elif (image_in_range(WPLS, imgg5) is not None or image_in_range(WPDS, imgg5) is not None):
        g5 = 'P'

    elif (image_in_range(BPLS, imgg5) is not None or image_in_range(BPDS, imgg5) is not None):
        g5 = 'p'

    elif (image_in_range(WBLS, imgg5) is not None or image_in_range(WBDS, imgg5) is not None):
        g5 = 'B'

    elif (image_in_range(BBLS, imgg5) is not None or image_in_range(BBDS, imgg5) is not None):
        g5 = 'b'

    elif (image_in_range(WNLS, imgg5) is not None or image_in_range(WNDS, imgg5) is not None):
        g5 = 'N'

    elif (image_in_range(BNLS, imgg5) is not None or image_in_range(BNDS, imgg5) is not None):
        g5 = 'n'

    elif (image_in_range(WRLS, imgg5) is not None or image_in_range(WRDS, imgg5) is not None):
        g5 = 'R'

    elif (image_in_range(BRLS, imgg5) is not None or image_in_range(BRDS, imgg5) is not None):
        g5 = 'r'

    elif (image_in_range(WQLS, imgg5) is not None or image_in_range(WQDS, imgg5) is not None):
        g5 = 'Q'

    elif (image_in_range(BQLS, imgg5) is not None or image_in_range(BQDS, imgg5) is not None):
        g5 = 'q'

    elif (image_in_range(WKLS, imgg5) is not None or image_in_range(WKDS, imgg5) is not None):
        g5 = 'K'

    elif (image_in_range(BKLS, imgg5) is not None or image_in_range(BKDS, imgg5) is not None):
        g5 = 'k'

    if (image_in_range(LS, imgh5) is not None or image_in_range(DS, imgh5) is not None):
        h5 = 1

    elif (image_in_range(WPLS, imgh5) is not None or image_in_range(WPDS, imgh5) is not None):
        h5 = 'P'

    elif (image_in_range(BPLS, imgh5) is not None or image_in_range(BPDS, imgh5) is not None):
        h5 = 'p'

    elif (image_in_range(WBLS, imgh5) is not None or image_in_range(WBDS, imgh5) is not None):
        h5 = 'B'

    elif (image_in_range(BBLS, imgh5) is not None or image_in_range(BBDS, imgh5) is not None):
        h5 = 'b'

    elif (image_in_range(WNLS, imgh5) is not None or image_in_range(WNDS, imgh5) is not None):
        h5 = 'N'

    elif (image_in_range(BNLS, imgh5) is not None or image_in_range(BNDS, imgh5) is not None):
        h5 = 'n'

    elif (image_in_range(WRLS, imgh5) is not None or image_in_range(WRDS, imgh5) is not None):
        h5 = 'R'

    elif (image_in_range(BRLS, imgh5) is not None or image_in_range(BRDS, imgh5) is not None):
        h5 = 'r'

    elif (image_in_range(WQLS, imgh5) is not None or image_in_range(WQDS, imgh5) is not None):
        h5 = 'Q'

    elif (image_in_range(BQLS, imgh5) is not None or image_in_range(BQDS, imgh5) is not None):
        h5 = 'q'

    elif (image_in_range(WKLS, imgh5) is not None or image_in_range(WKDS, imgh5) is not None):
        h5 = 'K'

    elif (image_in_range(BKLS, imgh5) is not None or image_in_range(BKDS, imgh5) is not None):
        h5 = 'k'

    if (image_in_range(LS, imga6) is not None or image_in_range(DS, imga6) is not None):
        a6 = 1

    elif (image_in_range(WPLS, imga6) is not None or image_in_range(WPDS, imga6) is not None):
        a6 = 'P'

    elif (image_in_range(BPLS, imga6) is not None or image_in_range(BPDS, imga6) is not None):
        a6 = 'p'

    elif (image_in_range(WBLS, imga6) is not None or image_in_range(WBDS, imga6) is not None):
        a6 = 'B'

    elif (image_in_range(BBLS, imga6) is not None or image_in_range(BBDS, imga6) is not None):
        a6 = 'b'

    elif (image_in_range(WNLS, imga6) is not None or image_in_range(WNDS, imga6) is not None):
        a6 = 'N'

    elif (image_in_range(BNLS, imga6) is not None or image_in_range(BNDS, imga6) is not None):
        a6 = 'n'

    elif (image_in_range(WRLS, imga6) is not None or image_in_range(WRDS, imga6) is not None):
        a6 = 'R'

    elif (image_in_range(BRLS, imga6) is not None or image_in_range(BRDS, imga6) is not None):
        a6 = 'r'

    elif (image_in_range(WQLS, imga6) is not None or image_in_range(WQDS, imga6) is not None):
        a6 = 'Q'

    elif (image_in_range(BQLS, imga6) is not None or image_in_range(BQDS, imga6) is not None):
        a6 = 'q'

    elif (image_in_range(WKLS, imga6) is not None or image_in_range(WKDS, imga6) is not None):
        a6 = 'K'

    elif (image_in_range(BKLS, imga6) is not None or image_in_range(BKDS, imga6) is not None):
        a6 = 'k'

    if (image_in_range(LS, imgb6) is not None or image_in_range(DS, imgb6) is not None):
        b6 = 1

    elif (image_in_range(WPLS, imgb6) is not None or image_in_range(WPDS, imgb6) is not None):
        b6 = 'P'

    elif (image_in_range(BPLS, imgb6) is not None or image_in_range(BPDS, imgb6) is not None):
        b6 = 'p'

    elif (image_in_range(WBLS, imgb6) is not None or image_in_range(WBDS, imgb6) is not None):
        b6 = 'B'

    elif (image_in_range(BBLS, imgb6) is not None or image_in_range(BBDS, imgb6) is not None):
        b6 = 'b'

    elif (image_in_range(WNLS, imgb6) is not None or image_in_range(WNDS, imgb6) is not None):
        b6 = 'N'

    elif (image_in_range(BNLS, imgb6) is not None or image_in_range(BNDS, imgb6) is not None):
        b6 = 'n'

    elif (image_in_range(WRLS, imgb6) is not None or image_in_range(WRDS, imgb6) is not None):
        b6 = 'R'

    elif (image_in_range(BRLS, imgb6) is not None or image_in_range(BRDS, imgb6) is not None):
        b6 = 'r'

    elif (image_in_range(WQLS, imgb6) is not None or image_in_range(WQDS, imgb6) is not None):
        b6 = 'Q'

    elif (image_in_range(BQLS, imgb6) is not None or image_in_range(BQDS, imgb6) is not None):
        b6 = 'q'

    elif (image_in_range(WKLS, imgb6) is not None or image_in_range(WKDS, imgb6) is not None):
        b6 = 'K'

    elif (image_in_range(BKLS, imgb6) is not None or image_in_range(BKDS, imgb6) is not None):
        b6 = 'k'

    if (image_in_range(LS, imgc6) is not None or image_in_range(DS, imgc6) is not None):
        c6 = 1

    elif (image_in_range(WPLS, imgc6) is not None or image_in_range(WPDS, imgc6) is not None):
        c6 = 'P'

    elif (image_in_range(BPLS, imgc6) is not None or image_in_range(BPDS, imgc6) is not None):
        c6 = 'p'

    elif (image_in_range(WBLS, imgc6) is not None or image_in_range(WBDS, imgc6) is not None):
        c6 = 'B'

    elif (image_in_range(BBLS, imgc6) is not None or image_in_range(BBDS, imgc6) is not None):
        c6 = 'b'

    elif (image_in_range(WNLS, imgc6) is not None or image_in_range(WNDS, imgc6) is not None):
        c6 = 'N'

    elif (image_in_range(BNLS, imgc6) is not None or image_in_range(BNDS, imgc6) is not None):
        c6 = 'n'

    elif (image_in_range(WRLS, imgc6) is not None or image_in_range(WRDS, imgc6) is not None):
        c6 = 'R'

    elif (image_in_range(BRLS, imgc6) is not None or image_in_range(BRDS, imgc6) is not None):
        c6 = 'r'

    elif (image_in_range(WQLS, imgc6) is not None or image_in_range(WQDS, imgc6) is not None):
        c6 = 'Q'

    elif (image_in_range(BQLS, imgc6) is not None or image_in_range(BQDS, imgc6) is not None):
        c6 = 'q'

    elif (image_in_range(WKLS, imgc6) is not None or image_in_range(WKDS, imgc6) is not None):
        c6 = 'K'

    elif (image_in_range(BKLS, imgc6) is not None or image_in_range(BKDS, imgc6) is not None):
        c6 = 'k'

    if (image_in_range(LS, imgd6) is not None or image_in_range(DS, imgd6) is not None):
        d6 = 1

    elif (image_in_range(WPLS, imgd6) is not None or image_in_range(WPDS, imgd6) is not None):
        d6 = 'P'

    elif (image_in_range(BPLS, imgd6) is not None or image_in_range(BPDS, imgd6) is not None):
        d6 = 'p'

    elif (image_in_range(WBLS, imgd6) is not None or image_in_range(WBDS, imgd6) is not None):
        d6 = 'B'

    elif (image_in_range(BBLS, imgd6) is not None or image_in_range(BBDS, imgd6) is not None):
        d6 = 'b'

    elif (image_in_range(WNLS, imgd6) is not None or image_in_range(WNDS, imgd6) is not None):
        d6 = 'N'

    elif (image_in_range(BNLS, imgd6) is not None or image_in_range(BNDS, imgd6) is not None):
        d6 = 'n'

    elif (image_in_range(WRLS, imgd6) is not None or image_in_range(WRDS, imgd6) is not None):
        d6 = 'R'

    elif (image_in_range(BRLS, imgd6) is not None or image_in_range(BRDS, imgd6) is not None):
        d6 = 'r'

    elif (image_in_range(WQLS, imgd6) is not None or image_in_range(WQDS, imgd6) is not None):
        d6 = 'Q'

    elif (image_in_range(BQLS, imgd6) is not None or image_in_range(BQDS, imgd6) is not None):
        d6 = 'q'

    elif (image_in_range(WKLS, imgd6) is not None or image_in_range(WKDS, imgd6) is not None):
        d6 = 'K'

    elif (image_in_range(BKLS, imgd6) is not None or image_in_range(BKDS, imgd6) is not None):
        d6 = 'k'

    if (image_in_range(LS, imge6) is not None or image_in_range(DS, imge6) is not None):
        e6 = 1

    elif (image_in_range(WPLS, imge6) is not None or image_in_range(WPDS, imge6) is not None):
        e6 = 'P'

    elif (image_in_range(BPLS, imge6) is not None or image_in_range(BPDS, imge6) is not None):
        e6 = 'p'

    elif (image_in_range(WBLS, imge6) is not None or image_in_range(WBDS, imge6) is not None):
        e6 = 'B'

    elif (image_in_range(BBLS, imge6) is not None or image_in_range(BBDS, imge6) is not None):
        e6 = 'b'

    elif (image_in_range(WNLS, imge6) is not None or image_in_range(WNDS, imge6) is not None):
        e6 = 'N'

    elif (image_in_range(BNLS, imge6) is not None or image_in_range(BNDS, imge6) is not None):
        e6 = 'n'

    elif (image_in_range(WRLS, imge6) is not None or image_in_range(WRDS, imge6) is not None):
        e6 = 'R'

    elif (image_in_range(BRLS, imge6) is not None or image_in_range(BRDS, imge6) is not None):
        e6 = 'r'

    elif (image_in_range(WQLS, imge6) is not None or image_in_range(WQDS, imge6) is not None):
        e6 = 'Q'

    elif (image_in_range(BQLS, imge6) is not None or image_in_range(BQDS, imge6) is not None):
        e6 = 'q'

    elif (image_in_range(WKLS, imge6) is not None or image_in_range(WKDS, imge6) is not None):
        e6 = 'K'

    elif (image_in_range(BKLS, imge6) is not None or image_in_range(BKDS, imge6) is not None):
        e6 = 'k'

    if (image_in_range(LS, imgf6) is not None or image_in_range(DS, imgf6) is not None):
        f6 = 1

    elif (image_in_range(WPLS, imgf6) is not None or image_in_range(WPDS, imgf6) is not None):
        f6 = 'P'

    elif (image_in_range(BPLS, imgf6) is not None or image_in_range(BPDS, imgf6) is not None):
        f6 = 'p'

    elif (image_in_range(WBLS, imgf6) is not None or image_in_range(WBDS, imgf6) is not None):
        f6 = 'B'

    elif (image_in_range(BBLS, imgf6) is not None or image_in_range(BBDS, imgf6) is not None):
        f6 = 'b'

    elif (image_in_range(WNLS, imgf6) is not None or image_in_range(WNDS, imgf6) is not None):
        f6 = 'N'

    elif (image_in_range(BNLS, imgf6) is not None or image_in_range(BNDS, imgf6) is not None):
        f6 = 'n'

    elif (image_in_range(WRLS, imgf6) is not None or image_in_range(WRDS, imgf6) is not None):
        f6 = 'R'

    elif (image_in_range(BRLS, imgf6) is not None or image_in_range(BRDS, imgf6) is not None):
        f6 = 'r'

    elif (image_in_range(WQLS, imgf6) is not None or image_in_range(WQDS, imgf6) is not None):
        f6 = 'Q'

    elif (image_in_range(BQLS, imgf6) is not None or image_in_range(BQDS, imgf6) is not None):
        f6 = 'q'

    elif (image_in_range(WKLS, imgf6) is not None or image_in_range(WKDS, imgf6) is not None):
        f6 = 'K'

    elif (image_in_range(BKLS, imgf6) is not None or image_in_range(BKDS, imgf6) is not None):
        f6 = 'k'

    if (image_in_range(LS, imgg6) is not None or image_in_range(DS, imgg6) is not None):
        g6 = 1

    elif (image_in_range(WPLS, imgg6) is not None or image_in_range(WPDS, imgg6) is not None):
        g6 = 'P'

    elif (image_in_range(BPLS, imgg6) is not None or image_in_range(BPDS, imgg6) is not None):
        g6 = 'p'

    elif (image_in_range(WBLS, imgg6) is not None or image_in_range(WBDS, imgg6) is not None):
        g6 = 'B'

    elif (image_in_range(BBLS, imgg6) is not None or image_in_range(BBDS, imgg6) is not None):
        g6 = 'b'

    elif (image_in_range(WNLS, imgg6) is not None or image_in_range(WNDS, imgg6) is not None):
        g6 = 'N'

    elif (image_in_range(BNLS, imgg6) is not None or image_in_range(BNDS, imgg6) is not None):
        g6 = 'n'

    elif (image_in_range(WRLS, imgg6) is not None or image_in_range(WRDS, imgg6) is not None):
        g6 = 'R'

    elif (image_in_range(BRLS, imgg6) is not None or image_in_range(BRDS, imgg6) is not None):
        g6 = 'r'

    elif (image_in_range(WQLS, imgg6) is not None or image_in_range(WQDS, imgg6) is not None):
        g6 = 'Q'

    elif (image_in_range(BQLS, imgg6) is not None or image_in_range(BQDS, imgg6) is not None):
        g6 = 'q'

    elif (image_in_range(WKLS, imgg6) is not None or image_in_range(WKDS, imgg6) is not None):
        g6 = 'K'

    elif (image_in_range(BKLS, imgg6) is not None or image_in_range(BKDS, imgg6) is not None):
        g6 = 'k'

    if (image_in_range(LS, imgh6) is not None or image_in_range(DS, imgh6) is not None):
        h6 = 1

    elif (image_in_range(WPLS, imgh6) is not None or image_in_range(WPDS, imgh6) is not None):
        h6 = 'P'

    elif (image_in_range(BPLS, imgh6) is not None or image_in_range(BPDS, imgh6) is not None):
        h6 = 'p'

    elif (image_in_range(WBLS, imgh6) is not None or image_in_range(WBDS, imgh6) is not None):
        h6 = 'B'

    elif (image_in_range(BBLS, imgh6) is not None or image_in_range(BBDS, imgh6) is not None):
        h6 = 'b'

    elif (image_in_range(WNLS, imgh6) is not None or image_in_range(WNDS, imgh6) is not None):
        h6 = 'N'

    elif (image_in_range(BNLS, imgh6) is not None or image_in_range(BNDS, imgh6) is not None):
        h6 = 'n'

    elif (image_in_range(WRLS, imgh6) is not None or image_in_range(WRDS, imgh6) is not None):
        h6 = 'R'

    elif (image_in_range(BRLS, imgh6) is not None or image_in_range(BRDS, imgh6) is not None):
        h6 = 'r'

    elif (image_in_range(WQLS, imgh6) is not None or image_in_range(WQDS, imgh6) is not None):
        h6 = 'Q'

    elif (image_in_range(BQLS, imgh6) is not None or image_in_range(BQDS, imgh6) is not None):
        h6 = 'q'

    elif (image_in_range(WKLS, imgh6) is not None or image_in_range(WKDS, imgh6) is not None):
        h6 = 'K'

    elif (image_in_range(BKLS, imgh6) is not None or image_in_range(BKDS, imgh6) is not None):
        h6 = 'k'

    if (image_in_range(LS, imga7) is not None or image_in_range(DS, imga7) is not None):
        a7 = 1

    elif (image_in_range(WPLS, imga7) is not None or image_in_range(WPDS, imga7) is not None):
        a7 = 'P'

    elif (image_in_range(BPLS, imga7) is not None or image_in_range(BPDS, imga7) is not None):
        a7 = 'p'

    elif (image_in_range(WBLS, imga7) is not None or image_in_range(WBDS, imga7) is not None):
        a7 = 'B'

    elif (image_in_range(BBLS, imga7) is not None or image_in_range(BBDS, imga7) is not None):
        a7 = 'b'

    elif (image_in_range(WNLS, imga7) is not None or image_in_range(WNDS, imga7) is not None):
        a7 = 'N'

    elif (image_in_range(BNLS, imga7) is not None or image_in_range(BNDS, imga7) is not None):
        a7 = 'n'

    elif (image_in_range(WRLS, imga7) is not None or image_in_range(WRDS, imga7) is not None):
        a7 = 'R'

    elif (image_in_range(BRLS, imga7) is not None or image_in_range(BRDS, imga7) is not None):
        a7 = 'r'

    elif (image_in_range(WQLS, imga7) is not None or image_in_range(WQDS, imga7) is not None):
        a7 = 'Q'

    elif (image_in_range(BQLS, imga7) is not None or image_in_range(BQDS, imga7) is not None):
        a7 = 'q'

    elif (image_in_range(WKLS, imga7) is not None or image_in_range(WKDS, imga7) is not None):
        a7 = 'K'

    elif (image_in_range(BKLS, imga7) is not None or image_in_range(BKDS, imga7) is not None):
        a7 = 'k'

    if (image_in_range(LS, imgb7) is not None or image_in_range(DS, imgb7) is not None):
        b7 = 1

    elif (image_in_range(WPLS, imgb7) is not None or image_in_range(WPDS, imgb7) is not None):
        b7 = 'P'

    elif (image_in_range(BPLS, imgb7) is not None or image_in_range(BPDS, imgb7) is not None):
        b7 = 'p'

    elif (image_in_range(WBLS, imgb7) is not None or image_in_range(WBDS, imgb7) is not None):
        b7 = 'B'

    elif (image_in_range(BBLS, imgb7) is not None or image_in_range(BBDS, imgb7) is not None):
        b7 = 'b'

    elif (image_in_range(WNLS, imgb7) is not None or image_in_range(WNDS, imgb7) is not None):
        b7 = 'N'

    elif (image_in_range(BNLS, imgb7) is not None or image_in_range(BNDS, imgb7) is not None):
        b7 = 'n'

    elif (image_in_range(WRLS, imgb7) is not None or image_in_range(WRDS, imgb7) is not None):
        b7 = 'R'

    elif (image_in_range(BRLS, imgb7) is not None or image_in_range(BRDS, imgb7) is not None):
        b7 = 'r'

    elif (image_in_range(WQLS, imgb7) is not None or image_in_range(WQDS, imgb7) is not None):
        b7 = 'Q'

    elif (image_in_range(BQLS, imgb7) is not None or image_in_range(BQDS, imgb7) is not None):
        b7 = 'q'

    elif (image_in_range(WKLS, imgb7) is not None or image_in_range(WKDS, imgb7) is not None):
        b7 = 'K'

    elif (image_in_range(BKLS, imgb7) is not None or image_in_range(BKDS, imgb7) is not None):
        b7 = 'k'

    if (image_in_range(LS, imgc7) is not None or image_in_range(DS, imgc7) is not None):
        c7 = 1

    elif (image_in_range(WPLS, imgc7) is not None or image_in_range(WPDS, imgc7) is not None):
        c7 = 'P'

    elif (image_in_range(BPLS, imgc7) is not None or image_in_range(BPDS, imgc7) is not None):
        c7 = 'p'

    elif (image_in_range(WBLS, imgc7) is not None or image_in_range(WBDS, imgc7) is not None):
        c7 = 'B'

    elif (image_in_range(BBLS, imgc7) is not None or image_in_range(BBDS, imgc7) is not None):
        c7 = 'b'

    elif (image_in_range(WNLS, imgc7) is not None or image_in_range(WNDS, imgc7) is not None):
        c7 = 'N'

    elif (image_in_range(BNLS, imgc7) is not None or image_in_range(BNDS, imgc7) is not None):
        c7 = 'n'

    elif (image_in_range(WRLS, imgc7) is not None or image_in_range(WRDS, imgc7) is not None):
        c7 = 'R'

    elif (image_in_range(BRLS, imgc7) is not None or image_in_range(BRDS, imgc7) is not None):
        c7 = 'r'

    elif (image_in_range(WQLS, imgc7) is not None or image_in_range(WQDS, imgc7) is not None):
        c7 = 'Q'

    elif (image_in_range(BQLS, imgc7) is not None or image_in_range(BQDS, imgc7) is not None):
        c7 = 'q'

    elif (image_in_range(WKLS, imgc7) is not None or image_in_range(WKDS, imgc7) is not None):
        c7 = 'K'

    elif (image_in_range(BKLS, imgc7) is not None or image_in_range(BKDS, imgc7) is not None):
        c7 = 'k'

    if (image_in_range(LS, imgd7) is not None or image_in_range(DS, imgd7) is not None):
        d7 = 1

    elif (image_in_range(WPLS, imgd7) is not None or image_in_range(WPDS, imgd7) is not None):
        d7 = 'P'

    elif (image_in_range(BPLS, imgd7) is not None or image_in_range(BPDS, imgd7) is not None):
        d7 = 'p'

    elif (image_in_range(WBLS, imgd7) is not None or image_in_range(WBDS, imgd7) is not None):
        d7 = 'B'

    elif (image_in_range(BBLS, imgd7) is not None or image_in_range(BBDS, imgd7) is not None):
        d7 = 'b'

    elif (image_in_range(WNLS, imgd7) is not None or image_in_range(WNDS, imgd7) is not None):
        d7 = 'N'

    elif (image_in_range(BNLS, imgd7) is not None or image_in_range(BNDS, imgd7) is not None):
        d7 = 'n'

    elif (image_in_range(WRLS, imgd7) is not None or image_in_range(WRDS, imgd7) is not None):
        d7 = 'R'

    elif (image_in_range(BRLS, imgd7) is not None or image_in_range(BRDS, imgd7) is not None):
        d7 = 'r'

    elif (image_in_range(WQLS, imgd7) is not None or image_in_range(WQDS, imgd7) is not None):
        d7 = 'Q'

    elif (image_in_range(BQLS, imgd7) is not None or image_in_range(BQDS, imgd7) is not None):
        d7 = 'q'

    elif (image_in_range(WKLS, imgd7) is not None or image_in_range(WKDS, imgd7) is not None):
        d7 = 'K'

    elif (image_in_range(BKLS, imgd7) is not None or image_in_range(BKDS, imgd7) is not None):
        d7 = 'k'

    if (image_in_range(LS, imge7) is not None or image_in_range(DS, imge7) is not None):
        e7 = 1

    elif (image_in_range(WPLS, imge7) is not None or image_in_range(WPDS, imge7) is not None):
        e7 = 'P'

    elif (image_in_range(BPLS, imge7) is not None or image_in_range(BPDS, imge7) is not None):
        e7 = 'p'

    elif (image_in_range(WBLS, imge7) is not None or image_in_range(WBDS, imge7) is not None):
        e7 = 'B'

    elif (image_in_range(BBLS, imge7) is not None or image_in_range(BBDS, imge7) is not None):
        e7 = 'b'

    elif (image_in_range(WNLS, imge7) is not None or image_in_range(WNDS, imge7) is not None):
        e7 = 'N'

    elif (image_in_range(BNLS, imge7) is not None or image_in_range(BNDS, imge7) is not None):
        e7 = 'n'

    elif (image_in_range(WRLS, imge7) is not None or image_in_range(WRDS, imge7) is not None):
        e7 = 'R'

    elif (image_in_range(BRLS, imge7) is not None or image_in_range(BRDS, imge7) is not None):
        e7 = 'r'

    elif (image_in_range(WQLS, imge7) is not None or image_in_range(WQDS, imge7) is not None):
        e7 = 'Q'

    elif (image_in_range(BQLS, imge7) is not None or image_in_range(BQDS, imge7) is not None):
        e7 = 'q'

    elif (image_in_range(WKLS, imge7) is not None or image_in_range(WKDS, imge7) is not None):
        e7 = 'K'

    elif (image_in_range(BKLS, imge7) is not None or image_in_range(BKDS, imge7) is not None):
        e7 = 'k'

    if (image_in_range(LS, imgf7) is not None or image_in_range(DS, imgf7) is not None):
        f7 = 1

    elif (image_in_range(WPLS, imgf7) is not None or image_in_range(WPDS, imgf7) is not None):
        f7 = 'P'

    elif (image_in_range(BPLS, imgf7) is not None or image_in_range(BPDS, imgf7) is not None):
        f7 = 'p'

    elif (image_in_range(WBLS, imgf7) is not None or image_in_range(WBDS, imgf7) is not None):
        f7 = 'B'

    elif (image_in_range(BBLS, imgf7) is not None or image_in_range(BBDS, imgf7) is not None):
        f7 = 'b'

    elif (image_in_range(WNLS, imgf7) is not None or image_in_range(WNDS, imgf7) is not None):
        f7 = 'N'

    elif (image_in_range(BNLS, imgf7) is not None or image_in_range(BNDS, imgf7) is not None):
        f7 = 'n'

    elif (image_in_range(WRLS, imgf7) is not None or image_in_range(WRDS, imgf7) is not None):
        f7 = 'R'

    elif (image_in_range(BRLS, imgf7) is not None or image_in_range(BRDS, imgf7) is not None):
        f7 = 'r'

    elif (image_in_range(WQLS, imgf7) is not None or image_in_range(WQDS, imgf7) is not None):
        f7 = 'Q'

    elif (image_in_range(BQLS, imgf7) is not None or image_in_range(BQDS, imgf7) is not None):
        f7 = 'q'

    elif (image_in_range(WKLS, imgf7) is not None or image_in_range(WKDS, imgf7) is not None):
        f7 = 'K'

    elif (image_in_range(BKLS, imgf7) is not None or image_in_range(BKDS, imgf7) is not None):
        f7 = 'k'

    if (image_in_range(LS, imgg7) is not None or image_in_range(DS, imgg7) is not None):
        g7 = 1

    elif (image_in_range(WPLS, imgg7) is not None or image_in_range(WPDS, imgg7) is not None):
        g7 = 'P'

    elif (image_in_range(BPLS, imgg7) is not None or image_in_range(BPDS, imgg7) is not None):
        g7 = 'p'

    elif (image_in_range(WBLS, imgg7) is not None or image_in_range(WBDS, imgg7) is not None):
        g7 = 'B'

    elif (image_in_range(BBLS, imgg7) is not None or image_in_range(BBDS, imgg7) is not None):
        g7 = 'b'

    elif (image_in_range(WNLS, imgg7) is not None or image_in_range(WNDS, imgg7) is not None):
        g7 = 'N'

    elif (image_in_range(BNLS, imgg7) is not None or image_in_range(BNDS, imgg7) is not None):
        g7 = 'n'

    elif (image_in_range(WRLS, imgg7) is not None or image_in_range(WRDS, imgg7) is not None):
        g7 = 'R'

    elif (image_in_range(BRLS, imgg7) is not None or image_in_range(BRDS, imgg7) is not None):
        g7 = 'r'

    elif (image_in_range(WQLS, imgg7) is not None or image_in_range(WQDS, imgg7) is not None):
        g7 = 'Q'

    elif (image_in_range(BQLS, imgg7) is not None or image_in_range(BQDS, imgg7) is not None):
        g7 = 'q'

    elif (image_in_range(WKLS, imgg7) is not None or image_in_range(WKDS, imgg7) is not None):
        g7 = 'K'

    elif (image_in_range(BKLS, imgg7) is not None or image_in_range(BKDS, imgg7) is not None):
        g7 = 'k'

    if (image_in_range(LS, imgh7) is not None or image_in_range(DS, imgh7) is not None):
        h7 = 1

    elif (image_in_range(WPLS, imgh7) is not None or image_in_range(WPDS, imgh7) is not None):
        h7 = 'P'

    elif (image_in_range(BPLS, imgh7) is not None or image_in_range(BPDS, imgh7) is not None):
        h7 = 'p'

    elif (image_in_range(WBLS, imgh7) is not None or image_in_range(WBDS, imgh7) is not None):
        h7 = 'B'

    elif (image_in_range(BBLS, imgh7) is not None or image_in_range(BBDS, imgh7) is not None):
        h7 = 'b'

    elif (image_in_range(WNLS, imgh7) is not None or image_in_range(WNDS, imgh7) is not None):
        h7 = 'N'

    elif (image_in_range(BNLS, imgh7) is not None or image_in_range(BNDS, imgh7) is not None):
        h7 = 'n'

    elif (image_in_range(WRLS, imgh7) is not None or image_in_range(WRDS, imgh7) is not None):
        h7 = 'R'

    elif (image_in_range(BRLS, imgh7) is not None or image_in_range(BRDS, imgh7) is not None):
        h7 = 'r'

    elif (image_in_range(WQLS, imgh7) is not None or image_in_range(WQDS, imgh7) is not None):
        h7 = 'Q'

    elif (image_in_range(BQLS, imgh7) is not None or image_in_range(BQDS, imgh7) is not None):
        h7 = 'q'

    elif (image_in_range(WKLS, imgh7) is not None or image_in_range(WKDS, imgh7) is not None):
        h7 = 'K'

    elif (image_in_range(BKLS, imgh7) is not None or image_in_range(BKDS, imgh7) is not None):
        h7 = 'k'

    if (image_in_range(LS, imga8) is not None or image_in_range(DS, imga8) is not None):
        a8 = 1

    elif (image_in_range(WPLS, imga8) is not None or image_in_range(WPDS, imga8) is not None):
        a8 = 'P'

    elif (image_in_range(BPLS, imga8) is not None or image_in_range(BPDS, imga8) is not None):
        a8 = 'p'

    elif (image_in_range(WBLS, imga8) is not None or image_in_range(WBDS, imga8) is not None):
        a8 = 'B'

    elif (image_in_range(BBLS, imga8) is not None or image_in_range(BBDS, imga8) is not None):
        a8 = 'b'

    elif (image_in_range(WNLS, imga8) is not None or image_in_range(WNDS, imga8) is not None):
        a8 = 'N'

    elif (image_in_range(BNLS, imga8) is not None or image_in_range(BNDS, imga8) is not None):
        a8 = 'n'

    elif (image_in_range(WRLS, imga8) is not None or image_in_range(WRDS, imga8) is not None):
        a8 = 'R'

    elif (image_in_range(BRLS, imga8) is not None or image_in_range(BRDS, imga8) is not None):
        a8 = 'r'

    elif (image_in_range(WQLS, imga8) is not None or image_in_range(WQDS, imga8) is not None):
        a8 = 'Q'

    elif (image_in_range(BQLS, imga8) is not None or image_in_range(BQDS, imga8) is not None):
        a8 = 'q'

    elif (image_in_range(WKLS, imga8) is not None or image_in_range(WKDS, imga8) is not None):
        a8 = 'K'

    elif (image_in_range(BKLS, imga8) is not None or image_in_range(BKDS, imga8) is not None):
        a8 = 'k'

    if (image_in_range(LS, imgb8) is not None or image_in_range(DS, imgb8) is not None):
        b8 = 1

    elif (image_in_range(WPLS, imgb8) is not None or image_in_range(WPDS, imgb8) is not None):
        b8 = 'P'

    elif (image_in_range(BPLS, imgb8) is not None or image_in_range(BPDS, imgb8) is not None):
        b8 = 'p'

    elif (image_in_range(WBLS, imgb8) is not None or image_in_range(WBDS, imgb8) is not None):
        b8 = 'B'

    elif (image_in_range(BBLS, imgb8) is not None or image_in_range(BBDS, imgb8) is not None):
        b8 = 'b'

    elif (image_in_range(WNLS, imgb8) is not None or image_in_range(WNDS, imgb8) is not None):
        b8 = 'N'

    elif (image_in_range(BNLS, imgb8) is not None or image_in_range(BNDS, imgb8) is not None):
        b8 = 'n'

    elif (image_in_range(WRLS, imgb8) is not None or image_in_range(WRDS, imgb8) is not None):
        b8 = 'R'

    elif (image_in_range(BRLS, imgb8) is not None or image_in_range(BRDS, imgb8) is not None):
        b8 = 'r'

    elif (image_in_range(WQLS, imgb8) is not None or image_in_range(WQDS, imgb8) is not None):
        b8 = 'Q'

    elif (image_in_range(BQLS, imgb8) is not None or image_in_range(BQDS, imgb8) is not None):
        b8 = 'q'

    elif (image_in_range(WKLS, imgb8) is not None or image_in_range(WKDS, imgb8) is not None):
        b8 = 'K'

    elif (image_in_range(BKLS, imgb8) is not None or image_in_range(BKDS, imgb8) is not None):
        b8 = 'k'

    if (image_in_range(LS, imgc8) is not None or image_in_range(DS, imgc8) is not None):
        c8 = 1

    elif (image_in_range(WPLS, imgc8) is not None or image_in_range(WPDS, imgc8) is not None):
        c8 = 'P'

    elif (image_in_range(BPLS, imgc8) is not None or image_in_range(BPDS, imgc8) is not None):
        c8 = 'p'

    elif (image_in_range(WBLS, imgc8) is not None or image_in_range(WBDS, imgc8) is not None):
        c8 = 'B'

    elif (image_in_range(BBLS, imgc8) is not None or image_in_range(BBDS, imgc8) is not None):
        c8 = 'b'

    elif (image_in_range(WNLS, imgc8) is not None or image_in_range(WNDS, imgc8) is not None):
        c8 = 'N'

    elif (image_in_range(BNLS, imgc8) is not None or image_in_range(BNDS, imgc8) is not None):
        c8 = 'n'

    elif (image_in_range(WRLS, imgc8) is not None or image_in_range(WRDS, imgc8) is not None):
        c8 = 'R'

    elif (image_in_range(BRLS, imgc8) is not None or image_in_range(BRDS, imgc8) is not None):
        c8 = 'r'

    elif (image_in_range(WQLS, imgc8) is not None or image_in_range(WQDS, imgc8) is not None):
        c8 = 'Q'

    elif (image_in_range(BQLS, imgc8) is not None or image_in_range(BQDS, imgc8) is not None):
        c8 = 'q'

    elif (image_in_range(WKLS, imgc8) is not None or image_in_range(WKDS, imgc8) is not None):
        c8 = 'K'

    elif (image_in_range(BKLS, imgc8) is not None or image_in_range(BKDS, imgc8) is not None):
        c8 = 'k'

    if (image_in_range(LS, imgd8) is not None or image_in_range(DS, imgd8) is not None):
        d8 = 1

    elif (image_in_range(WPLS, imgd8) is not None or image_in_range(WPDS, imgd8) is not None):
        d8 = 'P'

    elif (image_in_range(BPLS, imgd8) is not None or image_in_range(BPDS, imgd8) is not None):
        d8 = 'p'

    elif (image_in_range(WBLS, imgd8) is not None or image_in_range(WBDS, imgd8) is not None):
        d8 = 'B'

    elif (image_in_range(BBLS, imgd8) is not None or image_in_range(BBDS, imgd8) is not None):
        d8 = 'b'

    elif (image_in_range(WNLS, imgd8) is not None or image_in_range(WNDS, imgd8) is not None):
        d8 = 'N'

    elif (image_in_range(BNLS, imgd8) is not None or image_in_range(BNDS, imgd8) is not None):
        d8 = 'n'

    elif (image_in_range(WRLS, imgd8) is not None or image_in_range(WRDS, imgd8) is not None):
        d8 = 'R'

    elif (image_in_range(BRLS, imgd8) is not None or image_in_range(BRDS, imgd8) is not None):
        d8 = 'r'

    elif (image_in_range(WQLS, imgd8) is not None or image_in_range(WQDS, imgd8) is not None):
        d8 = 'Q'

    elif (image_in_range(BQLS, imgd8) is not None or image_in_range(BQDS, imgd8) is not None):
        d8 = 'q'

    elif (image_in_range(WKLS, imgd8) is not None or image_in_range(WKDS, imgd8) is not None):
        d8 = 'K'

    elif (image_in_range(BKLS, imgd8) is not None or image_in_range(BKDS, imgd8) is not None):
        d8 = 'k'

    if (image_in_range(LS, imge8) is not None or image_in_range(DS, imge8) is not None):
        e8 = 1

    elif (image_in_range(WPLS, imge8) is not None or image_in_range(WPDS, imge8) is not None):
        e8 = 'P'

    elif (image_in_range(BPLS, imge8) is not None or image_in_range(BPDS, imge8) is not None):
        e8 = 'p'

    elif (image_in_range(WBLS, imge8) is not None or image_in_range(WBDS, imge8) is not None):
        e8 = 'B'

    elif (image_in_range(BBLS, imge8) is not None or image_in_range(BBDS, imge8) is not None):
        e8 = 'b'

    elif (image_in_range(WNLS, imge8) is not None or image_in_range(WNDS, imge8) is not None):
        e8 = 'N'

    elif (image_in_range(BNLS, imge8) is not None or image_in_range(BNDS, imge8) is not None):
        e8 = 'n'

    elif (image_in_range(WRLS, imge8) is not None or image_in_range(WRDS, imge8) is not None):
        e8 = 'R'

    elif (image_in_range(BRLS, imge8) is not None or image_in_range(BRDS, imge8) is not None):
        e8 = 'r'

    elif (image_in_range(WQLS, imge8) is not None or image_in_range(WQDS, imge8) is not None):
        e8 = 'Q'

    elif (image_in_range(BQLS, imge8) is not None or image_in_range(BQDS, imge8) is not None):
        e8 = 'q'

    elif (image_in_range(WKLS, imge8) is not None or image_in_range(WKDS, imge8) is not None):
        e8 = 'K'

    elif (image_in_range(BKLS, imge8) is not None or image_in_range(BKDS, imge8) is not None):
        e8 = 'k'

    if (image_in_range(LS, imgf8) is not None or image_in_range(DS, imgf8) is not None):
        f8 = 1

    elif (image_in_range(WPLS, imgf8) is not None or image_in_range(WPDS, imgf8) is not None):
        f8 = 'P'

    elif (image_in_range(BPLS, imgf8) is not None or image_in_range(BPDS, imgf8) is not None):
        f8 = 'p'

    elif (image_in_range(WBLS, imgf8) is not None or image_in_range(WBDS, imgf8) is not None):
        f8 = 'B'

    elif (image_in_range(BBLS, imgf8) is not None or image_in_range(BBDS, imgf8) is not None):
        f8 = 'b'

    elif (image_in_range(WNLS, imgf8) is not None or image_in_range(WNDS, imgf8) is not None):
        f8 = 'N'

    elif (image_in_range(BNLS, imgf8) is not None or image_in_range(BNDS, imgf8) is not None):
        f8 = 'n'

    elif (image_in_range(WRLS, imgf8) is not None or image_in_range(WRDS, imgf8) is not None):
        f8 = 'R'

    elif (image_in_range(BRLS, imgf8) is not None or image_in_range(BRDS, imgf8) is not None):
        f8 = 'r'

    elif (image_in_range(WQLS, imgf8) is not None or image_in_range(WQDS, imgf8) is not None):
        f8 = 'Q'

    elif (image_in_range(BQLS, imgf8) is not None or image_in_range(BQDS, imgf8) is not None):
        f8 = 'q'

    elif (image_in_range(WKLS, imgf8) is not None or image_in_range(WKDS, imgf8) is not None):
        f8 = 'K'

    elif (image_in_range(BKLS, imgf8) is not None or image_in_range(BKDS, imgf8) is not None):
        f8 = 'k'

    if (image_in_range(LS, imgg8) is not None or image_in_range(DS, imgg8) is not None):
        g8 = 1

    elif (image_in_range(WPLS, imgg8) is not None or image_in_range(WPDS, imgg8) is not None):
        g8 = 'P'

    elif (image_in_range(BPLS, imgg8) is not None or image_in_range(BPDS, imgg8) is not None):
        g8 = 'p'

    elif (image_in_range(WBLS, imgg8) is not None or image_in_range(WBDS, imgg8) is not None):
        g8 = 'B'

    elif (image_in_range(BBLS, imgg8) is not None or image_in_range(BBDS, imgg8) is not None):
        g8 = 'b'

    elif (image_in_range(WNLS, imgg8) is not None or image_in_range(WNDS, imgg8) is not None):
        g8 = 'N'

    elif (image_in_range(BNLS, imgg8) is not None or image_in_range(BNDS, imgg8) is not None):
        g8 = 'n'

    elif (image_in_range(WRLS, imgg8) is not None or image_in_range(WRDS, imgg8) is not None):
        g8 = 'R'

    elif (image_in_range(BRLS, imgg8) is not None or image_in_range(BRDS, imgg8) is not None):
        g8 = 'r'

    elif (image_in_range(WQLS, imgg8) is not None or image_in_range(WQDS, imgg8) is not None):
        g8 = 'Q'

    elif (image_in_range(BQLS, imgg8) is not None or image_in_range(BQDS, imgg8) is not None):
        g8 = 'q'

    elif (image_in_range(WKLS, imgg8) is not None or image_in_range(WKDS, imgg8) is not None):
        g8 = 'K'

    elif (image_in_range(BKLS, imgg8) is not None or image_in_range(BKDS, imgg8) is not None):
        g8 = 'k'

    if (image_in_range(LS, imgh8) is not None or image_in_range(DS, imgh8) is not None):
        h8 = 1

    elif (image_in_range(WPLS, imgh8) is not None or image_in_range(WPDS, imgh8) is not None):
        h8 = 'P'

    elif (image_in_range(BPLS, imgh8) is not None or image_in_range(BPDS, imgh8) is not None):
        h8 = 'p'

    elif (image_in_range(WBLS, imgh8) is not None or image_in_range(WBDS, imgh8) is not None):
        h8 = 'B'

    elif (image_in_range(BBLS, imgh8) is not None or image_in_range(BBDS, imgh8) is not None):
        h8 = 'b'

    elif (image_in_range(WNLS, imgh8) is not None or image_in_range(WNDS, imgh8) is not None):
        h8 = 'N'

    elif (image_in_range(BNLS, imgh8) is not None or image_in_range(BNDS, imgh8) is not None):
        h8 = 'n'

    elif (image_in_range(WRLS, imgh8) is not None or image_in_range(WRDS, imgh8) is not None):
        h8 = 'R'

    elif (image_in_range(BRLS, imgh8) is not None or image_in_range(BRDS, imgh8) is not None):
        h8 = 'r'

    elif (image_in_range(WQLS, imgh8) is not None or image_in_range(WQDS, imgh8) is not None):
        h8 = 'Q'

    elif (image_in_range(BQLS, imgh8) is not None or image_in_range(BQDS, imgh8) is not None):
        h8 = 'q'

    elif (image_in_range(WKLS, imgh8) is not None or image_in_range(WKDS, imgh8) is not None):
        h8 = 'K'

    elif (image_in_range(BKLS, imgh8) is not None or image_in_range(BKDS, imgh8) is not None):
        h8 = 'k'

    return concat_values(a8, b8, c8, d8, e8, f8, g8, h8, "/", 
                                a7, b7, c7, d7, e7, f7, g7, h7, "/", 
                                a6, b6, c6, d6, e6, f6, g6, h6, "/", 
                                a5, b5, c5, d5, e5, f5, g5, h5, "/", 
                                a4, b4, c4, d4, e4, f4, g4, h4, "/", 
                                a3, b3, c3, d3, e3, f3, g3, h3, "/", 
                                a2, b2, c2, d2, e2, f2, g2, h2, "/", 
                                a1, b1, c1, d1, e1, f1, g1, h1, " b - - - -")

    

#endregion

count = 0
oldFen = ''

#if there is a change in position (opponent moved) calculate and play next best move
while True:
    fen_position = getFen()

    if fen_position == oldFen:
        continue

    try:
        stockfish.set_fen_position(fen_position)
        print(fen_position)
        if (fen_position == '8/8/8/8/8/8/8/8 b - - - -'):
            break
        best_move = stockfish.get_best_move()

    except StockfishException:
        continue

    source_square = best_move[:2]
    dest_square = best_move[2:]

    source_coords = coordinates[source_square]
    dest_coords = coordinates[dest_square]

    move(*source_coords, *dest_coords)

    oldFen = getFen()

    count += 1

#sleep randomization for less robotic gameplay
    if (count < 10):
        time.sleep(random.randint(2, 5))

    elif (count < 20):
        time.sleep(random.randint(3, 8))

    else:
        time.sleep(random.randint(1, 3))
import sys
from calculator import Cal

if __name__ == '__main__':
    print('File executing')
    x, y = sys.argv[1], sys.argv[2]
    c = Cal(int(x), int(y))
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())

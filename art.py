
import sys
import time
import math

W, H = 70, 28

V = [
    (-1,-1,-1), (1,-1,-1),
    (1,1,-1), (-1,1,-1),
    (-1,-1,1), (1,-1,1),
    (1,1,1), (-1,1,1)
]

E = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

def r(v, a, b, c):
    x, y, z = v

    y, z = y*math.cos(a)-z*math.sin(a), y*math.sin(a)+z*math.cos(a)
    x, z = x*math.cos(b)+z*math.sin(b), -x*math.sin(b)+z*math.cos(b)
    x, y = x*math.cos(c)-y*math.sin(c), x*math.sin(c)+y*math.cos(c)

    return x, y, z

def d(a, b, c):
    s = [[' ']*W for _ in range(H)]
    q = [[-999]*W for _ in range(H)]

    p = []

    for v in V:
        x, y, z = r(v, a, b, c)
        t = z + 4

        p.append((
            int(W/2 + x*22/t),
            int(H/2 - y*22/t),
            z
        ))

    for i, j in E:
        x1, y1, z1 = p[i]
        x2, y2, z2 = p[j]

        n = max(abs(x2-x1), abs(y2-y1), 1)

        for k in range(n+1):
            t = k/n
            x = round(x1+(x2-x1)*t)
            y = round(y1+(y2-y1)*t)
            z = z1+(z2-z1)*t

            if 0 <= x < W and 0 <= y < H and z > q[y][x]:
                q[y][x] = z
                s[y][x] = '#'

    return '\n'.join('\033[96m'+''.join(v)+'\033[0m' for v in s)

def m():
    a = b = c = 0
    sys.stdout.write('\033[?25l\033[2J')

    try:
        while True:
            sys.stdout.write('\033[H'+d(a,b,c))
            sys.stdout.write(
                '\n\033[91m       cube \033[0m'
                '\n\033[90m       made with ♥️ by sync\033[0m'
            )
            sys.stdout.flush()

            a += 0.025
            b += 0.035
            c += 0.015

            time.sleep(0.025)

    except KeyboardInterrupt:
        pass

    finally:
        sys.stdout.write('\033[0m\033[?25h\n')
        sys.stdout.flush()

if __name__ == "__main__":
    m()
    
import numpy as np
import math
import matplotlib.pyplot as plt

def generate_permutation() -> np.ndarray:
    return np.random.permutation(256)

permutation = generate_permutation()

def Noise2D(x, y):
    global permutation
    X = math.floor(x) & 255
    Y = math.floor(y) & 255
    
    xf = x - math.floor(x)
    yf = y - math.floor(y)
    
    topRight = np.array([xf - 1.0, yf - 1.0])
    topLeft = np.array([xf, yf - 1.0])
    bottomRight = np.array([xf - 1.0, yf])
    bottomLeft = np.array([xf, yf])
    
    
    vTopRight = permutation[permutation[X-1]-Y-1]
    vTopLeft = permutation[permutation[X]-Y-1]
    vBottomRight = permutation[permutation[X-1]-Y]
    vBottomRLeft = permutation[permutation[X]-Y]
    
    dotTopRight = topRight.dot(get_constant_vector(vTopRight))
    dotTopLeft = topLeft.dot(get_constant_vector(vTopLeft))
    dotBottomRight = bottomRight.dot(get_constant_vector(vBottomRight))
    dotBottomLeft = bottomLeft.dot(get_constant_vector(vBottomRLeft))
    
    u = fade(xf)
    v = fade(yf)
    
    return lerp(u, lerp(v, dotBottomLeft, dotTopLeft), lerp(v, dotBottomRight, dotTopRight))


def get_constant_vector(v: int) -> np.ndarray:
    h = v & 3
    if (h == 0):
        return np.array([1.0, 1.0])
    elif (h == 1):
        return np.array([-1.0, 1.0])
    elif (h ==2):
        return np.array([-1.0, -1.0])
    else:
        return np.array([1.0, -1.0])
    
def fade(val: float) -> float:
    return ((6*val - 15)*val +10) * val**3

def lerp(u: float, a1: np.ndarray, a2: np.ndarray) -> np.ndarray:
    return a1 + u*(a2-a1)


if __name__ == "__main__":
    terrain = np.ndarray((500, 500), dtype=tuple)
    for y in range(500):
        for x in range(500):
            n = 0.0
            a = 1.0
            f = 0.005
            
            for octet in range(8):
                v = a * Noise2D(x*f, y*f)
                n += v
                a *= 0.5
                f *= 2.0
            
            n += 1.0
            n *= 0.5
            
            rgb = round(255 * n)
            
            if (n < 0.5):
                terrain[x][y] = (0, 0,min(rgb * 2))
            elif (n < 0.9):
                terrain[x][y] = (0, rgb, round(rgb*0.5))
            else:
                terrain[x][y] = (rgb, rgb, rgb)
            
    plt.imshow(a, cmap='hot', interpolation='nearest')
    plt.show()
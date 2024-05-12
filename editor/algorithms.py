import math
from typing import Callable, Dict, List

from editor.point import PointInt, PointFloat

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    return -1

def draw_line(p_list):
    if len(p_list) < 2:
        return p_list
    if p_list[0].copy().equal(p_list[1].copy()):
        return [p_list[0].copy()]
    a, b = p_list[0].copy(), p_list[1].copy()
    result = []

    sign_x, sign_y = sign(b.x - a.x), sign(b.y - a.y)
    if a.x == b.x:
        for y in range(a.y, b.y + sign_y, sign_y):
            result.append(PointInt(a.x, y))
        return result

    k = a.slope(b)
    dy = abs(b.y - a.y)
    dx = abs(b.x - a.x)
    if abs(k) > 1:
        p = 2 * dx - dy
        x_begin = a.x
        for y in range(a.y, b.y + sign_y, sign_y):
            result.append(PointInt(x_begin, y))
            if p > 0:
                x_begin += sign_x
                p -= 2 * dy
            p += 2 * dx
    else:
        p = 2 * dy - dx
        y_begin = a.y
        for x in range(a.x, b.x + sign_x, sign_x):
            result.append(PointInt(x, y_begin))
            if p > 0:
                y_begin += sign_y
                p -= 2 * dx
            p += 2 * dy
    return result

def draw_rect(p_list):
    p0, p1 = p_list[0:2]
    sign_x, sign_y = sign(p1.x - p0.x), sign(p1.y - p0.y)
    res = []

    if sign_x == 0 or sign_y == 0:
        return res

    for x in range(p0.x, p1.x + sign_x, sign_x):
        res.extend([PointInt(x, p0.y), PointInt(x, p1.y)])

    for y in range(p0.y, p1.y + sign_y, sign_y):
        res.extend([PointInt(p0.x, y), PointInt(p1.x, y)])

    return res


def draw_ellipse(p_list):
    p0, p1 = p_list[0].copy(), p_list[1].copy()

    if p0.x > p1.x:
        p0.x, p1.x = p1.x, p0.x
    if p0.y > p1.y:
        p0.y, p1.y = p1.y, p0.y

    rx, ry = (p1.x - p0.x) / 2, (p1.y - p0.y) / 2
    rx2, ry2 = rx * rx, ry * ry
    xc, yc = (p1.x + p0.x) / 2, (p1.y + p0.y) / 2
    x, y = 0, ry
    quadrant: List[PointInt] = [PointInt(x, y)]
    p = ry2 - rx2 * ry + rx2 / 4

    while ry2 * x < rx2 * y:
        if p >= 0:
            y -= 1
            p += 2 * rx2 * (1 - y)
        p += ry2 * (3 + 2 * x)
        x += 1
        quadrant.append(PointInt(x, y))

    p = ry2 * (x + 0.5) * (x + 0.5) + rx2 * (y - 1) * (y - 1) - rx2 * ry2

    while y > 0:
        if p <= 0:
            x += 1
            p += 2 * ry2 * (1 + x)
        y -= 1
        p += rx2 * (3 - 2 * y)
        quadrant.append(PointInt(x, y))

    result = [PointInt(nx * p.x + xc - 0.001, ny * p.y + yc - 0.001) for p in quadrant for nx in (-1, 1) for ny in (-1, 1)]
    return result

def draw_curve(p_list):
    u, du = 0, 0.001
    n = len(p_list)
    result = []

    while u <= 1:
        p_copy = [PointFloat(p.x, p.y) for p in p_list]

        for i in range(n):
            for j in range(n - 1 - i):
                p0, p1 = p_copy[j], p_copy[j + 1]
                p_copy[j] = PointFloat((1 - u) * p0.x + u * p1.x, (1 - u) * p0.y + u * p1.y)

        result.append(PointInt(int(p_copy[0].x + 0.5), int(p_copy[0].y + 0.5)))
        u += du

    return result


def draw_polygon(p_list):

    if len(p_list) == 2:
        return draw_line(p_list)
    result = []
    for i in range(len(p_list)):
        result.extend(draw_line([p_list[i - 1], p_list[i]]))
    return result

def draw(type, p_list):
    return DRAW_FUNC[type](p_list)

DRAW_TYPE = Callable[[List[PointInt], str], List[PointInt]]
DRAW_FUNC: Dict[str, DRAW_TYPE] = {
    'line': draw_line, 'ellipse': draw_ellipse, 'polygon': draw_polygon, 'curve': draw_curve, 'rect': draw_rect
}

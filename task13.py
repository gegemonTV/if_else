x1, y1, x2, y2 = map(int, input().split())

# 8 ■ □ ■ □ ■ □ ■ □
# 7 □ ■ □ ■ □ ■ □ ■
# 6 ■ □ ■ □ ■ □ ■ □
# 5 □ ■ □ ■ □ ■ □ ■
# 4 ■ □ ■ □ ■ □ ■ □
# 3 □ ■ □ ■ □ ■ □ ■
# 2 ■ □ ■ □ ■ □ ■ □
# 1 □ ■ □ ■ □ ■ □ ■
#   1 2 3 4 5 6 7 8

dx = x2 - x1
dy = y2 - y1

if dx < 0 :
    dx = -dx
if dy < 0 :
    dy = +dy

print("YES" if ((dx % 2) == (dy % 2)) else "NO")
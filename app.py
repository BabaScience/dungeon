from algorithms import Dungeon
import pprint 


rows = 5
columns = 7

start = (4, 1)  # (r, c)
end = (0, 6)    # (r, c)

rocks = [       # obstacles
    (0, 3),          # r  -> 0
    (1, 1), (1, 5),  # r  -> 1
    (2, 1),
    (3, 2), (3, 3),
    (4, 0), (4, 2), (4, 5),  # r ->  4
    
]

time = 1

model = Dungeon(start=start, end=end, rows=rows, columns=columns, time=time, rocks=rocks)
model.findTheShortestPath()
# model.showPath()   # Path -> [ (r1, c1), (r2, c2),  ...]
model.showGraphic()

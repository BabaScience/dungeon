# this algorithm is optimed for the
# Dungeon Problem statement

from myQueue import Queue
import pprint
import time


class Dungeon:
    def __init__(self, start=(), end=(), rocks=[], rows=0, columns=0, time=1):
        self.visited = [[False for j in range(columns)] for i in range(rows)]
        self.start = start
        self.end = end
        self.rocks = rocks
        self.rows = rows
        self.columns = columns
        self.prev = [[None for _ in range(columns)] for __ in range(rows)]
        self.path = []
        self.queue = Queue()
        self.history = Queue()
        self.graph = []
        self.time = time

    def showGraphic(self):
        recovery = self.start
        self.__showGraph()
        for position in self.path:
            self.start = position
            self.__showGraph()
            time.sleep(self.time)
        self.start = recovery

    def __showGraph(self):
        self.graph = [[" " for _ in range(self.columns)]
                      for __ in range(self.rows)]
        for rock in self.rocks:
            a, b = rock
            self.graph[a][b] = "#"
        a, b = self.start
        if self.start == self.end:
            self.graph[a][b] = "S"
        else:
            self.graph[a][b] = "S"
            a, b = self.end
            self.graph[a][b] = "E"
        print("\n\n\n\n")
        pprint.pprint(self.graph)

    def showPath(self):
        print(self.path)

    def __Enqueue(self, node):
        self.queue.enqueue(node)
        self.history.enqueue(node)

    def findTheShortestPath(self):
        self.__bfs()
        #print("Previous -- ", self.prev)
        self.__reconstructPath()
        # print(self.path)

    def __bfs(self):
        a, b = self.start
        self.visited[a][b] = True
        self.__Enqueue(self.start)
        while not self.queue.isEmpty():
            node = self.queue.dequeue()
            #print("node", node)
            for neighbour in self.__findNeighbours(node):
                if neighbour != None:
                    self.__Enqueue(neighbour)
                    #print("\t->", neighbour)
                    i, j = neighbour
                    self.visited[i][j] = True
                    self.prev[i][j] = node
        #print("previous --", self.prev)
        # self.show_history()

    def show_history(self):
        self.history.showQueue()

    def __reconstructPath(self):
        x, y = self.end
        at = self.prev[x][y]
        if self.prev[x][y] != None:
            self.path.append(self.end)
            while at != None:
                x, y = at
                self.path.append(at)
                at = self.prev[x][y]
            self.path.reverse()

    def __findNeighbours(self, position):
        neighbours = []
        r, c = position
        #print("row:", position[0])
        #print("column:", position[1])
        if r == 0 and c == 0:  # left-Up corner
            #print("left-up corner")
            neighbours.append(self.__getDownNeighbour(position))
            neighbours.append(self.getRightNeighbour(position))
        elif r == 0 and c == self.columns-1:  # Right_up corner
            #print("right-up corner")
            neighbours.append(self.__getDownNeighbour(position))
            neighbours.append(self.__getLeftNeighbour(position))
        elif r == self.rows-1 and c == 0:  # Left_down corner
            #print("left-down corner")
            neighbours.append(self.__getUpNeighbour(position))
            neighbours.append(self.getRightNeighbour(position))
        elif r == self.rows-1 and c == self.columns-1:  # Right_down corner
            #print("down-right corner")
            neighbours.append(self.__getUpNeighbour(position))
            neighbours.append(self.__getLeftNeighbour(position))
        elif c == 0 and self.rows-1 > r > 0:  # left
            # print("left")
            neighbours.append(self.getRightNeighbour(position))
            neighbours.append(self.__getDownNeighbour(position))
            neighbours.append(self.__getUpNeighbour(position))
        elif r == 0 and self.columns-1 > c > 0:  # up
            # print("up")
            neighbours.append(self.getRightNeighbour(position))
            neighbours.append(self.__getDownNeighbour(position))
            neighbours.append(self.__getLeftNeighbour(position))
        elif c == self.columns-1 and self.rows-1 > r > 0:  # Right
            # print("right")
            neighbours.append(self.__getLeftNeighbour(position))
            neighbours.append(self.__getDownNeighbour(position))
            neighbours.append(self.__getUpNeighbour(position))
        elif r == self.rows-1 and self.columns-1 > c > 0:  # Down
            # print("down")
            neighbours.append(self.__getLeftNeighbour(position))
            neighbours.append(self.getRightNeighbour(position))
            neighbours.append(self.__getUpNeighbour(position))
        else:  # center
            # print("center")
            neighbours.append(self.__getLeftNeighbour(position))
            neighbours.append(self.getRightNeighbour(position))
            neighbours.append(self.__getDownNeighbour(position))
            neighbours.append(self.__getUpNeighbour(position))
        return neighbours

    def getRightNeighbour(self, position):  # (r, c)
        right = (position[0], position[1]+1)
        a, b = right
        if not self.visited[a][b] and right not in self.rocks:
            return ((a, b))
        return

    def __getLeftNeighbour(self, position):  # (r, c)
        left = (position[0], position[1]-1)
        a, b = left
        if not self.visited[a][b] and left not in self.rocks:
            return ((a, b))
        return

    def __getUpNeighbour(self, position):  # (r, c)
        up = (position[0]-1, position[1])
        a, b = up
        if not self.visited[a][b] and up not in self.rocks:
            return ((a, b))
        return

    def __getDownNeighbour(self, position):  # (r, c)
        down = (position[0]+1, position[1])
        a, b = down
        if not self.visited[a][b] and down not in self.rocks:
            return ((a, b))
        return

    def __getAllNeighbour(self, position):  # (r, c)
        neighbours = []
        neighbours.append(self.getRightNeighbour(position))
        neighbours.append(self.__getLeftNeighbour(position))
        neighbours.append(self.__getUpNeighbour(position))
        neighbours.append(self.__getDownNeighbour(position))
        return neighbours

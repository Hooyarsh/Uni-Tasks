import random
import collections
from collections import deque
from colorama import Fore
import os

wall, free, goal = 0, 1, 9


def save(random_maze, width, height):
    f = open('/Users/hooyarsh/Desktop/output.txt', 'w')
    f.write(str(height)+' ')
    f.write(str(width) + ' ')
    for i in range(height):
        for j in range(width):
            f.write(str(random_maze[i][j]) + ' ')
    f.close()


def Print(random_maze, width, height):
    for i in range(height):
        for j in range(width):
            if (random_maze[i][j] == 1):
                print(Fore.GREEN + "c", end=" ")
            elif (random_maze[i][j] == 9):
                print(Fore.BLUE + "g", end=" ")
            elif (random_maze[i][j] == 5):
                print(Fore.BLUE + "s", end=" ")
            else:
                print(Fore.RED + "w", end=" ")
        print()


def load():
    f = open("/Users/hooyarsh/Desktop/output.txt", "r")
    txt = f.readline().split()
    # print('txt=', txt)
    height = int(txt[0])
    width = int(txt[1])
    random_maze = [[random.randint(0, 1)
                    for i in range(width)] for j in range(height)]
    i = 2
    for j in range(height):
        for k in range(width):
            random_maze[j][k] = int(txt[i])
            i += 1
    startPoint = 0
    endPoint = 0
    for i in range(width):
        if random_maze[height-1][i] == 9:
            endPoint = i
        if random_maze[0][i] == 5:
            startPoint = i
    # print('startPoint= ', startPoint)
    for i in range(height):
        for j in range(width):
            if (random_maze[i][j] == 1):
                print(Fore.GREEN + "c", end=" ")
            elif (random_maze[i][j] == 9):
                print(Fore.BLUE + "g", end=" ")
            elif (random_maze[i][j] == 5):
                print(Fore.BLUE + "s", end=" ")
            else:
                print(Fore.RED + "w", end=" ")
        print()
    wasd(random_maze=random_maze, width=width, height=height,
         startpoint=startPoint, endpoint=endPoint)


def bfs(maze, start, width, height):
    queue = collections.deque()
    queue.append(start)
    seen = set(start)
    while queue:
        path = queue.popleft()
        x, y = path
        if maze[x][y] == goal:
            return True
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 and x2 < height and 0 <= y2 and y2 < width and maze[x2][y2] != wall and (x2, y2) not in seen:
                queue.append((x2, y2))
                seen.add((x2, y2))
    return False


def matrix_generator(width, height, start, end):
    random_maze = [[random.randint(0, 1)
                    for i in range(width)] for j in range(height)]
    # ww = random.randint(1, w)
    # hh = random.randint(1, h)
    for i in range(width):
        random_maze[0][i] = 0
    for i in range(height):
        random_maze[i][0] = 0
    for i in range(width):
        random_maze[height-1][i] = 0
    for i in range(height):
        random_maze[i][width-1] = 0

    random_maze[0][start] = 5
    random_maze[height-1][end] = 9
    aq = deque(random_maze)
    check = bfs(aq, (0, start), width, height)
    if check == True:
        Print(random_maze=random_maze, width=width, height=height)
    return check, random_maze


def wasd(random_maze, width, height, startpoint, endpoint):
    si = 0
    sj = startpoint

    while (True):
        if (si == height - 1 and sj == endpoint):
            print("You WON!")
            print("Print any key to continue!")
            a = input()
            break
        # si != height - 1 and sj != endpoint-1
        # print ('sj=',sj)
        t = input()

        os.system('cls' if os.name == 'nt' else "clear")
        if t[0] == "w":
            if si-1 >= 0 and random_maze[si-1][sj] != 0:
                random_maze[si][sj] = 1
                random_maze[si-1][sj] = 5
                si -= 1
                sj = sj
                Print(random_maze=random_maze, width=width, height=height)

            else:
                print("invalid move")
                Print(random_maze=random_maze, width=width, height=height)

        elif t[0] == "s":
            if si+1 < height and random_maze[si+1][sj] != 0:
                random_maze[si][sj] = 1
                random_maze[si+1][sj] = 5
                si += 1
                sj = sj
                Print(random_maze=random_maze, width=width, height=height)

            else:
                print("invalid move")
                Print(random_maze=random_maze, width=width, height=height)

        elif t[0] == "a":
            if sj-1 >= 0 and random_maze[si][sj-1] != 0:
                random_maze[si][sj] = 1
                random_maze[si][sj-1] = 5
                si = si
                sj -= 1
                Print(random_maze=random_maze, width=width, height=height)
            else:
                print("invalid move")
                Print(random_maze=random_maze, width=width, height=height)

        elif t[0] == "d":
            if sj+1 >= 0 and random_maze[si][sj+1] != 0:
                random_maze[si][sj] = 1
                random_maze[si][sj+1] = 5
                si = si
                sj += 1
                Print(random_maze=random_maze, width=width, height=height)
            else:
                print("invalid move")
                Print(random_maze=random_maze, width=width, height=height)

        elif t[0] == 'e':
            os.system('cls' if os.name == 'nt' else "clear")
            return
        elif t[0] == 'v':
            save(random_maze, width, height)
            Print(random_maze=random_maze, width=width, height=height)

        else:
            print("Invalid input!")
            Print(random_maze=random_maze, width=width, height=height)


def startGame():
    width, height = map(int, input("Enter width & height of maze: ").split())

    start_point = 0
    while True:
        start_point = int(input('Enter your StartPoint: '))

        if start_point < 0 or start_point >= width:
            print(
                f'Invalid input! Please enter number between 0 and {width-1}')
            continue
        else:
            break
    end_point = 0
    while True:
        end_point = int(input('Enter your EndPoint: '))

        if end_point < 0 or end_point >= width:
            print(
                f'Invalid input! Please enter number between 0 and {width-1}')
            continue
        else:
            break
    temp = matrix_generator(width, height, start_point, end_point)
    is_valid = temp[0]
    temp1 = 0
    while (is_valid == False):
        temp1 = matrix_generator(width, height, start_point, end_point)
        is_valid = temp1[0]

    # print(temp1[1])
    wasd(temp1[1], width, height, start_point, end_point)


if __name__ == "__main__":
    while (True):
        os.system('cls' if os.name == 'nt' else "clear")
        print("    MAZE    ")
        print("1_Start Game")
        print("2_Load")
        print("3_End")
        a1 = input()
        if a1[0] == '1':
            startGame()
            print('\n\n\n\n\n')
        elif a1[0] == "2":
            load()
        elif a1[0] == "3":
            exit()

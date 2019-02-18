import math
import random

class sudoku:
    size = 0
    sudoku_list = []
    check_flag = True

    def __init__(self):
        print("### SUDOKU SOLVER ###");
        while True:
            self.size = int(input("Enter the square size of sudoku: "))
            choice = input("Type 'yes' to proceed, 'no' to enter again :")
            if choice == "yes":
                break

    def build_sudoku(self):
        choice_pseudo = input("Press 'x' Build sudoku or 'y' for a random pre-defined sudoku: ")
        if choice_pseudo == "x":
            pred_list = []
            while True:
                choice = input("Press 'yes' to proceed or any other key to enter values into sudoku: ")
                if choice == "yes":
                    break
                while True:
                    x = int(input("Enter X coordinate: "))
                    if x > self.size:
                        print("out of bound. Enter again.")
                        continue
                    y = int(input("Enter Y coordinate: "))
                    if y > self.size:
                        print("out of bound. Enter again.")
                        continue
                    val = int(input("Enter value: "))
                    if val > self.size:
                        print("out of bound. Enter again.")
                        continue
                    pred_list.append([x, y, val])
                    break
            for i in range(0, self.size):
                temp_list = []
                for j in range(0, self.size):
                    flag = False
                    for search_i in range(0, len(pred_list)):
                        if i == pred_list[search_i][0] and j == pred_list[search_i][1]:
                            temp_list.append(pred_list[search_i][2])
                            flag = True
                            break
                    if flag is False:
                        temp_list.append(0)
                self.sudoku_list.append(temp_list)

        elif choice_pseudo == "y":
            if self.size == 9:
                random_seed = random.randint(1, 3)
                if random_seed == 1:
                    self.sudoku_list = [[6, 5, 0, 0, 0, 4, 7, 0, 9], [0, 0, 8, 6, 2, 0, 0, 1, 0],
                                        [9, 2, 3, 0, 5, 0, 8, 0, 0],
                                        [0, 0, 0, 0, 6, 5, 0, 0, 2], [8, 4, 0, 0, 0, 7, 3, 9, 5],
                                        [0, 1, 2, 8, 9, 3, 0, 0, 6],
                                        [7, 0, 9, 0, 3, 0, 6, 4, 0], [0, 3, 4, 0, 0, 0, 2, 5, 0],
                                        [0, 0, 0, 1, 0, 8, 0, 0, 7]]
                else:
                    self.sudoku_list = [[0, 0, 0, 2, 0, 1, 9, 0, 0], [4, 7, 5, 0, 0, 0, 0, 0, 6],
                                        [0, 0, 0, 0, 6, 0, 0, 8, 3],
                                        [0, 0, 8, 0, 5, 0, 1, 7, 0], [9, 0, 0, 0, 0, 3, 0, 2, 4],
                                        [6, 2, 1, 9, 7, 0, 5, 0, 0],
                                        [0, 9, 0, 0, 3, 7, 8, 6, 0], [7, 0, 2, 4, 0, 0, 0, 9, 0],
                                        [5, 3, 0, 8, 0, 9, 7, 0, 1]]

            elif self.size == 4:
                random_seed = random.randint(1, 5)
                if random_seed == 1:
                    self.sudoku_list = [[1, 0, 4, 0], [0, 3, 0, 0], [0, 0, 2, 0], [0, 1, 0, 4]]
                elif random_seed == 2:
                    self.sudoku_list = [[0, 4, 0, 3], [2, 0, 0, 0], [0, 0, 0, 1], [4, 0, 3, 0]]
                elif random_seed == 3:
                    self.sudoku_list = [[0, 2, 4, 0], [0, 0, 0, 2], [3, 0, 0, 0], [0, 1, 3, 0]]
                else:
                    self.sudoku_list = [[0, 0, 4, 0], [1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 3]]
        else:
            print("Sudoku with given size doesnt exist. Try Again")

    def show_sudoku(self):
        print("*** Sudoku ***")
        for i in range(0, self.size):
            print(self.sudoku_list[i])

    def check_rules(self, num, x, y):
        for i in range(0, self.size):
            if self.sudoku_list[x][i] == num:   # Compare the columns of 'i'th row
                return False

        for i in range(0, self.size):
            if self.sudoku_list[i][y] == num:   # Compare the rows of 'j'th column
                return False

        sqroot = int(math.sqrt(self.size))
        quantum_x = sqroot * (x // sqroot)
        quantum_y = sqroot * (y // sqroot)
        for i in range(quantum_x, quantum_x+sqroot):
            for j in range(quantum_y, quantum_y+sqroot):
                if self.sudoku_list[i][j] == num:       # compare inside the block
                    return False
        return True

    def solve_sudoku(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.sudoku_list[i][j] != 0:
                    continue
                temp_list = []  #list of possible values that can be fit in a sq
                for k in range(1, self.size+1):
                    if self.check_rules(k, i, j):
                        temp_list.append(k)
                self.sudoku_list[i][j] = temp_list

        # self.show_sudoku()
        count = 0
        return_flag = True
        while self.check_flag:
            count += 1
            for i in range(0, self.size):
                for j in range(0, self.size):
                    if isinstance(self.sudoku_list[i][j], int):     # check if it is int or a list
                        continue
                    elif len(self.sudoku_list[i][j]) == 1:
                        self.sudoku_list[i][j] = self.sudoku_list[i][j][0]
                        continue
                    else:
                        temp_list = []
                        for k in self.sudoku_list[i][j]:
                            if self.check_rules(k, i, j):
                                temp_list.append(k)
                        self.sudoku_list[i][j] = temp_list
            local_flag = False
            for i in range(0, self.size):
                for j in range(0, self.size):
                    if isinstance(self.sudoku_list[i][j], int) is False:
                        local_flag = True
            if not local_flag:
                self.check_flag = False
            if count > 20000:
                return_flag = False
                print("counted : " + str(count))
                break
        return return_flag


Sudo = sudoku()
Sudo.build_sudoku()

Sudo.show_sudoku()
if Sudo.solve_sudoku():
    print("Solved Successfully")
else:
    print("Cannot solve the sudoku puzzle. Est sol is")
Sudo.show_sudoku()

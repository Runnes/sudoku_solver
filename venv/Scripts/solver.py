from deepdiff import DeepDiff
from pprint import pprint
import sys
from functools import lru_cache
import functools
import random
import os

# first_quadrant = ['-','-',5,2,6,'-','-',1,'-']
# second_quadrant = ['-','-','-','-','-',9,'-','-',4]
# third_quadrant = [ '-','-',4,'-',7,'-','-','-',9]
# fourth_quadrant = [6,2,7,'-',9,8,'-','-','-']
# fifth_quadrant = [5,'-','-','-','-','-','-','-','-']
# sixth_quadrant = ['-', '-', '-', '-', '-', '-', '-', 7, '-']
# seventh_quadrant = ['-','-',8,3,'-',6,4,5,7]
# eight_quadrant = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
# ninth_quadrant = [1, '-', '-', '-', '-', '-', 8, 3, '-']


first_quadrant = ['-',3,'-',8,'-','-','-','-',5]
second_quadrant = [4,6,'-','-',7,2,'-',8,3]
third_quadrant = [9,8,'-','-',5,'-',7,'-','-']
fourth_quadrant = [6,4,'-',8,'-',3,'-','-',9]
fifth_quadrant = ['-',5,'-','-','-',1,6,'-','-']
sixth_quadrant = ['-','-','-',4,6,'-',8,'-','-']
seventh_quadrant = ['-','-','-','-','-','-','-','-','-',6]
eight_quadrant = [5,7,6,'-',1,9,'-','-','-']
ninth_quadrant = [2,3,8,6,4,7,9,5,'-']

all_quadrants = []
all_quadrants.append(first_quadrant)
all_quadrants.append(second_quadrant)
all_quadrants.append(third_quadrant)
all_quadrants.append(fourth_quadrant)
all_quadrants.append(fifth_quadrant)
all_quadrants.append(sixth_quadrant)
all_quadrants.append(seventh_quadrant)
all_quadrants.append(eight_quadrant)
all_quadrants.append(ninth_quadrant)

one_list = first_quadrant + second_quadrant + third_quadrant + fourth_quadrant + fifth_quadrant + sixth_quadrant + seventh_quadrant + eight_quadrant + ninth_quadrant

Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Reset = "\u001b[0m"

dict_for_colors = {
    0: Black,
    1: Red,
    2: Green,
    3: Yellow,
    4: Blue,
    5: Magenta,
    6: Cyan,
    7: White,
    8: Magenta

}

def printing(quadrants_copy):
    random_list = [x for x in range(0, 9)]
    for z in range(0, len(quadrants_copy) - 1, 9):
        color_index = random.choice(random_list)
        print(dict_for_colors[color_index], *quadrants_copy[z:z + 9], Reset)
        random_list.remove(color_index)


def check_function(quadrants, cell_index):
    possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_of_movements = [-72, -63, -54, -45, -36, -27, -18, -9, 9, 18, 27, 36, 45, 54, 63, 72]
    for x in list_of_movements:
        # print("trying to remove ",quadrants[cell_index+x])
        try:
            possibilities.remove(quadrants[cell_index + x])

        except:
            pass

        else:
            pass
            #print("up and down reason, removed: ", quadrants[cell_index + x])
    for y in range(cell_index, cell_index + 9 - cell_index % 9):
        try:

            possibilities.remove(quadrants[y])

        except:
            pass

        else:
            pass
            #print("right reason, removed: ", quadrants[y])
    for y in range(cell_index, cell_index - cell_index % 9 - 1, -1):
        try:
            possibilities.remove(quadrants[y])
            # if cell_index==8:
            #     print("usunalem",y)
            #     ##input()

        except:
            pass
        else:
            pass
            #print("left reason, removed: ", quadrants[y])

    if cell_index in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
        lista = [10, 11, 19, 20]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass

            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])
    if cell_index in [1, 4, 7, 28, 31, 34, 55, 58, 61]:
        lista = [8, 10, 17, 19]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass
            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])

    if cell_index in [2, 5, 8, 29, 32, 35, 56, 59, 62]:
        lista = [7, 8, 16, 17]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass
            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])
    if cell_index in [9, 12, 15, 36, 39, 42, 63, 66, 69]:
        lista = [-8, -7, 10, 11]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass
            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])
    if cell_index in [10, 13, 16, 37, 40, 43, 64, 67, 70]:
        lista = [-8, -10, 8, 10]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass
            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])

    if cell_index in [11, 14, 17, 38, 41, 44, 65, 68, 71]:
        lista = [8, 7, -10, -11]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass
            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])

    if cell_index in [18, 21, 24, 45, 48, 51, 72, 75, 78]:
        lista = [-8, -7, -17, -16]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass
            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])

    if cell_index in [19, 22, 25, 46, 49, 52, 73, 76, 79]:
        lista = [-8, -10, -17, -19]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass
            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])

    if cell_index in [20, 23, 26, 47, 50, 53, 74, 77, 80]:
        lista = [-10, -11, -19, -20]
        for x in lista:
            try:
                possibilities.remove(quadrants[cell_index + x])
            except:
                pass
            else:
                pass
                #print("quadrant reason, removed: ", quadrants[cell_index + x])
    # if cell_index ==3:
    #     print("poss for ",cell_index,possibilities)
    #     ###input()

    #print("checking cell index: ", cell_index)
    #print("check fun returns: ", possibilities)
    # if cell_index ==58:
    #     print("poss from main func ",possibilities)
    #     #input(0)
    return possibilities


def test(quadrants, possibilities, cell_index):
    total_possibilities_for_block = []
    # print(possibilities)
    # for possibility in possibilities:
    # print(cell_index,"posib",possibility)

    if cell_index in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
        lista = [0, 1, 2, 9, 18, 10, 11, 19, 20]
        for x in lista:
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))
                    #print("total possibilities for block: ", total_possibilities_for_block)

            except:
                pass

    elif cell_index in [1, 4, 7, 28, 31, 34, 55, 58, 61]:
        lista = [0, -1, 1, 9, 18, 8, 10, 17, 19]
        for x in lista:
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))
            except:
                pass



    elif cell_index in [2, 5, 8, 29, 32, 35, 56, 59, 62]:
        lista = [0, -2, -1, 9, 18, 7, 8, 16, 17]
        for x in lista:
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))
            except:
                pass

    elif cell_index in [9, 12, 15, 36, 39, 42, 63, 66, 69]:
        lista = [0, -9, 9, 1, 2, -8, -7, 10, 11]
        for x in lista:
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))

            except:
                pass

    elif cell_index in [10, 13, 16, 37, 40, 43, 64, 67, 70]:
        lista = [0, -1, 1, -9, 9, -8, -10, 8, 10]
        for x in lista:
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))
            except:
                pass

    elif cell_index in [11, 14, 17, 38, 41, 44, 65, 68, 71]:
        lista = [0, -1, -2, -9, 9, 8, 7, -10, -11]
        for x in lista:
            # if cell_index == 71:
            #     total_possibilities_for_block.sort()
            #     print(quadrants[cell_index+x],total_possibilities_for_block)
            #     ##input()
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))
                    #print(" cell_index +x = ", cell_index + x, "value there currently is: ", quadrants[cell_index + x],
                          #total_possibilities_for_block)

            except:
                pass

    elif cell_index in [18, 21, 24, 45, 48, 51, 72, 75, 78]:
        lista = [0, -9, -18, 1, 2, -8, -7, -17, -16]

        for x in lista:
            #print("checking quadrant, cell index:", cell_index + x)
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))
            except:
                pass

    elif cell_index in [19, 22, 25, 46, 49, 52, 73, 76, 79]:
        lista = [0, -1, 1, -9, -18, -8, -10, -17, -19]
        for x in lista:
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))
            except:
                pass

    elif cell_index in [20, 23, 26, 47, 50, 53, 74, 77, 80]:
        lista = [0, -2, -1, -9, -18, -10, -11, -20, -19]
        for x in lista:
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_for_block += check_function(quadrants, (cell_index + x))
            except:
                pass

    # ##input("przeszlo raz")
    # print(" cell_index +x = ", cell_index + x, "value there currently is: ", quadrants[cell_index + x],total_possibilities_for_block)
    #print("total z formuly: ", total_possibilities_for_block)
    list = ['temp', ]
    for pos in possibilities:
        formula = total_possibilities_for_block.count(pos)
        #print(pos, "total occurence", total_possibilities_for_block.count(pos))
        if formula == 1:
            # print(total_possibilities_for_block)
            # print(total_possibilities_for_block.count(pos))
            list.append(pos)
            # return pos
    #
    if len(list) == 2:
        #print("Quadrant ONLY ",list)
        ##input()
        return list[1]



def test_possibilities_row(quadrants, possibilities, cell_index):
    total_possibilities_row = []
    lista = ['temp']
    #print(possibilities)
    #input()
    if isinstance(possibilities, int) == False:
        try:
            for possibility in possibilities:
                for x in range(1,10):
                    try:
                        if quadrants[cell_index+x] == '-':
                            total_possibilities_row+=check_function(quadrants, (cell_index+x))
                    except:
                        pass

        except:
            pass
        else:
            pass
            #

            #print(possibilities)


        for pos in possibilities:
            formula = total_possibilities_row.count(pos)
            xxx=2#print(pos,"total occurence",total_possibilities_row.count(pos))
            if  formula==1:
                lista.append(pos)

    else:
        formula = total_possibilities_row.count(possibilities)
        if formula == 1:
            lista.append(possibilities)
    # if cell_index ==58:
    #     xxx=2#print("poss for quadrant ",cell_index,possibilities)
    #     ##input()
    #print("possibilities ROW ",possibilities)
    #print("ROW ZWRACA ", lista)
    if len(lista)==2:
        #print("ROW ZWRACA ",lista)
        ##input()
        return lista[1]


def test_possibilities_col(quadrants, possibilities,cell_index):
    total_possibilities_col=[]
    #print(not isinstance(possibilities,int))
    if isinstance(possibilities,int)==False :
        try:
            for possibility in possibilities:
                for x in range(1,10):
                    try:
                        if quadrants[cell_index+x] == '-':
                            total_possibilities_col+=check_function(quadrants, (cell_index*x))
                    except:
                        pass
        except:
            pass
            #print("wyskoczyl error")
        else:
            pass
            #print(possibilities)

    else:
        for x in range(1, 10):
            try:
                if quadrants[cell_index + x] == '-':
                    total_possibilities_col += check_function(quadrants, (cell_index * x))
            except:
                pass
    lista=['temp']
    if isinstance(possibilities, int) == False:
        for pos in possibilities:
            formula = total_possibilities_col.count(pos)

            if  formula==1:
                lista.append(pos)
    else:
        formula = total_possibilities_col.count(possibilities)

        if formula == 1:
            lista.append(possibilities)


    if len(lista)==2:
        #print("COL ZWRACA ",lista)
        ##input()
        return lista[1]


def check_number(quadrants,steps):
    cell_index = 0
    counter = quadrants.count("-")
    counter_after = quadrants.count("-")

    for cell in quadrants:

        if cell == '-':
            #print("i am checking cell index: ", cell_index, "cell value: ", cell)
            y = check_function(quadrants, cell_index)
            #print("return z funckji check: ", y)
            only_possibility = test(quadrants, y, cell_index)
            #print("only poss, test QUADRANT ONLY returns: ", only_possibility)
            only_possibility_row = test_possibilities_row(quadrants, y, cell_index)
            #print("only poss, test ROW ONLY returns: ", only_possibility_row)
            only_possibility_col = test_possibilities_col(quadrants, y, cell_index)
            #print("only poss, test COL ONLY returns: ", only_possibility_col)
            quadrants_copy = quadrants.copy()
            #print("lentgh of y is: ", len(y))
            if isinstance(only_possibility, int):

                quadrants_copy[cell_index] = only_possibility

                print("row: ", round(cell_index / 9, 0), "col: ", cell_index % 9 + 1,
                      "zrobilem only instancje" + ", with cell index " + str(
                          cell_index) + " Quadrant only possibility was " + str(only_possibility))
                print("counter of missing values: ", counter)
                print(DeepDiff(quadrants, quadrants_copy))
                printing(quadrants_copy)
                input()

            elif len(y) == 1 and not isinstance(only_possibility_col, int):

                quadrants_copy[cell_index] = y[0]
                counter_after = quadrants_copy.count("-")
                counter = counter_after
                print("row: ", round(cell_index / 9, 0), "col: ", cell_index % 9 + 1, "dodalem liczbe, przez only COL pos: ", y,
                      " w indxie: ", cell_index)
                #input()
                print("counter of missing values: ", counter)
                print(DeepDiff(quadrants, quadrants_copy))
                printing(quadrants_copy)
            # if cell_index ==39:
                input()


            elif isinstance(only_possibility_row,int):

                quadrants_copy[cell_index] = only_possibility_row

                print("row: ",round(cell_index/9,0), "col: ",cell_index%9+1,"zrobilem only instancje" + ", with cell index " + str(cell_index) + " only possibility was " + str(only_possibility_row))
                # if steps:
                print("counter of missing values: ", counter)
                print(DeepDiff(quadrants, quadrants_copy))
                printing(quadrants_copy)
                input()

            elif isinstance(only_possibility_col,int):

                quadrants_copy[cell_index] = only_possibility_col

                print("row: ",round(cell_index/9,0), "col: ",cell_index%9+1,"zrobilem only instancje" + ", with cell index " + str(cell_index) + " only possibility was " + str(only_possibility_row))
                # if steps:
                print("counter of missing values: ", counter)
                print(DeepDiff(quadrants, quadrants_copy))
                printing(quadrants_copy)
                input()



            # print(
            #     "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            #
            # print(
            #     "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

            print(u"{}[2J{}[;H".format(chr(27), chr(27)))
            #input()


            quadrants = quadrants_copy.copy()
            # print(cell_index)
        cell_index += 1
        # ##input()

        # if counter_after > counter:
        #     print(DeepDiff(quadrants, quadrants_copy))
        #     return

    # print(quadrants)
    return quadrants


# ilosc_pauz = check_number(one_list).count("-")
# print(ilosc_pauz)

# while ilosc_pauz>-1:
#     new_list = check_number(one_list)
#     ilosc_pauz = check_number(new_list).count("-")
#     one_list=new_list


def sudoku(list,steps=True):
    ilosc_pauz = check_number(list,False).count("-")
    # print(ilosc_pauz)
    while ilosc_pauz !=0:

        print("ilosc pauzz teraz to: ", ilosc_pauz)
        ilosc_pauz = check_number(list,False).count("-")
        new_list = check_number(list,False)

        list = new_list
        print("ilosc pauzz teraz to: ",ilosc_pauz)
    #new_list=list
    random_list = [x for x in range(0, 9)]
    for z in range(0, len(new_list) - 1, 9):
        color_index = random.choice(random_list)
        print(dict_for_colors[color_index], *list[z:z + 9], Reset)
        random_list.remove(color_index)


sudoku(one_list)

# print(sys.getrecursionlimit())



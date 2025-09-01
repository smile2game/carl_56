# encoding: utf-8
# a = input("please input a number:")
# print("hello world")

table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2sfgubhigfwsueghigfush1yguyguyg', 'ceshiyixiaba n2'],
    ['row3 column1', 'row3 column2']
]

#head num
#row num 是变化的 
def table_print(table_data):
    col = len(table_data[0])
    row = len(table_data) - 1 

    # hang_max = 0
    # for i in range(row):
    #     for j in range(col):
    #         hang_max = max(hang_max,len(table_data[i][j]))
    # print(f"hang_max is {hang_max}")
    # hang = "+" + "-" * hang_max + "--" #1+18

    hang_max = [0] * col
    hang = []
    for j in range(col):
        for i in range(row):
            # hang_max = max(hang_max,len(table_data[i][j]))
            hang_max[j] = max(hang_max[j],len(table_data[i][j]))
    # print(f"hang_max is {hang_max}")
    # hang = "+" + "-" * hang_max + "--" #1+18
    for i in range(col):
        hang.append( "+" + "-" * hang_max[i] + "--")
    # print(f"hang is {hang}")

    #分割线 
    for i in range(col):
        print(f"{hang[i]}",end = '') 
    print(f"+")

    #打表头
    for i in range(col):
        s_len = len(table_data[0][i])
        # print(f"s_len is {s_len}")
        print(f"| {table_data[0][i]}" + " " * (hang_max[i] - s_len + 1),end = '')
    print(f"|",end = "")
    print("")

    #分割线 
    for i in range(col):
        print(f"{hang[i]}",end = '') 
    print(f"+")

    #打表内容 
    for j in range(1,row+1):
        for i in range(col):
            s_len = len(table_data[j][i])
            print(f"| {table_data[j][i]}" + " " * (hang_max[i]- s_len +1 ),end = '') #9space
        print(f"|",end = "")
        print("")

    #分割线 
    for i in range(col):
        print(f"{hang[i]}",end = '') 
    print(f"+")
    

table_print(table_data)
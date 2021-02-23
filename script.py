board = [['0' for x in range(3)] for _ in range(3)]
list_empty= {}
count = 0
for i in range(len(board)):
    print(board[i])
    for row in range(len(board)):
        print(row)
    # for el in range(len(row)):
    #     if row[el] == 0:
    #         list_empty.update({count: el})

# print(f"empy indexing: {list_empty}")
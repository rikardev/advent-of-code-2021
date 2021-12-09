
numbers = []
boards = []
marks = []

with open('input1') as f:
    lines = f.readlines()
    nums = lines[0]
    for n in nums.split(','):
        numbers.append(int(n))

    lines = lines[2:]
    while len(lines) >= 5:
        board = []
        for j in range(5):
            board.extend([int(x) for x in lines[j].rstrip().split()])
        boards.append(board)
        marks.append([0] * len(board))
        lines = lines[6:]
        
    print(boards)
    print(marks)

def mark_board(board: list, marks: list, num: int) -> bool:
    for i, n in enumerate(board):
        if n == num:
            marks[i] = 1
            # check column
            col = i % 5
            if sum([marks[5*row+col] for row in range(5)]) == 5:
                return True
            
            # check row
            row = int(i / 5)
            if sum([marks[5*row+col] for col in range(5)]) == 5:
                return True

            return False
    
    return False

def calc_score(board: list, marks: list, num: int) -> int:
    return num * sum([board[k] for k, mark in enumerate(marks) if mark == 0])

def print_board(board, marks):
    for i in range(5):
        print(",".join([str(num) for num in board[5*i:5*i+5]]))
    for i in range(5):
        print(",".join([str(num) for num in marks[5*i:5*i+5]]))

for num in numbers:
    boards_left = []
    marks_left = []
    for i, board in enumerate(boards):
        bingo = mark_board(board, marks[i], num)
        if not bingo:
            boards_left.append(board)
            marks_left.append(marks[i])
            #print_board(board, marks[i])
        #else:
            #print("Removing bingoed board", num)
            #print_board(board, marks[i])

    if len(boards_left) == 0:
        score = calc_score(boards[0], marks[0], num)
        print("BINGO", num, boards[0], marks[0], score)
        break

    boards = boards_left
    marks = marks_left


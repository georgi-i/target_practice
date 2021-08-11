from math import pow
from prettytable import PrettyTable

class TargetPractice:
    
    def read_user_input():
        try:
            matrix_size = input('Enter matrix size: ').split()
            text = input('Enter some text: ')
            shot_parameters = list(map(int, input('Enter Row, Column and Radius of impact: ').split()))
        except Exception as e:
            print('Integers have to be separated by space.')
            
        return matrix_size, text, shot_parameters



    def fill_matrix(n, m, txt):
        matrix = [None] * n
        s = 0
        left = True
        for i in range(n - 1, -1, -1):
            matrix[i] = [None] * m
            
            for j in range(m):
                if s == len(txt):
                    s = 0
                if left:
                    matrix[i][m - j - 1] = txt[s]
                else:
                    matrix[i][j] = txt[s]
                s += 1

            left = not left
        
        return matrix
    

    def shoot_matrix(matrix, n, m, row, col, radius):
        for i in range(n):
            for j in range(m):
                inside_radius = pow(i - row, 2) + pow(j - col, 2) <= radius * radius
                if inside_radius:
                    inside_matrix_boundaries = i >= 0 and i < n and j >= 0 and j < m
                    if inside_matrix_boundaries:
                        matrix[i][j] = ' '
        return matrix


    def gravity_hits_matrix(matrix, n, m):
        for i in range(m):
            for j in range(n):
                if j + 1 < n:
                    while matrix[j + 1][i] == ' ' and matrix[j][i] != ' ':
                        matrix[j + 1][i] = matrix[j][i]
                        matrix[j][i] = ' '
                        j = 0
        return matrix

    
def main():

    while True:
        user_input = TargetPractice.read_user_input()
        if user_input:
            break
        else:
            TargetPractice.read_user_input()
        
    n, m = int(user_input[0][0]), int(user_input[0][1])
    text = user_input[1]
    row, col, radius = int(user_input[2][0]), int(user_input[2][1]), int(user_input[2][2]) 

    matrix = TargetPractice.fill_matrix(n, m, text)
    matrix = TargetPractice.shoot_matrix(matrix, n, m, row, col, radius)
    matrix = TargetPractice.gravity_hits_matrix(matrix, n, m)

    t = PrettyTable(range(m))
    for i in range(n):
        t.add_row(matrix[i])
    print(t)


if __name__ == '__main__':
    main()
def pascal_triangle(n):
        triangle = [[1]]

        #looping rows from 1 to n -1
        for i in range(1,n):
                row = []

                row.append(1) #start
                # looping row cells to fill it with values
                for j in range(i - 1): # for row no.2 we fill a single cell with index 0.
                        row.append(triangle[i-1][j] + triangle[i-1][j + 1])
                row.append(1) #end
                triangle.append(row)
        return triangle
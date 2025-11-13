
rows1 = int(input("Number of rows for the first matrix: "))
cols1 = int(input("Number of columns for the first matrix: "))
rows2 = int(input("Number of rows for the second matrix: "))
cols2 = int(input("Number of columns for the second matrix: "))


if cols1 != rows2:
    print("(Columns of A must equal rows of B)")
else:
    matrix1 = []
    matrix2 = []
    result = []
    
    
    print("\nFirst Matrix:")
    for i in range(rows1):
        row = []
        for j in range(cols1):
            value = int(input(f"Element [{i}][{j}]: "))
            row.append(value)
        matrix1.append(row)
    
    
    print("\nSecond Matrix:")
    for i in range(rows2):
        row = []
        for j in range(cols2):
            value = int(input(f"Element [{i}][{j}]: "))
            row.append(value)
        matrix2.append(row)
    

    for i in range(rows1):
        row = []
        for j in range(cols2):
            sum_val = 0
            for k in range(cols1):
                sum_val += matrix1[i][k] * matrix2[k][j]
            row.append(sum_val)
        result.append(row)
    
    
    print("\n Result :")
    for i in range(rows1):
        for j in range(cols2):
            print(result[i][j], end="\t")
        print()
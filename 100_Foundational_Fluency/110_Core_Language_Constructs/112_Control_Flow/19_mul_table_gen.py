# generate a multiplication table using nested loops

def generate_multiplication_table(sz):
    table = []
    for i in range(1, sz + 1):
        row = []
        for j in range(1, sz + 1):
            row.append(i * j)
        table.append(row)
    return table

size = int(input("Enter the size of the multiplication table: "))
multiplication_table = generate_multiplication_table(size)
for row in multiplication_table:
    print("\t".join(map(str, row)))

Prices = [[50.0, 2500],
          [719, 481]]

Array2 = [200, 100]

Ans = []

for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
         row_sum += Prices[i][j] * Array2[j]
    Ans.append(row_sum)

print (Ans)

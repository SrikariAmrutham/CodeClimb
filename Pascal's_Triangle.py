
  # Question: Pascal's Triangle
  # Description: Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it.
  
  def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1]  # First element is always 1

        for j in range(1, i):
            val = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(val)

        if i > 0:
            row.append(1)  # Last element is 1 for all rows except the first
        triangle.append(row)

    return triangle


numRows = int(input())


result = generate(numRows)


print(result)
  

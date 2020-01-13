#MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.
#Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.
#For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].

def exec(code):
  bonus = [1] * len(code)
  
  for i in range(len(code))[1:]:
    if code[i] > code[i-1]:
      bonus[i] = bonus[i-1] + 1
    elif code[i] == code[i-1]:
      bonus[i] = bonus[i-1]
    else:
      backtrack(i, bonus, code)
  return bonus

def backtrack(i, bonus, code):
  if i < 0:
    return

  if code[i-1] > code[i] and bonus[i-1] <= bonus[i]:
    bonus[i-1] = bonus[i-1] + 1
    backtrack(i - 1, bonus, code)
  elif code[i-1] == code[i] and bonus[i-1] <= bonus[i]:
    bonus[i-1] = bonus[i]
    backtrack(i - 1, bonus, code)

print(exec([1000, 400, 200, 40, 40, 1000, 60, 60, 30, 500]))
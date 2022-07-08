from itertools import permutations

def run(p:tuple, j:int, goal:int):
  # Find the loop
  global loop
  loop += [j+1]
  if p[j] == goal:
    return str(j+1)  # return if it meets the target(goal)
  return str(j+1) + "/" + run(p, p[j]-1, goal) # complete the loops and  return the whole loop


if __name__ == "__main__":
  amount = int(input("Prisoners amount:"))
  prisoners = [i for i in range(1, amount+1)]
  prisoners = list(permutations(prisoners))
  # loops = [[] for i in range(len(prisoners))]  # be observed when testing in small range
  statistics = [0, 0]  # [<=amount/2, >amount/2]
  with open("result.txt", mode="w") as f:
    for i in range(len(prisoners)):
      loop = []  # check in order not to repeat(1)
      loops = []  # save the result(2)
      for j in range(len(prisoners[i])):
        if j+1 in loop:  # (1)
          continue
        # loops[i] += [run(prisoners[i], j, j+1)]   # be observed when testing in small range
        loops += [run(prisoners[i], j, j+1)]  # (2)
      for k in loops:  # (2)
        if len(k.split("/")) > (amount/2):
          statistics[1] += 1
          break
      else:
        statistics[0] += 1
      f.write(str(loops) + "\n")  # save the process into result.txt
  print(f"{statistics} --> P(success)=1-{statistics[1]/sum(statistics):.2f}={1-(statistics[1]/sum(statistics)):.2f}")
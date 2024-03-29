from itertools import permutations
import matplotlib.pyplot as plt


def run(p:tuple, j:int, goal:int):
  # Find the loop
  global loop
  loop += [j+1]
  if p[j] == goal:
    return str(j+1)  # return if it meets the target(goal)
  return str(j+1) + "/" + run(p, p[j]-1, goal) # complete the loops and return the whole loop


if __name__ == "__main__":
  amount = int(input("Prisoners amount:"))
  prisoners = list(permutations(range(1, amount+1)))
  statistics = [0, 0]  # [<=amount/2, >amount/2]
  statistics_detail = [0 for i in range(amount)]  # details of every loops
  with open("result.txt", mode="w") as f:
    for i in range(len(prisoners)):
      loop = []  # check in order not to repeat
      loops = []  # save the result
      for j in range(len(prisoners[i])):
        if j+1 in loop:
          continue
        loops += [run(prisoners[i], j, j+1)]
      for k in loops: 
        if len(k.split("/")) > (amount/2):
          statistics[1] += 1
          break
      else:
        statistics[0] += 1
      statistics_detail[len(max(loops, key=len).split("/"))-1] += 1
      f.write(str(loops) + "\n")  # save the process into result.txt


  print(f"{statistics} {statistics_detail}")
  print(f"{[i/sum(statistics) for i in statistics]} ")
  print(f"{[i/sum(statistics_detail) for i in statistics_detail]}")
  print(f"--> P(success)=1-{statistics[1]/sum(statistics):.2f}")
  print(f"={1-(statistics[1]/sum(statistics)):.2f}")
  

  plt.figure(num=f"Prisoners-{amount}")
  plt.bar([i+1 for i in range(amount)], [i/sum(statistics_detail) for i in statistics_detail], width=0.3)
  plt.xticks(range(1, amount+1, 1))
  plt.xlabel("Longest Loop")
  plt.ylabel("Probability")
  plt.show()
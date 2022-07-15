import matplotlib.pyplot as plt


if __name__ == "__main__":
  amount = int(input("Prisoners amount:"))
  data_range = int(input("Data range:"))
  statistics = [0 for i in range(int(amount/2))]
  for i in range(int(amount/2)+1, amount+1):
    statistics += [1/i]
  print(f"P(success)=1-{sum(statistics[(int(amount/2)+1):]):.2f}")
  print(f"={1-sum(statistics[(int(amount/2)+1):]):.2f}")

  
  plt.figure(num=f"Prisoners-{amount}")
  plt.bar([i+1 for i in range(amount)], statistics)
  plt.xticks(range(0, amount+1, data_range))
  plt.xlabel("Longest Loop")
  plt.ylabel("Probability")
  plt.show()
  
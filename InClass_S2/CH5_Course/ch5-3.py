#河內塔 Hanoi Recursive

# PartI Vars
# n->圓盤數
# 如果 n=3 => ABC 不是指圓盤 是起始點中繼點終點
# A->起始點
# B->中繼點
# C->終點

# PartII Steps
# 1. n-1個圓盤從 A(起始點)經過 C(終點)的輔助移至 B(中繼點)
# 2. 1個圓盤從 A(起始點)經過 B(中繼點)移至 C(終點)
# 3. n-1個圓盤從 B(中繼點)經過 A(起始點)的輔助移至 C(終點)

# PartIII Codes
count = 0
def Hanoi(n, A, B, C):
    global count
    if n == 1:
        print("From", A, "move it to", C)
        count += 1
        return count
    else:
        Hanoi(n-1, A, C, B)
        Hanoi(n, A, B, C)
        Hanoi(n-1, B, A, C)
amount = int(input("Please Input Hanoi-Tower's amount-->"))
result = Hanoi(amount, "A", "B", "C")
print("移動次數:"+str(result))

class MyBomb:
    def __init__(self):
        self.map_size=(10,10)
        self.bomb_position = [(2,2),(4,4),(10,10)]
        self.remain_position =[]
        for i in range(1,11):
            for j in range(1,11):
                self.remain_position.append((i,j))
        #print(self.remain_position)
    def find_neighbor(self,step):
        neighbors = []
        x=step[0]
        y=step[1]
        neighbors.append((x-1,y-1))
        neighbors.append((x-1,y))
        neighbors.append((x-1,y+1))
        neighbors.append((x,y-1))
        neighbors.append((x,y))
        neighbors.append((x,y+1))
        neighbors.append((x+1,y-1))
        neighbors.append((x+1,y))
        neighbors.append((x+1,y+1))
        neighbors_new = []
        for pos in neighbors:
            if not(pos[0] > 10 or pos[0] < 1 or pos[1] > 10 or pos[1] < 1):
                neighbors_new.append(pos)
        #print(neighbors)
        #print(neighbors_new)
        return neighbors_new
    def mymain(self,step):
        # 1. 找出 step 的鄰居，呼叫 find_neighbor
        # 2. 判斷 step 的鄰居有無地雷
        #    if not => remove step
        #    if yes => 再找出地雷的鄰居，呼叫 find_neighbor
        #              移除地雷的鄰居
        step_neighbors = self.find_neighbor(step) # 第一步
        for xx in step_neighbors:
            flag = xx in self.bomb_position

            if flag == False:
                if step in self.remain_position:
                    self.remain_position.remove(step)
            if flag == True: # xx 就是地雷
                xx_bomb_neighbor = self.find_neighbor(xx)
                self.bomb_position.remove(xx)
                for temp in xx_bomb_neighbor:
                    if temp in self.remain_position:
                        self.remain_position.remove(temp)
        print('Remaining pos:',self.remain_position)
        print('Remaining bombs:',len(self.bomb_position))
        
    def show_map(self):
        for i in range(1, self.map_size[0]+1):
            tempstr = ""
            for j in range(1, self.map_size[1]+1):
                if (i, j) in self.remain_position:
                    tempstr += " O"
                else:
                    tempstr += " X"
            print(tempstr)

Test = MyBomb()
Test.show_map()
print("=============")
Test.mymain((3,3))
Test.show_map()

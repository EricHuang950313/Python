class myBomb:
    def __init__(self):
        self.map_size = (10, 10)
        self.bombs_position = [(2, 2), (5, 5), (8, 8)]
        self.remain_position = []
        for i in range(1, 11):
            for j in range(1, 11):
                self.remain_position += [(i, j)]
        self.user = []
        pass

    def find(self, step):
        # 1 =>
        for x in range(step[1]-1, step[1]+2):
            for y in range(step[0]-1, step[0]+2):
                if not(x < 1 or x > 10 or y < 1 or y > 10):
                    self.user += [(x, y)]
        return self.user

        # 2 =>
        '''
        temp = self.user.copy() # temp:執行的順序
        for i in temp:
            if i[0] < 1:
                print('remove',i)
                self.user.remove(i) # 但用user去remove
                                                    '''

        # 執行錯誤 => 如果remove了，for迴圈的順序會亂掉
        '''
        for i in self.user:
            if i[0] < 1:
                print('remove',i)
                self.user.remove(i) # 但用user去remove
                                                    '''

    def myMain(self, step):
        # 1. 找出 step 的鄰居，呼叫 find
        # 2. 判斷 step 鄰居有無地雷
        # 3. if not -> remove step
        #    if yes -> 找出地雷的鄰居，呼叫 find
        #              移除地雷的鄰居
        step_neighbors = self.find(step) # 第1步

        for landmine in step_neighbors: 
            flag = landmine in self.bombs_position

            if flag == False:
                if step in self.remain_position:
                    self.remain_position.remove(step)

            if flag == True:
                landmine_bomb_neighbor = self.find(landmine)
                for temp in landmine_bomb_neighbor:
                    if temp in self.remain_position:
                        self.remain_position.remove(temp)

        print("Remaining pos:", self.remain_position)
        print("Remaining bombs:", len(self.bombs_position))

            

user = myBomb()
user.find((1,1))
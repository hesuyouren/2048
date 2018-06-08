from copy import deepcopy
import random
from getch import getch

class Game:
    def __init__(self):
        self.li = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.score = 0
        self.form = self.initialize(self.li)
        self.mainloop()


    def initialize(self,li):
        for i in range(4):
            li[i] = [random.choice([0,0,0,0,2,2,4])for x in self.li[i]]
        return li

    def align(self,direction,f = []):
        if direction == 'a':
            for i in f:
                for x in range(i.count(0)):
                    i.remove(0)
                for j in range(4-len(i)):
                    i.append(0)
            return f
        elif direction == 'd':
            for i in f:
                for x in range(i.count(0)):
                    i.remove(0)
                for j in range(4-len(i)):
                    i.insert(0,0)
            return f
        elif direction == 'w':
            for i in range(4):
                temp = []
                for x in f:
                    temp.append(x[i])
                temp = self.align('a',[temp])
                for j in range(4):
                    f[j][i] = temp[0][j]
            return f
        elif direction == 's':
            for i in range(4):
                temp = []
                for x in f:
                    temp.append(x[i])
                temp = self.align('d',[temp])
                for j in range(4):
                    f[j][i] = temp[0][j]
            return f

    def merge(self,direction,f=[]):
        if direction == 'a':
            for i in f:
                for x in range(len(i)) :
                    try:
                        if i[x] == i[x+1]:
                            if i[x] == 0:
                                pass
                            else:
                                i[x] = 2*i[x]
                                self.score += i[x]
                                del i[x+1]
                                i.append(0)
                                continue
                        else:continue
                    except:
                        break
            self.align('a',f)
        elif direction == 'd':
            for i in f:
                for x in range(len(i)) :
                    try:
                        if i[3-x] == i[2-x]:
                            if i[3-x] == 0:
                                continue
                            else:
                                i[3-x] = 2*i[3-x]
                                self.score += i[3-x]
                                del i[2-x]
                                i.insert(0,0)
                                continue
                        else:continue
                    except:
                        break
            self.align('d',f)
        elif direction == 'w':
            for i in range(4):
                temp = []
                for x in f:
                    temp.append(x[i])
                temp = self.merge('a',[temp])
                for j in range(4):
                    f[j][i] = temp[0][j]
        elif direction == 's':
            for i in range(4):
                temp = []
                for x in f:
                    temp.append(x[i])
                temp = self.merge('d',[temp])
                for j in range(4):
                    f[j][i] = temp[0][j]
        return f

    def random_again(self):
        zero_pos = []
        for i in range(4):
            for j in range(4):
                if self.form[i][j] == 0:
                    zero_pos.append([i,j])
        rad = random.randint(0,len(zero_pos)-1)
        self.form[zero_pos[rad][0]][zero_pos[rad][1]] = random.choice([2,2,2,4])
        return self.form

    def win_def(self):
        for i in range(4):
            for j in range(4):
                if self.form[i][j] == 2048:
                    return True
                else:continue
        return False

    def lose_def(self):
        for i in range(4):
            for j in range(4):
                if self.form[i][j] == 0:
                    return False
                else:continue
        return True

    def display(self,v):
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[0][0], v[0][1], v[0][2], v[0][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[1][0], v[1][1], v[1][2], v[1][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[2][0], v[2][1], v[2][2], v[2][3]))
        print('{0:4} {1:4} {2:4} {3:4}'.format(v[3][0], v[3][1], v[3][2], v[3][3]))
        print('Your score:',self.score)
        print('a:left, w:up, s:down, d:right')

    def mainloop(self):
        self.display(self.form)
        while self.lose_def() == False:
            ins = getch()
            if ins not in['a','w','s','d']:
                print('輸入不正確，請重新輸入')
                self.display(self.form)
                continue
            self.align(ins,self.form)
            self.merge(ins,self.form)
            self.align(ins,self.form)
            self.display(self.random_again())
            if self.win_def():
                print('You win!')
        print('You lose')

if __name__ == '__main__':
    game = Game()

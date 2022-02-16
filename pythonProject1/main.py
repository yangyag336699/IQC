#array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
#i 表示第几轮“冒泡”(对比的轮数是实际的长度-1)
#for i in range(1, len(array)):
#    #j 表示“走访”到的元素索引，每一轮“冒泡”中，j 需要从列表开头“走访”到 len(array) - i 的位置
#        for j in range(0, len(array) - i):
            #列表中第j个元素大于第j+1个元素
#            if array[j] > array[j + 1]:
                #升序
#                array[j], array[j + 1] = array[j + 1], array[j]
#print(array)

#s = "1234567"
#print (s[4:])

#x = 10
#if x %2:
#    print("单单")
#else:
#    print("双双")

#x = 0
#for i in  range(10):
#    if i % 2:
#     x +=i
#    else:
#        continue
#print(x)

#import random
#s = 1
#x = 99
#key = random.randint(1,100)
#while 1:
#    guess = int(input("请输入一个整数%d" % s + "到%d:" % x))
#    if guess<key and guess > s:
#        s = guess
#        print("请输入%d到" % s+"到%d：" % x)
#    elif guess>key and guess<x:
#        x = guess
#        print("请输入%d" % s+"到%d:" % x)
#    elif guess <= 1 or guess >=100:
#        print("继续努力，请重新输入")
#    elif guess ==key:
#        print("真聪明，答对了")
#        break
"""""
class Count():
    def add(self, a,b):
        return a+b

    def acc(self,a,b):
        return a-b

    def aff(self,a,b):
        return self.add(a,b)*self.acc(a,b)
a =Count()
print(a.aff(3,1))
"""""


class people():
    def hand(self):
        s="这是呆瓜"
        return (s)
    def foot(self):
        x="这是笨蛋"
        return (x)
if __name__ == "__main__":
    girlfriend = people()
    print(girlfriend.hand())
    print(girlfriend.foot())
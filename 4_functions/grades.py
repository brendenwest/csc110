
def sumList(nums):
    total = 0
    for num in nums:
        if not type(num) is str:
            total = total + num
    return total

def toNumbers(strList):
    for i in range(len(strList)):
        if strList[i].isdigit():
            strList[i] = float(strList[i])
    
def main():
    
    f = open('grades.txt','r')
    for line in f.readlines():
        line = line.strip('\n')
        nums = line.split(',')

        toNumbers(nums)
        sum = sumList(nums)
 
        if type(nums[0]) is str:
            count = len(nums) -1

            print(nums[0],'average =',sum, '/', count,'=', round(sum/(count)))
        else:
            count = len(nums)
            print('average =',sum, '/', count,'=', round(sum/(count),1))
       
main()
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2 or len(s) < 2:
            return s
        array = [[None for _ in range(len(s))] for _ in range(numRows)]
        row = col = 0
        flag = True  # 定义现在字符所处的状态 True：向下走   False：斜向上走
        for s1 in s:
            array[row][col] = s1
            if flag:
                if row < numRows - 1:
                    row += 1
                else:
                    flag = not flag
                    row, col = row - 1, col + 1
            else:
                if row > 0:
                    row, col = row - 1, col + 1
                else:
                    flag = not flag
                    row += 1
        # 经过上面的程序，已经把字符串以字符的形式存放到二维数组中了，现在按一行一行的取出来就可以了
        result = ""
        for arr in array:
            for a in arr:
                if a: result += a

        return result

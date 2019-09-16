

class compare:
    '''
    判断预期结果是否在实际结果之中
    '''
    def is_contain(self, str_one, str_two):
        flag = None
        str_one = str(str_one)
        str_two = str(str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
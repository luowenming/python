def multiple_table():
    '''
    99乘法表
    :return:
    '''
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            result = i * j
            print('%d * %d = %d\t' % (i, j, result),end='')
            j += 1
        print('')
        i += 1
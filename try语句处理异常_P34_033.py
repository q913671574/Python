try:
    sum = 1 + '1'                   #TypeError
    f = open('我是一个文件.txt')   #OSError
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错了T_T\n错误的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错\n原因是' + str(reason))
finally:            
    f.close()        #无论如何都会执行的语句



"""
或
try:
    sum = 1 + '1'                   //TypeError
    f = open('我是一个文件.txt')  //OSError
    print(f.read())
    f.close
except (OSError, TypeError):
    print('文件出错了T_T'


"""

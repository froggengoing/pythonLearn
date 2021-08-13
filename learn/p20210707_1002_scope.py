# 内层并不能修改外层作用域的值
g_count = 1
g_tab = 2
g_list = [1, 2, 4]


def outer():
    print('global g_tab：', g_tab)
    g_count = 2
    g_list[1] = 10

    def inner():
        g_count = 3

    inner()
    print('outer after exe inner:', g_count)


if __name__ == '__main__':
    print(g_count)
    print(g_list)
    outer()
    print(g_count)
    print(g_list)


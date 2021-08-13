g_count=2
def change():
    # 修改全局作用域的值
    global g_count
    g_count=20
    l_count=10
    def inner():
        # 修改闭包作用域的值
        nonlocal l_count
        l_count=30
    inner()
    print(l_count)
if __name__ == '__main__':
    print(g_count)
    change()
    print(g_count)

import base64


def D_BASE64(origStr):
    '''
    输入的base64编码字符串必须符合base64的padding规则。“当原数据长度不是3的整数倍时, 如果最后剩下两个输入数据，
    在编码结果后加1个“=”；
    如果最后剩下一个输入数据，编码结果后加2个“=”；如果没有剩下任何数据，就什么都不要加，这样才可以保证资料还原的
    正确性。”
    :param origStr:
    :return:
    '''

    # base64 decode should meet the padding rules
    mflag = len(origStr) % 3
    if mflag== 1:
        origStr += "=="
    elif mflag == 2:
        origStr += "="
    # origStr = bytes(origStr, encoding='utf8')
    dStr = base64.b64decode(origStr)
    print("BASE64 Decode result is: \n", dStr)
    return dStr


def grab_logo():
    ilogo = '''PHN2ZyB3aWR0aD0iMjEiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCA
    yMSAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEzL
    jY5NDkgOS44NDQ2N0MxMy42OTQ5IDUuMjcwNDQgMTEuNDQxOSAxLjMxMDY2IDkuNzY5MjMgMC4wMTM0ODU5QzkuNzY5Mj
    MgMC4wMTM0ODU5IDkuNjMyNjkgLTAuMDU0Nzg2MyA5LjYzMjY5IDAuMTE1ODk0QzkuNDk2MTUgOC45OTEyNyA0Ljk1Nj
    A1IDExLjM4MDggMi40NjQxMiAxNC42MjM3Qy0zLjI3MDc0IDIyLjA5OTUgMi4wODg2MiAzMC4yOTIyIDcuNTE2MjUgMz
    EuODI4M0MxMC41NTQ0IDMyLjY4MTcgNi43OTk0IDMwLjMyNjMgNi4zMjE0OSAyNS4zNzY2QzUuNzQxMTggMTkuMzY4NiA
    xMy42OTQ5IDE0Ljc5NDQgMTMuNjk0OSA5Ljg0NDY3WiIgZmlsbD0id2hpdGUiLz4KPHBhdGggZD0iTTUuNTcyODEgMC4w
    MjU2MDIzQzUuNTM4NjcgLTAuMDA4NTMzNzYgNS41MDQ1NCAtMC4wMDg1MzM3NiA1LjQ3MDQgMC4wMjU2MDIzQzUuMzMz
    ODYgMS4xNTIwOSA0LjIwNzM2IDMuNTQxNjIgMi43NzM2NSA1LjcyNjMzQy0yLjE0MTk0IDEzLjE2OCAwLjY1NzIxNCAxNi43NTIz
    IDIuMjI3NDcgMTguNjYzOUMzLjE0OTE1IDE5Ljc5MDQgMi4yMjc0NyAxOC42NjM5IDQuNTE0NTkgMTcuNTM3NEM0LjY4NTI3IDE3L
    jQzNSA4Ljk1MjI4IDE1LjA0NTUgOS40MzAxOCA5LjYxNzg0QzkuODczOTUgNC4yOTI2MSA2LjY5OTMgMC45ODE0MTIgNS41NzI4MSAwL
    jAyNTYwMjNaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMC43NSAxMi44NTk0KSIgZmlsbD0iIzJFQTdFMCIvPgo8L3N2Zz4K'''
    print(len(ilogo))
    imagedata = D_BASE64(ilogo)
    print(imagedata)
    file = open('huobi.png', "wb")
    file.write(imagedata)
    file.close()


if __name__ == '__main__':
    # grab_logo()
    pass
    d_data = []
    for i in range(1, 33):
        d_data.append(i)
    ma5_dd = d_data[-5:]
    ma10_dd = d_data[-10:-5]
    ma30_dd = d_data[-30:-10]
    print(ma5_dd)
    print(ma10_dd)
    print(ma30_dd)

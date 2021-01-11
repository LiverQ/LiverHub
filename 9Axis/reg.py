class REG():
    def __init__(self):
        super(REG, self).__init__()

    AxH = 0x3B  # 为寄存器建类，方便调用
    AxL = 0x3C
    AyH = 0x3D
    AyL = 0x3E
    AzH = 0x3F
    AzL = 0x40

    GxH = 0x43
    GxL = 0x44
    GyH = 0x45
    GyL = 0x46
    GzH = 0x47
    GzL = 0x48

    # MxH =
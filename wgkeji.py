##
# 说明：python 核心类库
# 作者：王嘉庆
# QQ：1101202419
# 电话：15913974609
##

class FloatRange:
    """ 该类用于生成指定范围内的浮点数列表，
    """
    def __init__(self, start, end, step=0.1):
        """
        构造函数
        :param start:起始值（包含在内）
        :param end: 结束值（包含在内）
        :param step: 步长
        """
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


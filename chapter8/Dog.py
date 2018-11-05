class Dog:
    """一次模拟小狗的简单尝试"""
    
    # 这是2个下划线
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗坐下"""
        print(self.name.title() + ' is now sitting.')
    
    def roll_over(self):
        """模拟小狗翻滚"""
        print(self.name.title() + ' is rolling over.')

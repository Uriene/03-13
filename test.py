# 简单计算器 - 加法运算
def add_numbers():
    # 获取用户输入
    num1 = float(input("请输入第一个数字: "))
    num2 = float(input("请输入第二个数字: "))
    
    # 计算和
    total = num1 + num2
    
    # 格式化输出
    print(f"\n计算结果: {num1} + {num2} = {total}")

# 运行计算器
if __name__ == "__main__":
    print("=== 简单加法计算器 ===")
    add_numbers()
    print("=====================")
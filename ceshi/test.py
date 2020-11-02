a1 = input ("请问有您需要帮助么？") 
if a1 == "需要":
    print("请问您需要什么帮助呢？ 1、存款 2、货币兑换、3、咨询")
num = int(input ("请您选择："))
if num == 1:
        print("存款")
elif num == 2:
        mony=float(input("请问您需要兑换多少金加隆货币？汇率是1:51.3："))
        mony1 = mony * 51.3
        print("您的兑换人民币金额为：" ,mony1)        
elif num == 3:
        print("咨询")
elif num == 4:
        print("对不起您输入错误")
else:
        print("欢迎下次在来")


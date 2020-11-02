
import re
def menu():
    print('''
     ----------------学生信息管理系统----------------------
          =============功能菜单================
         1.录入学生信息
         2.查找学生信息
         3.删除学生信息
         4.修改学生信息
         5.排序
         6.统计学生总人数
         7.显示学生信息
         0.退出系统
         =====================================
         说明：通过数字或↕️方向建选择菜单
    ''')
def insert():
    stdentList = []
    mark = True
    while mark:
        id = input("输入ID：")
        if not id :
            break 
        name = input("请输入名字：")
        if not name:
            break 
        try:
            english = int(input("please enter Enlish score:"))
            python = int(input("please enter python score:"))
            c = int(input("please enter c score:"))
        except:
            print("The input is invalid,not an integer...plaese enter again")
            continue
        stdent = {"id":id,"name":name,"english":english,"python":python,"c":c}
        stdentList.append(stdent)
        print(stdentList)
        break
        
        
def search():
    search_user_name = input("请输入你要查询的学生的姓名")
    pass
def delete():
    pass
def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass
def main():
    ctrl = True
    while (ctrl):
        menu ()
        option =  input("请键入对应的数字:\n")
        option_str = re.sub("\D", "",option)
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int  = int(option_str)
            if option_int == 0:
                print ("您已退出学生信息管理系统！")
                ctrl = False
            elif option_int == 1:
                insert()
                break
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()

main()

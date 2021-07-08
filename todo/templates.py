from .models import Todo

# menu display
def menu_display() :
    print("===== 일정 관리 시스템 =====")
    print("1. 전체 목록 보기")
    print("2. 일정 등록")
    print("3. 일정 수정")
    print("4. 일정 삭제")
    print("5. 상세 보기")
    print("0. 종료")

    
# menu select
def menu_select() :
    menu = input("메뉴를 선택하세요 : ")
    return menu

# message display (성공, 실패)
def message_display(message) :
    print(message)

# 1. list display
def list_display(li) :
    print("=== 전체 목록 ===")
    for i in li : 
        print(i.info())

# 2. register person (input)
def input_display() :
    id = input("ID : ")
    title = input("TITLE : ")
    contents = input("CONTENTS : ")
    date = input("DATE : ")
    done = input("DONE : ")
    return Todo(id,title,contents,date,done)     # 객체생성

# 3,4,5 수정, 삭제, 상세보기 위한 id 입력 화면
def id_input_display(command) : 
    id = input("{0} 수정할 id를 선택하세요 : ".format(command))
    return id

# 수정할 데이터 입력 화면
def update_input_display(id) :
    name = input("NAME : ")
    contents = input("CONTENTS : ")
    date = input("DATE : ")
    done = input("DONE : ")
    return Todo(id,name,contents,date,done)


# person display
def listdata_display(id) :
    print("=== 상세 정보 ===")
    print(id.info())


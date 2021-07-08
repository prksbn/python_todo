from todo.exception import DuplicateError, NotFoundError
from todo.templates import * # 모듈로부터
from todo.views import TodoController # 현재 패키지에서 클래스를 
from todo.models import Todo

lis = [] # 초기화해서 저장
controller = TodoController()   # 객체 생성
#lis = controller.load_list()

while True :
    menu_display()
    menu = menu_select()
    if menu == "1" :
        # 목록보기  - views의 getAllData()  목록 리턴받아서 templates의 list_display() 호출
        dataList = controller.getAllData()
        list_display(dataList)

    elif menu == "2" :
        # 등록 - views의 register(객체) 호출
        # DuplicateError 처리
        while True :
            lis = input_display()
            try : 
                controller.register(lis)
                message_display(lis.id + " 등록 성공!")
            except DuplicateError as error :
                message_display(error)
            finally : 
                break
                # 그냥 여기에 break 써도 됨 (finally 안쓰고)

    elif menu == "3" :
        # 수정 - 수정할 id 입력받고 views의 getData(id)로 검색
        id = id_input_display("수정")
        try : 
            # person 타입에 따라 수정정보 입력받은 후 views의 update(객체)
            new_li = update_input_display(id)
            controller.update(new_li)
            message_display(id + " 수정 성공!")

        except NotFoundError as error :  # NotFoundError 처리
            message_display(error)

    elif menu == "4" :
        # 삭제 - 삭제할 id 입력받고 views의 remove(id) 호출\
        id = id_input_display("삭제")
        try :
            controller.remove(id)
            message_display(id + " 삭제 성공!")
        except NotFoundError as error:  # NotFoundError 처리
            message_display(error)
        
    elif menu == "5" :
        # 상세보기 - 상세보기할 id 입력받고 views의 getPerson(id) 호출
        id = id_input_display("검색")
        try :
            # templates의 list_display(person) 호출
            li = controller.getData(id)
            listdata_display(li)
        except NotFoundError as error :
            # NotFoundError 처리
            message_display(error)
        
    elif menu == "0" :
        # views.py 의 
        #controller.save_list(lis)
        message_display("인사시스템을 종료합니다.")
        break
    else :
        print()
        message_display("1,2,3,4,5,0번 중 선택하세요")
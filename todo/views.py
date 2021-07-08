from .exception import DuplicateError, NotFoundError
#from .file_registry import save_file, init_data_load

class TodoController :
    # 클래스에서 함수를 불러다가 쓸 때에는 self.-- 으로 쓴다.
    lis = [] # 클래스 변수

    def is_exist(self,id) :    # id 존재여부 판단
        for index, i in enumerate(TodoController.lis) :
            if i.id == id :
                return index     # 메소트 빠져나감, for문 끝남
                # index번째에 이미 존재합니다~
        return -1   # 임의의 음수

    def register(self,li) :
        # id 중복 check : 중복될 경우 DuplicateError(id)
        index = self.is_exist(li.id)
        if index > -1 : 
            raise DuplicateError(li.id)
        TodoController.lis.append(li)

    def update(self,li) :
        # id check : 존재하지 않을 경우 NotFoundError(id)
        index = self.is_exist(li.id)
        if index == -1 :
            raise NotFoundError(li.id)
        TodoController.lis[index] = li

    def remove(self,id) :
        # id check : 존재하지 않을 경우 NotFoundError(id)
        index = self.is_exist(id)
        if index == -1 :
            raise NotFoundError(id)
        TodoController.lis.pop(index)  # index번째 정보를 삭제

    def getData(self,id) :
        # id check : 존재하지 않을 경우 NotFoundError(id)
        index = self.is_exist(id)
        if index == -1 :
            raise NotFoundError(id)
        return TodoController.lis[index]

    def getAllData(self) :
        return TodoController.lis

"""
    def save_list(self,lis) :
        save_file(lis)

    def load_list(self) :
        lis = init_data_load()
        return lis
"""
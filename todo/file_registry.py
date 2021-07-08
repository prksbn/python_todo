from todo.views import TodoController
from todo.models import Todo
import os.path

def save_file(lis) :
    # 프로그램 종료시 views.py의 persons list를 파일 저장
    save_file = open("list.dat", "w")
    for index, p in enumerate(lis) :
        save_file.write("{0},{1},{2},{3},{4}\n" .format(p.id, p.title, p.contents, p.date, p.done))
    save_file.close()

def init_data_load() :
    lis = []
    # 프로그램 시작시 파일에 있는 내용을 읽어서 views.py persons list에 저장
    fileExist = os.path.isfile("list.dat")
    if fileExist :
        read_file = open("list.dat", "r")
        while True :    # 데이터가 있는 동안
            data = read_file.readline()     # 한 라인씩 읽어서
            data_list = data.split(",")     # ","로 구분해서 리스트에 넣어주고
            li = Todo(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4])
            lis.append(li)
            if not data : break     # 해당되는 데이터가 없으면 while을 나와라
        read_file.close()   # 자원반납
    return lis  # 파일의 데이터 객체로 저장한 리스트 리턴

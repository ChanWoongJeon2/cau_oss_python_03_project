# 필요한 모듈(file_manager, parking_spot_manager)을 불러온다
import file_manager
import parking_spot_manager

def start_process(path):
    str_list = file_manager.read_file(path) # path경로의 값 문자열 리스트에 저장
    obj_list = parking_spot_manager.str_list_to_class_list(str_list) # 문자열 리스트를 객체 리스트에 저장
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(obj_list) # 객체를 출력한다.
            
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                # 입력한 이름 키워드 값을 기준으로 filter_by_name 함수를 호출하여 새로운 obj_list 생성
                obj_list = parking_spot_manager.filter_by_name(obj_list, keyword) 
                
            elif select == 2:
                keyword = input('type city:')
                # 입력한 도시 키워드 값을 기준으로 filter_by_city 함수를 호출하여 새로운 obj_list 생성
                obj_list = parking_spot_manager.filter_by_city(obj_list, keyword)
                
            elif select == 3:
                keyword = input('type district:')
                # 입력한 district 키워드 값을 기준으로 filter_by_district 함수를 호출하여 새로운 obj_list 생성
                obj_list = parking_spot_manager.filter_by_district(obj_list, keyword)
                
            elif select == 4:
                keyword = input('type ptype:')
                # 입력한 ptype 키워드 값을 기준으로 filter_by_ptype 함수를 호출하여 새로운 obj_list 생성
                obj_list = parking_spot_manager.filter_by_ptype(obj_list, keyword)
                
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                keyword = (min_lat, max_lat, min_lon, max_lon) #위도 경도 값을 이용하여 튜블 생성
                # 입력한 최대 최소 위도,경도 키워드 튜플 값을 기준으로 filter_by_location 함수를 호출하여 새로운 obj_list 생성
                obj_list = parking_spot_manager.filter_by_location(obj_list, keyword)
                
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                # 입력한 keyword값이 keywords 리스트에 있으면 객체리스트 obj_list와 keyword값을 sort_by_keyword 함수를 호출하여 새로운 obj_list 생성
                obj_list = parking_spot_manager.sort_by_keyword(obj_list, keyword)
            else: print("invalid input")
        elif select == 4:
            print("Exit") 
            break # while문을 break한다
        else:
            print("invalid input")
class parking_spot:

    # 생성자함수를 통해 6개의 데이터를 딕셔너리 형태로 저장합니다.
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {
            'name' : str(name),
            'city' : str(city),
            'district' : str(district),
            'ptype' : str(ptype),
            'longitude' : float(longitude),
            'latitude' : float(latitude)
        }
    
    # get 함수 설정, 매개변수는 문자열 keyword로, __item[keyword]값을 반환하며, 기본인수는 'name'으로 지정 
    def get(self, keyword='name'):
        return self.__item[keyword]
    
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

# str_list_to_class_list함수 지정, str_list를 매개변수로 받아 parking_spot 클래스 객체를 리스트 변환 후 반환
def str_list_to_class_list(str_list):
    class_list = []
    for data in str_list:
        num, name, city, district, ptype, longitude, latitude = data.split(',')
        data1 = parking_spot(name, city, district, ptype, longitude, latitude)
        class_list.append(data1)    
    return class_list
    
# print_spots 함수 지정, 각각의 값을 출력해준다.
def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for data in spots:
        print(data)
# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
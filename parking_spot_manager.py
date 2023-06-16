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

# filter_by_name 함수 지정, 리스트 함축을 이용하여 이름을 기준으로 필터링 한 후 새로운 리스트 반환
def filter_by_name(spots, name):
    name_list = [data for data in spots if name in data.get('name')]
    return name_list

# filter_by_city 함수 지정, 리스트 함축을 이용하여 도시을 기준으로 필터링 한 후 새로운 리스트 반환
def filter_by_city(spots, city):
    city_list = [data for data in spots if city in data.get('city')]
    return city_list

# filter_by_district 함수 지정, 리스트 함축을 이용하여 district을 기준으로 필터링 한 후 새로운 리스트 반환
def filter_by_district(spots, district):
    district_list = [data for data in spots if district in data.get('district')]
    return district_list

# filter_by_ptype 함수 지정, 리스트 함축을 이용하여 ptype을 기준으로 필터링 한 후 새로운 리스트 반환
def filter_by_ptype(spots, ptype):
    ptype_list = [data for data in spots if ptype in data.get('ptype')]
    return ptype_list

# filter_by_location 함수 지정, 리스트 함축을 이용하여 위도,경도를 기준으로 필터링 한 후 새로운 리스트 반환
def filter_by_location(spots, locations):
    location_list = [data for data in spots if locations[0] < data.get('latitude') < locations[1] and \
                                               locations[2] < data.get('longitude') < locations[3]]
    return location_list

#sort_by_keyword 함수 지정, lambda 함수를 이용하여 spots이라는 변수로 받아온 객체리스트 keyword 값을 기준으로 정렬 후 새로운 리스트 반환
def sort_by_keyword(spots, keyword):
    sorted_list = sorted(spots, key=lambda data:data.get(keyword))
    return sorted_list

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
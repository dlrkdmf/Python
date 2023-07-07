class Elevator:
    total_floors = 10
    source_floor = 1
    dest_floor = 0
    direction = ""
    saram_nums = 0

    def gotofloor(self):
        # 사람이 층을 눌렀을 때
        self.dest_floor = int(input("가고싶은 층(1~10)을 눌러주세요: "))
        self.saram_nums = int(input("몇 명이 탑승합니까?: "))

        if self.dest_floor == self.source_floor:
            print("이미 해당 층에 있습니다.")

        elif not 1 <= self.dest_floor <= self.total_floor:
            print("존재하지 않는 층입니다.")

    def check_floor(self):
        # 층이 움직이는 정보 확인
        if self.source_floor < self.dest_floor:
            self.direction = 'UP'
            print(f"{self.dest_floor}층으로 이동합니다. \n")
        
        elif self.source_floor > self.dest_floor:
            self.direction = 'DOWN'
            print('')
            print(f"{self.dest_floor}층으로 이동합니다. \n")

        elif self.source_floor == self.dest_floor:
            self.direction = 'STAY'

        # 층을 이동하는 중간 방향을 나타내는 기능
    def info(self):
        if self.direction == 'UP':
            while self.source_floor != self.dest_floor:
                self.source_floor += 1
                print(f"현재 {self.source_floor}층, {self.dest_floor}층으로 이동 중입니다..")
            print("도착했습니다.")
        elif self.direction == 'DOWN':
            # self.source_floor == self.dest_floor
            while self.source_floor != self.dest_floor:
                self.source_floor -= 1
                print(f"현재 {self.source_floor}층, {self.dest_floor}층으로 이동 중입니다..")
            print("도착했습니다.")
    def info_elevator(self):
        print('=' * 15)
        print(f"전체 층 수: {self.total_floor}")
        print(f"현재 층: {self.source_floor}")
        print(f"이동 방향: {self.direction}")
        print('=' * 15)

# 테스트 코드
el = Elevator()      

while True:
    el.info_elevator()
    el.gotofloor()
    el.check_floor()
    el.info()
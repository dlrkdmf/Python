import sys

class Coffee:
    total_amount = 10              
    total_amount_price = 5000       
    coffee_price = 300               
    put_price = 0	
    req_coffee_nums = 0
    remaining_price = 0

    def get(self, put_price, req_coffee_nums):
        # 커피 살 돈을 충분히 넣은 경우
        price = req_coffee_nums * self.coffee_price
        if put_price >= price:
            remaining_price = put_price - price
            # 거스름돈이 없는 경우
            if remaining_price == 0:
                print(f"커피를 {req_coffee_nums}개 줍니다.")
            # 거스름돈이 있는 경우
            else:
                print(f"커피를 {req_coffee_nums}개 줍니다 그리고 거스름 돈은 {remaining_price} 입니다. ")
                self.total_amount_price -= remaining_price
            self.total_amount -= req_coffee_nums
            # 돈을 불충분하게 넣은 경우
        else:
            print("돈이 부족합니다. 돈을 더 넣어주세요.")
            print(f"넣은 돈 {put_price}을 돌려드립니다.")
    
    def info(self):
        print('*' * 15)
        print("자판기가 보유한 총 금액:", self.total_amount_price)
        print("자판기가 보유한 커피 개수:", self.total_amount)
        print('*' * 15)
    
    def check_amount(self):
        if self.total_amount <= 0 or self.total_amount_price <= 0:
            return False
        else:
            return True
c = Coffee()

while True:
    c.request()
    if c.check_amount():
        c.get(c.put_price, c.req_coffee_nums)
        c.info()
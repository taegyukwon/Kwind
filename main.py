import sys
import locale

locale.setlocale(locale.LC_ALL, '')

#메뉴 출력 함수
def show_menu():
    #메뉴 출력
    selected_item_dic = {}
    for num, key in enumerate(item_dict, 1):
        selected_item_dic[num] = key
        print(f"{num}. {key}의 가격은 {item_dict[key][0]:n}")
    
    #메뉴 입력
    print()
    print("장바구니에 담을 메뉴의 번호를 입력해주세요")
    print("(메인으로 돌아가시려면 0번을 눌러주세요)")
    select_number = int(input(": "))
    if select_number == 0:
        return
    menu = selected_item_dic[select_number]
    detail_menu(menu)

#프로그램 종료 함수
def end_pro():
    #무한 루프 종료
    sys.exit()

#메뉴 상세(장바구니 담기) 함수
def detail_menu(menu):
    #장바구니에 담기
    print(f"선택하신 메뉴는 {menu}의 가격은 {item_dict[menu][0]}\n {item_dict[menu][1]}")
    order_number = int(input ("장바구니에 담으실 갯수를 입력해주세요(0을 입력시에는 메인으로 돌아갑니다.) : "))
    #메인으로 돌아가기
    if order_number == 0:
        return
    #장바구니에 담기
    else:
        basket_menu[menu] = order_number
        print('정상적으로 담겼습니다.')

#장바구니 삭제 함수
def delete_basket():
    selected_item_dic = {}
    print('삭제하실 항목을 골라주세요.')
    for num, key in enumerate(basket_menu, 1):
        selected_item_dic[num] = key
        print(f"{num}. {key}")
    select_number = int(input(": "))
    del basket_menu[selected_item_dic[select_number]]
    print("정상적으로 삭제가 되었습니다.")

#장바구니 초기화 함수
def delete_all():
    basket_menu.clear()
    print("장바구니가 초기화 되었습니다.")

#장바구니 목록 보기 함수
def show_basket():
    if not basket_menu:
        print("장바구니가 비어있습니다.")
        print("")
        return
    for num, key in enumerate(basket_menu, 1):
        print(f"{num}. {key} - {item_dict[key][0]:n} X {basket_menu[key]}")
        # amout_price = item_dict[key][0] * basket_menu[key]
        # print(f"{num}. {item_dict[key]}의 {basket_menu[key]} 총 가격은 {amount_price:n}")
    print("")
    print("1. 결제하러가기")
    print("2. 메뉴 추가하러 가기")
    print("3. 장바구니 메뉴 삭제하기")
    print("4. 장바구니 초기화 하기")
    print("0. 메인으로 가기")
    select_number = int(input(": "))
    if select_number == 1:
        pay()
    elif select_number == 2:
        show_menu()
    elif select_number == 3: 
        delete_basket()
    elif select_number == 4:
        delete_all()
    elif select_number == 0:
        return
    else:
        print("번호를 잘못 입력했습니다.")
        show_basket()

basket_menu = {}
item_dict = {
    '김치찌개': (5000, '고기와 국산 김치를 우려서 만든 김치찌개입니다.'),
    '된장찌개': (2000, '할머니집에서 만든 된장찌개의 맛을 여기에서 맛보세요.'),
    '미역국': (7000, '오늘이 생일인것 같은, 매일매일이 생일이라고 생각하고 드세요.'),
    '만두': (1000, '고기만두와 김치만두가 각각 10개씩 담겨져있는 패키지입니다.'),
    '육개장': (5000, '한우 소꼬리를 이용하여 만든 얼큰한 육개장입니다.'),
    '만두국': (7000, '직접 만든 만두와 곰탕으로 만든 특제만두국입니다.'),
    '콜라': (500, '코카콜라 500ml 캔입니다.'),
    '사이다': (500, '칠성사이다 500ml 캔입니다.'),
    '웰치스': (700, '웰치스 700ml 캔입니다.'),
    '소주': (1000, '수령시에 성인인증을 하오니, 준비해주세요'),
}

while True:
    print("----K식당에 오신것을 환영합니다.----") 
    print("")
    print("1. 메뉴 보기")
    print("2. 나의 장바구니 보러가기")
    print("0. 종료하기")
    print("")
    main_step = input("번호를 입력해주세요 : ")
    if(main_step=="1"):
        show_menu()
    elif(main_step=="2"):
        show_basket()
    elif(main_step=="0"):
        end_pro()
    else:
        print("번호 입력을 잘못 하였습니다.")
        continue


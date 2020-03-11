while True:
    try:
        response_1 = input('Enter an Number:')
        response_2 = input('Enter an Divided number:')
        print(int(response_1) / int(response_2))
        # break
        # break可以加在這裡，同樣可以跳出迴圈，因為碰到break關鍵字，就會去找最接近那層的迴圈，然後跳出
        # break應該只會跳出一層迴圈
        # 像是if-else、try-except等地控制flow的block-code，不受break影響
        # 為什麼?因為if-else、try-except等都是敘述的程式碼
        # 執行完成就執行完了，只不過加個迴圈在外層，就會不斷的執行
        # 不過Python還有內建一個方法，else，方法如下
    except ValueError:
        print(f'Please Enter an Number:{ValueError}')
        # ValueError是指轉換丟給其轉換的Function可以轉換的類別參數，但是是沒辦法處理參數
        # 像是int('5')，在Python中是可把字串'5'轉換成integer
        # 不過像是int('int')，在Python中就沒辦法
        # Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value
    except TypeError:
        print(f'Please Enter an Number:{TypeError}')
        # 此錯誤跟ValueError最大的不同點是丟給轉換Function不同型態的資料
        # 像是int([1])
        # Passing arguments of the wrong type (e.g. passing a list when an int is expected) should result in a TypeError
    else:
        print('Code is finished!!Thanks')
        break
        # Python的try-except結構，還有else可以用，用的時間應該當try執行完後，再執行的程式區塊



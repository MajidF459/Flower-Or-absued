import random,os
aq=os.system("cls")
while True:
    vorodi= input("Open windows One or Tow. (1, 2) , Exit Non_Alphanumeric and Integers ")
    if vorodi.isalnum():
        list_vorodi=["1", "2"]
        if vorodi in list_vorodi:
            print("_"*10)
            if vorodi=="1":
                while True:
                    cup=(input( "Number Cups or Output Except Alphabets and Integers "))#تعداد لیوان
                    print("_"*10)
                    chance=(input("How Many Chances or Output Except Alphabets and Integers "))#تعداد حدس لیوان
                    txt="s"
                    if cup.isalnum() and chance.isalnum():#حروف الفبا یا عدد
                        if cup.isdigit() and chance.isdigit():#فقط عدد
                            cup=int(cup)
                            chance=int(chance)
                            if (chance) <= (cup) and (chance) >0:
                                #تعداد حدس لیوان بزرگ تر از ضفر و  کوچک تر از تعداد لیوان => بین تعداد لیوان
                                ai1=random.randint(1,cup)
                                print("_"*10)
                                m=0
                                mad=set()
                                while m < chance:#تعداد گردش حدس زدن
                                    if chance -m==1:
                                        txt=""  
                                    print(f"{chance-m} Chance {txt} Left. ")
                                    print("_"*10)
                                    ai_chance=(input(f'Guess [1-{cup}]: '))#ورودی حدس
                                    if ai_chance.isdigit():   
                                        ai_chance=int(ai_chance)
                                        if ai_chance in range(1,cup+1):
                                            if ai_chance in mad:
                                                m-=1
                                            if ai1==ai_chance:
                                                print("_"*10)
                                                print("You Gussed Right. ")
                                                print(f'The Right Answer is {ai1} ')
                                                break
                                            else:
                                                print("_"*10)
                                                print("Wrong Guess. ")
                                                mad.add(ai_chance)
                                        else:
                                            print("_"*10)
                                            m-=1
                                        m+=1
                                    print(mad)
                                print("_"*10)
                            else:
                                print("_"*10)
                                continue
                            if ai1==ai_chance:
                                print("_"*10)
                                print("You Won ")
                                print("_"*10)
                            else:
                                print("_"*10)
                                print(f'The Right Answer is {ai1} ')
                                print("You Lost Sorry ")
                                print("_"*10)
                        else:
                            print("_"*10)
                            continue
                    else:
                        print("_"*10)
                        print("Exit")
                        print("_"*10)
                        break
            else:
                while True:
                    cup=(input("Number Cups or Output Except Alphabets and Integers "))#تعداد لیوان
                    txt="s"
                    if cup.isalnum() :#حروف الفبا یا عدد
                        if cup.isdigit():#فقط عدد
                            chance=random.randint(1,int(cup))
                            cup=int(cup)
                            chance=int(chance)
                            if (chance) <= (cup) and (chance) >0:
                                #تعداد حدس لیوان بزرگ تر از ضفر و  کوچک تر از تعداد لیوان => بین تعداد لیوان
                                ai1=random.randint(1,cup)
                                print("_"*10)
                                m=0
                                mad=set()
                                while m < chance:#تعداد گردش حدس زدن
                                    if chance -m==1:
                                        txt=""  
                                    print(f"{chance-m} Chance {txt} Left. ")
                                    print("_"*10)
                                    ai_chance=(input(f'Guess [1-{cup}]: '))#ورودی حدس
                                    if ai_chance.isdigit():   
                                        ai_chance=int(ai_chance)
                                        if ai_chance in range(1,cup+1):
                                            if ai_chance in mad:
                                                m-=1
                                            if ai1==ai_chance:
                                                print("_"*10)
                                                print("You Gussed Right. ")
                                                print(f'The Right Answer is {ai1} ')
                                                break
                                            else:
                                                print("_"*10)
                                                print("Wrong Guess. ")
                                                mad.add(ai_chance)
                                        else:
                                            print("_"*10)
                                            m-=1
                                        m+=1
                                    print(mad)
                                print("_"*10)
                            else:
                                print("_"*10)
                                continue
                            if ai1==ai_chance:
                                print("_"*10)
                                print("You Won ")
                                print("_"*10)
                            else:
                                print("_"*10)
                                print(f'The Right Answer is {ai1} ')
                                print("You Lost Sorry ")
                                print("_"*10)
                        else:
                            print("_"*10)
                            continue
                    else:
                        print("_"*10)
                        print("Exit")
                        print("_"*10)
                        break
        else:
            print("_"*10)
            print("N0 , Just Choose 1 or 2")
            print("_"*10)
    else:
        print("Exit")
        break

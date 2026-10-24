#Логические операции 

# Or

temp = 36
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Отменим наше мероприятие")
else:
    print("Все в силе")


# And

temp1 = 29
is_sanny = True

if temp1 >=28 and is_sanny:
    print("Жарковато для улицы")
    print("Очень жарко")
else:
    print("Хорошая погода")


# Not

temp2 = -6
is_cold = False

if temp2 >= 0 and not is_cold:
    print("На улице тепло")
else:
    print("Холодновато")
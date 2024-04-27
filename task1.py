def cases(num):
    if num % 100 in [11, 12, 13, 14]:
        return f"{num} компьютеров"
    elif num % 10 == 1:  
        return f"{num} компьютер"
    elif num % 10 in [2, 3, 4]:  
        return f"{num} компьютера"
    else:  
        return f"{num} компьютеров"

all_times = ['1h 45m,360s,25m,30m 120s,2h 60s'] #основной список

times_split = all_times[0].split(",")    #строка без пробелов

total_minutes = 0                #общее кол-во минут

for time in times_split:
    units = time.split()
    for unit in units:           #тут часы переводим в минуты
        if 'h' in unit:
            total_minutes += int(unit.replace('h', '')) * 60
        elif 'm' in unit:            #тут минуты оставляем как есть
            total_minutes += int(unit.replace('m', ''))
        elif 's' in unit:            #тут секунды переводим в минуты 
            total_minutes += int(unit.replace('s', '')) / 60
print(total_minutes) 
world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

#добавляем 2022 год
world_champions[2022] = 'Аргентина'

#выводим всех чемпионов в формате год - страна
for year, country_name in world_champions.items():
    print(year, '-', country_name)

#проверяем, выигрывала ли Италия  
country = 'Италия'

if country in world_champions.values():
    print('Италия становилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
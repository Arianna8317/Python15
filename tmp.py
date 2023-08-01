from datetime import datetime, date, time
import logging
#import argparse

def data_parser(text):
    year = datetime.now().year
    week_days = {"понедельник": 1, "вторник": 2, "среда": 3, "четверг": 4, "пятница": 5, "суббота": 6, "воскресенье": 7}
    months = {"января": 1, "февраля": 2, "марта": 3,"апреля": 4, "мая": 5, "июня": 6, "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}
    data = text.split() 
    week_day = 0
    month = 0 
    TEXT = "Формат даты : 3-е воскресенье февраля"
    logging.basicConfig(filename ="parser.log" , encoding = "Utf-8", level=logging.ERROR)
    if len(data)==3:
        if not data[2].isdigit():
            if data[2] in months.keys():
                month = months[data[2]]
                
        if int(data[2]) in months.values():
            month = int(data[2])
        
        if month == 0:
            logging.error("Вы ввели месяц не верно ! " + TEXT)
            return False
            
        if not data[1].isdigit():
            if data[1] in week_days.keys():
                week_day = week_days[data[1]] 
        if int(data[1]) in week_days.values():
            week_day = int(data[1])
        if week_day == 0:
            logging.error("Вы ввели день недели  не верно ! " + TEXT)
            return False    
            
        if not data[0][0].isdigit()
            logging.error("Вы ввели номер дня недели  не верно ! " + TEXT)
            return False
    
            
    pointer = (int(data[0][0])-1)*7   
         
    date_1 = date(year, month, 1)
    first_day = date_1.isoweekday()
    delta = 0 
    
    delta = week_day - first_day + pointer
    if week_day < first_day:
        delta += 7  
    return date(year, month, 1+delta)

    
d = data_parser("1-е 5 июля")
print(d)
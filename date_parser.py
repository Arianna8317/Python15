'''Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.Логируйте ошибки, если текст не соответсвует формату.
📌 Добавьте возможность запуска из командной строки.
📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
📌 Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

'''
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
    first_day = 0
    first_arg, second_arg, third_arg = True, True, True
    pointer = 0
    TEXT = "Формат даты : 3-е воскресенье февраля"
    logging.basicConfig(filename ="parser.log" , encoding = "Utf-8", level=logging.ERROR)
    if len(data)==3:
        if not data[2].isdigit():
            if data[2] in months.keys():
                month = months[data[2]]
                
        elif int(data[2]) in months.values():
            month = int(data[2])
        
        if month == 0:
            logging.error("Вы ввели месяц не верно ! " + TEXT)
            return False
            
        if not data[1].isdigit():
            if data[1] in week_days.keys():
                week_day = week_days[data[1]] 
        elif int(data[1]) in week_days.values():
            week_day = int(data[1])
        if week_day == 0:
            logging.error("Вы ввели день недели  не верно ! " + TEXT)
            return False    
            
        if not data[0][0].isdigit(): 
            logging.error("Вы ввели номер дня недели  не верно ! " + TEXT)
            return False
        elif int(data[0][0]) < 1 or int(data[0][0])>4:
            logging.error("Вы ввели номер дня недели  не верно ! " + TEXT)
            return False
        else:     
            pointer = (int(data[0][0])-1)*7 
            
    elif len(data) == 2:
        #В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
        
        if not data[0].isdigit(): # первый введенный аргумент текстовый
            if data[0] in week_days.keys(): # считаем, что это день недели
                week_day = week_days[data[0]] 
        elif not data[0].isalpha() and int(data[0]) in week_days.values():
            week_day = int(data[0])    
            # тогда второй - месяц         
                
        if not data[1].isdigit(): # текстом
            if data[1] in months.keys(): 
                month = months[data[1]]  # числом
        elif int(data[1]) in months.values():
            month = int(data[1])        
            
        
       
        # проверим, можно ли считать первый аргумент номером дня недели
        if data[0][0].isdigit() and not data[0].isalpha() : 
            if int(data[0][0]) < 1 or int(data[0][0])>4:
                logging.error("Вы ввели номер дня недели  не верно ! " + TEXT)
                return False
            else: # все нормально
                pointer = (int(data[0][0])-1)*7 
                if not data[1].isdigit(): 
                    if data[1] in week_days.keys(): # считаем, что это день недели
                        week_day = week_days[data[1]] 
                elif not data[1].isalpha() and int(data[1]) in week_days.values():
                        week_day = int(data[1])   
                month = datetime.now().month
               
        if week_day == 0 or month == 0:
            logging.error("Не верный формат! " + TEXT)
            return False  
                
    else:         
        logging.error("Ввод не верный! " + TEXT)
        return False
            
    date_1 = date(year, month, 1)
    first_day = date_1.isoweekday() # день недели 1 числа месяца
    delta = week_day - first_day + pointer + 1 
    if week_day < first_day:
        delta += 7  
    return date(year, month, delta)
    

print(data_parser("2-й вторник августа "))
print(data_parser("2-й вторник аваста ")) # не верно месяц - в лог
print(data_parser("2-й виток августа "))  # не верно день недели - в лог
print(data_parser("2-й 2 августа "))
print(data_parser("3-й 4 5"))
print(data_parser("вторник 8 "))
print(data_parser("2 августа"))
print(data_parser("2 8 "))
print(data_parser("3-й вторник"))
print(data_parser("3-й 2"))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсер даты')
    parser.add_argument('param', metavar='number_in_month week_day month', type=str,  nargs="*", help='пример ввода аргументов: 1-e воскресенье сентября')
    args = parser.parse_args()
    print(data_parser(*args.param))  
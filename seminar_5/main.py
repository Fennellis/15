import datetime
import logging
import sys
import argparse


logger = logging.getLogger(__name__)
my_format = '{levelname:<10} - {asctime:<20} - {funcName} - {msg}'
logging.basicConfig(filename='mylog.log', filemode='a', encoding='UTF-8',
                    level=logging.INFO, style='{', format=my_format)

WEEKDAYS = ['понедельник', 'вторник', 'среда',
            'четверг', 'пятница', 'суббота', 'воскресенье']
MONTHS = ['января', 'февраля', 'марта', 'апреля',
          'мая', 'июня', 'июля', 'августа',
          'сентября', 'октября', 'ноября', 'декабря']

def func(data: str) -> datetime.date:
    try:
        cnt, weekday, month = data.split(' ')
    except ValueError:
        logger.error(f'Неверный формат {data}')

    try:
        cnt = int(''.join(c if c.isdigit() else ' ' for c in cnt))
        if not 0 < cnt < 6:
            logger.error(msg=f'Неверный формат порядкового номера дня недели в месяце: {cnt}')
    except ValueError as e:
        logger.error(msg=e)

    try:
        weekday = WEEKDAYS.index(weekday)
    except ValueError as e:
        logger.error(msg=f'Неверный формат дня недели: {weekday}')

    try:
        month = MONTHS.index(month) + 1
    except ValueError as e:
        logger.error(msg=f'Неверный формат месяца: {month}')

    cur_year = datetime.datetime.now().year

    first_month_weekday = datetime.date(year=cur_year, month=month, day=1)
    offset = 1 if weekday < first_month_weekday.weekday() else 0

    for i in range(7):
        data_delta = first_month_weekday + datetime.timedelta(days=i)
        if data_delta.weekday() == weekday:
            day = data_delta.replace(day=data_delta.day + (7 * (cnt - 1)))
            return day


def create_parser():
    parser_ = argparse.ArgumentParser()
    parser_.add_argument('-c', '--cnt', default='1')
    parser_.add_argument('-w', '--weekday', default=datetime.datetime.now().weekday())
    parser_.add_argument('-m', '--month', default=datetime.datetime.now().month)

    return parser_


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    print(func(f'{namespace.cnt} {WEEKDAYS[namespace.weekday]} {namespace.month}'))
    input()

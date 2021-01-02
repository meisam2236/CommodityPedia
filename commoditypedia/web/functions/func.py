from persiantools.jdatetime import JalaliDate
from datetime import timedelta
import time


def num_convertor(num):
	number = num
	number = str(number).replace('0', '۰').replace('1', '۱').replace('2', '۲').replace('3', '۳').replace('4', '۴').replace('5', '۵').replace('6', '۶').replace('7', '۷').replace('8', '۸').replace('9', '۹')
	return number

def price_convertor(num):
	number = f'{num:,}'
	number = str(number).replace('0', '۰').replace('1', '۱').replace('2', '۲').replace('3', '۳').replace('4', '۴').replace('5', '۵').replace('6', '۶').replace('7', '۷').replace('8', '۸').replace('9', '۹')
	return number

def month_convertor(date):
	if date == '01':
		return 'فرودین'
	elif date == '02':
		return 'اردیبهشت'
	elif date == '03':
		return 'خرداد'
	elif date == '04':
		return 'تیر'
	elif date == '05':
		return 'مرداد'
	elif date == '06':
		return 'شهریور'
	elif date == '07':
		return 'مهر'
	elif date == '08':
		return 'آبان'
	elif date == '09':
		return 'آذر'
	elif date == '10':
		return 'دی'
	elif date == '11':
		return 'بهمن'
	elif date == '12':
		return 'اسفند'

def date_convertor(date):
	date = date + timedelta(hours = 4, minutes=30)
	time = str(date).split(' ')[1].split('+')[0]
	splited_time = time.split(':')
	hours = splited_time[0]
	hours_modified = num_convertor(hours)
	minutes = splited_time[1]
	minutes_modified = num_convertor(minutes)
	jdate = JalaliDate(date)
	jdate_list = str(jdate).split('-')
	year = jdate_list[0]
	month = jdate_list[1]
	day = jdate_list[2]
	month_string = month_convertor(month)
	day_modified = num_convertor(int(day))
	year_modified = num_convertor(year)
	date_modified = day_modified + ' ' + month_string + ' ' + year_modified + ' ساعت ' + hours_modified + ':' + minutes_modified
	return date_modified


def sending_time_calculation(registered_time):
	time_now = time.time()
	difference_time = time_now - registered_time  
	
	if  difference_time > 10 and difference_time < 60: sending_time =  "همین الان"
	elif  difference_time > 60 and difference_time < 300: sending_time = "یک دقیقه پیش"
	elif  difference_time > 300 and difference_time < 600: sending_time = "پنج دقیقه پیش"
	elif  difference_time > 600 and difference_time < 1200: time = "ده دقیقه پیش"
	elif  difference_time > 1200 and difference_time < 3600: sending_time = "بیست دقیقه پیش"
	elif  difference_time > 3600 and difference_time < 3600*2: sending_time = "یک ساعت پیش"
	elif  difference_time > 3600*2 and difference_time < 3600*3: sending_time = "دو ساعت پیش"
	elif  difference_time > 3600*3 and difference_time < 3600*6: sending_time = "سه ساعت پیش"
	elif  difference_time > 3600*6 and difference_time < 3600*12: sending_time = "شش ساعت پیش"
	elif  difference_time > 3600*12 and difference_time < 86400: sending_time = "دوازده ساعت پیش"
	elif  difference_time > 86400 and difference_time < 864002*2: sending_time = "یک روز پیش"
	elif  difference_time > 86400*2 and difference_time < 86400*3: sending_time = "دو روز پیش"
	elif  difference_time > 86400*3 and difference_time < 86400*4: sending_time = "سه روز پیش"
	elif  difference_time > 86400*4 and difference_time < 86400*5: sending_time = "چهار روز پیش"
	elif  difference_time > 86400*5 and difference_time < 86400*6: sending_time = "پنج روز پیش"
	elif  difference_time > 86400*6 and difference_time < 604800: sending_time = "شش روز پیش"
	elif  difference_time > 604800 and difference_time < 604800*2: sending_time = "یک هفته پیش"
	elif  difference_time > 604800*2 and difference_time < 604800*3: sending_time = "دو هفته پیش"
	elif  difference_time > 604800*3 and difference_time < 2419200: sending_time = "سه هفته پیش"
	elif  difference_time > 2419200 and difference_time < 2419200*2: sending_time = "یک ماه پیش"
	elif  difference_time > 2419200*2 and difference_time < 2419200*3: sending_time = "دو ماه پیش"
	elif  difference_time > 2419200*3 and difference_time < 2419200*4: sending_time = "سه ماه پیش"
	elif  difference_time > 2419200*4 and difference_time < 2419200*5: sending_time = "چهار ماه پیش"
	elif  difference_time > 2419200*5 and difference_time < 2419200*6: sending_time = "پنج ماه پیش"
	elif  difference_time > 2419200*6 and difference_time < 2419200*7: sending_time = "شش ماه پیش"
	elif  difference_time > 2419200*7 and difference_time < 2419200*8: sending_time = "هفت ماه پیش"
	elif  difference_time > 2419200*8 and difference_time < 2419200*9: sending_time = "هشت ماه پیش"
	elif  difference_time > 2419200*9 and difference_time < 2419200*10: sending_time = "نه ماه پیش"
	elif  difference_time > 2419200*10 and difference_time < 2419200*11: sending_time = "ده ماه پیش"
	elif  difference_time > 2419200*11 and difference_time < 29030400: sending_time = "یازده ماه پیش"
	elif  difference_time > 29030400 and difference_time < 29030400*2: sending_time = "یک سال پیش"
	elif  difference_time > 29030400*2 and difference_time < 29030400*3: sending_time = "دو سال پیش"
	elif  difference_time > 29030400*3 and difference_time < 29030400*4: sending_time = "سه سال پیش"
	elif  difference_time > 29030400*4 and difference_time < 29030400*5: sending_time = "چهار سال پیش"
	elif  difference_time > 29030400*5 and difference_time < 29030400*6: sending_time = "پنج سال پیش"
	elif  difference_time > 29030400*6 and difference_time < 29030400*7: sending_time = "شش سال پیش"
	elif  difference_time > 29030400*7 and difference_time < 29030400*8: sending_time = "هفت سال پیش"
	elif  difference_time > 29030400*8 and difference_time < 29030400*9: sending_time = "هشت سال پیش"
	elif  difference_time > 29030400*9 and difference_time < 29030400*9: sending_time = "نه سال پیش"
	elif  difference_time > 29030400*10 and difference_time < 29030400*11: sending_time = "ده سال پیش"
	else: sending_time = "خیلی سال پیش :)"
	return sending_time
import datetime as dt
import os

# ===== Config =====
OUTPUT_PATH = 'output.txt'
# TEMPLATE = '[Happy %Y %B DAY @ Sweden, HOURSh MINUTESm late]'
TEMPLATE = 'Happy %Y %B DAY @ Sweden, HOURSh MINUTESm late'
LAST_DATE = input('Last message on (YYYY-MM-DD): ')
TIMEZONE_OFFSET = 2  # e.g. for UTC+2 => 2, UTC-7 => -7


# ===== Code =====
last_date_dt = dt.date.fromisoformat(LAST_DATE)
today = dt.datetime.now(dt.UTC) + dt.timedelta(hours=TIMEZONE_OFFSET)
# today = dt.datetime.fromisoformat("2025-07-08T00:40:00")
messages = []

def day_with_suffix(day):
    day = int(day)
    if str(day)[-1] in ['1', '2', '3']:
        if str(day)[-2:] in ['11', '12', '13']: return f'{day}th' # 11-13 exceptionally th
        elif str(day)[-1] == '1': return f'{day}st'
        elif str(day)[-1] == '2': return f'{day}nd'
        elif str(day)[-1] == '3': return f'{day}rd'
    else: return f'{day}th'


if __name__ == '__main__':
    for i in range(1, (today.date() - last_date_dt).days + 1):
        message_day = last_date_dt + dt.timedelta(days=i)
        days_behind = (today.date() - message_day).days
        print(days_behind)
        
        # month full name
        message = message_day.strftime(TEMPLATE)
        
        # message's day without zerofill
        message = message.replace('DAY', day_with_suffix(message_day.day), 1)
        
        # time behind UTC midnight without zerofill
        # with days use template 'DAYSd HOURSh MINUTESm late'
        #if days_behind > 0: message = message.replace('DAYS', str(days_behind))
        #else: message = message.replace('DAYSd ', '')
        
        # without days use template 'HOURSh MINUTESm late'
        if days_behind > 0: message = message.replace('HOURS', str(days_behind*24+today.hour))
        elif today.hour > 0: message = message.replace('HOURS', str(today.hour))
        else: message = message.replace('HOURSh ', '')
        
        if today.minute > 0: message = message.replace('MINUTES', str(today.minute))
        else: message = message.replace('MINUTESm ', '')
        
        messages.append(message)
    with open(OUTPUT_PATH, 'w') as file:
        file.write('\n'.join(messages))
        os.startfile(OUTPUT_PATH)


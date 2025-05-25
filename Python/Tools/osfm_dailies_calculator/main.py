import datetime as dt
import os

# ===== Config =====
output_path = 'output.txt'
template = '[Happy %Y %B DAY @ Sweden, HOURSh MINUTESm late]'
last_date = input('Last message on (YYYY-MM-DD): ')
timezone_offset = 2  # e.g. for UTC+2 => 2, UTC-7 => -7


# ===== Code =====
last_date_dt = dt.date.fromisoformat(last_date)
today = dt.datetime.now(dt.UTC)
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
        current_hour = today.hour+timezone_offset
        print(days_behind)
        
        # month full name
        message = message_day.strftime(template)
        
        # message's day without zerofill
        message = message.replace('DAY', day_with_suffix(message_day.day), 1)
        
        # time behind UTC midnight without zerofill
        # with days use template 'DAYSd HOURSh MINUTESm late'
        #if days_behind > 0: message = message.replace('DAYS', str(days_behind))
        #else: message = message.replace('DAYSd ', '')
        
        # without days use template 'HOURSh MINUTESm late'
        if days_behind > 0: message = message.replace('HOURS', str(days_behind*24+current_hour))
        elif current_hour > 0: message = message.replace('HOURS', str(current_hour))
        else: message = message.replace('HOURSh ', '')
        
        if today.minute > 0: message = message.replace('MINUTES', str(today.minute))
        else: message = message.replace('MINUTESm ', '')
        
        messages.append(message)
    with open(output_path, 'w') as file:
        file.write('\n'.join(messages))
        os.startfile(output_path)


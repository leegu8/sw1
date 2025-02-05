# Import Required Library
from tkinter import *
import datetime
import time
import winsound
import os
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x300")

# Use Threading
def Threading():
    # 알람 시간이 유효한지 확인
    if validate_time():
        t1 = Thread(target=alarm)
        t1.start()
    else:
        print("현재 시간보다 미래의 시간을 설정하세요.")

def validate_time():
    # 현재 시간과 비교하여 알람 시간이 미래 시간인지 확인
    alarm_time = datetime.datetime.now().replace(hour=int(hour.get()), minute=int(minute.get()), second=int(second.get()))
    return alarm_time > datetime.datetime.now()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            if os.path.exists("sound.wav"):
                print("Time to Wake up")
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            else:
                print("sound.wav 파일이 없습니다.")
            break

def stop_alarm():
    winsound.PlaySound(None, winsound.SND_PURGE)  # 알람 소리 멈춤
    print("알람이 종료되었습니다.")

# Add Labels, Frame, Button, Optionmenus
Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
Button(root, text="Stop Alarm", font=("Helvetica 15"), command=stop_alarm).pack(pady=10)

# Execute Tkinter
root.mainloop()

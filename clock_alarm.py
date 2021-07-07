import datetime as dt
import webbrowser
import numpy as np
import time

a = input("What time do you want to wake up?(22:54)  ")
z = dt.datetime.strptime(a, '%H:%M')
now = dt.datetime.now()

while not(z.hour == now.hour  and z.minute == now.minute):
    now = dt.datetime.now()
    alarm_time = dt.datetime.strftime(z,"%H:%M")
    print(f"The alarm will be activated {alarm_time}")
    time.sleep(2)

print("Time to Wake up!")
randm = np.random.randint(0,4)
with open('url_list.txt') as f:
    lines = [line.rstrip() for line in f]

chrome_path = '/usr/bin/google-chrome %s'
webbrowser.get(chrome_path).open(lines[randm])

exit()




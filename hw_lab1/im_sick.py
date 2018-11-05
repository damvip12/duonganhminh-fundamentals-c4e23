from gmail import GMail, Message
from random import  choice
import datetime
now = datetime.datetime.now()

gmail = GMail("minhle54langha", "hoangmjnh")

sickness_list = ["thương hàn", "kiết lị", "tiêu chảy"]
n = 2

template ='''
<p>Chào sếp,</p>
<p>Hôm nay ngủ dậy , {{symptom}} vl , bác sĩ bảo em bị {{sick}} .</p>
<p>Thế nên sếp cho em nghỉ hnay nhé , dái đi làm được đâu.</p>
<p>ok iu sếp</p>
'''
sickness = choice(sickness_list)
symptom = "phê vl"

content = template.replace("{{sick}}",sickness).replace("{{symptom}}",symptom)

message = Message("Xin nghỉ hôm nay", to="qhuydtvt@gmail.com", html=content )

while True:
   if now.hour == 7:
    gmail.send(message)
   else:
       print("Chưa đến lúc đi làm")
       break

#!/usr/bin/env python
import pika
import json
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)


#populate vehicle

vn = ["TN37J2565","TN37r4567","TN38H6785","TN66K9807","TN66g8976","TN99A1111","TN99A1234","TN99A2122","TN99Z9999","TN99g6754"]
mm = ["HONDA 2010","HERO 2015","VOLVO 2015","MARUTI 2004","ASHOK LEYLAND 2014", "BHARAT BENZ 2015", "BHARAT BENZ 2017", "ASHOK LEYLAND 2012", "HONDA 2017","VOLVO 2008"]
km = [10000, 25000, 154200, 24150, 24782, 12301, 142501, 21450, 57482, 102450]
iv=["1JAN2020","2FEB2020","3MAR2020","4APR2020","5MAY2020","6JUN2020","7JUL2020","8AUG2020","9SEP2020","10OCT2020"]
lsm=["1JAN2020","2FEB2020","3MAR2020","4APR2020","5MAY2020","6JUN2020","7JUL2020","8AUG2020","9SEP2020","10OCT2020"]
i=0
j=0
y=0
for y in range(10):
	v=vn[i]
	m=mm[i]
	k=km[i]
	ii=iv[i]
	ls = lsm[i]
	a = 5
	tp = 100
	os = 100
	fs = 100
	data = { "$class": "org.nec.hack.Vehicle",  "vehicle_num": v,  "make_model": m,  "km_driven": k,"insurance_validity": ii, "tyre_pressure": tp, "oil_status": os, "last_serviced_date": ls, "fuel_status": fs, "remarks": "Good"}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()



#populate driver

vn = ["D1","D2","D3","D4","D5"]
mm = ["SACHIN","ARAVIND","KUMAR","SHIVA","LAKSMAN"]
iv=["L1001","L1002","L1003","L1004","L1005"]

i=0
j=0
y=0
for y in range(5):
	v=vn[i]
	m=mm[i]
	ii=iv[i]
	data = { "$class": "org.nec.hack.Driver", "driver_id": v, "driver_name": m, "licence_num": ii, "remarks": "Good" }
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()

#populate trip

vn = ["TN37J2565","TN37r4567","TN38H6785","TN66K9807","TN66g8976","TN99A1111","TN99A1234","TN99A2122","TN99Z9999","TN99g6754"]

tn = ["T1","T2","T3","T4","T5"]
dd = ["D1","D2","D3","D4","D5"]
mm = [100,200,300,400,500]

i=0
j=0
y=0
for y in range(5):
	t=tn[i]
	v=vn[i]
	m=mm[i]
	d=dd[i]
	data = {  "$class": "org.nec.hack.Trip",  "trip_id": t,  "vehicle": v,  "driver": d,  "km_travelled": m, "remarks": "Good"}
	message = json.dumps(data)
	channel.basic_publish(exchange='', routing_key='hello', body=message)
	print(message)
	time.sleep(1)
	i=i+1
connection.close()

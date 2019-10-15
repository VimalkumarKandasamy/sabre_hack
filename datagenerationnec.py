
#!/usr/bin/env python
import pika
import json
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)


'''
#update_Insurance	
data5 = {      "$class": "org.nec.hack.Update_insurance", "vehicle": "TN99A1234", "insurance_validity": "21Aug2019"}
message = json.dumps(data5)
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(message)
time.sleep(15)
	



#update_maintenance	
data6 = {"$class": "org.nec.hack.Update_maintenance","vehicle": "TN99A1234", "serviced_date": "21Aug2019",}
message = json.dumps(data6)
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(message)
time.sleep(15)
	



#update_maintenance	
data7 = {"$class": "org.nec.hack.Update_trip", "vehicle": "TN99A1234", "driver": "D1", "km_travelled": 100}
message = json.dumps(data7)
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(message)
time.sleep(15)
	
'''

#update_readings

vn = ["TN37J2565","TN37r4567","TN38H6785","TN66K9807","TN66g8976","TN99A1111","TN99A1234","TN99A2122","TN99Z9999","TN99g6754"] 	
i=0
j=0
y=0
for y in range(100):
	if i > 9:
		i = j
	v=vn[i]
	a = 5
	tp = 100
	os = 100
	fs = 100
	
	for x in range(10):
		data = { "$class": "org.nec.hack.Update_readings",  "vehicle": v,  "tyre_pressure": tp,  "oil_status": os,  "fuel_status": fs}
		message = json.dumps(data)
		channel.basic_publish(exchange='', routing_key='hello', body=message)
		print(message)
		time.sleep(10)
		tp = tp-1
		os = os-2
		fs=fs-5
		a = a+5
	i=i+1
	if y > 99:
		y = j
	
connection.close()



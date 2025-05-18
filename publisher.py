import zmq, time
from constPS import * #-
import random

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+HOST+":"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address

topics = ['TIME', 'RPS', 'COIN']
rps_values = ['rock', 'paper', 'scissors'] # simulated rock/paper/scissors game
coin_flip_values = ['heads', 'tails'] # simulated coin flip game

while True:
	time.sleep(3)                    # wait every 3 seconds
	topic = random.choice(topics)
	if topic == 'TIME':
		msg = str.encode("TIME " + time.asctime())
		s.send(msg) # publish the current time
	
	if topic == 'RPS':
		msg = str.encode("RPS " + ''.join(random.choices(rps_values, k=2)))
		s.send(msg)

	if topic == 'COIN':
		msg = str.encode("COIN " + random.choice(coin_flip_values))
		s.send(msg)

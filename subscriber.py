import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # subscribe to TIME messages
s.setsockopt_string(zmq.SUBSCRIBE, "RPS")
s.setsockopt_string(zmq.SUBSCRIBE, "COIN")

for i in range(10):  # Ten iterations
	msg = s.recv()   # receive a message
	print (bytes.decode(msg))

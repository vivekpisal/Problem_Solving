import threading

def fun():
	print("coding thunder")

timer=threading.Timer(5.0,fun)
timer.start()
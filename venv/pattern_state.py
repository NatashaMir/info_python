from abc import ABCMeta, abstractmethod


class State:

	def printText(self):
		pass

	def stopPrint(self):
		pass

	def checkPaper(self):
		pass


class OnState(State):

	def printText(self):
		print('Printing in progress')

	def stopPrint(self):
		print('Print canceled')

	def checkState(self):
		print('Is the status check')


class OffState(State):

	def printText(self):
		print('Printer is off')

	def stopPrint(self):
		print('Printer is off')

	def checkState(self):
		print('Printer is off')


class NoPaperState(State):

	def printText(self):
		print('No paper')

	def stopPrint(self):
		print('The printer is already stopped.')

	def checkState(self):
		print('Insert paper')


class Printer:

	def __init__(self, state):
		self.state = state

	def change_state(self, state):
		self.state = state

	def printText(self):
		self.execute('printText')

	def stopPrint(self):
		self.execute('stopPrint')

	def checkState(self):
		self.execute('checkState')

	def execute(self, operation):
		try:
			func = getattr(self.state, operation)
			func()
		except AttributeError:
			print('Command not defined')


offState = OffState()
onState = OnState()
noPaperState = NoPaperState()
printer = Printer(offState)
print('OUTPUT:')
printer.printText()
printer.change_state(onState)
printer.printText()
printer.checkState()
printer.change_state(noPaperState)
printer.printText()
printer.stopPrint()
printer.change_state(onState)
printer.printText()
printer.stopPrint()

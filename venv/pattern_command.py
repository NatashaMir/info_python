from abc import ABCMeta, abstractmethod


class Line:

	def draw(self, direction):
		print('Draw')

	def remove(self):
		print('Remove')

#Basic class
class Command(metaclass=ABCMeta):

	@abstractmethod
	def execute(self):
		pass

	@abstractmethod
	def unexecute(self):
		pass	


class DrawCommand(Command):
	def __init__(self, line):
		self.line = line

	def execute(self):
		self.line.draw('Draw line')

	def unexecute(self):
		self.line.remove()


class RemoveCommand(Command):

	def __init__(self, line):
		self.line = line

	def execute(self):
		self.line.draw('Remove line')

	def unexecute(self):
		self.line.remove()


class LineInterface:

	def __init__(self, draw, remove):
		self.draw_command = draw
		self.remove_command = remove
		self.current_command = None	

	def draw(self):
		self.current_command = self.draw_command
		self.draw_command.execute()

	def remove(self):
		self.current_command = self.remove_command
		self.remove_command.execute()

	def stop(self):
		if self.current_command:
			self.current_command.unexecute()
		else:
			print('Nothing to remove')


line = Line()
interface = LineInterface(DrawCommand(line), RemoveCommand(line))
interface.draw()
interface.stop()
interface.remove()
interface.stop()

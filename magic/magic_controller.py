from controller import Controller

class MagicController(Controller):
	STATES = {
		'DRAW': 0,
		'MAIN1': 1,
		'COMBAT': 2,
		'MAIN2': 3,
		'END': 4,
	}

	@classmethod
	def main_loop(cls):
		while(True):
			# if self.curr_state == self.STATES['DRAW']:
			# 	self.draw_card()

			print('Enter a command')


	def initial_state(self):
		return self.STATES['DRAW']

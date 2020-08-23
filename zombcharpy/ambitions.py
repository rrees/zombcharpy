import random

def finding():
	def objective():
		return random.choice((
			"their family",
			"safety",
			"clean water",
			"a hot shower",
			"a cure",
			"batteries",
			"a working radio",
			"supplies",
			"gasoline"
		))

	return f"find {objective()}"

def ambition():
	ambitions = (
		"get home",
		"follow the mysterious radio signal",
		"stay alive",
		"reach a settlement",
		"join a gang",
		"start a farm",
		"revenge",
		"to repair their vehicle",
	)



	potential_ambition = random.choice(ambitions)

	if callable(potential_ambition):
		return potential_ambition()

	return potential_ambition


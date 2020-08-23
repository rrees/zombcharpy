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
			"gasoline",
			"a library",
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
		"repair their vehicle",
		"start a band",
		"meet someone new",
		"fall in love again",
	)

	desire = random.choice(('hope', 'want', 'would like', 'need'))

	potential_ambition = random.choice(ambitions)

	modifier = ''

	if random.random() < 0.1:
		modifier = random.choice(("really", "desperately", "bitterly")) + " "

	ambition = potential_ambition() if callable(potential_ambition) else potential_ambition

	return f"{modifier}{desire} to {ambition}"


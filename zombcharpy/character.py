import random

def former_job():
	jobs =["farmer",
		"forester", "checkout clerk", "call centre operator", "lawyer", "taxi driver", "chef", "talk show host",
		"prison guard",
		"junkie",
		"mechanic",
		"hairdresser",
		"barrista",]

	return random.choice(jobs)

def current_job():
	jobs = ["smuggler", "courier", "guard", "medic", "guide", "loner", "tracker", "bounty hunter", "fisherman", "trader"]

	return random.choice(jobs)

def ambition():
	ambitions = (
		"get home",
		"find their family",
		"find safety",
		"find a cure",
		"follow the mysterious radio signal",
		"stay alive",
		"reach a settlement",
		"join a gang",
		"find supplies",
		"start a farm",
		"revenge",
		"to repair their vehicle",
	)

	return random.choice(ambitions)


def create_character():
	return f"""You meet someone.
Before everything happened they used to be a {former_job()}; now they're a {current_job()}.
They want to {ambition()}."""
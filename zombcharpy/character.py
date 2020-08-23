import random

from .ambitions import ambition
from .jobs.jobs import current_job

def former_job():
	jobs =["farmer",
		"forester", "checkout clerk", "call centre operator", "lawyer", "taxi driver", "chef", "talk show host",
		"prison guard",
		"junkie",
		"mechanic",
		"hairdresser",
		"barrista",
		"shop assistant",
		"teacher",
		"trucker",]

	return random.choice(jobs)


def create_character():
	return f"""You meet someone.
Before everything happened they used to be a {former_job()}; now they're a {current_job()}.
{ambition()}."""
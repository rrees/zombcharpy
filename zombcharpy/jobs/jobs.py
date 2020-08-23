import random

from .post_apocalypse_jobs import jobs

def current_job():
	return random.choice(jobs)


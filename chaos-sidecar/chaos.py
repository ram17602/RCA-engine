import random, time


def inject():
    while True:
        if random.random() < 0.3:
            time.sleep(random.uniform(0.5, 2))
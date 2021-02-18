import random

def add_a_brick():
    brick_type=random.randint(1,4)
    brick_type='brick'+str(brick_type)
    return brick_type

from envtest import greeting_func

import pandas as pd 
import random

greetings = ["Hi, how are you?", 
                 "You look nice today",
                 "I love your shoes",
                 "Can I buy you a drink?",
                 "Tip top of the morning to ya",
                 "Great to see you again",
                 "Salutations",
                 "Hey!",
                 "What the frick is up bro"]

output = random.choice(greetings)
print(output)
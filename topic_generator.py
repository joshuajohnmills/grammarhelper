import random
import os
class TopicGenerator:
    def __init__(self):
        topic = "e_42"
        self.topic = topic

    def get_topic(self):
        #open the excersise file and text file in topics/{topic}/explination.txt
        self.topic = f'e_{random.choice(range(0,30))}'

        with open(f"topics/{self.topic}/explanation.txt", "r",encoding= 'utf-8') as file:
            topic = file.read()


        #get the excersise file and text file in topics/{topic}/excersise.txt
        with open(f"topics/{self.topic}/exercises_1.txt", "r", encoding= 'utf-8') as file:
            excersise = file.read()
            
        return {"topic": topic, "excersise": excersise}
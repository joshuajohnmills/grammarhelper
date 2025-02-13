from openai import OpenAI

class QuestionGenerator:
    def __init__(self):
        self.client = OpenAI()

    def get_question(self,topic):
        self.messages=[
            {"role": "developer", "content": "You are a helpful quiz maker. You make a single line question to practice the grammar taught in the topic. The question should be in French, or occasionally an english to french translation. The question should be clear and concise. The question should be based on the text and excersise provided."},
            {
                "role": "user",
                "content": topic['topic']  + " " + topic['excersise']
            },
            {
                "role": "user",
                "content": "Based on this text can you create a single line quetion. Make it understandable even if I have not seen the text or has no other context. When I answer a question respoond with the correct answer an epxlanation of why my answer is correct or incorrect in a breakdown form. This should be in English. Praise the me for the correct pointt"
            }
        ]
        completion =  self.client.chat.completions.create(
                model="gpt-4o",
                messages=self.messages
        )
        print(completion.choices[0].message.content)
        self.messages.append({"role": "assistant", 'content': completion.choices[0].message.content})
        return completion.choices[0].message.content

    def correct_question(self, response):
        self.messages.append({"role": "user", "content": response})
        completion =  self.client.chat.completions.create(
                model="gpt-4o",
                messages=self.messages
        )
        print(completion.choices[0].message.content)
        self.messages = []
        return completion.choices[0].message.content
    
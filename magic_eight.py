from random import randrange
user = input('What is your question?: ')
while user != 'quit':
    def function():
        user = input('What is your question?: ')
        return user
    def check_question(user):
        if user[-1] == '?':
            answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
            'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Do not count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
            x = randrange(len(answers))
            print(answers[x])
        else:
            print('I’m sorry, I can only answer questions')
    check_question(user)
    user = function()

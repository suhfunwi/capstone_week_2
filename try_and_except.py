import requests
question = input('Enter your question for the magic 8 ball: ')
magic_8_ball_url = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'
try:
    response = requests.get(magic_8_ball_url).json()
    answer = response['magic']['answer']
    print(f'The magic 8 ball says... {answer}')
except Exception as e:
    print('Sorry, can\'t ask the magic 8 ball. Are you connected to the internet?')
    print(e)
#     only do this while developing to help debug. don't use in production app

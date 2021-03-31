from datetime import datetime

def test():
    print('--- THE TEST FC RAN')

def getTime():
    time = datetime.now().time()
    time = time.strftime("%I:%M %p")
    print("It's ", time)




mappings = {
    'greeting' : test,
    'time' : getTime,
}
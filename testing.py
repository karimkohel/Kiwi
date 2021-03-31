from datetime import datetime

time = datetime.now().time()

time = time.strftime("%I:%M %p")

print(time)
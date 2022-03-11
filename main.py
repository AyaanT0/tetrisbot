import subprocess

filename = 'tetris-bot.py'
while True:
    p = subprocess.Popen('python3 '+filename, shell=True).wait()

    if p != 0:
        continue
    else:
        break


#this restarts the bot if it runs out of memory
#this explanation was written for ian
#you're welcome ian
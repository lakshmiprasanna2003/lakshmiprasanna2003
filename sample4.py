import time 
def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Fire in the hole!!') 
t = input("Enter the time in seconds: ") 
countdown(int(t))





output:

Enter the time in seconds: 10
00:1000:0900:0800:0700:0600:0500:0400:0300:0200:01Fire in the hole!!




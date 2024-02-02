from time import sleep

number = 1
try:        #try this
    while True:     #infinite loop
        try:        #try this
            print(number)       #print current value of [number] starting with 1
            number += 1     #incrementally add 1
            sleep(1)        #delay 1 second
        except KeyboardInterrupt:       #if there is a keyboard interruption
            break       #stop
finally:        #when original try loop end, 'finally' try this
    print(f'''You stopped at {number - 1}. Way to go!''')       #print output
    
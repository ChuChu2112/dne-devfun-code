from time import sleep

firstNumber = int(input("Which number would you like to start counting from: "))

def counter(firstNumber):
    try:        #try this
        while True:     #infinite loop
            try:        #try this
                print(firstNumber)       #print current value of [number] starting with 1
                firstNumber += 1     #incrementally add 1
                sleep(1)        #delay 1 second
            except KeyboardInterrupt:       #if there is a keyboard interruption
                break       #stop
    finally:        #when original try loop end, 'finally' try this
        print(f'''You stopped at {firstNumber - 1}. Way to go!''')       #print output
        
counter(firstNumber)
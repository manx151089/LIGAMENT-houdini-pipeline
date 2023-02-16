import time
    
num_tasks=range(1,24)

with hou.InterruptableOperation("aaa",open_interrupt_dialog=True) as operation:
    for i in num_tasks:
        #
        #
        #
        print i
        time.sleep(1)
        #
        #
        percent = float(i)/float(len(num_tasks))
        operation.updateProgress(percent)
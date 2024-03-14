# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 4, length = 100, fill = '|', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix} | complete = {iteration}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

# import time

# # A List of Items
# items = list(range(0, 57))
# l = len(items)
# import pandas as pd
# df =pd.DataFrame()
# for i in range(100):
#     df = df.append({"name":f"User{i}"}, ignore_index=True)
# # Initial call to print 0% progress
# l= len(df)
# printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 100)
# # for i, item in enumerate(df):
# for i in range(len(df)):
#     # Do stuff...
#     time.sleep(0.1)
#     # Update Progress Bar
#     printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 100)
import os
print(os.getcwd())
with open('data.txt', 'a') as file:
    file.write('\n789')

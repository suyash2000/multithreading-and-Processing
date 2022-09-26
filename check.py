# Code to Measure time taken by program to execute.
import time
  
# store starting time
begin = time.time()
  
# program body starts
  
for i in range(10):
    print("GeeksForGeeks")
# program body ends
  
# store end time
end = time.time()
  
# total time taken
print(f"Total runtime of the program is {end - begin}")
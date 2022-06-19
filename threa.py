import threading
import time

def job():
  for i in range(5):
    print("Child thread:", i)
    time.sleep(1)
    
# # 建立一個子執行緒
# t = threading.Thread(target = job)

# # 執行該子執行緒
# t.start()

# # 主執行緒繼續執行自己的工作
# for i in range(3):
  # print("Main thread:", i)
  # time.sleep(1)

# # 等待 t 這個子執行緒結束
# t.join()

# print("Done.")


def job(num):
  print("Thread", num)
  time.sleep(1)
# 建立 5 個子執行緒
threads = []
for i in range(5):
  threads.append(threading.Thread(target = job, args = (i,)))
  
  threads[i].start()
  
# 等待所有子執行緒結束
for i in range(5):
  threads[i].join()

print("Done.")

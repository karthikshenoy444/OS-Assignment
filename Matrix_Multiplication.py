import threading

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result=[[0, 0, 0] for _ in range(3)]
parts=[[[0, 0, 0] for _ in range(3)] for _ in range(3)]
threads=[]


def multiply(i,j,k):
    value=A[i][k]*B[k][j]
    parts[i][j][k]=value
    print(f"Thread {i}{j}{k}: {A[i][k]}*{B[k][j]} = {value}")


for i in range(3):
    for j in range(3):
        for k in range(3):
            thread=threading.Thread(target=multiply, args=(i, j, k))
            threads.append(thread)
            thread.start()

for thread in threads:
    thread.join()

for i in range(3):
    for j in range(3):
        result[i][j] = sum(parts[i][j])

print("\nResult matrix:")
for row in result:
    print(row)

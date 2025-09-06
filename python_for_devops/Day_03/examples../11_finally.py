#Use: Always executes after try/except


try:
    print(10 / 2)
finally:
    print("This always runs")

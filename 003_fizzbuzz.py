print("How many shall we count?")
num = input()
num = int(num)
print("OK! We count to ",num,".")
print("Please press ENTER to Start.")
input()

for i in list(range(1,num+1)):
  if i%15==0:
    print("FizzBuzz")
  elif i%5==0:

    print("Buzz")
  elif i%3==0:
    print("Fizz")
  else:
    print(i)

print("")
print("Thank you!")
print("")
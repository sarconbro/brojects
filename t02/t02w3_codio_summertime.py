# # Write a script that asks the user to input numbers in a loop. The script will continuously calculate the sum of all the numbers typed.
# When the sum reaches 1000 (or more), the loop will stop and the final sum will be printed.

# codio@shipbridge-geneticdemo:~/workspace$ python3 .guides/demo_scripts/demo_summer.cpython-311.pyc
# Enter your number: 998
# Enter your number: 1
# Enter your number: 1
# Final sum: 1000
# codio@shipbridge-geneticdemo:~/workspace$ 


def main():
  total = 0
  while total < 1000:
    num = int(input('Enter your number: '))
    total += num
  print('Final sum:', total)

if __name__ == "__main__":
    main()

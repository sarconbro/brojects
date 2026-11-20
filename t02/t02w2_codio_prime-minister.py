def get_range():
  start = int(input('Enter start range:'))
  end = int(input('Enter end range:'))
  return start, end

def is_divisible_by(number, by):
  return number % by == 0

def is_prime(number):
#  if number == 2:                                  #edge case abfangen, weil sonst number = 2 None ergibt in loop und range // ausgeklammert, löst sich unten auch auf bei return True
#    return True
  for possible_divisor in range(2, number-1):       #checkt jede zahl zwischen 2 und number-1 (prime nur durch 1 und sich selbst teilbar, also checke ich alle dazwischen)
    if is_divisible_by(number, possible_divisor):   #checkt ob number durch die zahlen in range teilbar ist - wenn irgendwo True (==0, kein Rest), dann kein Prime
      return False
  return True                                       #wenn nach ende der schleife kein False war, muss es True sein
  
def primes_in_range(start, end):
  for number in range(start, end):
    if is_prime(number):
      print(f'The number {number} is prime')

def main():
  start, end = get_range()
  primes_in_range(start, end)
  

if __name__ =="__main__":
  main()
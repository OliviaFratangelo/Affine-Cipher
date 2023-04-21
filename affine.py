def Euclidian(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = Euclidian(b % a, a)
        return gcd, y - (b // a) * x, x
        
def modinverse(a, n): 
  gcd, x, y = Euclidian(a, n) 
  return x % n
 

def decrypt(ciphertext, key): 
  return ''.join([ chr((( modinverse(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in ciphertext ]) 

def main(): 
   file = input("Enter the ciphertext: ")
   while (file != -1):
     start = int(input("Enter 1 to start the loop or enter 2 to exit: "));
     if start == 1:
       a = int(input("Enter first number: "));
       b = int(input("Enter second number: "));
       key = [a,b]
       print('Decrypted Text: {}'.format(decrypt(file, key) )) 
     if start == 2:
        file = -1
        print('Loop ended') 
if __name__ == '__main__': 
  main() 

import json

def power(a, n, mod):
  pow = 1
  prevPower = a
  while n > 0:
    if n % 2 == 1:
      pow = (pow * prevPower) % mod
    n //= 2
    prevPower = (prevPower * prevPower) % mod
  return pow
  
  
def lambda_handler(event, context):
    #print("OM=====",event)
    bodyStr = event["body"]
    bodyJson = json.loads(bodyStr)
    passwordEntered = bodyJson["pwd"]
    
    passwordAsInt = int(passwordEntered)
    N = 1500450271 * 3267000013
    p =  2860486313
    g = 3
    e = 65537
    d = 3440213260876878353
    trials = 30
    encodedPassword = power(g, passwordAsInt, p)   
    encryptedPassword = power(encodedPassword, e, N)
    
    
    decryptedPassword = power(encryptedPassword, d, N)
    
    works = True
    for i in range(trials):
      r = random.randint(0,p-2)
      exponent = power(g, r, p)
      encryptedExponent = power(exponent, e, N)
      decryptedExponent = power(encryptedExponent, d, N)
      if random.randint(0,1) == 0:
        val = (passwordAsInt + r) % (p-1)
        encryptedVal = power(val, e, N)
        decryptedVal = power(encryptedVal, d, N)
        works = ((decryptedExponent * decryptedPassword) == power(g, decryptedVal)
      else:
        val = r
        encryptedVal = power(val, e, N)
        decryptedVal = power(decryptedVal, d, N)
        works = decryptedExponent == power(g, r, N)
    

    pwds = {
      "encodedPassword": encodedPassword,
      "encryptedPassword": encryptedPassword,
      "decryptedPassword": decryptedPassword
      
    }
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(pwds)
    }
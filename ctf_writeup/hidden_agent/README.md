# hidden_agent

**Category:** Blind SQL Injection — User Enumeration

## Vulnerability
Boolean oracle exploited to enumerate a hidden user account and extract their password hash.

## Approach
Discovered a hidden user via enumeration, then extracted their password field:
```
' OR email='hidden' AND ascii(mid(password,{i},1))={ord(c)} #
```
The oracle response confirmed each character match.

## Key Insight
The boolean response leaked information about *any* user in the database — not just the current session user. This enabled enumeration of hidden and admin accounts.

## Exploit
See [blind_sqli.py](./blind_sqli.py)

## Mitigation
- Prepared statements
- Consistent response times regardless of query results — eliminate boolean oracles
- Sensitive accounts should not share the same DB table as regular users

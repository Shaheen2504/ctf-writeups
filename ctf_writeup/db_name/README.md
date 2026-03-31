# db_name

**Category:** Blind SQL Injection

## Vulnerability
Blind SQLi using the `database()` function to extract the current database name character by character.

## Approach
```
' OR id=1 AND ascii(mid(database(),{i},1))={ord(c)} #
```
Extracted the full database name. Flag was formed by removing the first character.

## Key Insight
Direct `database()` calls worked even when subqueries were blocked by the application.

## Exploit
See [blind_sqli.py](./blind_sqli.py)

## Mitigation
- Prepared statements
- Restrict DB user privileges — no access to `database()` in a meaningful context
- Rate limiting on login endpoint

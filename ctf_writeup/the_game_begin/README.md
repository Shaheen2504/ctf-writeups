# the_game_begin

**Category:** SQL Injection

## Vulnerability
Classic SQL Injection in the login form. User input was directly concatenated into the SQL query without sanitization:
```sql
SELECT * FROM users WHERE email='$email' AND MD5(password)='$pass_hash'
```

## Approach
Injected into the password field to short-circuit the AND condition using OR:
- **Payload:** `' OR email='attacker@example.com' #`

The `#` comments out the rest of the query, bypassing the password check entirely. Flag was visible in the profile Bio after login.

## Exploit
See [exploit.py](./exploit.py)

## Mitigation
- Use prepared statements — never concatenate user input into SQL queries
- Apply input validation on all user-supplied fields
- Deploy a WAF to detect SQL injection patterns

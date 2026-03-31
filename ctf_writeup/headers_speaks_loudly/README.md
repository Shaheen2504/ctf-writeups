# headers_speaks_loudly

**Category:** HTTP Header Manipulation

## Vulnerability
The application used HTTP request headers for authentication logic without treating them as untrusted input. Setting specific header values unlocked hidden functionality.

## Approach
Crafted a request with specific header values the application expected:
```
User-Agent:   CTF-Agent
Referer:      referer.example.com
DNT:          1
X-UIDH:       <specific value>
Cookie:       admin=1
```
Sent to `/?p=apps&f=2` — flag revealed in response.

## Key Insight
HTTP headers are fully client-controlled. Setting `Cookie: admin=1` combined with specific header values bypassed the access check entirely.

## Exploit
See [exploit.py](./exploit.py)

## Mitigation
- Never use HTTP headers for authentication or authorisation decisions
- Treat all headers as untrusted user input
- Use proper session-based authentication — never trust cookie values like `admin=1`

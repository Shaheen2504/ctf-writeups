# CTF Writeups — Web Security

A collection of web security CTF challenge writeups with exploit scripts.

## Challenges

| Challenge | Category | Technique |
|-----------|----------|-----------|
| [the_game_begin](./the_game_begin/) | SQL Injection | Classic SQLi login bypass |
| [get_your_pa55word](./get_your_pa55word/) | Blind SQLi | Boolean-based blind SQLi |
| [db_name](./db_name/) | Blind SQLi | Extract DB name character by character |
| [db_user](./db_user/) | Blind SQLi | Extract DB user character by character |
| [hidden_agent](./hidden_agent/) | Blind SQLi | Hidden user account enumeration |
| [database_hunting](./database_hunting/) | UNION SQLi | WAF bypass + UNION-based injection |
| [headers_speaks_loudly](./headers_speaks_loudly/) | Header Injection | HTTP header manipulation |
| [agent_lfi](./agent_lfi/) | LFI | Local File Inclusion via path traversal |
| [agent_rfi](./agent_rfi/) | File Upload | Unrestricted file upload + PHP webshell |
| [game_of_collisions](./game_of_collisions/) | PHP Type Juggling | MD5 magic hash collision |

## Skills Demonstrated

- SQL Injection — classic, blind boolean, UNION-based, WAF bypass
- Local File Inclusion and path traversal
- Unrestricted file upload and PHP code execution
- PHP type juggling vulnerabilities
- HTTP header manipulation
- Automated exploit scripting in Python

## Tools

`Python 3` `requests` `Burp Suite`

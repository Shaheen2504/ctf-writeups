# game_of_collisions

**Category:** PHP Type Juggling / MD5 Magic Hash Collision

## Vulnerability
PHP type juggling — the application compared two MD5 hashes with loose `==` instead of strict `===`. In PHP, strings starting with `0e` followed only by digits are interpreted as scientific notation (0 × 10^N = 0), so any two such strings compare equal.

## Magic Hashes Used

| Input | MD5 Hash |
|-------|----------|
| `0e215962017` | `0e291242476940776845150308577824` |
| `0e807097110` | `0e289979931537747905798937436305` |

Both start with `0e` + digits only → PHP evaluates both as `0` → `0 == 0` is `TRUE`.

## Approach
Submitted `arg1=0e215962017` and `arg2=0e807097110` — PHP loose comparison returned TRUE and revealed the flag.

**Alternative — Array bypass:**
```
GET /?p=apps&f=1&arg1[]=a&arg2[]=b
```
`md5([])` returns `NULL` in PHP, and `NULL == NULL` is also `TRUE`.

## Exploit
See [exploit.py](./exploit.py)

## Mitigation
- Always use strict comparison (`===`) for hash comparisons
- Use `hash_equals()` for constant-time secure comparison
- Never compare MD5 hashes with `==` in PHP

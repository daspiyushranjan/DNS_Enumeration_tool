# DNS_Enumeration_tool

A basic Python-based DNS enumeration tool created for learning and practicing DNS concepts.

## Features

* IPv4 address lookup
* IPv6 address lookup
* Basic subdomain enumeration
* Subdomain wordlist support
* Basic error handling

## Files

* `dns_enum.py` — Main Python program
* `subdomains.txt` — List of subdomains used for enumeration

## Requirements

* Python 3.x
* No external libraries required

## Usage

Make sure `dns_enum.py` and `subdomains.txt` are in the same directory.

Run:

```bash
python dns_enum.py
```

Enter a domain when prompted:

```text
Enter domain (example.com):
```

The tool will perform DNS lookups and check the subdomains listed in `subdomains.txt`.

## Purpose

This project was built as a beginner cybersecurity learning project to understand:

* DNS resolution
* IPv4 and IPv6
* Subdomains
* Python socket programming
* File handling
* Basic reconnaissance concepts

## Disclaimer

Use this tool only on domains you own or have permission to test.

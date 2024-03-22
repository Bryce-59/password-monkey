# About this Project

I use both a Windows PC and a Mac Laptop. A problem I have come across is that my password managers are not synced. Either Google or Apple will generate a random password for me, and it will be completely inaccessible from my other device.

As a result, I created Password Monkey to generate deterministic strings that satisfy strong password requirements. With a simple key and a (optionally resusable) security code (which could be a random string, a username, a PIN code, etc) it returns a specific random string. This makes passwords easier to remember and easier to sync across devices.

Password Monkey is less secure the more people use it, and the entire space of possible passwords could be recorded with a rainbow table. However, even in the worst case, it is more secure than plaintext (but less secure than true random strings).

# How to Run

`make init`
`python3 monkey/password_monkey.py`

# Roadmap

If I wanted to develop this project further, I could create a login system which gives each user a unique password space using unique salt. In that case, the base Password Monkey could still be implemented as a guest mode.

# Credits
- 2023 Bryce Richardson

# License
- [MIT License](https://choosealicense.com/licenses/mit/)
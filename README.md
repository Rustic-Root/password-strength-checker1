# Password Strength Checker

## Description
A simple Python tool to check the strength of a password. It ensures your password is secure and helps you avoid weak or commonly used passwords.

## Features
- Checks password length, variety, and common patterns.
- Optionally checks if a password has been part of a data breach using the Have I Been Pwned API.

## Installation
1. Clone this repository: git clone https://github.com/your-username/password-strength-checker.git
2. Navigate to the project directory: cd password-strength-checker
3. Install the required library: pip install requests

## Usage
1. Run the program: python password_checker.py
2. Enter a password when prompted and check the results.

## Example
Enter a password to check: Pass123 
Weak: Password must be at least 8 characters long.

Enter a password to check: StrongPass@123! 
Strong: Your password is secure! Safe: This password has not been found in any known breaches.

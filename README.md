# password-strength-analyzer-

🔐 Password Strength Analyzer

A defensive security tool that evaluates password strength using rule-based analysis and entropy estimation, providing transparent feedback on why a password is weak or strong.

This project is designed to demonstrate secure coding practices, input validation, and security-aware software design.

# 🔐 Password Strength Analyzer

## ✨ Features
- Rule-based password analysis
- Entropy estimation (bits)
- Human-readable feedback
- JSON output for automation
- Command-line interface (CLI)
- Fully unit-tested
- No password storage or logging


🧠 How It Works

Password strength is evaluated using two complementary approaches:

1️⃣ Rule-Based Analysis

Checks for:

Password length

Character variety (upper, lower, digits, symbols)

Repeated characters

Sequential patterns (e.g. abc, 123)

Each rule adjusts a score and produces an explanation if weaknesses are found.

2️⃣ Entropy Estimation

Entropy is calculated using:

entropy = length × log2(character_pool_size)


This estimates resistance to brute-force attacks and prioritizes length over complexity, aligning with modern security guidance.

▶️ Usage
python cli.py --password "Tr0ub4dor&3"


Example output:

Strength: Moderate (63/100)
Entropy: 57.21 bits

Issues:
- Password length is below the recommended 12 characters


JSON output:

python cli.py --password "Xy9!fQ2$LmR@p" --json

🧪 Running Tests
python -m pytest

🔒 Security & Ethics

Passwords are processed in memory only

No passwords are logged, stored, or transmitted

This tool is intended for defensive and educational use

Inspired by real-world authentication systems

📌 Future Enhancements

Crack-time estimation

Configurable password policies

Unicode character support

Packaging as a pip-installable tool
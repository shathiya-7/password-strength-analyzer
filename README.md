# 🔐 Password Strength Analyzer

A Python-based cybersecurity tool that evaluates the strength of a user-entered password using password length, character diversity, estimated entropy, and security checks.

The tool provides a simple final assessment containing the **password length, entropy, score, and overall verdict**.

---

## 📌 Features

* 📏 Password length calculation
* 🔐 Estimated password entropy
* 📊 Password strength score
* 🚦 Strength verdict
* 🔤 Lowercase character detection
* 🔠 Uppercase character detection
* 🔢 Number detection
* 🔣 Special-character detection
* 🚫 Common-password detection
* 🔁 Repeated-character detection
* 🔒 Hidden password input
* 💡 Uses only Python standard libraries

---

## 🛠️ Technologies Used

* **Python 3**
* `re` — Regular expressions
* `math` — Entropy calculation
* `getpass` — Hidden password input

No external Python packages are required.

---

## 📂 Project Structure

```text
password-strength-analyzer/
│
├── password_analyzer.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ How It Works

The analyzer evaluates the password using several factors.

### 1. Password Length

The number of characters in the password is calculated.

Longer passwords generally provide better resistance against brute-force attacks.

### 2. Entropy

Estimated entropy represents the theoretical uncertainty of the password.

The simplified calculation is:

```text
Entropy = Password Length × log₂(Character Set Size)
```

The character set is estimated from the presence of:

* Lowercase letters
* Uppercase letters
* Numbers
* Special characters

Entropy is displayed in **bits**.

### 3. Strength Score

The password receives a score out of **7**.

| Criterion         | Points |
| ----------------- | -----: |
| 12+ characters    |     +2 |
| 8–11 characters   |     +1 |
| Lowercase letter  |     +1 |
| Uppercase letter  |     +1 |
| Number            |     +1 |
| Special character |     +1 |

Common passwords and repeated characters can reduce the score.

### 4. Verdict

The final verdict is based on the score and estimated entropy.

| Verdict     | General Interpretation                      |
| ----------- | ------------------------------------------- |
| WEAK        | Easily guessable or insufficient complexity |
| MODERATE    | Some security characteristics are present   |
| STRONG      | Good password characteristics               |
| VERY STRONG | High complexity and estimated resistance    |

---

## 🚀 Running the Project

### Using GitHub Codespaces / VS Code

Open the repository in the GitHub VS Code environment and open the integrated terminal.

Run:

```bash
python password_analyzer.py
```

If your environment uses `python3`, run:

```bash
python3 password_analyzer.py
```

---

## 💻 Example

```text
Password Strength Analyzer
---------------------------
Your password will not be stored or displayed.

Enter your password:

=============================================
       PASSWORD STRENGTH ANALYZER
=============================================

Password Length : 14
Entropy         : 91.81 bits
Score           : 7/7
Verdict         : VERY STRONG

=============================================
```

---

## 🔒 Security Considerations

This project is intended for educational purposes.

* Passwords are not stored.
* Passwords are not printed to the terminal.
* Password input is hidden using Python's `getpass` module.
* The common-password list is only a small demonstration list.
* Entropy is an estimate and does not guarantee that a password is actually random or secure.

For production authentication systems, password strength checking should be combined with secure password hashing, multi-factor authentication, rate limiting, and breached-password detection.

---

## 🎯 Learning Objectives

This project demonstrates:

* Python functions
* Regular expressions
* Conditional logic
* Sets
* Mathematical calculations
* Password security concepts
* Entropy estimation
* Secure user input
* Basic cybersecurity programming

---

## 🔮 Future Improvements

Possible improvements include:

* 📈 Graphical password-strength meter
* 🔑 Secure password generator
* 🧪 Unit testing
* 🌐 Web interface using Flask or FastAPI
* 📚 Larger breached-password database
* 🧠 More advanced password-strength estimation
* 📊 Detailed password analysis report

---

## ⚠️ Disclaimer

This project is intended for educational and cybersecurity learning purposes. Do not use it to collect, store, or monitor passwords belonging to other users.

---

## 👩‍💻 Author

**Shathiya K**


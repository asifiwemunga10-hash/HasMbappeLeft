# 🐢 Has Mbappé Left Madrid Yet?

A fully automated Twitter bot that posts daily:

Nope. Day X.

Tracking how many days Kylian Mbappé has (not) left Real Madrid.

---

## 🚀 Features

- 📅 Posts once per day automatically
- 🔢 Day counter increases every day
- ⚙️ Runs using GitHub Actions (no server needed)
- 🔐 Secure (uses GitHub Secrets for API keys)
- 🧠 Fully hands-off after setup

---

## 🛠️ How It Works

- Uses the X (Twitter) API to post tweets
- GitHub Actions runs the script daily
- The bot calculates the current day using UTC time

---

## ⏰ Schedule

Runs automatically every day at:

- 5:07 AM UTC  
- ≈ 10:07 PM (Washington time)

---

## 📂 Project Structure

.
├── bot.py
└── .github/
    └── workflows/
        └── post-daily.yml

---

## 🔐 Required Secrets

In your GitHub repo, go to:

Settings → Secrets and variables → Actions

Add these:

- X_API_KEY (Consumer Key)
- X_API_SECRET (Consumer Secret)
- X_ACCESS_TOKEN (Access Token)
- X_ACCESS_TOKEN_SECRET (Access Token Secret)

---

## ▶️ How to Run

### Automatic
Runs daily via GitHub Actions (no input needed)

### Manual (for testing)
1. Go to Actions tab
2. Click workflow
3. Click Run workflow

---

## ⚠️ Notes

- Do NOT hardcode API keys in your code
- If the bot doesn’t run:
  - Check the workflow is committed
  - Check the schedule exists
  - Check GitHub Actions logs

---

## 🧠 Example Output

Nope. Day 670.  
Nope. Day 671.  
Nope. Day 672.

---

## 🔥 Future Ideas

- Add random variations ("Still nope.", "Not today.")
- Add football facts alongside the day
- Add multiple daily posts

---

## 💀 Disclaimer

This is a fun, automated fan project.
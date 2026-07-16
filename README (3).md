# IshikaChatBot ✨

Advanced Telegram Group Manager Bot + AI Chatbot, powered by Pyrogram + MongoDB + Gemini.

## Features
- Admin Tools (Tagall, TagAdmins)
- Couples
- **AI Chatbot** (Gemini) — DM mein har message ka reply, group mein sirf jab
  bot ko mention/reply karo
- MongoDB Storage

## Commands
- `/start` — Welcome message
- `/tagall <text>` / `/all <text>` — Sabko mention karo
- `/stop` — Tagall band karo
- `/tagadmins` — Sirf admins ko tag karo
- `/couple` — Aaj ka random couple
- Koi bhi normal message (DM mein, ya group mein bot ko @mention/reply karke) — AI chatbot reply dega

## Environment Variables
`.env.example` copy karke `.env` banao aur values bharo:
- `API_ID`, `API_HASH` — my.telegram.org se
- `BOT_TOKEN` — @BotFather se
- `BOT_USERNAME` — bot ka username (bina @)
- `OWNER_ID` — apni Telegram user ID
- `MONGO_DB_URI` — MongoDB Atlas connection string
- `GEMINI_API_KEY` — Google AI Studio se free Gemini API key

## Run Locally
```bash
pip install -r requirements.txt
python -m ishika
```

## Deploy on Render
1. Repo ko GitHub pe push karo, phir Render dashboard → **New → Web Service** → repo select karo
   (`render.yaml` already isi repo mein hai, Render use auto-detect kar lega)
2. Environment tab mein saare vars upar wali list se daalo
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `python -m ishika`

**Important — Free tier spin-down:** Render ka free Web Service 15 min inactivity
ke baad so jaata hai, jisse bot offline ho jayega. Isse bachne ke liye
[UptimeRobot](https://uptimerobot.com) (free) pe apna Render URL (`https://your-app.onrender.com/`)
har 5 min pe ping karwao, ya phir paid instance ($7/mo se) use karo agar bot
24x7 chahiye without any gaps.

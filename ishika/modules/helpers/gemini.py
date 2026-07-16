import aiohttp

from ishika.config import GEMINI_API_KEY

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent"
)

SYSTEM_PROMPT = (
    "You are Ishika, a friendly Telegram group assistant. "
    "Reply in casual Hinglish (Hindi + English mix), keep replies short "
    "(2-4 lines), and use a warm, playful tone with the occasional emoji. "
    "Never claim to be a human."
)


async def ask_gemini(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "Gemini API key set nahi hai. `.env` mein GEMINI_API_KEY daal ke bot restart karo 🙏"

    payload = {
        "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
    }
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY,
    }

    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post(GEMINI_URL, json=payload, headers=headers) as resp:
            data = await resp.json()

            if resp.status != 200:
                message = data.get("error", {}).get("message", "Gemini API error")
                raise RuntimeError(f"[{resp.status}] {message}")

            candidates = data.get("candidates") or []
            if not candidates:
                return "Kuch samajh nahi aaya, dobara try karo 🙈"

            parts = candidates[0].get("content", {}).get("parts", [])
            text = "".join(p.get("text", "") for p in parts).strip()
            return text or "..."

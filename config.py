import os

# توکن بات رو از پنل بله (ble.ir) بگیر و اینجا یا در متغیر محیطی BOT_TOKEN بذار
BOT_TOKEN = os.getenv("BOT_TOKEN", "PUT-YOUR-TOKEN-HERE")

# آدرس پایه‌ی API بله
BALE_API_BASE = "https://tapi.bale.ai/bot"
# آدرس پایه‌ی دانلود فایل از بله (این با آدرس API فرق داره! بدون این، دانلود فایل‌ها از تلگرام تلاش می‌شد نه بله)
BALE_FILE_BASE = "https://tapi.bale.ai/file/bot"

# فقط این آیدی عددی، مالک بات محسوب میشه و به پنل مدیریت (فقط در پیوی) دسترسی داره
OWNER_IDS = [581301761]

# کلمات ممنوعه‌ی پیش‌فرض (از پنل هم قابل افزودن/حذفه)
DEFAULT_BAD_WORDS = [
    "کلمه_نامناسب_۱",
    "کلمه_نامناسب_۲",
]

# جلوگیری از لینک/تبلیغ توسط اعضای عادی (پیش‌فرض)
BLOCK_LINKS_FOR_MEMBERS_DEFAULT = True

# --- تنظیمات پیش‌فرض آنتی‌فلود سطح‌بندی‌شده ---
FLOOD_MAX_MESSAGES = 6        # حداکثر پیام مجاز در بازه
FLOOD_WINDOW_SECONDS = 8      # بازه‌ی زمانی بررسی (ثانیه)
FLOOD_MUTE_MINUTES = 10       # مدت میوت خودکار سطح اول
FLOOD_LONG_MUTE_MINUTES = 60  # مدت میوت طولانی برای تکرار

DB_PATH = "gapbot.db"

# نام و هویت بات
BOT_NAME = "گروه‌یار"
BOT_INTRO = "🤝 گروه‌یار در خدمته! برای شروع بنویس «راهنما» دوست عزیز 🤝"

# ایموجی‌های ثابت برای طراحی یکپارچه‌ی پیام‌ها
EMOJI = {
    "welcome": "🎉",
    "wave": "👋",
    "rules": "📖",
    "warn": "⚠️",
    "ban": "🚫",
    "kick": "👢",
    "mute": "🔇",
    "unmute": "🔊",
    "stats": "📊",
    "panel": "🛠",
    "broadcast": "📣",
    "banner": "🖼",
    "channel": "📢",
    "check": "✅",
    "cross": "❌",
    "game": "🎮",
    "coin": "🪙",
    "vip": "👑",
    "lock": "🔒",
    "unlock": "🔓",
    "fire": "🚨",
    "star": "⭐️",
    "back": "🔙",
    "add": "➕",
    "remove": "➖",
}

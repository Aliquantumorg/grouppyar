from config import BOT_INTRO
from registry import COMMANDS, PREFIX_COMMANDS


def build_help_text() -> str:
    sections = {
        "public": ("🎮 *عمومی و بازی‌ها:*", []),
        "admin": ("⚖️ *فقط ادمین گروه یا مالک بات:*", []),
    }
    for key, (trigger, _handler, scope, desc) in COMMANDS.items():
        if scope in sections:
            sections[scope][1].append(f"«{trigger}» » {desc}")

    lines = []
    lines.append(sections["public"][0])
    lines.extend(sections["public"][1])
    lines.append("")
    lines.append(sections["admin"][0])
    lines.extend(sections["admin"][1])
    lines.append("")
    lines.append("🔧 *دستورات آرگومان‌دار:*")
    for prefix, desc in PREFIX_COMMANDS.items():
        lines.append(f"«{prefix} ...» » {desc}")
    lines.append("")
    lines.append("🛑 «لغو بازی» » لغو هر بازی‌ای که همین الان در جریانه (فقط بازیکن‌ها یا ادمین/مالک)")
    lines.append("")
    lines.append(f"🛠 *فقط مالک بات، فقط در پیوی:* «پنل» » پنل مدیریت کامل و ویرایش نام دستورات\n")
    lines.append(f"💡 {BOT_INTRO}")
    return "\n".join(lines)


HELP_TEXT = build_help_text()

import requests
import time
import json
import os
from datetime import datetime
TOKEN = "2039524654:jGw-rTRQsqnPMxRyn7f2QeCEO6lZGfYjRwU"
ADMIN_ID = 1245087906
BASE = f"https://tapi.bale.ai/bot{TOKEN}"
USERS_FILE = "users.json"
try:
    import jdatetime
    HAS_J = True
except:
    HAS_J = False
def fa_num(s):
    s = str(s)
    en = "0123456789"
    fa = "۰۱۲۳۴۵۶۷۸۹"
    for e, f in zip(en, fa):
        s = s.replace(e, f)
    return s
def now_fa():
    if HAS_J:
        n = jdatetime.datetime.now()
        d = n.strftime("%d %B %Y")
        t = n.strftime("%H:%M")
    else:
        n = datetime.now()
        d = n.strftime("%Y/%m/%d")
        t = n.strftime("%H:%M")
    return fa_num(d), fa_num(t)
def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except:
            return set()
    return set()
def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(list(users), f)
users = load_users()
user_state = {}
def api(method, payload=None):
    r = requests.post(BASE + "/" + method, json=payload or {}, timeout=35)
    return r.json()
def send_message(chat_id, text, reply_markup=None):
    data = {"chat_id": chat_id, "text": text}
    if reply_markup:
        data["reply_markup"] = reply_markup
    try:
        return api("sendMessage", data)
    except Exception as e:
        print("send error:", e)
        return None
def answer_cb(cb_id, text=None):
    try:
        api("answerCallbackQuery", {"callback_query_id": cb_id, "text": text or ""})
    except:
        pass
def main_menu():
    return {
        "inline_keyboard": [
            [{"text": "🛍 سفارش‌ها", "callback_data": "orders"},
             {"text": "🎨 نمونه‌کار AETHER", "callback_data": "samples"}],
            [{"text": "✍ ثبت نظر", "callback_data": "feedback"},
             {"text": "📞 پشتیبانی", "callback_data": "support"}],
            [{"text": "🌌 درباره AETHER", "callback_data": "about"}]
        ]
    }
def back_menu():
    return {"inline_keyboard": [[{"text": "🔙 برگشت به منو", "callback_data": "home"}]]}
def orders_menu():
    return {
        "inline_keyboard": [
            [{"text": "🌐 سایت تک‌فایل مثل AETHER", "callback_data": "order_site"}],
            [{"text": "🤖 ربات بله", "callback_data": "order_bot"}],
            [{"text": "⚡ پروژه خاص", "callback_data": "order_custom"}],
            [{"text": "🔙 برگشت", "callback_data": "home"}]
        ]
    }
WELCOME = (
    "🌌 به جهان AETHER خوش اومدی\n\n"
    "من ربات رسمی پروژه‌ی ۴۵ روزه‌ام.\n"
    "از منوی شیشه‌ای پایین انتخاب کن:\n"
    "🛍 سفارش • 🎨 نمونه‌کار • ✍ نظر • 📞 پشتیبانی"
)
ABOUT = (
    "🌌 AETHER چیه؟\n\n"
    "۴۵ شب تلاش، ۱۸۰+ ساعت کد، ۲۱۴۰ خط کد خالص.\n"
    "تک‌فایل، بدون قالب آماده، با موتور کهکشان، آزمایشگاه ذرات و ترمینال مخفی.\n\n"
    "این تازه یکی از خفن‌ترین پروژه‌هاست."
)
SAMPLES = (
    "🎨 نمونه‌کار AETHER\n\n"
    "🌌 موتور کهکشان زنده با ۲۲۰ ستاره\n"
    "⚛ آزمایشگاه فیزیک ذرات\n"
    "⌨ ترمینال مخفی با دستور secret\n"
    "🎹 پد صوتی نئونی\n\n"
    "فایل سایت رو باز کن و خرابش کن."
)
SUPPORT_TXT = (
    "📞 پشتیبانی\n\n"
    "حرفت رو همین‌جا بنویس بفرست.\n"
    "مستقیم میرسه دست مدیر و جواب میده."
)
def handle_message(msg):
    chat_id = msg["chat"]["id"]
    text = msg.get("text", "").strip()
    from_u = msg.get("from", {})
    name = (from_u.get("first_name", "") + " " + from_u.get("last_name", "")).strip() or "کاربر"
    username = from_u.get("username", "-")
    if chat_id != ADMIN_ID:
        users.add(chat_id)
        save_users(users)
    if text.startswith("/start"):
        user_state.pop(chat_id, None)
        send_message(chat_id, WELCOME, main_menu())
        if chat_id != ADMIN_ID:
            send_message(ADMIN_ID, f"👤 کاربر جدید استارت زد\nنام: {name}\nآیدی: {chat_id}\nیوزرنیم: @{username}")
        return
    if chat_id == ADMIN_ID and text.startswith("/stats"):
        send_message(chat_id, f"📊 آمار ربات\nکاربرها: {fa_num(len(users))}")
        return
    if chat_id == ADMIN_ID and text.startswith("/reply"):
        parts = text.split(maxsplit=2)
        if len(parts) < 3:
            send_message(chat_id, "فرمت: /reply آیدی_عددپیام")
            return
        try:
            target = int(parts[1])
            send_message(target, "💬 جواب مدیر:\n\n" + parts[2])
            send_message(chat_id, "✅ فرستاده شد.")
        except:
            send_message(chat_id, "آیدی درست نیست.")
        return
    if chat_id == ADMIN_ID and text.startswith("/all"):
        body = text.replace("/all", "").strip()
        if not body:
            send_message(chat_id, "فرمت: /all متن پیام همگانی")
            return
        c = 0
        for u in list(users):
            try:
                send_message(u, "📢 اطلاعیه:\n\n" + body)
                c += 1
            except:
                pass
        send_message(chat_id, f"✅ به {fa_num(c)} نفر فرستاده شد.")
        return
    st = user_state.get(chat_id)
    if st == "waiting_feedback":
        d, t = now_fa()
        formatted = f"سلام من {name} هستم\nخواستم بهت بگم که {text} ✨\nتاریخ : {d} 🌃\nساعت : {t} ⏳️"
        send_message(ADMIN_ID, f"✍ نظر جدید از ربات:\n\n{formatted}\n\n👤 {name} | {chat_id} | @{username}")
        send_message(chat_id, "✅ نظرت فرستاده شد. ممنون که نظر دادی ✨", back_menu())
        user_state.pop(chat_id, None)
        return
    if st == "waiting_order":
        d, t = now_fa()
        send_message(ADMIN_ID, f"🛍 سفارش جدید:\n\n{text}\n\n👤 {name} | {chat_id} | @{username}\n📅 {d} ⏳ {t}")
        send_message(chat_id, "✅ سفارشت ثبت شد. مدیر به‌زودی جواب میده 🙌", back_menu())
        user_state.pop(chat_id, None)
        return
    if st == "waiting_support":
        send_message(ADMIN_ID, f"📞 پیام پشتیبانی:\n\n{text}\n\n👤 {name} | {chat_id} | @{username}")
        send_message(chat_id, "✅ پیامت رسید دست مدیر. صبر کن جواب بده.", back_menu())
        user_state.pop(chat_id, None)
        return
    if chat_id != ADMIN_ID:
        d, t = now_fa()
        send_message(ADMIN_ID, f"📩 پیام جدید:\n\n{text}\n\n👤 {name}\n🆔 {chat_id}\n🔗 @{username}\n📅 {d} ⏳ {t}\n\nبرای جواب: /reply {chat_id} متن")
        send_message(chat_id, "✅ پیامت رسید دست مدیر ✨")
    else:
        send_message(chat_id, "این پیام از طرف مدیر ثبت شد. برای جواب به کاربر: /reply آیدی متن")
def handle_callback(cb):
    cb_id = cb["id"]
    chat_id = cb["message"]["chat"]["id"]
    data = cb.get("data", "")
    from_u = cb.get("from", {})
    name = from_u.get("first_name", "کاربر")
    if data == "home":
        answer_cb(cb_id)
        send_message(chat_id, "منوی اصلی 👇", main_menu())
    elif data == "orders":
        answer_cb(cb_id)
        send_message(chat_id, "🛍 بخش سفارش‌ها:\n\n🌐 سایت تک‌فایل\n🤖 ربات بله\n⚡ پروژه خاص\n\nیکی رو انتخاب کن:", orders_menu())
    elif data in ("order_site", "order_bot", "order_custom"):
        answer_cb(cb_id)
        mp = {"order_site": "سایت تک‌فایل", "order_bot": "ربات بله", "order_custom": "پروژه خاص"}
        user_state[chat_id] = "waiting_order"
        send_message(chat_id, f"🛍 سفارش {mp[data]} انتخاب شد.\n\nتوضیح سفارشت رو همین‌جا بنویس بفرست:", back_menu())
    elif data == "samples":
        answer_cb(cb_id)
        send_message(chat_id, SAMPLES, back_menu())
    elif data == "about":
        answer_cb(cb_id)
        send_message(chat_id, ABOUT, back_menu())
    elif data == "support":
        answer_cb(cb_id)
        user_state[chat_id] = "waiting_support"
        send_message(chat_id, SUPPORT_TXT, back_menu())
    elif data == "feedback":
        answer_cb(cb_id)
        user_state[chat_id] = "waiting_feedback"
        send_message(chat_id, f"{name} عزیز، نظرت درباره کارم و سایتم رو همین‌جا بنویس بفرست 👇", back_menu())
    else:
        answer_cb(cb_id)
def run():
    print("AETHER Bot روشن شد...")
    offset = 0
    while True:
        try:
            res = requests.post(BASE + "/getUpdates", json={"offset": offset, "timeout": 25}, timeout=35).json()
            if not res.get("ok"):
                time.sleep(3)
                continue
            for up in res.get("result", []):
                offset = up["update_id"] + 1
                if "callback_query" in up:
                    handle_callback(up["callback_query"])
                elif "message" in up:
                    if "text" in up["message"]:
                        handle_message(up["message"])
                    else:
                        ch = up["message"]["chat"]["id"]
                        try:
                            api("forwardMessage", {"chat_id": ADMIN_ID, "from_chat_id": ch, "message_id": up["message"]["message_id"]})
                            send_message(ADMIN_ID, f"📦 فایل جدید از {ch}")
                            send_message(ch, "✅ رسید دست مدیر ✨")
                        except:
                            pass
        except Exception as e:
            print("loop error:", e)
            time.sleep(3)
if __name__ == "__main__":
    run()
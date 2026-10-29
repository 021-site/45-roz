import requests
import time
import json
import os
import jdatetime

TOKEN = "973886928:FISShsMogHPRYz2HHomnhqXqfwE2Xxzj2rE"
ADMIN_ID = 1245087906
BASE = f"https://tapi.bale.ai/bot{TOKEN}"
USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def send_message(chat_id, text):
    try:
        r = requests.post(f"{BASE}/sendMessage", data={"chat_id": chat_id, "text": text}, timeout=15)
        return True
    except Exception as e:
        print("خطا در ارسال:", e)
        return False

def get_updates(offset):
    try:
        r = requests.post(f"{BASE}/getUpdates", data={"offset": offset, "timeout": 20}, timeout=25)
        j = r.json()
        if j.get("ok"):
            return j.get("result", [])
        else:
            print("پاسخ غیرمنتظره:", j)
            return []
    except Exception as e:
        print("خطا در اتصال:", e)
        time.sleep(3)
        return []

def now_fa():
    try:
        return jdatetime.datetime.now().strftime("%Y/%m/%d ساعت %H:%M")
    except:
        return time.strftime("%Y/%m/%d %H:%M")

def main():
    print("ربات AETHER روشن شد...")
    print("مدیر:", ADMIN_ID)
    users = load_users()
    offset = 0

    while True:
        updates = get_updates(offset)
        for u in updates:
            offset = u["update_id"] + 1
            msg = u.get("message")
            if not msg:
                continue

            chat = msg.get("chat", {})
            chat_id = chat.get("id")
            text = msg.get("text", "").strip()
            from_info = msg.get("from", {})
            name = (from_info.get("first_name", "") + " " + from_info.get("last_name", "")).strip()
            username = from_info.get("username", "")

            if not text:
                continue

            # دستورات مدیر
            if chat_id == ADMIN_ID:
                if text == "/start":
                    send_message(ADMIN_ID, "سلام مدیر 👋\nربات روشن است.\n/stats - آمار\n/reply آیدی متن - جواب\n/all متن - پیام همگانی")
                elif text == "/stats":
                    total = len(users)
                    send_message(ADMIN_ID, f"📊 آمار ربات AETHER\n\n👥 تعداد کاربرها: {total}\n🕒 {now_fa()}")
                elif text.startswith("/reply"):
                    try:
                        parts = text.split(maxsplit=2)
                        if len(parts) < 3:
                            send_message(ADMIN_ID, "فرمت درست:\n/reply 123456 سلام، ممنون از پیامت")
                        else:
                            target_id = parts[1]
                            answer = parts[2]
                            ok = send_message(target_id, f"💬 جواب مدیر:\n{answer}")
                            if ok:
                                send_message(ADMIN_ID, "✅ ارسال شد.")
                            else:
                                send_message(ADMIN_ID, "❌ ارسال نشد.")
                    except Exception as e:
                        send_message(ADMIN_ID, f"خطا: {e}")
                elif text.startswith("/all"):
                    msg_text = text.replace("/all", "", 1).strip()
                    if not msg_text:
                        send_message(ADMIN_ID, "فرمت درست:\n/all سلام به همه")
                    else:
                        count = 0
                        for uid in list(users.keys()):
                            if send_message(uid, f"📢 پیام مدیر:\n{msg_text}"):
                                count += 1
                            time.sleep(0.1)
                        send_message(ADMIN_ID, f"✅ پیام همگانی به {count} نفر ارسال شد.")
                else:
                    # پیام معمولی مدیر، راهنما
                    send_message(ADMIN_ID, "دستورات:\n/stats\n/reply آیدی متن\n/all متن")
            else:
                # کاربر عادی
                uid = str(chat_id)
                if uid not in users:
                    users[uid] = {"name": name, "username": username, "first_seen": now_fa()}
                    save_users(users)

                if text == "/start":
                    send_message(chat_id, "سلام به AETHER خوش اومدی 🌌\nنظرت رو همین‌جا بنویس، مستقیم به مدیر می‌رسه.")
                    send_message(ADMIN_ID, f"👤 کاربر جدید\nنام: {name}\nآیدی: {chat_id}\nیوزرنیم: @{username}\n🕒 {now_fa()}")
                else:
                    # فوروارد به مدیر
                    send_message(ADMIN_ID, f"💬 پیام جدید از بله\n\n👤 نام: {name}\n🆔 آیدی: {chat_id}\n🔗 یوزرنیم: @{username}\n\n📝 متن:\n{text}\n\n🕒 {now_fa()}\n\nبرای جواب:\n/reply {chat_id} متن")
                    send_message(chat_id, "✅ پیامت رسید، ممنون که نظر دادی ✨")

        time.sleep(1)

if __name__ == "__main__":
    main()
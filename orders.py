from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ORDERS_CHAT_ID = "-1002993388534"
ASK_CHAT_ID = "-1003196454615"

COUNTER_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "registered_count.txt"
)
INITIAL_COUNT = 11
MAX_COUNT = 100000

userState = {}

USERS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.txt")
ADMIN_ID = 7861055850


def load_users():
    if not os.path.exists(USERS_FILE):
        open(USERS_FILE, "a", encoding="utf-8").close()
        return set()
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return {int(line) for line in f if line.strip().isdigit()}


userIds = load_users()


def add_user(user_id):
    if user_id in userIds:
        return
    userIds.add(user_id)
    with open(USERS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{user_id}\n")


def save_count(value):
    with open(COUNTER_FILE, "w", encoding="utf-8") as f:
        f.write(str(value))


def load_count():
    if not os.path.exists(COUNTER_FILE):
        save_count(INITIAL_COUNT)
        return INITIAL_COUNT

    try:
        with open(COUNTER_FILE, "r", encoding="utf-8") as f:
            value = int(f.read().strip())
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        save_count(INITIAL_COUNT)
        return INITIAL_COUNT


registered_count = load_count()


def reserve_seat():
    global registered_count
    registered_count += 1
    save_count(registered_count)
    return registered_count


def set_count(value):
    global registered_count
    registered_count = value
    save_count(registered_count)


TEXT_STEP1 = """
بسم الله الرحمن الرحيم 🌟

التدريب رح يكون مقسم ل 4 أشهر او لنهاية الفصل الأول مابعرف 📅.

لحتى تسافر لأي مدينة المسا 🌆، ما ضروري يكون كل الطريق منوّر، بكفي تنور مترين قدامك لحتى توصل لوجهتك.
هاد المبدأ بالضبط يلي رح نطبقه بتدريبنا بهالدفعة كونها مخصصة فقط لطلاب السنة الاولى يلي ما بيعرفو شي عن المجال 👨‍💻.

بعرف انه معظم الطلاب حالياً ماعندهن لابتوب 💻 لهيك مابدنا مباشر نبلش بالتطبيق العملي لأن معك بحر وقت اولاً ⏳، ف رح نشتغل بقسم نظري لمدة 3 أسابيع 📚.

هيك انت بتتعود على جو الجامعة والمواد 🏛 وبنفس الوقت عم تتعلم كيف الدنيا بتمشي بالمجال لوقت يتوفر معك اللابتوب ونقدر نمشي بالتأسيس البرمجي ⚙️.

جاهز احكيلك الخطة يلي رح نتبعها ؟ 🤔💬
"""

TEXT_STEP2 = """
المرحلة الأولى: اكتساب المعرفة النظرية. 📘

تخيل انه في طلاب بتوصل للسنة التالتة وهي مابتعرف شو بتفرق البرمجيات عن البرمجة، او ماعندها أقل معرفة كيف الشركات بتوظف وشو المهارات المطلوبة لسوق العمل وشو بتفرق البرمجة عن لغة البرمجة!! 🤯

اي رح نتعلم هالمفاهيم بشكل واقعي عن طريق اجتماعات مباشرة ومسجلة، نحكي فيه بالتفصيل وكلام أي حدا بالمجال بيتمنى يسمعه ببداية طريقه. 🎙

مهارات رح نكتسبها: ✅

- تعلم كيف تتعلم. 🧠
مهارة التعلم الذاتي من أهم المهارات للشخص الناجج بأي مجال بالدنيا، ولكن الخطوات مالها عشوائية ابداً. 📈
رح نشرح كلشي خطوة بخطوة كيف منتعلم أي مهارة تقنية بالدنيا. 🗺

- وهم المصادر والكورسات التعليمية. 📚
سامع بمصطلح جحيم الكورسات ؟ اي اهلاً وسهلاً فيك بالهندسة المعلوماتية يلي تعتبر مستنقع الكورسات والتشتت فيها بكترة المصادر وليس ندرتها. 🌀
لتتعلم سي بلس رح تلاقي مليون كورس ورح تلاقي مليون رأي وكل حدا ليقلك شي، طيب شو رأيك لو انت تعلمت كيف اصلاً تختار المصدر المناسب الك ؟ احا هالشي ممكن ؟ اكيد!! 💻
يلي مهووس بالجيم والنادي والعضلات من أول نظرة رح يعرف اذا النادي مناسب اله او لأ، اي انت رح تكتسب هالمهارة بالتطبيق العملي وبحضورنا لكورسات من اكتر من مصدر عربية واجنبية 💪

- مين المهندس الفاشل. 📉
حكينا كتير عن الطلاب الناجحين وتجاربهن، بس هل تعلم انه مليار طالب بيتخرج كل سنة وهو فايت بالحيط ؟ 🚶‍♂️
طيب هدول كيف فشلو ؟ شو كانت العادات الهن بالمجال ؟ كيف تتجنب اخطائهن ؟ ⚠️

والكثير من المواضيع المشابهة يلي رح تشبع فضولك تجاه المجال ورح تطلع منها بعقلية جديدة بإذن الله، رح كون حريص اني ما خبّي عنك ولا معلومة ولا اترك سؤال مو مجاوب عليه. 💡

جاهز تنتقل للمرحلة البعدا ونقرأ عن التوجيه الأكاديمي ؟😁
"""

TEXT_STEP3 = """
مرحلة التوجيه الأكاديمي هي مسار جديد عم ضيفه لشغوف وخاصة فقط بمواد السنة الأولى ورح يساعدنا فيها زميلتنا جميلة، الاولى على دفعتها ومتدربة بشركة إتمام وعندها خبرة بالمسابقة البرمجية ومليون شغلة. 👩‍🎓

انك تتفوق بموادك ماله مرتبط بالجهد ابداً، وكتير ناس رح تشوفهن عم يقنعوك تسجل دورات وكذا وانت رح تقتنع وتتطمن، لانك متخرج من منظومة البكالوريا الفاشلة يلي هدفها تحشي راسك بمعلومات تتقيئها على ورقة الفحص 🙂 🏫
طيب مرحبا انت هون صرت بمرحلة جديدة ورح نضمن انك تكتسب العقلية الصح لحتى تدرس مقررات الجامعة والدورات ويكون في جلسات مخصصة لكل مادة بالفصل الأول متل التحليل او البرمجة الخ... 📚

ونحاول يكون تدريبنا شامل للأساس البرمجي والأساس الأكاديمي بحيث نعلمك تصطاد ونزودك بالقارب والدليل والمعدات وكلشي، ومنعطيك السمكة جاهزة كمان 😆 🎣

بس ذكرت أساس برمجي ؟ شو هاد ؟؟ يعني مو بس نحضر ابو هدهود ؟؟؟ 🤨
تابع لحتى نحكي اكتر 👇
"""

TEXT_STEP4 = """
الأساس البرمجي هو الجزئية الأصعب والأمتع بنفس الوقت، البرمجة هي شي كتير غليظ وصعب ومالها للجميع. 💻

رح نبدأ من الصفر

اولاً بمسار لنتعلم مهارات وبرامج الـ ICDL وناخد شهادة حضور لنهاية المسار

بعدها رح نتعلم كلشي بيلزمنا عن 'الكنبيوتر' والبرمجيات، كيف البرمجة بتشتغل ؟ كيف عقلية المبرمج بتنبنى صح ؟ كيف البرمجة بتغير اسلوب حياتك ؟ 🧠

ومننطلق لأول لغة برمجة ومنبلش نكتب اول كود بإيدنا، هون ببلش التطبيق العملي 100٪ ورح نطبق كلشي تعلمناه سابقاً نظرياً ونحضر مقتطفات من اكتر من مصدر عربي وأجنبي. 🌍
مارح نتقيد بمسار شخص واحد فقط، منطبق بتاسكات وشغلات عملية وتحديات بنفس العناوين المطلوبة منك بمادة البرمجة 1. ⚙️

هون بتطلع مخك مستوي حرفياً. 😁

وشايف كل هالبروسيسس يلي حكيناها ؟
مارح تتعلمها لحالك، رح يكون في مينتور فوق راسك بكل مرحلة وفي اكتر من 100 شغوف عم يتعلم نفس العناوين.

طيب هلق كيف منبلش ؟ تعال نحكي عتفاصيل الدفع 💳
"""

TEXT_STEP5 = """
⚠️ والإشتراك للناس يلي بدها تستثمر وقتها مو للناس يلي داخلة تجرب حالها.

💴 والتكلفة 42$ بدون أي أقساط إضافية مستقبلاً

فينك بتحولها لما بيتم قبولك، بتمنى يكون هالمبلغ مو عبئ عليك وبوعدك انك رح تاخد قيمة مقابل هالشي ومارح تحس حالك استثمرت مصاري اهلك بمكان غلط.

وطبعاً بإمكانك تقسطهن بمدة بتحددها لأن هدفنا الأساسي هو الفائدة ان شاء الله

والتدريب كامل اونلاين، مش محتاج تنزل لمكان والاجتماعات مسائية مناسبة لأوقات الجميع وغير متضاربة مع دوام الجامعة

‼️ ملاحظة هاااامة:
بإمكانك استرجاع قيمة الاشتراك خلال 20 يوم من بدء الاشتراك، لأي سبب كان فينك تخبرنا ومنرجعلك كلشي، لهيك بتضل متطمن، ومابتكمل الا اذا متأكد كلشي مناسبك بإذن الله.

(وحتى بدي ياك هيك لبعدين، ماتدفع مصاري بمكان الا تكون متأكد من القيمة يلي رح تاخدها، تقديراً لتعبك وتعب أهلك معك)

✅ هلق اذا انت متأكد مليار بالمية انه رح تكمل ف اكبس على زر "احجز مقعدك" ورح يتواصل معك الفريق بأسرع وقت. شكراً لأنك رح تكون رفيق هالرحلة عزيزي الشغوف 💟

الشغوفين المسجلين بالدفعة: {registered_count}

احجز مقعدك رقم: {next_seat} او الغِ العملية
"""


def build_step5_text():
    return TEXT_STEP5.format(
        registered_count=registered_count,
        next_seat=registered_count + 1,
    )


TEXT_USERNAME_WARNING = """⚠️ ياريت نحط معرف تلغرام كرمال اقدر اتواصل معك، وطبعاً المعرف غير الإسم انتبه وفوت غيرها من الإعدادات وبعدها ارجع اعمل start للبوت"""

TEXT_CONFIRM_EXPIRED = "انتهت الجلسة أو تم تسجيل طلبك مسبقاً، ارسل /start للبدء من جديد"
TEXT_ORDER_CONFIRMED = """⚠️ تم تهكيرك بنجاح وأخذنا مليون ليرة من حسابك!

عم نمزح معك 😄 تم تسجيل طلبك، ورح يتواصل معك فريق شغوف بأقرب وقت ممكن. لوقتها، روح احضر حلقة من ضيعة ضايعة أو أي شي مُسلّي 📺"""
TEXT_ORDER_CANCELLED = """⚠️ تم تهكيرك بنجاح وأخذنا مليون ليرة من حسابك!

عم نمزح معك 😄 تم إلغاء طلبك بنجاح. المقعد رجع فاضي... شكله زعل شوي، بس رح يتخطّى الموضوع 🪑😔"""

KB_STEP1 = InlineKeyboardMarkup(
    [[InlineKeyboardButton("جاهز، احكيلي الخطة 🤔", callback_data="stage2")]]
)

KB_STEP2 = InlineKeyboardMarkup(
    [[InlineKeyboardButton("جاهز، التوجيه الأكاديمي 😁", callback_data="stage3")]]
)

KB_STEP3 = InlineKeyboardMarkup(
    [[InlineKeyboardButton("تابع، الأساس البرمجي 👇", callback_data="stage4")]]
)

KB_STEP4 = InlineKeyboardMarkup(
    [[InlineKeyboardButton("تفاصيل الدفع 💳", callback_data="stage5")]]
)

KB_CONFIRM_CANCEL = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("احجز مقعدك ✅", callback_data="confirm")],
        [InlineKeyboardButton("❌ إلغاء العملية", callback_data="cancel")],
    ]
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = f"@{user.username}" if user.username else f"ID: {user.id}"

    await context.bot.send_message(ASK_CHAT_ID, f"{user.full_name}\n{username}")
    add_user(user.id)

    if not user.username:
        await update.message.reply_text(TEXT_USERNAME_WARNING)
        return

    userState[user.id] = {"step": "step1"}

    await update.message.reply_text(TEXT_STEP1, reply_markup=KB_STEP1)


async def edit_registered(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usage = f"عدد المسجلين الحالي: {registered_count}\n" "الاستخدام: /editRegistered 75"

    if not context.args:
        await update.message.reply_text(usage)
        return

    if len(context.args) != 1:
        await update.message.reply_text(f"⚠️ قيمة غير صالحة\n\n{usage}")
        return

    try:
        value = int(context.args[0])
    except ValueError:
        await update.message.reply_text(f"⚠️ قيمة غير صالحة\n\n{usage}")
        return

    if value < 0 or value > MAX_COUNT:
        await update.message.reply_text(f"⚠️ قيمة غير صالحة\n\n{usage}")
        return

    set_count(value)

    await update.message.reply_text(
        f"تم تعديل عدد المسجلين إلى: {registered_count}\n"
        f"رقم المقعد التالي: {registered_count + 1}"
    )


async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query

    user = q.from_user
    cid = user.id
    data = q.data

    if data == "confirm" and userState.get(cid, {}).get("step") != "step5":
        await q.answer(TEXT_CONFIRM_EXPIRED, show_alert=True)
        return

    await q.answer()

    if data == "stage2":
        userState[cid] = {"step": "step2"}
        await q.edit_message_text(TEXT_STEP2, reply_markup=KB_STEP2)

    elif data == "stage3":
        userState[cid] = {"step": "step3"}
        await q.edit_message_text(TEXT_STEP3, reply_markup=KB_STEP3)

    elif data == "stage4":
        userState[cid] = {"step": "step4"}
        await q.edit_message_text(TEXT_STEP4, reply_markup=KB_STEP4)

    elif data == "stage5":
        userState[cid] = {"step": "step5"}
        await q.edit_message_text(build_step5_text(), reply_markup=KB_CONFIRM_CANCEL)

    elif data == "confirm":
        userState.pop(cid, None)
        seat = reserve_seat()

        username = f"@{user.username}" if user.username else f"ID: {user.id}"

        await context.bot.send_message(
            ORDERS_CHAT_ID,
            f"""اشتراك جديد:
            الاسم: {user.full_name}
            المعرف: {username}
            رقم المقعد: {seat}""",
        )

        await q.edit_message_text(TEXT_ORDER_CONFIRMED)

    elif data == "cancel":
        userState.pop(cid, None)
        await q.edit_message_text(TEXT_ORDER_CANCELLED)

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return

    text = update.message.text.partition(" ")[2].strip()
    if not text:
        await update.message.reply_text("الاستخدام: /broadcast نص الرسالة")
        return

    sent = 0
    failed = 0
    for uid in list(userIds):
        try:
            await context.bot.send_message(uid, text)
            sent += 1
        except Exception:
            failed += 1
        await asyncio.sleep(0.05)

    await update.message.reply_text(f"تم الإرسال: {sent}\nفشل: {failed}")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("editregistered", edit_registered))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CallbackQueryHandler(handle_query))

    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    if not WEBHOOK_URL:
        app.run_polling()
    else:
        PORT = int(os.getenv("PORT"))
        SECRET_TOKEN = os.getenv("SECRET_TOKEN")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            secret_token=SECRET_TOKEN,
            webhook_url=WEBHOOK_URL,
            drop_pending_updates=True,
            url_path="shagh-orders-bot",
        )


if __name__ == "__main__":
    main()

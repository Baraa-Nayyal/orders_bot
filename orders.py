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

userState = {}

TEXT_START = """
بسم الله الرحمن الرحيم

اشتراك شغوف الدفعة الثامنة 🔥

رح تنضم لبروسيسس سبقك فيها اكتر من 300 طالب مهتم بتطوير مهاراته، اشتراك شغوف مانه كورس ولا دورة ولا قسط، هو المكان يلي رح تبدأ فيه باكتساب مهارات حقيقية ان شاء الله، مارح تكون عم تتعلم لحالك إنما مع مجتمع كامل عم يشتغل يومياً،

تعلم برمجة وانت حاسس بأمان، مارح تضيع ولا تتشتت وعد 🤍

‼️ الدفعة هي مخصصة لطلاب جامعة حلب السنة الأولى يلي خلصو فحص ولسه حاسين انهن ضايعين ‼️

الخطة رح تكون مقسمة ل 5 اسابيع:
- الأسبوع الأول: ترميم الأساسيات بلغة سي بلس، طريقة تفكير الخوارزميات واساسيات الـ Data Structure يلي رح تمرق معكن بالسنة الثانية، وبدايتنا على موقع codeforces وناخد نظرة عن المسائل.

- الأسبوع الثاني والثالث: بدايات بعالم الويب والاختصاص منتعلم فيها Html&Css يلي يعتبرو هلق صارو بديهيات، ومن ثم مننتقل للغة Javascript بعد ما أخدنا أساس برمجي قوي بأول لغة برمجة تعلمناها.

- الأسبوع الرابع والخامس: مخصص لبناء مشاريع وتطبيق عملي لكلشي تعلمناه سابقاً:

🧱 بناء مشاريع html css بشكل سريع لأن هي المرحلة أخدها ال ai ولكن لازم نتأكد انه نحن منعرف نبني أي تصميم ويب.

📌 نتعلم جافاسكربت بكورس سريع وبعدها نطبق 5 مشاريع صغيرة وسريعة انا مصورها ومع كل مشروع في مهام إضافية واستفسارات لحتى نتأكد انه فهمنا

📍 نتعرف على git & github ونرفع مشاريعنا عليه ونستكشف عالم ال open source projects

🤝 الإشتراك مااانه كورس، الإشتراك هو بيئة عم تتعلم فيها مع ناس بنفس شغفك ورح يكون في اجتماعات دورية.

❓ كيف منبدأ ؟
لما بيتم قبولك رح توصلك دعوة للمجتمع ورح نعمل اجتماع 15د نحكي فيه شو الآلية يلي رح نتبعها والأهداف.


❓ ليش فقط لطلاب الأولى ؟
لأن رح نبدأ من الصفر بغض النظر شو متعلم سابقاً، ولأن من السنة الثانية لازم تبلش تاخد المجال بجدية وتشتغل على حالك كرمال ما تضيع فرصك ان شاء الله.

❓ لو أنا مشارك بالمسابقة البرمجية ؟
مكانك هو بالكونتيسات والمسابقة والمعسكرات، التدريب هون للفئة يلي ماشاركت بالمسابقة وحاسة حالها ضايعة اكتر
"""

# TEXT_START = """

# اهلاً وسهلاً بالشغوف المستقبلي 🔥

# يبدو انك عرفت بالبوت وتحمست من ستوري الانستاغرام او حدا من اصدقاءك، مقدّر حماسك ولكن حالياً متوقف التسجيل على الدفعة الثامنة لاكتمال العدد، فيك تخبرنا لو انت بحاجة استثناء ✍️

# في حال عندك سؤال او استفسار او استشارة لا تتردد 👇
# @shagh1

# """


TEXT_USERNAME_WARNING = """⚠️ ياريت نحط معرف تلغرام كرمال اقدر اتواصل معك، وطبعاً المعرف غير الإسم انتبه وفوت غيرها من الإعدادات وبعدها ارجع اعمل start للبوت"""


TEXT_STEP2 = """
⚠️ والإشتراك للناس يلي بدها تستثمر وقتها مو للناس يلي داخلة تجرب حالها.

💴 والتكلفة 3.5$ فينك بتحولها لما بيتم قبولك، بتمنى يكون هالمبلغ مو عبئ عليك وبوعدك انك رح تاخد قيمة مقابل هالشي ومارح تحس حالك استثمرت مصاري اهلك بمكان غلط.

‼️ ملاحظة هاااامة:
بإمكانك استرجاع قيمة الاشتراك خلال 7 يوم من بدء الاشتراك، لأي سبب كان فينك تخبرنا ومنرجعلك كلشي، لهيك بتضل متطمن، ومابتكمل الا اذا متأكد كلشي مناسبك بإذن الله.

(وحتى بدي ياك هيك لبعدين، ماتدفع مصاري بمكان الا تكون متأكد من القيمة يلي رح تاخدها، تقديراً لتعبك وتعب أهلك معك)

✅ هلق اذا انت متأكد مليار بالمية انه رح تكمل ف اكبس على تأكيد ورح يتواصل معك الفريق بأسرع وقت. شكراً لأنك رح تكون رفيق هالرحلة عزيزي الشغوف 💟

العدد بالدفعة رح يكون محدود 20 طالب فقط لضمان جودة المتابعة، خلص ماعاد بدنا عدد كبير.

ولو سجلت انت وزميلك ف الكن الأولوية بالقبول كرمال ما حدا منكن يزعل انه انقبل الأول وما انقبل التاني، وكتير الموضوع مشجع لما تتعلم مع حدا بتعرفه لذلك ياريت تخبرنا هون @ask_shagh_bot بمعرفك ومعرّف زميلك لحتى نقبلكن سوا ان شاء الله.

أما اذا عندك سؤال، فينك تبعت على العم شغوف والفريق رح يجاوبك فوراً 
@ask_shagh_bot

وكل التوفيق للشغوف القادم 🔥
"""

KB_CONTINUE = InlineKeyboardMarkup(
    [[InlineKeyboardButton("تحمست، متابعة 😁", callback_data="continue")]]
    # [[InlineKeyboardButton("كبسة مو شغالة", callback_data="stop")]]
)

KB_CONFIRM_CANCEL = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("تأكيد ✅", callback_data="confirm")],
        [InlineKeyboardButton("❌ إلغاء", callback_data="cancel")],
    ]
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = f"@{user.username}" if user.username else f"ID: {user.id}"

    await context.bot.send_message(ASK_CHAT_ID, f"{user.full_name}\n{username}")

    if not user.username:
        await update.message.reply_text(TEXT_USERNAME_WARNING)
        return

    userState[user.id] = {"step": "start"}

    await update.message.reply_text(TEXT_START, reply_markup=KB_CONTINUE)


async def handle_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    user = q.from_user
    cid = user.id
    data = q.data

    if data == "continue":
        userState[cid] = {"step": "confirm"}
        await q.edit_message_text(TEXT_STEP2, reply_markup=KB_CONFIRM_CANCEL)

    elif data == "confirm":
        username = f"@{user.username}" if user.username else f"ID: {user.id}"

        await context.bot.send_message(
            ORDERS_CHAT_ID,
            f"""اشتراك جديد:
            الاسم: {user.full_name}
            المعرف: {username}""",
        )

        await q.edit_message_text("تم تسجيل طلبك ✅")
        userState.pop(cid, None)

    elif data == "cancel":
        userState.pop(cid, None)
        await q.edit_message_text("تم الإلغاء ❌")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
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

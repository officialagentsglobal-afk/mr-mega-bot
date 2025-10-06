import telebot
from telebot import types
import os
import time
import logging

# إعدادات التسجيل
logging.basicConfig(level=logging.INFO)

# جلب التوكن من البيئة
TOKEN = os.environ.get('BOT_TOKEN', '8197924856:AAG7xobyrcIVeOQft169YNU1GkZNlYE1oV8')
bot = telebot.TeleBot(TOKEN)

# القنوات الإجبارية
REQUIRED_CHANNELS = [
    {"name": "القناة الرسمية", "link": "https://t.me/PariPulse_Egypt_Official", "@": "@PariPulse_Egypt_Official"},
    {"name": "قناة البوت", "link": "https://t.me/onexmega_official", "@": "@onexmega_Official"}
]

# تخزين لغة المستخدم
user_language = {}

# النصوص بلغتين
TEXTS = {
    'ar': {
        'welcome': "🏆 MR MEGA - البرنامج الرسمي للوكلاء 🏆\n\nشركاء النجاح في عالم المراهنات الاحترافية\nنقدم لك فرصة تميز حقيقية برعاية أكبر المنصات العالمية",
        'choose_lang': "🌍 اختر لغتك المفضلة",
        'main_menu': "🏠 القائمة الرئيسية",
        'become_agent': "🚀 انضم كوكيل معتمد",
        'about_us': "🏢 من نحن",
        'agent_info': "📊 معلومات البرنامج", 
        'contact_admin': "📞 تواصل مع الإدارة",
        'official_channels': "📢 قنواتنا الرسمية",
        'back_home': "🔙 العودة للرئيسية",
        
        # قسم الوكلاء
        'choose_platform': "🎯 اختر المنصة المناسبة لبدء رحلتك",
        'application_method': "📝 طريقة التقديم الرسمية",
        
        # نصوص أخرى
        'subscription_required': "🔒 الوصول مقيد\n\nللحفاظ على جودة خدماتنا، يرجى الاشتراك في قنواتنا الرسمية أولاً",
        'join_channel': "انضم لـ {}",
        'check_subscription': "✅ تحقق من الاشتراك",
        'not_subscribed': "❌ لم تشترك في جميع القنوات بعد",
        
        # من نحن
        'about_us_text': """
🏢 من نحن

نحن فريق MR MEGA الرسمي

• ✅ شركاء معتمدون رسمياً من إدارة 1xBet العالمية
• 📊 فريق متكامل من المحترفين في مجال التسويق والمراهنات
• 🌍 نعمل بأعلى معايير الجودة والاحترافية
• 🔒 مرخصون ونعمل ضمن الأطر القانونية

🎯 مهمتنا:
تقديم فرص عمل حقيقية للشباب الطموح من خلال برنامج وكلاء مميز، مع توفير دعم فني وإداري متكامل.

📈 رؤيتنا:
أن نكون الرقم الأول في مجال وكالات المراهنات بالشرق الأوسط.
        """,
        
        # قنوات رسمية
        'official_channels_text': """
📢 قنواتنا الرسمية

القناة الرئيسية:
@PariPulse_Egypt_Official

قناة البوت:
@onexmega_Official

✅ اشترك الآن لتكون على اطلاع دائم بآخر المستجدات والعروض الحصرية.
        """,
        
        'application_video': """
🎥 شرح مفصل - طريقة التقديم الرسمية

شاهد هذا الفيديو التوضيحي لتعرف بالضبط كيفية:
• تقديم الطلب لتصبح وكيل معتمد
• تعبئة البيانات بشكل صحيح  
• تفعيل البروموكود الخاص بك
• بدء جني الأرباح

📹 رابط الفيديو التوضيحي:
https://youtu.be/2ufm6KLVDIs?si=pRd4lcfkIHduqZkp

✅ الشرح ينطبق على كل من:
• PariPulse
• MelBet
        """,
        
        'contact_admin_text': """
📞 تواصل مع إدارة البرنامج

👨‍💼 المدير المسؤول:
@PariPulse_Manager_EG

🎯 للاستفسارات حول:
• تفعيل الحسابات والبروموكود
• متابعة حالة الطلبات
• استفسارات الدعم الفني
• مشاكل التسجيل والتقديم
• الحساب التجريبي المجاني

⏰ متاحون لمساعدتك على مدار الساعة
        """,
        
        'agent_info_text': """
📊 معلومات البرنامج - MR MEGA

🎯 نظام العمل:
• أنت كـ وكيل معتمد بتكسب عمولة على كل عملية رهان
• الشركة توفر لك بروموكود خاص وحساب أفلييت متكامل
• الأرباح يومية وتقدر تسحبها في أي وقت
• دعم فني وإداري متكامل 24/7

💰 نظام العمولات والسحب:
• العمولة تُحسب يومياً على كل رهان
• السحب أسبوعي (كل يوم ثلاثاء)
• أقل حد للسحب: 30 دولار
• طرق السحب: بالعملة المحلية للوكيل

📈 متوسط أرباح الوكلاء:
• مبتدئ: 500-1000 دولار/شهر
• محترف: 2000-5000 دولار/شهر  
• متميز: 10000+ دولار/شهر

🔒 نحن معك خطوة بخطوة حتى تحقيق النجاح
        """,
        
        'pari_text': """
🎯 PariPulse - الوكالة الرسمية

🔗 رابط التسجيل الرسمي:
https://pari-pulse.com/Fxiv-aff

📋 خطوات التسجيل:
1️⃣ افتح الرابط وسجّل بياناتك الشخصية
2️⃣ احفظ اسم المستخدم وكلمة المرور في مكان آمن
3️⃣ بعد التسجيل، اتصل فوراً بالإدارة:
   @PariPulse_Manager_EG

🎁 بعد التواصل مع الإدارة:
• تفعيل البروموكود الخاص بك
• تسليم الحساب التجريبي المجاني
• تدريب كامل على نظام العمل
• متابعة مستمرة لأدائك

⚠️ ملاحظة هامة:
المعلومات المدخلة يجب أن تكون صحيحة 100% لضمان استلام الأرباح
        """,
        
        'melbet_text': """
🎯 MelBet - الوكالة الرسمية

🔗 رابط التسجيل الرسمي:
https://melbetpartners.com/ae/sign-up?tag=d_4756296m_3993c_ml_1631412

📋 خطوات التسجيل:
1️⃣ افتح الرابط وسجّل بياناتك الشخصية
2️⃣ احفظ اسم المستخدم وكلمة المرور في مكان آمن
3️⃣ بعد التسجيل، اتصل فوراً بالإدارة:
   @PariPulse_Manager_EG

🎁 بعد التواصل مع الإدارة:
• تفعيل البروموكود الخاص بك
• تسليم الحساب التجريبي المجاني
• تدريب كامل على نظام العمل
• متابعة مستمرة لأدائك

⚠️ ملاحظة هامة:
المعلومات المدخلة يجب أن تكون صحيحة 100% لضمان استلام الأرباح
        """
    },
    'en': {
        'welcome': "🏆 MR MEGA - Official Agents Program 🏆\n\nSuccess partners in professional betting world\nWe offer you real distinction opportunity sponsored by top global platforms",
        'choose_lang': "🌍 Choose Your Preferred Language",
        'main_menu': "🏠 Main Menu",
        'become_agent': "🚀 Join as Certified Agent",
        'about_us': "🏢 About Us",
        'agent_info': "📊 Program Information",
        'contact_admin': "📞 Contact Administration", 
        'official_channels': "📢 Our Official Channels",
        'back_home': "🔙 Back to Home",
        
        # قسم الوكلاء
        'choose_platform': "🎯 Choose Your Platform to Start Journey",
        'application_method': "📝 Official Application Method",
        
        # نصوص أخرى
        'subscription_required': "🔒 Access Restricted\n\nTo maintain our service quality, please subscribe to our official channels first",
        'join_channel': "Join {}",
        'check_subscription': "✅ Check Subscription",
        'not_subscribed': "❌ Not subscribed to all channels yet",
        
        # من نحن
        'about_us_text': """
🏢 About Us

We are MR MEGA official team

• ✅ Officially certified partners of 1xBet global management
• 📊 Complete team of professionals in marketing and betting
• 🌍 Working with highest quality and professional standards
• 🔒 Licensed and working within legal frameworks

🎯 Our Mission:
Providing real job opportunities for ambitious youth through distinguished agent program, with complete technical and administrative support.

📈 Our Vision:
To be number one in betting agencies field in Middle East.
        """,
        
        # قنوات رسمية
        'official_channels_text': """
📢 Our Official Channels

Main Channel:
@PariPulse_Egypt_Official

Bot Channel:
@onexmega_Official

✅ Subscribe now to stay updated with latest news and exclusive offers.
        """,
        
        'contact_admin_text': """
📞 Contact Program Administration

👨‍💼 Responsible Manager:
@PariPulse_Manager_EG

🎯 For inquiries regarding:
• Account and promo code activation
• Application status follow-up
• Technical support inquiries
• Registration and application issues
• Free trial account

⏰ Available to assist you 24/7
        """
    }
}

# كيبورد اختيار اللغة
def language_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('العربية 🇪🇬')
    btn2 = types.KeyboardButton('English 🇺🇸') 
    markup.add(btn1, btn2)
    return markup

# الكيبورد الرئيسي
def main_keyboard(lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(TEXTS[lang]['become_agent'])
    btn2 = types.KeyboardButton(TEXTS[lang]['about_us'])
    btn3 = types.KeyboardButton(TEXTS[lang]['agent_info'])
    btn4 = types.KeyboardButton(TEXTS[lang]['contact_admin'])
    btn5 = types.KeyboardButton(TEXTS[lang]['official_channels'])
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4, btn5)
    return markup

# كيبورد الوكلاء
def agents_keyboard(lang):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('PariPulse 🎯')
    btn2 = types.KeyboardButton('MelBet 🎯')
    btn3 = types.KeyboardButton(TEXTS[lang]['application_method'])
    btn4 = types.KeyboardButton(TEXTS[lang]['back_home'])
    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup

# زر للتحقق من الاشتراك
def check_subscription_keyboard(lang):
    markup = types.InlineKeyboardMarkup()
    for channel in REQUIRED_CHANNELS:
        markup.add(types.InlineKeyboardButton(TEXTS[lang]['join_channel'].format(channel['name']), url=channel['link']))
    markup.add(types.InlineKeyboardButton(TEXTS[lang]['check_subscription'], callback_data="check_subscription"))
    return markup

# التحقق من اشتراك المستخدم
def check_user_subscription(user_id):
    try:
        for channel in REQUIRED_CHANNELS:
            chat_member = bot.get_chat_member(chat_id=channel['@'], user_id=user_id)
            if chat_member.status not in ['member', 'administrator', 'creator']:
                return False
        return True
    except:
        return False

# رسالة البداية مع اختيار اللغة
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    
    if not check_user_subscription(user_id):
        subscription_text = TEXTS['ar']['subscription_required']
        for channel in REQUIRED_CHANNELS:
            subscription_text += f"\n📢 {channel['name']}"
        subscription_text += "\n\nبعد الاشتراك، اضغط على زر التحقق ✅"
        
        bot.send_message(message.chat.id, subscription_text, reply_markup=check_subscription_keyboard('ar'))
        return
    
    bot.send_message(message.chat.id, TEXTS['ar']['choose_lang'], reply_markup=language_keyboard())

# اختيار اللغة
@bot.message_handler(func=lambda message: message.text in ['العربية 🇪🇬', 'English 🇺🇸'])
def handle_language_selection(message):
    user_id = message.from_user.id
    lang = 'ar' if message.text == 'العربية 🇪🇬' else 'en'
    user_language[user_id] = lang
    
    bot.send_message(message.chat.id, TEXTS[lang]['welcome'], reply_markup=main_keyboard(lang))

# التعامل مع زر التحقق
@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_subscription_callback(call):
    user_id = call.from_user.id
    
    if check_user_subscription(user_id):
        bot.send_message(call.message.chat.id, TEXTS['ar']['choose_lang'], reply_markup=language_keyboard())
        bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, TEXTS['ar']['not_subscribed'], show_alert=True)

# التحقق من الاشتراك واللغة قبل أي أمر
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.from_user.id
    
    # إذا لم يكن مشتركاً
    if not check_user_subscription(user_id):
        subscription_text = TEXTS['ar']['subscription_required']
        for channel in REQUIRED_CHANNELS:
            subscription_text += f"\n📢 {channel['name']}"
        subscription_text += "\n\nبعد الاشتراك، اضغط على زر التحقق ✅"
        
        bot.send_message(message.chat.id, subscription_text, reply_markup=check_subscription_keyboard('ar'))
        return
    
    # إذا لم يختر لغة بعد
    if user_id not in user_language:
        bot.send_message(message.chat.id, TEXTS['ar']['choose_lang'], reply_markup=language_keyboard())
        return
    
    lang = user_language[user_id]
    
    # معالجة الأزرار حسب اللغة
    if message.text == TEXTS[lang]['become_agent']:
        bot.send_message(message.chat.id, TEXTS[lang]['choose_platform'], reply_markup=agents_keyboard(lang))
    
    elif message.text == TEXTS[lang]['application_method']:
        bot.send_message(message.chat.id, TEXTS[lang]['application_video'], reply_markup=agents_keyboard(lang))
    
    elif message.text == TEXTS[lang]['contact_admin']:
        bot.send_message(message.chat.id, TEXTS[lang]['contact_admin_text'], reply_markup=main_keyboard(lang))
    
    elif message.text == TEXTS[lang]['agent_info']:
        bot.send_message(message.chat.id, TEXTS[lang]['agent_info_text'], reply_markup=main_keyboard(lang))
    
    elif message.text == TEXTS[lang]['about_us']:
        bot.send_message(message.chat.id, TEXTS[lang]['about_us_text'], reply_markup=main_keyboard(lang))
    
    elif message.text == TEXTS[lang]['official_channels']:
        bot.send_message(message.chat.id, TEXTS[lang]['official_channels_text'], reply_markup=main_keyboard(lang))
    
    elif message.text in ['PariPulse 🎯', 'MelBet 🎯']:
        if message.text == 'PariPulse 🎯':
            bot.send_message(message.chat.id, TEXTS[lang]['pari_text'], reply_markup=agents_keyboard(lang))
        else:
            bot.send_message(message.chat.id, TEXTS[lang]['melbet_text'], reply_markup=agents_keyboard(lang))
    
    elif message.text == TEXTS[lang]['back_home']:
        bot.send_message(message.chat.id, TEXTS[lang]['main_menu'], reply_markup=main_keyboard(lang))
    
    else:
        bot.send_message(message.chat.id, TEXTS[lang]['main_menu'], reply_markup=main_keyboard(lang))

if __name__ == "__main__":
    while True:
        try:
            logging.info("🟢 البوت شغال على الاستضافة!")
            bot.polling(none_stop=True, interval=1)
        except Exception as e:
            logging.error(f"🔴 خطأ: {e}")
            time.sleep(10)

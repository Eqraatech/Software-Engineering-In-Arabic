---
title: "Linux Commands Cheatsheet"
description: "A quick reference to essential Linux commands for file management, process control, networking, and system monitoring—perfect for daily use or interview prep."
excerpt: "لما نتعلم أوامر Linux، هنقدر اننا نـ Automate أغلب مهام الشغل اليومي بتاعتنا ونسهل حاجات كتير في شغلنا، وكمان هنقدر نتحكم في كل حاجة في النظام بتاعنا بسهولة."
tags: ["linux", "devops", "backend", "frontend"]
updatedAt: "2024-09-10"
featured: false
image: "https://assets.eqraatech.com/guides/linux-commands-cheatsheet.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/linux-commands-cheatsheet.png" alt="Linux Commands Cheatsheet" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

نظام التشغيل Linux بقى واحد من أكتر الأنظمة اللي بيستخدمها المطورين، خاصة في تطوير البرمجيات وإدارة الـ Servers والـ Cloud Infrastructure. وده لإن Linux نظام مفتوح المصدر ومرن، وبيدي للمطورين سيطرة كاملة على البيئة اللي بيشتغلوا فيها، فده بيخلي تعلمنا وفهمنا لأوامر الـ Linux حاجة أساسية لو عاوزين نبقى شغالين بكفاءة وفعالية أكتر.

الـ Linux بيعتمد بشكل كبير على الـ Command Line Interface أو زي ما بنقول عليها "Terminal"، واللي هي أداة قوية جدًا وبتسمح للمطورين يعملوا مهام كتيرة زي إدارة الملفات، مراقبة العمليات، تثبيت البرامج، وكمان التحكم في الأذونات.

لما نتعلم أوامر Linux، هنقدر اننا نـ Automate أغلب مهام الشغل اليومي بتاعتنا ونسهل حاجات كتير في شغلنا، وكمان هنقدر نتحكم في كل حاجة في النظام بتاعنا بسهولة.

فورقة وقلم وتعالوا نتكلم عن أكثر الـ Commands المستخدمة للمطورين 🚀

---

## Most Used Linux Commands For Developers

<!-- File Management -->
```bash
# عرض الملفات والمجلدات
ls -l /home/user

# تغيير المجلد الحالي
cd /var/logs

# عرض المسار الحالي
pwd

# إنشاء مجلد جديد
mkdir eqraatech

# حذف ملف
rm old_file.txt

# نسخ ملف
cp index.html /var/www/html/

# نقل أو إعادة تسمية
mv old_name.txt new_name.txt
```

<!-- File Operations -->
```bash
# عرض محتويات ملف
cat /var/logs/eqraatech.log

# البحث عن نص في ملف
grep "User not found" /var/logs/eqraatech.log

# البحث عن ملفات
find /home/user -name "*.log"

# تغيير أذونات الملف
chmod 755 eqraatech_background_runner.sh

# تغيير ملكية الملف
chown root:root /etc/passwd
```

<!-- Process Control -->
```bash
# عرض العمليات النشطة
ps aux

# إنهاء عملية
kill 995840

# مراقبة العمليات في الوقت الفعلي
top

# فتح ملف في محرر nano
nano config.json

# فتح ملف في محرر vim
vi index.html
```

<!-- System & Network -->
```bash
# تحميل ملف من الويب
wget https://eqraatech.com/In-a-nutshell-v1.zip

# إنشاء أرشيف مضغوط
tar -cvzf archive.tar.gz /path/to/dir

# تشغيل أمر بصلاحيات root
sudo apt-get update

# عرض معلومات النظام
uname -a

# عرض مساحة القرص
df -h
```

---

الأوامر دي بتغطي مجموعة واسعة من المهام اللي المطورين بيشتغلوا بيها بشكل دوري في بيئة Linux، بداية من إدارة الملفات وصولًا إلى التحكم في العمليات وإدارة النظام.
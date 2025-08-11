---
title: "How QR Codes Work"
description: "QR codes store data in a 2D grid of black and white squares, readable by scanners and cameras. This guide explains how they encode information, support error correction, and enable fast, contactless access to content."
excerpt: "ال QR Codes من الأشياء اللي بنشوفها بشكل شبه يومي في كل مكان فورقة وقلم و تعالوا نفهم هما إيه ونعرف إزاي ال Quick-Response Codes بتتحول ل URLs و إزاي كمبرمج تقدر تعمل تطبيق بسيط بيعمل generation ل QR Codes."
tags: ["data", "binary", "backend", "frontend", "web-development","computer-science"]
updatedAt: "2024-07-16"
featured: false
image: "https://assets.eqraatech.com/guides/how-qr-codes-work.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/how-qr-codes-work.png" alt="How QR Codes Work" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

ال QR Codes من الأشياء اللي بنشوفها بشكل شبه يومي في كل مكان 

فورقة وقلم و تعالوا نفهم هما إيه ونعرف إزاي ال Quick-Response Codes بتتحول ل URLs و إزاي كمبرمج تقدر تعمل تطبيق بسيط بيعمل generation ل QR Codes.

---

قبل ما نبتدي خلينا نعرف إن الهدف الأساسي وراء اختراع ال QR Codes هو تمثيل قدر كبير من المعلومات في مكان صغير.

ال QR Codes تم اختراعها في مصنع سيارات في اليابان من ٣٠ سنة عشان يكتبوا أكبر قدر من المعلومات عن القطعة المصنعة عليها.

## **فكرة العمل؟**

الفكرة كانت تطوير لفكرة الـ barcode اللي بقدر أمثل بيها أرقام المنتجات باستخدام شرائط طولية ولكن الخطوط الطولية بتديني combinations محدودة وبالتالي أقدر أعبر عن معلومات قليلة ولكن لو بدلنا الخطوط بمربعات صغيرة هيبقي عندي combinations أكثر وبالتالي أقدر أمثل بيها معلومات أكثر 

خلينا نفكر في اللونين الأبيض والأسود للـ QR Code على أنهم صفر و واحد, نظام ثنائي عادي من اللي كلنا عارفينه, وكل 8 مربعات مع بعض هنعتبرهم وحدة واحدة (مش بيفكرك دا بال bytes?!) و بس كدا زي ما 011 بتمثل رقم 3 بال binary system فمربعين أسود وواحد أبيض هتمثل رقم 3 في رسمة ال qr code 

ونفس فكرة تحويل ال binary ل hexadecimal and ASCII هنقدر نكتب معلومات تحتوي على حروف وأرقام.

ولأن ممكن تحويل الأبيض والأسود (أو أي لونين متباينين) بسهولة لصفر و واحد تفهمه الأجهزة بسهولة بتعتبر ال QR Codes حل ذكي وسريع لتمثيل عنواين المواقع و دا يعتبر استخدامها الأشهر حاليًا, ولكن يمكن استخدامها في تمثيل أي بيانات.

---

## **مما يتكون ال QR Code** 

 ال qr code بيستخدم المربعات الأبيض والأسود في أجزاء رئيسية:

- **Position markers**: ودول ٣ مربعات كبيرة علي ٣ من زوايا المربع بتستخدمهم الكاميرات وأجهزة المسح عشان تحدد مساحة الكود وتقدر تقرأه بدقة 
- **Alignment pattern**: ودا عبارة عن مربع آخر صغير يستخدم للاستدلال علي إتجاه قراءة الكود ليساعد الكاميرات علي سرعة تحليل الكود بمعرفة إتجاهه الصحيح 
- **White Margin**: ودي مساحة بيضاء حوالين ال كود كله عشان تفصله وتعمل تباين بينه وبين الخلفية وكذلك في مساحة بيضاء حوالين ال position markers عشان تبرز وجودهم 
- **Data**: وكتابة البيانات علي الكود بتبدأ من الركن الأيمن السفلي وكل 8 مربعات صغيرة بنعتبرهم وحدة واحدة
---
title: "Payment Fees Explained"
description: "Every online transaction involves fees paid to different parties—payment gateways, processors, card networks, and banks. This guide breaks down how payment fees work, the types of charges involved, and why businesses pay them."
excerpt: "عند إجراء عملية دفع إلكتروني أو عبر نقاط البيع، المبلغ يمر بعدة أطراف، وكل طرف يخصم جزءًا من الرسوم مقابل خدمته ودوره في إتمام العملية. هذه الرسوم موزعة بين بنك العميل، شبكة البطاقات، بنك التاجر، وأحيانًا بوابة الدفع. والنتيجة أن التاجر لا يحصل على كامل المبلغ، بل أقل بقليل بعد خصم هذه الرسوم."
tags: ["fintech", "payment", "backend"]
updatedAt: "2025-08-21"
featured: false
image: "https://assets.eqraatech.com/guides/payment-fees-explained.png"
author: "mhdbassiouny"
---

<img src="https://assets.eqraatech.com/guides/payment-fees-explained.png" alt="Payment Fees Explained" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

في حاله دفع ١٠٠ ريال في موقع الكتروني او نقاط البيع (POS)، كم يصل للتجار فعليا؟

  عملية الدفع عملية معقدة بتمر بأكثر من جهة لكي تكتمل. كل جهة بيكون لها رسوم بيتم استقطاعها من مبلغ العملية قبل وصوله للتاجر.

 الرسوم التي يتم خصمها تكون موزعة كالآتي:

---

## 1- الـ Interchange Fees - عمولة البنك مُصدِر البطاقة (Issuer)

البنك مُصدِر البطاقة يخصم العمولة الاكبر. وبيتم فرضها على التاجر مقابل إتاحة البطاقة وخدمة العميل. 

نسبة العمولة تختلف حسب:

- طبيعة نشاط التاجر (MCC: Merchant Category Code) (لو في مجال التعليم مثلا العمولة بتكون أقل من مجال آخر مثل السفر) 
- نوع البطاقة: بطاقة Debit رسومها اقل من ال Credit، وايضا ال card tier الأعلى مثلا (Signature / Infinite) رسومها أعلي لأنها تمول امتيازات البطاقة.
- هل الدفع تم من خلال نقاط البيع POS؟ هنا بتكون العملية نوعها (Card Present) ومخاطرها ورسومها اقل، بعكس الدفع اونلاين بيكون (Card Not Present) بمستوي مخاطر ورسوم أعلي.
- هل التاجر في نفس الدولة Local ام دولة اخري International. العمليات ال International او تسمي (Cross-Border) رسومها أعلى.

==متوسط النسبة بيكون مثلا: 1.5٪ – 2٪==

---

## 2- الـ Assessment or Network Fees: عموله شبكة البطاقة (Visa/Mastercard/Mada)

  

- الشبكة تخصم Network Fee وهي نسبة صغيرة مقابل تمرير المعاملة عبر الشبكة وادارة عمليات الدفع.
- في حالة ان العملية عبر دولة مختلفة (Cross-Border) بتزيد العمولة أو لو عملة مختلفة فبتطلب تحويل للعملات (Currency Conversion) بتزيد العمولة.

==متوسط النسبة بيكون مثلا: 0.1٪ – 0.3٪==

---

## 3- الـ Acquirer Markup: عمولة بنك التاجر (Acquirer Bank) 

- بيتم خصم رسوم مقابل إدارة حساب التاجر وتحمله جزء من مخاطر عمليات الدفع.
- بنك التاجر (Acquirer) يضيف نسبة أو مبلغ ثابت فوق الرسوم الأساسية (Interchange + Network Fees)، ويقدّمها للتاجر في صورة عمولة واحدة.
- ايضا النسبة تعتمد علي طبيعة نشاط التاجر (MCC: Merchant Category Code)، وكمان عدد عمليات التاجر.
- قد تزيد النسبة بناء علي معدل عمليات الاعتراض علي الدفع (Chargeback) الخاص بالتاجر.

==متوسط النسبة بيكون مثلا: 0.5٪ – 1.5٪==

---

## 4- الـ Gateway Fees: عمولة بوابة الدفع

- عمولة بيتم خصمها مقابل توفير الواجهة البرمجية للربط. بالإضافة لتأمين بيانات الدفع (PCI DSS Compliance).
- ابضا تعتمد علي المميزات المقدمة من بوابه الدفع: فعلي سبيل المثال بعض بوابات الدفع تفرض رسوم اضافية علي ال Auth/Cap (امكانية حجز المبلغ لمدة وخصمه بعد فترة من الدفع) عن ال Purchase (الدفع المباشر).

---

## في الختام

في حالة دفع ١٠٠ ريال، يصل منها للتاجر في المتوسط من ٩٦ ل ٩٩ ريال. الخصومات بتكون موزعة بين الجهات المشاركة في عملية الدفع. طبعا كل جهة بيكون ليها نسبة للربحية، لكن ايضا gتغطية مخاطر العملية (Fraud Risk). كل ما زادت مخاطرة العملية زادت نسبة الخصم الي بتتم منها.
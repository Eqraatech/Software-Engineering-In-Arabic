---
title: "Package Managers"
description: "Package managers automate installing, updating, and managing software dependencies. This guide explains how tools like npm, pip, and apt streamline development and ensure consistent environments."
excerpt: "الـ Package manager هو مساعد المبرمج المخلص في كل مشاريعه، فلو شغال Frontend هتلاقيك بتستخدم npm ولو شغال Backend فلكل لغة package manager بردو زي composer في PHP ولو شغال مع الذكاء الاصطناعي"
tags: ["devops", "web-development", "frontend", "backend"]
updatedAt: "2024-01-04"
featured: false
image: "https://assets.eqraatech.com/guides/package-managers.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/package-managers.png" alt="Package Managers" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ Package manager هو مساعد المبرمج المخلص في كل مشاريعه، فلو شغال Frontend هتلاقيك بتستخدم `npm` ولو شغال Backend فلكل لغة package manager بردو زي `composer` في `PHP` ولو شغال مع الذكاء الاصطناعي أو هندسة البيانات أو لغة `python` عامة فهتلاقيك بتستخدم `pip` 

## فخلونا نسأل سؤال وجودي ونقول ايه هي ال package ؟

ال package - الحزمة البرمجية - مصطلح عام بيشير لقطعة من الكود أو برنامج ممكن يكون كبير بحجم framework أو library زي `Angular` or `React` بستفيد منها في مهام متعددة وممكن يكون بيعمل مهمة واحدة بسيطة أنا محتاجها زي ال `Date format` مثلاً. 

💡الشاهد إنه برنامج جاهز بستفيد بيه بدل ما نعيد اختراع العجلة واستخدامها بيسرع عملية تطوير التطبيقات المختلفة.

## طيب ليه استخدم package manager ؟

> ما ممكن أنزلهم بنفسي وخلاص زي البرامج العادية

في الواقع لو عملت كدا **هتقابلك مشاكل كتير زي:**

-  Installation : تنزيل الـ packages مش زي بعضها, وكتير منها بيحتاج configuration معينة عشان تشتغل على الـ OS System بتاعك, فال package manager  بيقولك متشغلش بالك بحوارات ال `OS` دي وقولي أنت عاوز تنزل برامج إيه وانا هنزلها من Repository معين من الانترنت وهعملها Configuration على نظام التشغيل بتاعك 
- Dependency Resolution: عدد ال packages اللي بتحتاجها غالبًا بيكون كبير وإدارة كل واحدة على حدة مهمة رخمة ومكلفة في الوقت, فتخيل محتاج تنزل أو تعمل `update` ل 50 برنامج مثلاً عشان تطبيقك يشتغل!!
- Configuration Management and Uninstallation وضع الـ packages دي في المكان المناسب في نظام التشغيل وكذلك مسحها أو تحديثها
---

فال package manager **بيحل كل المشاكل دي بسهولة وبيسرع شغلك** **بل** **وبيقدم لك مميزات تانية زي:**

- User Permissions: فيسمح لمستخدمين محددين بتنزيل وتعديل ال packages
- Digital Signatures: يتأكد من كون ال package دي من مصدر مأمون ومفيهاش أي malicious code 
- Package Version Management: يحرص على استخدام النسخ المناسبة من ال dependencies لتشغيل البرنامج 

---

فكرة ال Package manager أثبتت إنتاجيتها ومع الوقت المبرمجين أضافوا ميزات تكميلية ليها عشان تحسن تجربة تطوير البرامج. فلو خدنا `npm` الشهيرة هنلاقي انهم كمان عملوا `Package Registry` اسمه `npmjs` وهو مكان واحد موثوق عشان كل ال Developers يقدروا يلاقوا وينشروا ال packages المختلفة. 

ال Package Registry هي المخزن أو ال Repository اللي بنزل منها ال Package لكن مزودة بواجهة احسن ومميزات إضافية. 

من التفاصيل اللي مفيد نكون ملمين بها في طريقة عمل الـ Package manager إنه ي**قدر ينزل ال package على مستوى:** 

- Locally فتكون متاحة في ال repository اللي شغال فيه فقط 
- Globally وتقدر تستخدمها في أي مكان في نظام التشغيل بتاعك

💡طبعًا يفضل تنزل ال package علي مستوي ال repository أو المجلد اللي فيه تطبيقك بس, ليه؟ لأن ممكن اطور أكثر من تطبيق على الجهاز ومن نفس ال package احتاج نسخ مختلفة.
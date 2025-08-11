---
title: "OAuth2"
description: ""
excerpt: "ال Open authorization هو Standard أو authorization framework أو طريقة متفق عليها بنستخدمها في ال Delegated third party access وليه اصدارين الاول والثاني, الفرق بينهم كبير و هنا هنتكلم عن طريقة عمل Oauth 2 بما أنه الأسهل والأكثر انتشارًا حاليًا."
tags: ["security", "OAuth2", "web-development", "authroization", "SSO"]
updatedAt: "2024-01-30"
featured: false
image: "https://assets.eqraatech.com/guides/oauth2.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/oauth2.png" alt="OAuth2" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

 بما أن الإنسان كائن ملول ومش كل شوية هنعمل حسابات جديدة بكلمات مرور جديدة علي كل موقع بندخله بنلاقي أمامنا خيار أنك تدخل ب Gmail account or Facebook or … بتختاره ومبروك وفرت ربع ساعة Sign up وإدخال معلومات لموقع جديد 🥳, لكن عمرك فكرت كمبرمج الموقع دا ازاي قدر يعملك اكونت من غير ما يعرف كلمة مرور الـ Gmail بتاعك؟

فورقة وقلم وتعالوا نعرف ما هو ال `OAuth` (open authorization) Protocol  السر وراء سحر ال Third Party authorization  

## ايه الـمشكلة اللي بيقوم الـ OAuth بحلها؟

بافتراض انك بتشترك في خدمة أو تطبيق جديد ولنقل Notion وبدل ما تعمل أكونت من الصفر بتستخدم أكونت ال Gmail بتاعك للدخول وهنا Notion كموقع مش محتاج من أكونت ال Gmail بتاعك غير بعض المعلومات زي البريد الإلكتروني وتأكيد هويتك وصورتك الشخصية عشان يحطها كصورة شخصية  للاكونت بتاعك بس هيعمل دا ازاي؟

> 💡في السنين الأولى للانترنت والمواقع عشان Notion يعمل كدا كان هيطلب منك كلمة المرور الخاصة بالـ Gmail بتاعك عشان يعمل بيها Login علي ال Gmail services ويقدر يسحب البيانات دي من الاكونت وياخدها الموقع , طبعًا واضحة المشكلة!!

هو كدا عنده Access على "كل" بياناتك حرفيًا وممكن يتصرف فيها كأنه أنت!! بعد تنوع وانتشار التطبيقات اكتشفنا ان الطريقة دي مفيهاش Security بجنيه فتم الغاء التعامل بيها وظهر بدالها ال Open authorization

---

ال Open authorization هو Standard أو authorization framework أو طريقة متفق عليها بنستخدمها في ال Delegated third party access وليه اصدارين الاول والثاني, الفرق بينهم كبير و هنا هنتكلم عن طريقة عمل `OAuth2` بما أنه الأسهل والأكثر انتشارًا حاليًا.

---

**فتعالوا نشوف Notion ازاي هياخد البيانات اللي هنسمحله بيها فقط من ال Gmail  باستخدام ال Oauth** 

- هنطلب Sign up with Gmail من علي موقع Notion 
- الموقع هيعمل Redirect وياخذك كمستخدم لموقع Gmail 
- هتظهر قائمة بالبيانات اللي بيطلب Notion أخذها من الـ Gmail (البريد, الاسم, الصورة…) هنا كمستخدم بتراجع الطلبات دي وتقيم هل أمان أدي ل Notion تصريح باستخدامها أو لاء.

>💡مراجعة البيانات دي مهمة لأنه لو موقع أنت لا تثق فيه وطلب معلومات زي معلومات بطاقة الدفع المرتبطة بالحساب مفروض ترفض وتتراجع عن استخدام الخطوة دي.

- بموافقتك هترجع لموقع Notion المرة دي معاك authorization  code ودا تصريح مؤقت بموافقتك على استخدام البيانات 
- نوشن هنا هنشير ليه ب Third party app هيبعت Request لل authorization server الخاص بموقع Gmail فيه ال code الخاص بموافقتك والكود الخاص بيه ك Third party app عشان الـ Auth server يديله ال Access token ودي اللي يستخدمها بشكل مستمر للوصول للبيانات المحددة من Gmail servers.

 مثال فتح حساب علي تطبيق مختلف بال OAuth مش الحالة الوحيدة ولكنها الأشهر, نقدر نعمم وصفنا لاستخدامه بأنه يساعدنا ن Integrate أي طرف ثالث باستخدام طريقة منظمة وآمنة ونديله صلاحيات للوصول لموارد متفق عليها بغض النظر هي بريد إلكتروني, ملفات او صور.
---
title: "API Testing with Hoppscotch"
description: "Hoppscotch is a fast, open-source tool for testing and debugging APIs. This guide shows how to use Hoppscotch to send requests, inspect responses, and streamline your API development workflow."
excerpt: "بديل مفتوح المصدر ومجاني تمامًا بدا كمشروع بسيط اسمه Postwoman وسهل تشتغل عليه سواء من المتصفح أو حتى تنزله Self-host على جهازك أو سيرفرك الخاص، عشان تحافظ على بياناتك وتشتغل براحتك."
tags: ["APIs", "hoppscotch", "api-testing", "backend", "frontend", "postwoman", "REST", "GraphQL"]
updatedAt: "2025-04-09"
featured: false
image: "https://assets.eqraatech.com/guides/api-testing-with-hoppscotch.png"
author: "ikhaledabdelfattah"
---

<img src="https://assets.eqraatech.com/guides/api-testing-with-hoppscotch.png" alt="API Testing with Hoppscotch" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />


**لو زهقت من Postman ؟ جرّب Hoppscotch!**

لو اشتغلت قبل كده على `APIs`، أكيد سمعت عن `Postman`. هو من أشهر الأدوات اللي بنستخدمها عشان نجرّب ونتأكد من الـ `APIs` اللي بنبنيها شغالة صح. بس `Postman` بقى تقيل، وبيدفعك فلوس على حاجات ممكن تكون محتاجها ببلاش. وهنا بييجي `Hoppscotch`.

يعتبر `Hoppscotch` بديل مفتوح المصدر ومجاني تمامًا بدا كمشروع بسيط اسمه `Postwoman` وسهل تشتغل عليه سواء من المتصفح أو حتى تنزله `Self-host` على جهازك أو سيرفرك الخاص، عشان تحافظ على بياناتك وتشتغل براحتك.

---

## **مميزات Hoppscotch**

1. **سهل وسريع وخفيف على الجهاز**

الواجهة بتاعته بسيطة ومش بتلغبط، بتحط الـ `URL`، تختار الميثود `(GET, POST, DELETE...)`، وتبعت الريكوست، وتبدأ تتابع الرد بسهولة.

2. **بيشتغل Offline**

على عكس `Postman` اللي لازم تكون متصل بالنت حتى لو بتختبر `API` انت لسه بتطوره علي جهازك local . `Hoppscotch` ممكن تشتغل عليه أوفلاين كأنه `PWA` (Progressive Web App)، يعني تفتحه من المتصفح وتشتغل بدون نت.

3. **تقدر تشغله Self-Hosted**

ودي من أهم النقط، تقدر تنزّل `Hoppscotch` عندك على سيرفر أو جهازك، وتتحكم فيه ١٠٠٪. ده مفيد جدًا للشركات أو المشاريع اللي عندها بيانات حساسة ومش حابة تشتغل على أدوات سحابية.

4. **يدعم بروتوكولات مختلفة**

مش بس `REST`، `Hoppscotch` بيدعم كمان `GraphQL` و `WebSocket` و `MQTT` و `Socket.IO`... لو بتشتغل على تطبيق فيه real-time communication، هتحتاج الحاجات دي.

5. **يتيح لك كتابة Tests و Scripts**

لو محتاج تتأكد إن الـ `API` بترجع نفس الداتا اللي متوقعها، أو تكتب أكواد `JavaScript` بسيطة قبل الريكوست – `Hoppscotch` بيسهّل ده وبيوفر لك code snippets تساعدك تكتب بسرعة.

6. **يقدم خاصية ال History**

كل request بتبعته بيتسجّل في التاريخ، فتقدر ترجع له في أي وقت، وتشوف الرد اللي جالك، من غير ما تبعت من جديد.

7. **Environments و Collections**

زي `Postman` بالظبط، تقدر تحط متغيرات عامة (زي الـ `token` أو الـ `baseURL`)، وتستخدمها في أكتر من ريكوست، وكمان تنظم الريكوستات في Collections عشان تشتغل بطريقة مرتبة.

8. **يسهل التعاون بين الفريق ببلاش**

في `Postman` لو عايز تضيف أكتر من ٣ أشخاص لازم تدفع. في `Hoppscotch`، الكل يشتغل مع بعض ببلاش! وتقدر تعمل workspaces خاصة وتحدد مين يعمل إيه جوه الفريق.

9. **Hoppscotch CLI**

لو بتحب تشتغل من الTerminal ، فيه CLI خاص بـ Hoppscotch تقدر تستخدمه عشان تجرّب الريكوستات، أو تعمل export/ import للـ collections بسهولة.

10. **مفتوح المصدر وبيكبر بسرعة**

الميزة الكبيرة كمان إنه Open Source، يعني المجتمع كله بيطوّره، وبيتحسن بسرعة. لو عندك فكرة أو مشكلة، ممكن تفتح issue على GitHub، أو تتابع الناس على Discord.

---

## في الختام

لو انت مطور بتشتغل على `APIs` كتير، وعايز أداة خفيفة وسريعة وتتحكم فيها براحتك، `Hoppscotch` اختيار ممتاز. هو مش بس بديل مجاني لـ Postman، لكنه كمان بيديّك حرية أكتر، وبيشتغل في أي بيئة، سواء عندك أو على الكلاود.
لو عايز تبدأ، ممكن تدخل على [hoppscotch.io](https://hoppscotch.io/?ref=eqraatech.com) وتبدأ فورًا، أو تنزله على جهازك وتستمتع بالـ `Self-Hosting`.
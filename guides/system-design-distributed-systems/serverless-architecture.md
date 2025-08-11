---
title: "Serverless Architecture"
description: "Serverless lets developers run code without managing servers. This guide explains how functions-as-a-service (like AWS Lambda) work, when to use them, and how they simplify scaling and reduce operational overhead."
excerpt: "ظهر الـ Serverless Architecture كطريقة أو نمط للتصميم يسمح للـ Developers بتحقيق الأمنية دي , وإن هم يبقوا قادرين على بناء الـ Software بدون الاهتمام بالبنية التحتية واداراتها."
tags: ["aws", "lambda", "serverless", "faas", "microservices", "distributed-systems", "system-design", "backend"]
updatedAt: "2024-04-28"
featured: false
image: "https://assets.eqraatech.com/guides/serverless-architecture.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/serverless-architecture.png" alt="Serverless Architecture" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

من زمان والناس نفسها انه تتيح للـ Developers الفرصة أنهم يركزوا على جزء الـ Development وانهم يكونوا قادرين على بناء Services قوية ويبدعوا فيها بدون عوائق الـ Infrastructure أو التفكير فيها ..

بحيث يركزوا على الـ Core Product أو المنتج اللي مهتمين بيه بمعنى أصح ، من غير ما يهتموا بازاي هيديروا البنية التحتية للـ Product ده

> وعشان كده ظهر الـ Serverless Architecture كطريقة أو نمط للتصميم يسمح للـ Developers بتحقيق الأمنية دي , وإن هم يبقوا قادرين على بناء الـ Software بدون الاهتمام بالبنية التحتية واداراتها

## ازاي Serverless Architecture بتشتغل ؟

كلنا عارفين أن الـ Servers عشان تسمح للـ Users بإنهم يتواصلوا مع أي تطبيق والـ Business Logic بتاعه , ده هيتطلب Resources وبنية تحتية هتطلب موارد واهتمام وادارة زي :

- Server Hardware
- Security Updates
- Backups
- Resources Management

ومن خلال اتباع الـ Serverless Architecture احنا بنشيل العبء ده كله وبنخلي الـ Developers يهتموا بس بجزء الـ Business Logic / Core Product وانهم يكتبوا الـ Application Code وبنشيل عبء البنية التحتية ونخليها مسئولية Third Party Provider زي الـ Cloud Services اللي موجودة دلوقتي ومن أشهرهم AWS , Google Cloud , Microsoft Azure

---

أحد أشهر الـ Serverless Architecture هي الـ FaaS واللي هي اختصار لـ Function as a Service , واللي من خلالها الـ Developers بيكتبوا الـ Application بتاعهم والـ Core Product اكنه بالظبط عبارة عن مجموعة محددة من الـ Functions اللي بتتنفذ واللي بيحصلها Triggering من خلال الـ Events زي مثلا ان حد يبعت رسالة لحد , أو ان يتبعت Email أو ان يحصل HTTP Request بشكل معين.

**وبالشكل ده انت كـ Developer مسئول عن :**

1. كتابة الـ Function أو الـ Application Code على هيئة الـ Functions دي وتعملها Upload / Deploy على الـ Cloud Provider
2. تحدد الـ Trigger أو ايه هو الحدث اللي هيتسبب في إن الـ Function بتاعتك يحصلها Invocation ويتم تنفيذها ؟ يعني امتة بالظبط الـ Cloud Provider ينادي عليها وينفذها ؟

وبعد ما تعمل ده أول مالـ Cloud Provider بيعرف أن حصل Trigger بيبدأ هو يعمل Execution للـ Function بتاعتك على أحد الـ Servers واللي ده بيكون من اختصاصه هو, ولو ماكنش فيه Servers وقتها قايمة فدوره انه يعمل Spawning لواحد ويبدأ ينفذ عليه الـ Function بتاعتك.

وبالشكل ده الـ Developer بيكون معزول تماما عن ايه بيحصل من ناحية البنية التحتية , ولكن بيكون تركيزه منصب في الـ Function Logic فقط

## أمثلة على الـ FaaS

الـ FaaS ظهرت بشكل كبير أول ما AWS قدمت لينا AWS Lambda واللي بيتم استعمالها دلوقتي بشكل كبير جدًا من عدد كبير من الـ Developers في أنحاء العالم بالإضافة لإن عندنا كذلك :

- Google Cloud Functions - GCF
- Microsoft Azure Functions
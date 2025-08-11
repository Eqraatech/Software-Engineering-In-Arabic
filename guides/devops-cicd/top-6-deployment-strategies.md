---
title: "Top 6 Deployment Strategies"
description: "From Blue-Green to Canary and Rolling, this guide explores six essential deployment strategies, highlighting how they work, when to use them, and how they reduce risk during software releases."
excerpt: "لما نيجي نتكلم عن الـ Deployment Strategies اللي بتستخدمها الشركات الكبيرة، الهدف الأساسي بيبقى إننا ننقل التحديثات الجديدة للـ Production Environment بأقل تأثير سلبي ممكن على المستخدمين."
tags: ["deployment", "kubernetes", "microservices", "devops", "docker", "canary", "blue-green", "A/B"]
updatedAt: "2024-11-08"
featured: true
image: "https://assets.eqraatech.com/guides/top-6-deployment-strategies.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/top-6-deployment-strategies.png" alt="Top 6 Deployment Strategies" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

لما نيجي نتكلم عن الـ **Deployment Strategies** اللي بتستخدمها الشركات الكبيرة، الهدف الأساسي بيبقى إننا ننقل التحديثات الجديدة للـ **Production Environment** بأقل تأثير سلبي ممكن على المستخدمين.

فورقة وقلم وخلونا نستعرض الأنواع المختلفة من الاستراتيجيات دي مع مميزات وعيوب كل واحدة فيهم 🚀

---

## Blue-Green Deployment

في الاستراتيجية دي بيبقى عندنا بيئتين شغالين في نفس الوقت: بيئة قديمة بتبقى هي دي الـ (`Blue`) وبيئة جديدة بتكون هي دي الـ (`Green`).

أول ما التحديث الجديد يبقى جاهز، بنحول الـ `Traffic` من بيئة الـ Blue للـ Green مرة واحدة. فيبدأ الناس بدل ما كانت بتروح للـ `Blue Deployment` تروح للـ `Green` وهنا بنتكلم طبعًا عن `Real Traffic` اتعمله `Routing` باستعمال `Load Balancer` للـ `Green Deployments`.

---

## Canary Deployment

الاستراتيجية دي بتعتمد على إننا ننقل التحديث بشكل تدريجي يعني `Gradually` لعدد محدود من المستخدمين الأول، ولو الأمور مشيت كويس، نكمل تعميم التحديث لباقي المستخدمين.

وليكن هنعمل Apply على التحديث الجديد لـ 20% من الـ Machines اللي عندنا و 80% هيفضلوا لسه محافظين على النسخة القديمة وبالتالي الناس لما يطلبوا الخدمة 20% منهم هيروح للجديد و 80% هيفضلوا لسه بيجيلهم النسخة القديمة والنسبة دي طبعا احنا بنتحكم فيها على حسب احتياجاتنا.

---

## Rolling Deployment

في الـ Rolling Deployment، التحديث بيتنقل بشكل تدريجي لمجموعة من السيرفرات بدلاً من نقل التحديث بالكامل مرة واحدة.

فلو عندنا مثلا 10 Servers هيبدأ يتعمله `Apply` على واحد تلو الآخر بشكل تدريجي لحد مايتم على كل الأجهزة والـ Servers اللي موجودة.

---

## A/B Testing Deployment

دي استراتيجية بتساعدنا إننا نختبر التحديث الجديد على مجموعة من المستخدمين، بس الفرق هنا إننا بنقارن بين نسختين مختلفتين من الـ **Feature** (مثلاً واجهة جديدة مقابل واجهة قديمة) في نفس الوقت.

---

## Shadow Deployment

في النوع ده، التحديث بيكون شغال جنب النسخة القديمة بدون ما المستخدمين يحسّوا بالتغيير، الهدف هنا هو إننا نراقب أداء التحديث قبل تعميمه.

---

## Recreate Deployment

الاستراتيجية دي بتعتمد على فكرة بسيطة جدًا، وهي إننا بنوقف السيرفرات اللي عليها الإصدار القديم وبعدين نشغل التحديث الجديد مرة واحدة.
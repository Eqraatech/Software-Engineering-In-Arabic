---
title: "Observability Pillars"
description: "gRPC is a high-performance, open-source framework for remote procedure calls (RPC). This guide explains how gRPC enables efficient, language-agnostic communication between microservices using Protocol Buffers."
excerpt: "علشان تقدر تتابع نظامك وتفهم إيه اللي بيحصل جواه، لازم يكون عندك Observability واللي بيعتمد على 3 أعمدة رئيسية: Logs، Metrics، وTraces. فتعالوا نتعرف على دور كل واحد منهم في مراقبة الأنظمة"
tags: ["monitoring", "observability", "traces", "logs", "metrics", "distributed-systems", "system-design"]
updatedAt: "2024-12-25"
featured: false
image: "https://assets.eqraatech.com/guides/observability-pillars.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/observability-pillars.png" alt="Observability Pillars" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

كثيرًا ما نسمع عن ال Observability ولكن ما هي حقًا ، وما هي أهدافها وإزاي نستغلها لتوصيف وحل أي مشكلة في أي نظام؟!

ورقة وقلم وخلونا نبدأ بقصة طبية بسيطة تفهمنا كل حاجة عن الموضوع دا قبل ما ندخل في الكلام عنه.

---

## توصيف الـ Observability في الحياة العملية

الإنسان لما بيتعب بيروح للطبيب اللي بدوره بيعمل عدة خطوات تساعده في تقييم الحالة وإيجاد العلاج المناسب:

- بيقوم بأخذ مؤشرات الشخص الحيوية 
- بيسأل الشخص بعض الأسئلة عشان يقدر يوصف الأعراض 
- وبيقوم بعمل أشعة على الجسم لتحديد مكان الألم 

جسم الإنسان عبارة عن نظام متكامل ولكن هو كذلك عبارة عن أجهزة مختلفة بتتعاون مع بعض زي الجهاز الهضمي والتنفسي وإلخ… والخطوات دي بتساعد الطبيب يعرف مصدر الشكوى ويحدد لها علاج مناسب وأساليب وقائية لمنع تكرارها.

أي `Software` في الدنيا زي الجسم بالظبط ، بيبقي نظام متكامل يتكون من عدة أنظمة أصغر. 

هدف ال `Observability` الأساسي هو تحويل النظام من Blackbox إلى Glass Box.

---

## أهم عناصر المراقبة (Pillars of Observability)

ولازم المبرمج يقوم بنفس خطوات التشخيص اللي قام بيها الطبيب عشان يحل أي مشكلة بتطرأ علي هذا النظام

### **Metrics** 

فالمؤشرات الحيوية عندنا عبارة عن ال `Metrics` :وهي مؤشرات رقمية تعطينا معلومات سريعة عن حالة النظام مثل ال `CPU and Memory Usage`, `Transaction per second` إلخ..

### **Logs** 

خلاص عرفنا إن فيه مشكلة ، بس هي إيه؟ هنا يجي دور ال `Logs` لتوصيف الأعراض

### Traces 

عرفنا إن فيه مشكلة وعرفنا ماهيتها ولكن مش عارفين مكانها! هنا يجي دور الـ `Traces` وهي `Entries` بتتبع مسار البيانات في النظام
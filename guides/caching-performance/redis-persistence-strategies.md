---
title: "Redis Persistence Strategies"
description: "Learn about Redis persistence mechanisms including RDB, AOF, and hybrid approaches for data durability."
excerpt: "كلنا عارفين إن Redis واحدة من أسرع الـ Key-Value Stores اللي موجودة في الساحة، وأكتر استعمالتها بيكون في الـ Caching وعشان كده أكيد جه في دماغ أي حد بيستخدمها سؤال مهم: لو حصل crash للسيرفر، إيه اللي هيحصل للداتا؟"
tags: ["redis", "caching", "persistence", "database", "performance"]
updatedAt: "2025-07-04"
featured: true
image: "https://assets.eqraatech.com/guides/redis-persistence.png"
author: mahyoussef
---

<img src="https://assets.eqraatech.com/guides/redis-persistence.png" alt="Redis Caching and Persistence Strategies infographic" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

كلنا عارفين إن `Redis` واحدة من أسرع الـ `Key-Value` Stores اللي موجودة في الساحة، وأكتر استعمالتها بيكون في الـ Caching وعشان كده أكيد جه في دماغ أي حد بيستخدمها سؤال مهم: لو حصل crash للسيرفر، إيه اللي هيحصل للداتا؟

**والإجابة هنا بتكون:** على حسب إحنا مشغلين أنهي طريقة من طرق الـ Persistence (الحفاظ على البيانات) اللي Redis بتوفرها.

## Data Persistence
الـ Data Persistence معناها إن الـ data اللي في الذاكرة (RAM) ما تضيعش لما السيرفر يوقع أو يحصل فيه مشاكل أو حتى يحصله restart. وكلنا عارفين إن redis شغالة أساسًا in-memory، وده معناه إنها سريعة جدًا بس عرضة لتضيع كل البيانات لو ما فيش backup نقدر نسترجع بيه البيانات دي.

عشان كده Redis بتوفرلنا طريقتين رئيسيتين لحفظ الداتا:

1. RDB (Redis Database)
2. AOF (Append Only File)

## RDB Snapshotting
> في الطريقة دي Redis بتعمل snapshot من كل الداتا الموجودة في الذاكرة (RAM) وتحطها في ملف .rdb.

## ازاي الـ RDB بيشتغل؟
كل شوية (حسب الـ `config` أو من خلال manual trigger)، Redis بتاخد نسخة Snapshot من كل البيانات اللي موجودة وتكتبها في ملف على الـ disk. فلو حصل crash لأي سبب من الأسباب للـ redis instance .. تقدر تعمل restore للداتا بشكل طبيعي من آخر snapshot حصل.

فالأول `Redis` بتعمل `fork()`: فبيكون عندنا Parent / Child Process الـ Parent Process بتقدر تستقبل read/write requests بشكل طبيعي جدًا، في حين إن الـ child process اللي حصلها `fork()` بتبدأ تكتب الـ snapshot في ملف مؤقّت على الـ disk.

بعد ما الـ child process يخلص، الملف المؤقّت بيتغيّر للـ `dump.rdb` بشكل آمن.

العملية دي بتستخدم كمان الـ `copy-on-write` علشان تقلل التأثير على الأداء خصوصًا لو كان حجم البيانات كبير فتقدر تنقل البيانات بشكل فعال.

## AOF (Append Only File)
الطريقة دي بتخلي `Redis` يكتب كل عملية `write` بتحصل (زي set, del) في ملف log. بمعنى أدق كل الـ commands اللي حصلت بتتكتب في الـ .log وبتتخزن على الـ Disk.

## ازاي الـ AOF بيشتغل؟
كل ما يحصل أي تعديل في الداتا، `Redis` بتكتب الـ `command` اللي حصل في آخر ملف الـ AOF. بشكل append-only ولما يحصل وليكن restart أو crash، تقدر وقتها تقرأ كل العمليات اللي في الملف ده واحدة واحدة وترجع الداتا.


---
title: "Database Connection Pool"
description: "A database connection pool manages a set of reusable connections to improve performance and reduce overhead. This guide explains how pooling works, why it’s essential, and how to configure it effectively."
excerpt: "في كل مرة تطبيقك بيحتاج يتعامل مع قاعدة البيانات، بيحتاج يفتح اتصال (Connection) — وفتح الاتصال ده عملية تقيلة ومكلفة لو بتحصل بشكل متكرر. علشان كده بنستخدم Database Connection Pooling: تقنية ذكية بتوفر مجموعة جاهزة من الاتصالات (Connections) بيتشاركها التطبيق بدل ما يفتح ويقفل في كل مرة."
tags: ["database", "performance", "connection-pool", "backend"]
updatedAt: "2024-04-21"
featured: false
image: "https://assets.eqraatech.com/guides/database-connection-pool.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/database-connection-pool.png" alt="Database Connection Pool" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

تخيل تروح فرع لبنك او أي فرع لشركة تليفون عشان تستفسر عن حاجة معينة وتلاقي مفيش غير شباك واحد , وفيه مئات الناس مستنيين أدوارها تيجي , وعلى ما يجي دورك وتستفسر ومسئول الشباك يساعدك بتكون استهلكت وقت كبير جدًا.

طب هيكون ايه رد فعلك لو مع كل حد هيجي يسال عن حاجة معينة, الفرع هيروح يدور على حد يوظفه يقعد في الشباك يساعدك وبعدين يمشي الموظف ده ؟

💡هو ده كان هيبقى شكل حياة تطبيقاتنا من غير Database Connection Pool بكل بساطة

---

## Database Connection Lifecycle

خلونا قبل ما نتكلم عن الـ `Database Connection Pool` , نعرف ايه اللي بيحصل اما بنعوز نتصل بقاعدة البيانات من خلال التطبيق بتاعنا :

1. التطبيقات بتستعمل **Database Drivers** عشان تفتح **Connection** مع قاعدة البيانات
2. بيتم **فتح Network Socket** عشان نوصل التطبيق بقاعدة البيانات
3. المستخدم بيتعمله **Authentication** وفي حالتنا هنا بيكون التطبيق
4. بعد ما العملية تتم بنجاح , ممكن الـ **Connection يتقفل**
5. ومن ثم الـ **Network Socket بيتقفل** هوا كمان

فزي ما احنا شايفين فتح وقفل الـ `Connection` مع قواعد البيانات **عملية مش سهلة وبتضمن أكتر من خطوات بالإضافة لكونها مستهلكة للـ Resources**.

وطبعًا هنلاحظ ان ده ممكن يكون عادي في لو **التطبيقات كانت صغيرة** , ولكن مع نمو وتطور التطبيقات بتاعتنا هيواجهنا مشكلة كبيرة بخصوص الموضوع ده .

---

## ليه نستعمل Connection Pool ؟

الـ Database Connection Pool جه في الأساس عشان يعالج المشكلة اللي شوفناها بتاعة فرع البنك او شركة التليفون , وهو ان عشان **تكلفة الـ Database Connections** عالية **وبتستهلك Resources** فقام موفر أكتر من شباك لخدمة الناس .. أو بمعنى أصح **مخزن أكتر من Database Connection جاهزين** ..

وده عشان واول ما بيجي Request من التطبيق عشان يتواصل مع قاعدة البيانات نبدأ **نعيد استعمال** الـ Connections دي , بدل ما كل مرة نروح نفتح ونقفل Connection من أول وجديد .
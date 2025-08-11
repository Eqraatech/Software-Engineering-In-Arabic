---
title: "CQRS Architecture Pattern"
description: "CQRS (Command Query Responsibility Segregation) separates read and write operations for better scalability and performance. This guide explains how CQRS works and when to use it in modern systems."
excerpt: " بناء البرمجيات زي بناء المباني بالظبط محتاج ترتب أجزاء المبني وعلاقتهم ببعض بطريقة مناسبة لوظيفة المبني والمستخدمين, فالبيت مبني وكذلك الجامعة مبني ولكن الحجم, والوظيفة والمستخدمين مختلفين ومن هنا بتيجي فكرة ال Architectural Patterns في البرمجيات."
tags: ["software-architecture", "microservices", "CQRS", "backend", "distributed-systems", "system-design"]
updatedAt: "2024-09-22"
featured: false
image: "https://assets.eqraatech.com/guides/cqrs-architecture-pattern.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/cqrs-architecture-pattern.png" alt="CQRS Architecture Pattern" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

 بناء البرمجيات زي بناء المباني بالظبط محتاج ترتب أجزاء المبني وعلاقتهم ببعض بطريقة مناسبة لوظيفة المبني والمستخدمين, فالبيت مبني وكذلك الجامعة مبني ولكن الحجم, والوظيفة والمستخدمين مختلفين ومن هنا بتيجي فكرة ال Architectural Patterns في البرمجيات.

والشطارة بتكون في ازاي استخدم النمط الأكثر إفادة لوظيفة وحجم ونوع الاستخدام لمشروعي اللي شغال عليه.

---

## Command Query Responsibility Segregation (CQRS)

في معظم مشاريعنا بنستخدم `CRUD Pattern` وبنعتمد علي الوظائف الأساسية فيه زي Create, Read, Update, Delete وبالفعل هو نمط مناسب للمشاريع البسيطة والصغيرة والمتوسطة في الحجم لأنه سهل.

ولكن في حالات بنحتاج فيها Data Manipulation اكثر من الـ `CRUD` يقدر يقدمه , زي اننا نشتغل في Business العلاقات فيه بين ال `objects` معقدة أكتر أو تطبيق يكون فيه استهلاك البيانات فيه عالي وكذلك كتابتها ودا بيوقعنا في مشكلة لأن متطلبات الـ `Scaling` في حالة الـ Heavy Reads تختلف عن متطلباته في حالة الـ Heavy Writes 

ال **CQRS اختصار لـ Command Query Responsibility Segregation** أو Separation وهو نمط هدفه الفصل بين الـ `Commands` و الـ `Queries` في الكود وبنعّرف فيه:

- **الأوامر (Commands):** : هي عملية كتابة أو تغيير البيانات وهي العمليات اللي فيها بتتغير حالة النظام. والأوامر جي بتقوم بـ "فعل" شيء وتؤثر على حالة النظام.
- **الاستعلامات (Queries):** عملية قراءة البيانات وهي العمليات اللي بتسترجع بيانات و لكن لا تغير حالة النظام. بمعنى أنها "تسأل" عن شيء معين ولا تعدل أي شيء.

---

الـ `CQRS` يستخدم اثنين من الـ Models المختلفة عشان يحقق الأوامر (`Commands`) بالـ Model المناسب ليها و كذلك `Model` خاص بالـ للاستعلامات (`Queries`). وبما إن دا `Architectural Pattern` فبيسيب للمبرمج حرية اختيار وتنويع الـ `Models` اللي شايفها بتحقيق الهدفين دول وايه الأنسب لمشروعه وده بيدينا مرونة في التنفيذ. 

كمان نقدر في تنفيذه نستخدم 2 من قواعد البيانات -الطريقة الأكثر شيوعًا- واحدة مخصصة للاستعلامات وواحدة للأوامر ويتعمل بينهم `Syncing`.
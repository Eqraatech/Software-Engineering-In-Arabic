---
title: "ACID Properties in DBMS"
description: "ACID stands for Atomicity, Consistency, Isolation, and Durability—key properties that ensure reliable database transactions. This guide breaks down each property and how they maintain data integrity."
excerpt: "ال ACID ببساطة عبارة عن اختصار ل 4 قواعد لازم تحققهم قاعدة البيانات و العمليات اللي بتتم عليها بغض النظر عن أي Software or Hardware Failure أو حتى Power Failure. و ال 4 قواعد دي هي الضمان إن ال Database دي والبيانات اللي فيها صحيحة وموثوق فيها و دا عامل أساسي في مجال البرمجيات ككل صحة البيانات."
tags: ["database", "transaction", "atomicity", "consistency", "isolation", "durability", "backend" , "performance"]
updatedAt: "2024-05-05"
featured: false
image: "https://assets.eqraatech.com/guides/acid-properties-in-dbms.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/acid-properties-in-dbms.png" alt="ACID Properties in DBMS" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

من المفاهيم الاساسية والشهيرة في الـ Relational Databases هي الـ ACID فورقة وقلم وتعالوا نعرف هي إيه وليه مهم إن قاعدة البيانات تكون بتحققها. 

> ال ACID ببساطة عبارة عن اختصار ل 4 قواعد لازم تحققهم قاعدة البيانات و العمليات اللي بتتم عليها بغض النظر عن أي Software or Hardware Failure أو حتى Power Failure.

و ال 4 قواعد دي هي الضمان إن ال Database دي والبيانات اللي فيها صحيحة وموثوق فيها و دا عامل أساسي في مجال البرمجيات ككل "صحة البيانات".

**ال 4 قواعد هما:**

- Atomicity 
- Consistency 
- Isolation (Safe Concurrent Transactions Execution)
- Durability(Committed Transactions Must Be Durable)

---

## Atomicity 

القاعدة دي بتقول ان ال Transaction الواحد واللي بيعني "عملية مفيدة كاملة من وجهة نظر النظام" يا اما يتنفذ كله يا ما يتنفذش خالص, فمثال على ال Transaction لو شغال علي برنامج لبنك هيكون عملية نقل الأموال من حساب للتاني العملية دي كلها مع بعض البرنامج هينفذها على 3 خطوات:

1. اتاكد ان الحساب فيه 100 جنيه
2. خصم 100 جنيه من الحساب 
3. احط 100 جنيه في حساب الطرف الثاني

فهنا القاعدة بتقول ان لازم ننفذ كل الخطوات دي مع بعض كعملية واحدة، ولكن في حالة فشل أي خطوة في النص فلازم يحصل تراجع عن كل الخطوات اللي تم تنفيذها مسبقًا - بمعنى اصح Rollback - لأنها هتحط قاعدة البيانات في حالة غير مفهومة وغير صحيحة لو ما تراجعناش عن كل الخطوات اللي اتنفذت قبلها.

---

## Consistency 

القاعدة هنا بتقول ان كل عملية تتم على قاعدة البيانات لازم تسيبها في حالة صحيحة و معروفة, ودا هيتم بإن قاعدة البيانات تتأكد من كل ال Constraints أو الشروط المحددة لها. وكمثال لو بعمل برنامج لاستعارة الكتب ومحدد إن أقصى عدد للكتب يقدر يستعيره المستخدم هو 3, لازم ال DB ترفض عملية استعارة 4 كتب لأن دا بيكسر واحد من ال Constraints.

---

## Isolation 

القاعدة دي مرتبطة بشكل وثيق بفكرة ال Concurrency أو العمليات اللي بتتم علي ال Database في نفس الوقت لازم متدخلش في شغل بعض وإلا النتيجة النهائية هتكون غلط كمثال في برنامج البنك لو افترضنا ان في شخصين بيسحبوا من حساب واحد في نفس الوقت.

---

## Durability

والقاعدة دي بتقول ببساطة أن ال Committed Transactions -العمليات التي تم تنفيذها بشكل صحيح على قاعدة البيانات لازم تتخزن بشكل نهائي ودائم. 

ودا ينبع من طريقة تنفيذ الكمبيوتر للمهام لأنه يعتمد على الـ RAM وهي Volatile Memory فلو تم تنفيذ العملية ولم يتم تخزينها في Non-Volatile Memory زي ال Hard Disk وحصل Power Failure فهنا بنواجه Inconsistent State لقاعدة البيانات.

---

## في الختام

كلا مبدأي ال Isolation and Durability كل لما مستوى الأمان يزيد و نحقق الشرط بقوة كل لما دا هيأثر على سرعة أداء قاعدة البيانات أو هيكون مكلف أكثر. 

وبالتالي المبرمج الشاطر هو اللي فاهم النظام ومتطلباته و فاهم ال Trade-offs وقادر يختار المستويات المناسبة.
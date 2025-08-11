---
title: "Database Cheatsheet for System Design"
description: "A quick guide to choosing and using databases in system design. Covers SQL vs. NoSQL, normalization, indexing, transactions, replication, sharding, and when to use each technique for scalability and performance."
excerpt: "لازم نكون عارفين ان اختيارنا للـ Database في الـ System اللي بنبنيه، هو قرار مش سهل وقرار هنبقى ملزمين بيه لفترة طويلة فلازم نختارها بعناية خصوصًا لو كمان الموضوع هيتضمن Budget وفلوس هتندفع."
tags: ["database", "nosql", "sql", "software-arhcitecture", "backend", "distributed-systems", "system-design"]
updatedAt: "2023-12-21"
featured: false
image: "https://assets.eqraatech.com/guides/database-cheatsheet-for-system-design.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/database-cheatsheet-for-system-design.png" alt="Database Cheatsheet for System Design" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

لازم نكون عارفين ان اختيارنا للـ Database في الـ System اللي بنبنيه، هو قرار مش سهل وقرار هنبقى ملزمين بيه لفترة طويلة فلازم نختارها بعناية خصوصًا لو كمان الموضوع هيتضمن Budget وفلوس هتندفع.

عشان نسهل على نفسنا الاختيار هنحاول الأول نجاوب على السؤال ده: 

---

**هو ايه نوع الـ Data اللي محتاجين نخزنها في الـ System ؟** 

والاجابة هتكون حاجة من 3 واللي هنحاول سوا نبني Mind-Map في عقلنا عشان نسهل الاختيار علينا شوية: 

1. Structured Data (Standard SQL Table Schema)
2. Semi-Structured Data (JSON, XML, etc..)
3. UnStructured Data (Blob) 

بعد معرفتنا بنوع البيانات اللي هنخزنها، هنكون محتاجين نعرف حاجتين اتنين بس:  

1. ايه هي الـ Use-Case أو هدفنا من تخزين البيانات 
2. هل هنروح ناحية الـ Cloud ولا هيبقى اعتمادنا على الـ Open-Source والـ 3rd Party ؟ 

💡وده لإن تحديد الهدف من التخزين هيفرق في اختيار الـ Database وهيخلينا نروح لنطاق أقل من الاختيار، واعتمادنا على الـ Cloud من عدمه كذلك هيسهل علينا الاختيار وهيضيق نطاق الاختيار. 

### **Structured Data**

لو البيانات اللي هنخزنها Structured فوقتها عندنا 2 Use Cases : 

1. Transactions / OLTP (Online Transaction Processing)
2. Analytics / OLAP (Online Analytical Processing)

لو هدفنا كان OLTP فوقتها هنتجه للـ **Relational Databases** اما لو كان OLAP فوقتها هنروح للـ **Columnar Database** والاتنين مختلفين عن بعض من ناحية طريقة تخزين البيانات وهيكلتها.

ووقتها نقدر بناء على معرفتنا هل هنروح للـ Cloud ولا لا نختار من الجدول اللي موجود في الصورة ، وطبعا بعد قراءتنا عن الفروقات بينهم وايه اللي هيخدمنا أكتر من ناحية الـ Performance, Pricing Model, وعوامل تانية كتير.

---

### **Un-Structured Data**

لو البيانات اللي هنخزنها UnStructuredزي الصور والفيديوهات فوقتها بعد معرفتنا هنروح للـ Cloud ولا لا نقدر نختار من الجدول

### **Semi-Structured Data**

ودي اللي بنقول عليها NoSQL Databases وليها أنواع واستخدامات كتيرة جدًا:  

 1. **In-Memory Databases**: لو ناوين نتجه لناحية الـ Key-Value Database ، لو كان الهدف من التخزين اننا يبقى عندنا In-Memory Database فوقتها هنروح للـ Cache Databases.
2. **Wide-Column Databases**: لو كان الهدف من التخزين الـ Real-Time Analysis أو وجود كميات ضخمة من البيانات أو Concurrent Queries بشكل كبير خصوصا في عمليات الكتابة ومحتاجين High Throughput in Writes وقتها هنتجه للـ Wide-Column Databases.
3. **Time-Series Databases**: لو كان الهدف اننا محتاجين نركز على بناء Metrics أو Real-Time Dashboards ومعتمدين على البيانات خلال فترات زمنية فهنتجه للـ Time-Series Databases.
4. **Immutable Ledger Databases**: لو كان الهدف اننا محتاجين Audit Trails أو حاجة بتدعم الـ Supply Chain والـ Crypto Currency والـ Digital Assets فوقتها هنتجه للـ Immutable Ledger Databases.
5. **Geospatial**: لو كان الهدف اننا محتاجين نعتمد على الـ Location أو بنبني  Geographic Information Service فوقتها هنتجه للـ Geospatial.
6. **Text Search**: لو كان الهدف اننا محتاجين نعمل Full Text Search فهنتجه للـ Text Search واللي أشهرهم Elastic Search من ناحية الـ Open Source.
7. **Graph**: لو كان الهدف اننا محتاجين يبقى عندنا Entity-Relationship بين البيانات وبعضها وهتكون العلاقات دي معقدة فوقتها هنتجه للـ Graph Databases.

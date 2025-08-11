---
title: "How to Store Passwords In Database"
description: "Process scheduling is how an operating system decides which process runs next. This guide covers key algorithms like Round Robin, Priority, and Shortest Job First to manage CPU time efficiently."
excerpt: "تخزين كلمات المرور بشكل آمن مش مجرد خطوة تقنية، دي مسؤولية أساسية لحماية بيانات المستخدمين. فتعالوا نتعلّم **إزاي تخزن الباسوردات بطريقة صحيحة وآمنة** بعيدًا عن الممارسات الخطيرة زي التخزين النصي العادي (plaintext)."
tags: ["hashing", "salt", "database", "plaintext", "web-development"]
updatedAt: "2024-11-30"
featured: false
image: "https://assets.eqraatech.com/guides/how-to-store-passwords-in-database.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/how-to-store-passwords-in-database.png" alt="How to Store Passwords In Database" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

ازاي الـ Passwords بتتخزن في الـ Database وازاي نقدر نتأكد من الـ Password بتاع الـ User سليم وهو بيعمل Login ؟ 

وقبل ما نبدأ نتكلم عن ده خلونا في البداية نأكد على أهمية الموضوع وأن تخزين الـ Passwords في الـ Database لازم يتم بشكل ميسهلش للـ Hackers أنهم يوصلوا للـ Passwords حتى لو حصل اختراق للـ Database.

### **طب ايه هي الحاجات اللي بتسهل عملية الوصول للـ Passwords ؟** 

فيه بعض الحاجات اللي مفروض نبعد عنها تمامًا عشان بتسهل للـ Hackers انهم يوصلوا للـ Passwords زي: 

1. اننا نخزن الـ Passwords كـ `Plaintext` في الـ Database ، ده هيخلي اي حد Internal شغال في الشركة انه يكون ليه `Access` على كل الـ Passwords وعارفهم كلهم .. وده برضو هيخلي اختراق الـ Database عملية بتسهل الوصول لكل الـ Passwords اللي موجودة، فالـ Hacker هيكون قدامه الـ Passwords على طبق من ذهب ..
2. اننا نستعمل `Legacy Hashing Algorithms` زي الـ [MD5](https://en.wikipedia.org/wiki/MD5?ref=eqraatech.com) و الـ [SHA-1](https://en.wikipedia.org/wiki/SHA-1?ref=eqraatech.com#:~:text=In%20cryptography%2C%20SHA%2D1%20\(,rendered%20as%2040%20hexadecimal%20digits.) فبالرغم من انهم يعتبروا `Algorithms` سريعة جدًا، إلا أنهم يعتبروا Not Secured وسهل يتم معرفة الـ Passwords من خلالهم.

### **طب ازاي نخزن الـ Passwords بشكل آمن ؟** 

وفقًا لمشروع الـ [OWASP](https://owasp.org/?ref=eqraatech.com) واللي هو اختصار لـ Open Web Application Security Project فهم ادونا شوية Guidelines نقدر نمشي عليها عشان نخزن الـ Passwords بشكل آمن زي:

**اول حاجة** اننا نستعمل `Modern Hashing Algorithms` والـ Hashing هنا هو عبارة عن طريق واحد رايح مبيرجعش، فهي عبارة عن Function بتديها الـ Password ومينفعش تعمل عكس العملية دي عشان تعرف الـ Password . 

وفي نفس الوقت لو حصل اي اختراق والـ Attacker وصل للـ Passwords فهو مش هيقدر يستعملها في الـ Application لانها Hashed .. ومن أمثلة الـ `Modern Hashing Function` الـ [Bcrypt](https://en.wikipedia.org/wiki/Bcrypt?ref=eqraatech.com) واللي بعتر بطيء بسبب الـ Resources اللي بيحتاجها عشان يـ `Compute` الـ `Hashed Value` ..

**تاني حاجة** هي اننا نضيف شوية ملح على الـ Password منسيبهوش كده .. والـ `Salt` هنا هو عبارة عن `Unique Random Generated String` بينضاف على الـ Password قبل ما يتعمل `Hashing` وبعدين يتعمل `Hashing` ليهم مع بعض ..

---

### **طب ليه مينفعش نخزن الـ Passwords كـ Hashed بس ؟** 

لان الـ Attacker ممكن من خلال `Pre-Computation Attacks` يقدر يتغلب على الـ `One-Way Hash` وفيه Techniques زي الـ `Rainbow Table` اللي ممكن تساعده في حاجة زي كده ويتعرف على الـ Password .. 

فدلوقتي عشان نخزن أي Password في الـ Database بنزود عليه Salt ونعمل للـ Combination دي `Hashing` مع بعض ونخزن الـ `Hash(Password+Salt) Output` في الـ Database بالاضافة للـ `Salt` وهنعرف ده ليه دلوقتي .. 

### **Password Validation**

لما الـ User بيجي يكتب الـ Password ، بنروح نجيب الـ Salt اللي اتزود على الـ Password بتاعه من الـ Database ونزوده على الـ User Password اللي كتبه ونعملهم Hashing مع بعض ونقارن الـ Hashed Combination ده مع اللي موجود في الـ Database لو طلعوا زي بعض ، اذن الـ Password سليم.
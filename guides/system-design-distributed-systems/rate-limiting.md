---
title: "Rate Limiting"
description: "Rate limiting controls how often users or systems can make requests, protecting APIs from abuse and ensuring fair usage. This guide explains key algorithms like Token Bucket and Leaky Bucket, and when to use them."
excerpt: "ال Rate Limiting هي واحدة من أهم الطرق الأساسية عشان نحقق الـ Robustness في الـ Service اللي بنبنيها وده من خلال تحديد عدد Requests معينة مسموح للمستخدم يطلبها في فترة زمنية محددة."
tags: ["rate-limiting", "resiliency", "backend", "web-development", "distributed-systems", "system-design"]
updatedAt: "2023-12-21"
featured: false
image: "https://assets.eqraatech.com/guides/rate-limiting.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/rate-limiting.png" alt="Rate Limiting" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

ال Rate Limiting هي واحدة من أهم الطرق الأساسية عشان نحقق الـ Robustness في الـ Service اللي بنبنيها وده من خلال تحديد عدد Requests معينة مسموح للمستخدم يطلبها في فترة زمنية محددة.

ومش بس كده، ده كمان بتساعد في تحقيق الـ Security وده من خلال انها بتساعد في صد بعض الـ Attacks المهمة.

💡الـ Rate Limiting عامل زي ظابط المرور اللي بيوقف السواق ويديله مخالفة لو تجاوز السرعة المسموح بيها.

---

### **أشهر استخدامات الـ Rate Limiting**

من أشهر الأماكن اللي بتشوف فيها ال Rate Limiting هي صفحات تسجيل الدخول اللي بعد عدد معين من إدخال كلمة مرور غير صحيحة في فترة صغيرة من الزمن بتمنعك تحاول تاني لمدة معينة.

تحديد عدد الـ Requests ده بيحمي الـ APIs من الاستخدام السيئ أو من الضغط الزائد عليه واللي ممكن يحصل من خلال: 

##### **1- الـ DDoS Attacks**

ودي نوع من أنواع الـ Cyber Attacks لو مقدرناش نصدها فغالبًا الـ Server أو الـ Service بتقع، لانها مش قادرة تتحمل ضغط الـ Traffic الزايد واللي بنسبة كبيرة بيقوم بتنفيذها Bots، بالإضافة لإنها بتعمل Resource Starvation وده معناه انها بتستغل كل موارد الـ Server لمستخدم واحد بس وبالتالي بتمنع باقي المستخدمين من الاستفادة بالـ Service ..

##### **2- الـ Brute Force Attacks :**

فاكرين صفحة تسجيل الدخول ؟ دا نوع من الهجمات بيستهدف الصفحات دي و يجرب كل الاحتمالات لكلمة مرور معينة, واستخدام ال Rate Limiters بينجح في صد النوع دا بسهولة لأنه بعد عدد محاولات معينة بيقفل استقبال الصفحة للمحاولات من المستخدم دا.

##### **3- الـ Web Scraping** 

ال scraping هو عبارة عن استخراج كل المعلومات من موقع ما معين, وممكن يتم استخدامه بشكل جيد أو سئ. وكتير من المواقع بتمنعه أو بتحده زي مواقع الـ Social Media زي Twitter أو Instagram اللي بيعملوا Limit لعدد مرات الـ Home Refresh في الساعة لمنع النوع دا من الاستخدام لمواقعهم.


---

### **طب ازاي الـ Rate Limiting بيشتغل ؟** 

فكرة عمله بسيطة جدًا, بيحدد لكل مستخدم بناءًا على الـ IP Address بتاعه عدد Requests معينة لو تجاوزها بيقفل الخدمة للمستخدم ده, مثال على ده لو عندنا API بيسمح بـ 200 Request في الدقيقة للمستخدم، لو المستخدم استهلك الـ 200 كلهم خلال الدقيقة بيقفل الخدمة عليه لبقية الدقيقة ومن الدقيقة الجديدة بيرجع يسمح ليه بـ 200 Request جداد وهكذا. 

### Rate Limiting Algorithms

طبعًا في Algorithms مختلفة لتنفيذ الفكرة دي ولكنها بتعتمد على نفس المبدأ: عدد معين من الـ Requests هيكون مسموح للـ IP في خلال فترة زمنية وبعدها بيتم رفض أو تأخير الطلب من الـ IP ده. أشهر الـ Algorithms اللي بيتم استخدامها لتنفيذه: 

- **Token Bucket**
- **Leaky Bucket**
- **Fixed Window Counter**
- **Sliding Window Log**
- **Sliding Window Counter**

> الـ Rate Limit ممكن يتنفذ في الـ Application Logic بتاعك من خلال تنفيذ الـ Algorithms دي، أو ممكن تعتمد على Functionality جاهزة بيقدمهالك Component زي الـ API Gateway لو شغال على الـ Cloud، وممكن برضو تستخدم 3rd Party Service جاهزة تقوم بالدور له.
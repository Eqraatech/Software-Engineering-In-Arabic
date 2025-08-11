---
title: "Load Balancer"
description: "A load balancer distributes incoming traffic across multiple servers to improve performance, reliability, and scalability. This guide explains how it works, common algorithms, and where it's used in modern system architectures."
excerpt: "الـ load balancer أو مُوزع الأحمال هو بكل بساطة ضابط مرور بيوجه الطلبات اللي جاية من الـ clients إلى الـ server المناسب في النظام. زمان كنت بتعمل application ويشتغل على سيرفر لكن مع تزايد عدد الطلبات، السيرفر مش بيقدر يخدم كل دا وبيقع. فبنتجه للـ Scaling."
tags: ["load-balancer", "microservices", "network", "backend", "distributed-systems", "system-design"]
updatedAt: "2023-10-23"
featured: false
image: "https://assets.eqraatech.com/guides/load-balancer.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/load-balancer.png" alt="Load Balancer" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ load balancer أو “مُوزع الأحمال” هو بكل بساطة ضابط مرور بيوجه الطلبات اللي جاية من الـ clients إلى الـ server المناسب في النظام.

زمان كنت بتعمل application ويشتغل على سيرفر لكن مع تزايد عدد الطلبات، السيرفر مش بيقدر يخدم كل دا وبيقع. فبنتجه للـ Scaling: 

1.  تشغل أكثر من نسخة من التطبيق على أكتر من server
2.  تقسم التطبيق لأجزاء مستقلة ونحط كل جزء علي server مختلف

 **بس في الحالتين الـ client هيعرف هيكلم انهي سيرفر بالظبط ازاي؟** 

### ازاي الـ Client هيعرف الـ Server اللي مفروض يكلمه ؟

هنا بيجي دور الـload balancer اللي بيكون عنده جدول فيه كل السيرفرات المتاحة، وعنده معلومات عن كل واحد عليه service ايه بالظبط؟ هل الـ Server شغال ولا واقع؟ ولو شغال فمشغول اد ايه؟ وباستخدام خوارزمية معينة بيوجه الـ client لل server المناسب.

---

### خوارزميات الـ Load Balancer

 الخوارزميات اللي بيشتغل بيها موزع الأحمال بسيطة في فكرتها ولكن فعالة ومن أهمهم: 

1.  Round Robin
2. Least Connections
3. Least Response Time
4. Hash

وهنعرف كل واحد بيشتغل ازاي في ورقة تانية بإذن الله.

### مميزات الـ Load Balancer

 الـ load balancer بفكرته البسيطة بيقدم مميزات كتير منها: 

1.  بيقلل الوقت اللي بيكون فيه النظام مش متاح؛ لأنه ببساطة لو سيرفر وقع الـload balancer مش هيبعت له أي طلبات من الـclients.
2. بيخلي النظام ككل، أكثر كفاءة ومرونة، ويقدر يتعامل مع عدد أكبر من الطلبات في وقت أسرع.

**الـload balancer من الأفكار السهلة ولكن الأساسية في تصميم النظم، وليه نوعين: نوع hardware ونوع software ودا الأكثر استخدامًا؛ لأنه بالتأكيد أكثر مرونة من الـhardware**.
---
title: "Proxy vs. Reverse Proxy"
description: "A proxy sits between a client and the internet, hiding the client’s identity. A reverse proxy sits in front of servers, handling requests on their behalf for load balancing, caching, or security. This guide explains the differences and when to use each."
excerpt: "الـ Proxy والـ Reverse Proxy بيشتغلوا كـ وسيط بين طرفين الـ Client والـ Server، لكن كل واحد فيهم بيخدم هدف مختلف."
tags: ["proxy", "microservices", "network", "backend", "load-balancer", "distributed-systems", "system-design"]
updatedAt: "2023-10-24"
featured: false
image: "https://assets.eqraatech.com/guides/proxy-vs-reverse-proxy.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/proxy-vs-reverse-proxy.png" alt="Proxy vs. Reverse Proxy" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

كتير من الشركات دلوقتي بتستعمل الـ Proxy عشان تـ Route وتـ Secure الـ Traffic بين الـ Networks وبعضها بالاضافة لفوايد تانية كتير هنعرفها سوا.

### ايه هو الـ Proxy ؟

الـ Proxy بكل بساطة بيتمثل دوره في كونه عبارة عن وسيط بين الـ Clients والـ Servers، وفيه نوعين ليه وهم الـ Forward Proxy والـ Reverse Proxy

### Forward Proxy 

وعادة بيتم الاشارة ليه بكلمة Proxy بس .. فلو قابلت اسم Proxy المفترض ان يكون المقصد هو الـ Forward Proxy .. والنوع ده من الـ Proxy بيكون شغله ناحية الـ Clients وبيشتغل كوسيط بين الـ Clients والـ Servers

---

### استخدامات الـ Forward Proxy

1. وأحد أهم استخداماته هو انه بيعمل Processing للـ `Requests` الخارجة من الـ Clients ورايحة للـ Outgoing Resources أو للـ Internet
2. الـ Forward Proxy برضو بيتم استعماله في الشركات بشكل كبير عشان يحمي الـ Clients اللي موجودين في Private Network من أنهم يعملوا Access للـ Internet Resources
3. الـ Client Anonymity يعني بيخفي هوية الـ Client وده لإن الـ Outgoing Requests اللي خارجة من الـ Clients ورايحة للـ Servers أو للانترنت عمومًا .. بيكون المسئول عنها دلوقتي هو الـ Proxy لانه بيستقبل الـ Request ويبعته بالنيابة عنهم .. وبالتالي الـ Servers مش عارفة هوية الـ Clients الحقيقية .. (ودي احدى اهم استخداماته واللي بنشوفها في الـ `VPN` )
4. الـ Content Filtering وده لإن زي ما عرفنا انه هو بيستقبل الـ Requests من الـ Client فيقدر يعمل عليها `Filtration` قبل ميبعتها وبالتالي ممكن هنا يعمل `URL Blocking` لكتير من الـ Websites اللي ممكن تمثل `Threats`.
5. الـ Performance Improvement وده من خلال انه يقدر باستعمال `Caching` Mechanisms يطور ويحسن من الأداء ويبقى بمثابة `Boost` لكتير من الـ Client Requests.

### Reverse Proxy 

النوع ده من الـ Proxy بيكون شغله ناحية الـ Server-Side Infrastructure أكتر، فالـ Reverse Proxy هنا دوره أنه بيضمن أن الـ Clients ميقدروش يتواصلوا بشكل Direct مع الـ Web Servers ولكن بيتواصلوا معاهم بشكل غير مباشر من خلال الـ Reverse Proxy اللي بيستقبل الـ Client Requests دي قبل ميبعتها للـ Web Servers.

### استخدامات الـ Reverse Proxy

1. وعشان كده أحد أهم استخدامات الـ Reverse Proxy هو انه بنسبة كبيرة بيتم الاعتماد عليه كـ Load Balancer في انه بيوزع الـ `Incoming Requests` من الـ Clients على الـ Web Servers.
2. الـ Server Anonymity يعني بيخفي هوية الـ Server وده لإن الـ Client دلوقتي أصبح بيبعت الـ Request واللي بيستقبله هو الـ Reverse Proxy
3. الـ `DDoS` Mitigation وده معناه انه يقدر يخفف من الـ `DDoS` من خلال عملية الـ `Throttling` اللي ممكن يعملها للـ Incoming Requests
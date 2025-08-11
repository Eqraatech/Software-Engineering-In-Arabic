---
title: "Load Balancer Algorithms"
description: "Load balancer algorithms decide how to distribute incoming traffic across multiple servers. This guide covers common strategies like Round Robin, Least Connections, IP Hash, and how they impact performance and reliability."
excerpt: "في الأنظمة اللي بتخدم آلاف أو ملايين المستخدمين، لازم الحمل يتوزّع على السيرفرات بشكل ذكي علشان الأداء يفضل ثابت وسريع. هنا بييجي دور Load Balancer Algorithms — خوارزميات بتحدد إزاي الطلبات تتوزع على السيرفرات."
tags: ["load-balancer", "microservices", "network", "backend", "distributed-systems", "system-design"]
updatedAt: "2023-10-24"
featured: false
image: "https://assets.eqraatech.com/guides/load-balancer-algorithms.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/load-balancer-algorithms.png" alt="Load Balancer Algorithms" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

في الأنظمة اللي بتخدم آلاف أو ملايين المستخدمين، لازم الحمل يتوزّع على السيرفرات بشكل ذكي علشان الأداء يفضل ثابت وسريع. هنا بييجي دور Load Balancer Algorithms — خوارزميات بتحدد إزاي الطلبات تتوزع على السيرفرات.

---

### Load Balancer Static Algorithms

  
 1. **Round Robin :** وهو من أبسطهم وفيه الـ Requests اللي الـ Client بيبعتها ويستقبلها الـ LB بتتبعت لـ Service Instance مختلفة عن اللي قبلها بشكل Sequential. الـ LB بيكون عنده List بالـ Available Servers وبيبدأ يـ Route كل Request للـ Server المقابل .. فالـ Request No.1 يروح للـ Server No.1 وهكذا ..  
  
2. **Sticky Round Robin :** وهو عبارة عن تحسين بسيط للـ Round Robin واللي فيه مثلا لو “محمود” بعت Request للـ Service Instance No.1 فالـ Requests الجاية هتتبعت برضو لنفس الـ Service Instance. وهنا بتكمن قوة الـ Sticky Round Robin وده مهم جدًا خصوصًا للـ Sessions فمفيش حد هيحب كل شوية يلاقي الـ Shopping Cart بتاعته فاضية عشان Service تانية غير اللي قبلها اللي استقبلت الـ Request  
  
3. **Weighted Round-Robin :** وده برضو تحسين بسيط للـ Round Robin بس هنا بنحط Weight أو نسبة على كل Service واللي عليها نسبة أعلى أو Weight أكبر بيـ Handle Requests أكتر.  
  
 4. **Hash :** وهنا بنتطبق Hashing Function على الـ IP مثلًا أو الـ URL وبناءًا على نتيجة الـ Hash Function الـ Request بيوصل للـ Service Instance المطلوبة. في الطريقة دي مثلا كل الـ Requests اللي بتروح لنفس الـ URL هتتـ Handle من خلال نفس الـ Service Instance

### Load Balancer Dynamic Algorithms
  
1. **Least Connections :** وهنا الـ Request اللي الـ Client بيبعته بيتـ Handle من خلال الـ Service Instance اللي عندها أقل عدد من الـ Concurrent Connection.  
  
2. **Least Response Time :** وهنا الـ Request اللي الـ Client بيبعته بيتـ Handle من خلال الـ Service Instance اللي عندها اسرع Response Time.  

---
  
> **دول كانوا أشهر الـ Algorithms وأكترها شيوعًا وكل واحد منهم ليه الـ Trade-Offs الخاصة بيه واللي تحديده بيفرق من Application للتاني على حسب الـ use-cases واحتياجات التصميم.**
---
title: "Domain Name System (DNS)"
description: "DNS translates human-readable domain names (like example.com) into IP addresses that computers use to identify each other. This guide explains how DNS works, its components, and its role in web performance and reliability."
excerpt: "الـ DNS بيحول عنوان الموقع لـ IP Address يقدر الكمبيوتر يفهمه, لكن ايه هو ال DNS أصلاً؟ الكمبيوتر مبيفهمش لغة البشر ومع ذلك لما بتكتبله (eqraatech.com) بيفتحلك الموقع فعلاً، وده بيحصل من خلال مساعدة الـ DNS."
tags: ["dns", "network", "ip", "domain"]
updatedAt: "2023-10-24"
featured: false
image: "https://assets.eqraatech.com/guides/dns.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/dns.png" alt="DNS" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ DNS بيحول عنوان الموقع لـ IP Address يقدر الكمبيوتر يفهمه, لكن ايه هو ال DNS أصلاً؟ الكمبيوتر مبيفهمش لغة البشر ومع ذلك لما بتكتبله ([eqraatech.com](https://eqraatech.com/)) بيفتحلك الموقع فعلاً، وده بيحصل من خلال مساعدة الـ DNS.

### ايه هو الـ DNS ؟

الـ DNS هو عبارة عن سيرفر (متقسم شبه دفتر التليفونات) بنخزن فيه اسم الموقع وعنوانه الفعلي ووقت ما بنحب نفتح موقع معين بتحصل الخطوات دي:

1.  بتكتب اسم الـ Website في الـ Browser وتوفيرًا للوقت والجهد بيدور في ال Local Cache الخاصة بيه علي العنوان المقابل للأسم لأنه غالبًا طلبت الصفحة دي قبل كدا
2. لو ملقهاش بيبعت اسم الـ Website للـ DNS Server اللي بيدور في ال Cache بتاعته توفيرًا للوقت والجهد وإذا لقى العنوان المقابل بيبعته للمتصفح
3. لو ملقهوش في الـ Cache بيبتدي يدور عنده في الجدول الكبير على العنوان و بيبعته للـ Browser
4. المتصفح بيستعمل العنوان دا في انه يطلب الـ Website
5. السيرفر المسؤول عن الـ Website بيبعت الصفحات اللي طلبها الموقع وتقدر تتصفحها

الـ 5 خطوات دول بيحصلوا في وقت صغير جدًا فتبان العملية كلها بشكل لحظي (Seamless) كأن الكمبيوتر فهم الـ Request بتاعك لاسم الـ Website مباشرة.


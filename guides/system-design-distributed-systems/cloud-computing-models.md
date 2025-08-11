---
title: "Cloud Computing Models"
description: "Cloud computing models define how services are delivered: IaaS provides infrastructure, PaaS offers platforms for development, and SaaS delivers complete software solutions. This guide breaks down each model with use cases and examples."
excerpt: "فيه بعض الـ Cloud Computing Models الشهيرة اللي بقينا بنشوفها كتير بعد توجه كتير من الشركات والناس لاستعمال الـ Cloud وهي الـ IaaS والـ PaaS والـ SaaS .. طب ايه هي المصطلحات دي ؟."
tags: ["cloud", "microservices", "SaaS", "IaaS", "PaaS", "on-prem", "backend", "distributed-systems", "system-design"]
updatedAt: "2023-11-24"
featured: false
image: "https://assets.eqraatech.com/guides/cloud-computing-models.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/cloud-computing-models.png" alt="Cloud Computing Models" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

فيه بعض الـ Cloud Computing Models الشهيرة اللي بقينا بنشوفها كتير بعد توجه كتير من الشركات والناس لاستعمال الـ Cloud وهي الـ IaaS والـ PaaS والـ SaaS .. طب ايه هي المصطلحات دي ؟ 

### Infrastructure As a Service – IaaS

خلونا نبدأ بالـ IaaS واللي هي اختصار لـ Infrastructure as a Service : 

الـ IaaS هي باختصار انك تأجر أساسيات البنية التحتية اللي انت محتاجها سواء كانت Physical أو Virtualized Resources من خلال الإنترنت، فأنت بتأجر المكونات الرئيسية زي الـ Servers و الـ Storage وأجزاء الـ Network اللي محتاجها.

مثال على ده لو انت عاوز تعمل Web Application ليه وظيفة معينة ، فانت مش محتاج تروح تشتري Server عشان تشغل عليه الـ Web Application ده ، بل أصبح متاح دلوقتي انك من خلال الـ Cloud بشوية ضغطات بسيطة انك تأجر على سبيل المثال الـ Virtual Servers اللي محتاجة تقوم الـ Web Application .. بل وكمان تقدر تتحكم في الـ Scalability بتاعته من حيث انك تزود Resources أو تنقص بناء على حجم الـ Traffic .. وكل ده بشكل Automatic من غير أي عبء أو قلق .. 

### Platform As a Service – PaaS

الـ PaaS واللي هي اختصار لـ Platform as a Service : 

وهي أعلى درجة من الـ IaaS من حيث انها مش بس بتوفر الـ Infrastructure ده كمان تشمل الـ Platform أو الـ Environement اللي هتشتغل عليها واللي بتسمحلك انك تـ Build و تـ Deploy وتـ Manage التطبيقات من غير ما تشغل بالك بالتعقيدات المتأصلة بالـ Infrastructure أو بأي حاجة تانية غير كتابة الـ Code .. 

ومثال على ده نفس الـ Web Application اللي عاوزين نبنيه ، فباستعمال الـ PaaS مش هنفكر في حاجة غير كتابة الـ Code وبس .. مش هنشغل بالنا بالـ Operating System ولا بالـ Server Management وده لانه هيشيل من علينا حمل الـ Hosting والـ Updates والـ Scaling on Demand بناء على الـ Traffic اللي هو شايفها .. 

### Software As a Service – SaaS

الـ SaaS واللي هي اختصار لـ Software as a Service : 

وهي فكرة انك تـ Deliver بعض الـ Software Applications من خلال الانترنت عن طريق الاشتراكات على سبيل المثال فالناس تقدر تشترك وتاخد الـ Software ده كخدمة متكاملة من خلال الانترنت من غير الاحتياج لانهم يشتروا الـ Software ويبدأوا يعملوله Installment على الأجهزة.  

ومثال على ده انك دلوقتي تقدر تشوف الـ Emails بتاعتك كلها من خلال الـ Gmail من غير ما تحتاج تـ Install حاجة على الجهاز بتاعك أو تشوف الـ Documents بتاعتك على الـ Drive , أو الـ Office Productivity Tools زي Microsoft 365 كل دي أمثلة للـ SaaS والـ Service Provider هو اللي بيكون مسئول عن الخدمات دي وعن الـ Updates الخاصة بيها

---

فباختصار : 

- الـ IaaS بتوفرلك الـ Infrastructure Components الأساسية 
- الـ PaaS بيوفرلك Platform عشان الـ Application Development فوق الـ Infrastructure 
- الـ SaaS بيوفرلك الـ Software Application مباشرة من غير ما تحتاج تعمله Installments
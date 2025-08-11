---
title: "REST Vs. GraphQL"
description: "REST uses fixed endpoints to fetch data, while GraphQL lets clients request exactly what they need with a single query. This guide compares flexibility, performance, and use cases to help you choose the right API style."
excerpt: "غالبًا لو عملت APIs قبل كده هتكون استعملت REST وهيبقي عندك زميلك اللي عمال يقولك ما تيجي نشتغل بـ GraphQL زي الناس اللي هناك دي..فتعالى نعرف الفرق بين اثنين من أشهر أنواع الـ API Architectures."
tags: ["RESTful", "GraphQL", "API", "backend", "frontend", "web-development", "http"]
updatedAt: "2023-11-28"
featured: false
image: "https://assets.eqraatech.com/guides/rest-vs-graphql.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/rest-vs-graphql.png" alt="REST Vs. GraphQL" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

غالبًا لو عملت `APIs` قبل كده هتكون استعملت `REST` وهيبقي عندك زميلك اللي عمال يقولك ما تيجي نشتغل بـ `GraphQL` زي الناس اللي هناك دي..فتعالى نعرف الفرق بين اثنين من أشهر أنواع الـ `API Architectures` الأول لازم نعرف أن الاتنين ليهم نفس أساس العمل وهو ان عندي Server ببعتله `HTTP Request` فيجاوب عليا بالمعلومات اللي طلبتها. 👌 

### REST APIs

الـ `REST` بينظم ال `API` علي شكل `Endpoints` وبيقولك تقدر تناديها ب عمليات محددة أشهرهم الـ `GET, POST, PUT, DELETE` وهيرد عليك بـ Standard Response 

### GraphQL

بينما الـ `GraphQL` بيقولك هي `Endpoint` واحدة تقدر تكلمها وتوصف انت عاوز ايه بالظبط من خلال استعمال Query وهيرد عليك بـ Standard Response طب ما والله نفس الشيء ايش استفدت؟ الـ `GraphQL` بيحل مشاكل ظهرت مع استخدامنا للـ `REST` في كل الأنظمة لسهولته والطبيعي انه مش حل واحد يناسب الكل 

### المشاكل اللي بيحلها الـ GraphQL

1. **مشكلة الـ Over-Fetching and Under-Fetching**

الـ `REST` بينظم الـ `Resources` بطريقة ثابتة تناسب العمليات اللى قولنا عليهم فلو انت علي موقع اقرأ تك وطلبت منه قائمة بأسماء الكتاب في المنصة علي الـ Endpoint: `eqraatech/authors` فهيرد عليك بكل المعلومات عنهم مع انك محتاج أساميهم بس ودا اسمه Over Fetching, مشكلته بقي انه بيستهلك الـNetwork Bandwidth في نقل معلومات انت مش محتاجها أصلاً وبيبطأ ال `Endpoint` علي ما تجيب لك كل المعلومات دي 

2. **نسبح في بحر الـ Endpoints** 

كل `Resource` انت بتطلبه بـ `REST` ليه `Endpoint` أو عنوان مختلف, ففي المواقع المعقدة بينتهي بيك الأمر لآلاف من ال `Endpoints` 

3. **الـ Multiple Round-Trips** 

ودي المشكلة اللي خلت Facebook تقدم الـ `GraphQL` كحل لمشكلة الـ Mobile Application بتاعهم لما لقوا ان Screen واحدة بتتحاج أكتر من Call لـ `Endpoints` مختلفة ومع ذلك بتستخدم جزء بسيط جدًا منها, فتخيل انت عشان تشوف بوست باسم واحد صاحبك الابليكيشن كان محتاج يروح يجيب معلوماته كلها عشان يعرض لك الاسم وصورته الشخصية! 

وعشان نحل المشاكل دي قدمنا حل مميز وهو الـ GraphQL واللي بيقسم ال API على شكل `Schema` كبيرة عاملة شبه الـ `Graph` وبيقولك اكتبلي `Query` باللي انت محتاجه بس وانا اجيبهولك, بكدا حلينا مشكلة الـ Over-Fetching وكمان بغض النظر انت محتاج ايه فأنت بتكلم `Endpoint` واحدة وهو بيقدر يوصل للمعلومة من خلال العلاقات بين الـ Resources في الـ `Graph` . 

### طب هل مانقدرش نحقق ده من خلال الـ REST؟

في الواقع هو ممكن ولكنه هيتطلب الكثير من التعقيدات اللي ممكن نكون في غنى عنها والمهارة اللازمة لتحقيق ده ! طبعًا الناس مش هتبطل تستخدم الـ `REST` كون تعلمه أسهل من `GraphQL` وكذلك مناسب لحالات كتير وبالأخص المشاريع الصغيرة والمتوسطة, ولكن ال `GraphQL` كذلك من أنسب الحلول للـ Mobile Applications Backend وبالتأكيد أسرع. بعد ما فهمنا الفرق الجوهري بينهم هنسيبكم في الصورة مع مقارنة تقنية سريعة ما بينهم.
---
title: "HTTP Short Polling vs. Long Polling vs. SSE"
description: "Short polling repeatedly requests updates, long polling holds the request open until data is available, and Server-Sent Events (SSE) push updates from server to client. This guide compares their use cases, efficiency, and real-time capabilities."
excerpt: "انهاردة هنتكلم عن 3 من التقنيات المهمة جدًا واللي مهم جدًا نكون عارفين الفرق بينهم اثناء تصميم Realtime Web Applications والـ 3 تقنيات دول هم الـ Long Polling , Short Polling , Server-Sent Events."
tags: ["realtime", "http", "websocket", "sse", "long-polling", "short-polling", "web-development", "communication"]
updatedAt: "2024-05-24"
featured: false
image: "https://assets.eqraatech.com/guides/http-short-polling-vs-long-polling-vs-sse-in-a-nutshell.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/http-short-polling-vs-long-polling-vs-sse-in-a-nutshell.png" alt="HTTP Short Polling vs. Long Polling vs. SSE" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

انهاردة هنتكلم عن 3 من التقنيات المهمة جدًا واللي مهم جدًا نكون عارفين الفرق بينهم اثناء تصميم Realtime Web Applications والـ 3 تقنيات دول هم الـ Long Polling , Short Polling , Server-Sent Events.

الـ Web Applications في الأساس مبنية على فكرة بسيطة الا وهي الـ Client - Server Model واللي بدوره الـ Client بيبعت Request للـ Server والـ Server يعمل Processing للـ Request ويرجع الـ Response للـ Client.

ومع تطور تطبيقات الـ Web واللي بدورها أصبحنا في احتياج أكتر للتطبيقات اللي متطلبة تحديثات دورية بتحصل بشكل فعلي يعني Realtime Applications , كان لازم نحاول نفكر بشكل مختلف في طريقة تسمحلنا نهيئ من خلالها الـ Client - Server Model اللي متعودين عليه .

فخلونا نشوف مع بعض الـ 3 تقنيات اللي جم عشان يحلوا المشكلة دي , ونتناقش في مميزات وعيوب كل تقنية منهم ونشوف امتة نستعملها.

---

## الـ HTTP Short Polling

الـ HTTP Short Polling فكرته ببساطة عاملة زي اكنك بتكلم واحد صاحبك كل شوية تسأله عن موضوع معين مستني تعرف منه ايه اللي حصل فيه , فكل شوية تكلمه تقوله : هاا ؟ فيه اخبار جديدة ؟ ولا لسه ؟ وانت وحظك يا هيكون فيه اخبار جديدة يا مفيش .. وترجع تكلمه بعد شوية وتكرر نفس الموضوع ..

فالـ Client بيبعت Request للـ Server كل ثانية أو ثانيتين على سبيل المثال بشكل دوري وزي ما شوفنا ممكن الـ Server يرد عليه بـ Response فاضي عادي جدًا لو مفيش أي اخبار جديدة.

---

## الـ HTTP Long Polling

خلونا نرجع لمثال صاحبك اللي بتكلمه عشان تسأله عن موضوع معين , ومستني تعرف ايه اللي حصل فيه , فخلونا نقول ان النتيجة ظهرت , وانت بتكلم صاحبك عاوز تعرف كل شوية هو عمل ايه , شوفنا مع بعض ان في الـ Short Polling كل شوية هتكلمه , وهتساله عن النتيجة .. ولكن ممكن لما تكلمه يكون النتيجة لسه مظهرتش فهو يرد عليك ان لسه مظهرتش ..

وعشان نعالج المشكلة دي في الـ Long Polling كل اللي هنعمله انك بدل ما كل شوية تكلمه وتساله عمل ايه .. هتكلمه مرة واحدة وليكن مكالمة مدتها ٥ دقايق , وتفضل سايب الخط مفتوح وتقوله اول مالنتيجة تظهر طمني , فانت كده بعت كلمته مرة واحدة بس , وهو لما باه عنده اخبار جديدة , بعتلك وقالك الاخبار دي علطول ..

فالـ Client بيبعت Request للـ Server , وهنا باه الفرق ان الـ Request ده هيفضل مفتوح بين الـ Client / Server لحد مالـ Server يبعت تحديثات للـ Client أو ان يحصل Timeout وبالتالي الـ Connection يتقفل.

---

## الـ Server Sent Events

تعالوا نرجع لنفس المثال , بدل ما هتكلم صاحبك تسأله عن النتيجة , هو بنفسه هيبعتلك كل شوية رسالة يقولك فيها الاخبار الجديدة من غير ما تسأله خالص.

فالـ Server بيبعت تحديثات للـ Client بشكل مستمر من غير مالـ Client يبعت يسأله.

---

## في الختام

الـ Short Polling كويس لو مش محتاجين تحديثات لحظية ومش عايزين تعقيد كتير. الـ Long Polling أفضل لو محتاجين تحديثات أسرع لكن في التطبيقات الصغيرة اللي مش متطلبة Scale كبير، والـ Server Sent Events ممتاز لو محتاج تحديثات لحظية.

فكل تقنية من دول ليها استخداماتها ومميزاتها وعيوبها، والاختيار بينهم بيعتمد على الاحتياجات اللي الـ Business بيتطلبها.
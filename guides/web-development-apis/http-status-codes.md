---
title: "HTTP Status Codes"
description: "HTTP status codes are responses from a server that indicate the outcome of a request. Ranging from 1xx (informational) to 5xx (server errors), they help clients understand what happened and how to respond."
excerpt: "أثناء تعاملنا أو تطويرنا للـ API Endpoints بنقابل الـ Http Status Code وهو عبارة عن رقم مكون من 3 خانات:الخانة الأولى بتعبر عن الفئة اللي بينتمي ليها الـ Code."
tags: ["http", "status-codes", "backend", "frontend", "web-development", "restful"]
updatedAt: "2023-11-24"
featured: false
image: "https://assets.eqraatech.com/guides/http-status-codes.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/http-status-codes.png" alt="HTTP Status Codes" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

أثناء تعاملنا أو تطويرنا للـ `API Endpoints` بنقابل الـ `HTTP Status Code` وهو عبارة عن رقم مكون من 3 خانات: الخانة الأولى بتعبر عن الفئة اللي بينتمي ليها الـ Code 

والاثنين الباقيين بيعبروا عن رقم الـ Code بحد ذاته, الـ Code دا الـ Server بيبعته كـ Response علي الـ Request اللي اتبعت من الـ Client عشان يوصل معلومة معينة أو يوضح إن في خطأ معين.

### **أهمية الـ Status Codes**

-  معرفتك بال Status Codes بيساعدك كمبرمج تصمم الـ Endpoints بشكل مضبوط و تتعامل مع كل السيناريوهات المختلفة بأحسن شكل ممكن 
-  و بكونها Standard ففي حالة استخدامنا لـ APIs جاهزة بينبهنا للمشكلة وبيعرفنا ازاي نـ Identify الـ Root Cause بتاعها سواء كان من عندنا أو من عند الـ Server ذات نفسه، وبالتالي بتوفر وقت في الـ Troubleshooting

وكمثال لو انت بتبعت `GET` Request لموقع اقرأ تك عشان تشوف مقال معين والـ Server رد عليك بنجاح فهيبعتلك الكود `200 Status Code: OK` , طيب في حالة كتبت اسم المقال غلط  فهيرجعلك الـ Code 404  المشهور واللي معناه `Not found` لأن مفيش مقال موجود بالاسم دا.

---
### HTTP Status Codes Categories

الـ Status Codes دي مٌقسمة لخمس فئات أساسية بيعتمد عليها كل مبرمج في التصميم أو التعامل مع الـ APIs وهي:

1. **1xx :** ودي غرضها نقل معلومة فقط من الـ Server للـ Client 
2. **2xx:** ودي بتعبر عن تنفيذ الطلب بنجاحولكن بطرق مختلفة على حسب كل Code
3. **3xx :** ودي بتشير ان هيتم توجيه الطلب لعنوان تاني سواء كانت اعادة التوجيه دي دائمة زي ان يكون اسم الموقع اتغير مثلا فيبعتلك 
الـ Code 301 أو 308, أو اعادة توجيه مؤقتة و بعد فترة هترجع الـ Endpoint دي تشتغل تاني بنفس العنوان فيبعتلك السيرفر الـ Code رقم 307 
4. **4xx:** والفئة دي هي الأشهر لأنها بتعبر عن خطأ حصل في الطلب نفسه, الخطأ ممكن يكون على سبيل المثال خطأ في الكتابة أومبعتناش Auth Tokens وإلخ 

وينصح بمراجعة الاكواد في الفئة دي كونها مختلفة عن بعض

5. **5xx:** والفئة دي بيبعتها الـ Server عشان يوضح لك ان المشكلة من عنده 

### بنشوف الـ Status Codes فين ؟

تقدر تشوف الـ Status Codes في أكثر من مكان:

- خانة الـ `Network` اللي بتظهر في الـ `Browser` وأنت بتعمل `Inspect`
- في أي أداة للتعامل مع الـ `APIs` زي `Postman` 
- أثناء استخدامك الـ `Debugger` المرفق بالـ `IDE`

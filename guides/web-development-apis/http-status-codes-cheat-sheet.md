---
title: "HTTP Status Codes Cheat Sheet"
description: "A quick reference to common HTTP status codes—from 200 (OK) and 301 (Redirect) to 404 (Not Found) and 500 (Server Error). Learn what each code means and when to use it."
excerpt: "اتكلمنا قبل كدا عن ايه هي ال Http status codes وليه مهمة في تصميمنا لـ APIs , النهارده هنتكلم عن أشهر 15 status code منهم وعاملين cheat sheet بيهم تقدر تساعدك في انك تفتكر استخداماتهم سريعًا في وقت الشغل."
tags: ["http", "APIs", "backend", "frontend", "web-development", "restful"]
updatedAt: "2024-05-21"
featured: false
image: "https://assets.eqraatech.com/guides/http-status-codes-cheat-sheet.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/http-status-codes-cheat-sheet.png" alt="HTTP Status Codes Cheat Sheet" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

اتكلمنا قبل كدا عن ايه هي ال Http status codes وليه مهمة في تصميمنا لـ APIs , النهارده هنتكلم عن أشهر 15 status code منهم وعاملين cheat sheet بيهم تقدر تساعدك في انك تفتكر استخداماتهم سريعًا في وقت الشغل.

## Success Codes 2xx

**1- 200 OK**

يعبر عن تنفيذ ال request و ايصاله لل client بنجاح 

**2- 201 Created**

يستخدم هذا الكود ليعبر عن إنشاء resource جديد بنجاح 

و يستخدم مع ال `POST` Method ويمكنك أن تعيد معه أيضَا ال resource ID 

**3- 202 Accepted**

يعبر عن قبول الطلب بنجاح ولكنه لا يزال قيد التنفيذ على ال server , ويمكنك أن تستخدم هذا الكود حينما يفوض السيرفر الطلب لسيرفر أخر أو background task قد تستغرق وقتًا  

```
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "message": "Request accepted for processing",
  "status_uri": "/status/123"
}
```

---

## Redirect Codes 3xx

**4- 301 Moved Permanently** 

عندما تقوم بتغيير ال `URL` يمكنك أن تستخدم هذا الكود لتوضح أنه قد تم نقل ال `API` لعنوان جديد بدلاً من العنوان المستخدم في هذا الطلب وفي ال response body تضع العنوان الجديد ليتم استخدامه فيما بعد.

```
HTTP/1.1 301 Moved Permanently
Location: https://example.com/new-location
Content-Type: text/html
```

**5- 302 Found (Moved Temporarily)**

يستخدم هذا الكود في حالة تغيير عنوان ال `API` لعنوان آخر بشكل مؤقت لعمل صيانة أو تحديث لل `API` علي هذا العنوان, يقوم ال client بعمل `redirect` للعنوان المؤقت الجديد و لكن فيما بعد يستطيع العودة لاستخدام ال `URL` القديم.

**6- 304 Not Modified** 

يستخدم هذا الكود في حالة ال conditional `GET` حيث يتم إرسال `if-modified-since` بداخل الـ `request headers` فيجيب الserver بهذا الكود كي يعلم ال client بأن الـ resource لم يتغير ويمكن لل client استخدام النسخة التي لديه في الـ `cache`.

---

## Client Error Codes 4xx

**7- 400 Bad Request** 

يستخدم حينما يحتوي ال  request علي خطأ أو ينقصه `required parameter` فلا يفهم ال server الطلب,  فعندما يطلب ال client مورد معين كمثال معلومات الطالب ولا يرسل اسم الطالب الذي يريد بياناته يمكنك أن ترد باستخدام هذا الكود.

```
HTTP/1.1 400 Bad Request
Content-Type: text/plain
400 Bad Request: Missing required parameter 'username'
```

 **8- 401 Unauthorized** 

تجد هذا الكود حينما يطلب الclient الوصول لل `API`  بدون Authentication أو باستخدام بيانات الـ `authentication` الخاطئة كاسم مستخدم أو كلمة مرور غير صحيحة.

**9- 403 Forbidden** 

يتم استخدامه في حالة طلب ال client الوصول لبيانات أو صفحات ليس لديه صلاحية دخولها, كمحاولة المستخدم العادي الوصول لصفحة الـ Admin.

**10- 404 Not Found** 

يرد ال server بهذا الكود حينما لا يستطيع الوصول إلي الصفحة المطلوبة غالبًا يكون هناك خطأ في كتابة العنوان أو أن الصفحة لم تعد متاحة أو تم نقلها.

**11- 405 Not Allowed** 

يرد الserver  بهذا الكود حينما يرسل ال client طلبًا باستخدام Method غير مسموح بها على هذا العنوان, وكمثال يتم إرسال `POST` Request علي `URL` لا يدعم سوى آل `GET` Method.

**12- 408 Request Time-out** 

يأتي هذا الكود ردًا على أن ال client استهلك كل الوقت المتاح لإتمام ال request فيقوم ال server بإغلاق ال `connection` وإرسال هذا الكود. ال `Timeout` يمكن أن يحدث لأسباب عديدة منها slow network `connection` أو أن ال client لديه performance issues تمنعه من إتمام الطلب في الوقت المحدد.

---

## Server Error Codes 5xx

**13- 500 Internal Server Error** 

يظهر هذا الكود حينما يواجه الserver  مشكلة في الرد علي ال requests, ويحدث ذلك لأسباب عديدة منها ك `unexpected error` في عمل السيرفر ولا يتم توضيح ما هو الخطأ في ال response body لأن ذلك يعد من المعلومات الحساسة عن النظام وقد يؤدي استغلالها لإظهار نقاط ضعف النظام واختراقه.

**14- 502 Bad Gateway** 

كثير من البرمجيات النهارده بتستخدم server as gateway كطبقة أولية قبل ال servers اللي بتنفذ الشغل فعلاً, فال `gateway server` بيكون مسؤول عن forwarding الطلبات بين ال client and real servers وبيرجع لنا الكود دا في حالة وصول `invalid response` من السيرفرات ليه أو مكنش في response أصلاً.

**15- 503 Service not available**

بنستخدم الكود دا في حالة عدم توافر الخدمة على الـ `API` و دا بيكون في حالة أن ال server بيتعامل مع طلبات كتيرة جدًا وحاصله overload أو حاليًا ال server  في حالة صيانة.

---

## في الختام

استخدام الـ `HTTP Status codes` المناسبة في تصميم وبرمجة ال `APIs` بيخلي التعامل معاها بعد كده سلس وبيساعدنا ويسرع من عملية ال debugging لأي مشكلة في استخدامها.

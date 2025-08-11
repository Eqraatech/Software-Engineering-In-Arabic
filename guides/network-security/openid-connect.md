---
title: "OpenID Connect"
description: "OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0, enabling secure user authentication and single sign-on (SSO). This guide explains how OIDC works and why it's widely used in modern web apps."
excerpt: "ال OpenID Connect هو واحد من أشهر طرق الـ User Authentication وأكثرها فعالية ومع ذلك فكرة عمله بسيطة جدًا فورقة وقلم وتعالوا نتعرف إزاي  ال OpenID Connect بيشتغل و إيه الفرق بينه وبين الـ OAuth"
tags: ["OpenID", "OAuth", "security", "authentication", "authroization", "SSO"]
updatedAt: "2024-07-25"
featured: false
image: "https://assets.eqraatech.com/guides/openid-connect.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/openid-connect.png" alt="OpenID Connect" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

ال `OpenID Connect` هو واحد من أشهر طرق الـ User Authentication وأكثرها فعالية ومع ذلك فكرة عمله بسيطة جدًا فورقة وقلم وتعالوا نتعرف إزاي  ال `OpenID Connect` بيشتغل و إيه الفرق بينه وبين الـ `OAuth`

---

## OpenID Connect

الـ `OpenID Connect` هو Identity Layer فوق الـ `OAuth2`. ولكن اللي يهمنا حاليًا عن الـ OAuth إنهUser Authorization Method فتركيزه الأساسي بيكون على "صلاحيات الوصول"  Access Rights ودا عن طريق "تفويض" الـ Third Party App إنه يوصل للمعلومات اللي محتاجها عن ال User أو يدير موارد محددة للـ User بدون معرفة كلمة السر الخاصة بيه ولذلك الـ `OAuth` مش بنستخدمه عشان نعمل Login ولكن بنستعمله للوصول لصلاحيات معينة في موقع تاني.

> الـ `OpenID Connect` هيتيح لينا نفس المميزات ولكن هيحتاج يعرف هوية المستخدم وبياناته الشخصية عشان يتأكد من هويته.

## مقارنة بين الـ OAuth والـ OpenID Connect

|وجه المقارنة|OAuth|OpenID Connect|
|---|---|---|
|الهدف|إدارة صلاحيات الوصول Authorisation|التأكد من هوية المستخدم Authentication|
|علاقتهما ببعض|يمكن استعماله بمفرده|مبني على الـ OAuth|
|ال Tokens المستعملة|Access token, Refresh Token|Access Token, Refresh Token, ID Token|
|الاستخدامات|إعطاء صلاحيات الوصول للموارد|User Authentication, SSO (Single Sign-On)|

---

هنلاحظ دايما واحنا بنعمل تسجيل في أي موقع إن فيه كذا طريقة ممكن من خلال الـ Email والـ Password أو من خلال مثلا نستعمل Google / GitHub / Facebook وده اللي بقينا نشوفه حاليا في أغلب المواقع.

فالطرق التقليدية للـ `User Authentication` اللي بنضطر فيها مثلا ندخل الـ Email والـ Password كان بيوجد طرفين فقط هما الـ User والـ Website والـ Website بيتحقق بنفسه من هوية المستخدم ويستخرج الـ Access والـ `Identity Tokens` بنفسه.

ولكن في حالة استخدام الموقع للـ `OpenID Protocol` فهو بيفوض مهمة التأكد من الهوية دي للـ `OpenID Provider` وكذلك عملية إصدار الـ `Tokens` اللي هيتم استخدامها في عملية التواصل بين الموقع والمستخدم.

الـ `Access Token` وكذلك الـ `Identity Tokens` عادة ما يكونوا في صيغة `JWT Tokens`.

---

الاستخدامات المثلى لكلا من الـ `OpenID Connect` والـ `OAuth` بتكون في حالات التعامل مع Third Party لأنهم يسمحوا للـ Third Party يستخدم جزء من البيانات الخاصة بالمستخدم في موقعك أو إتاحة  `SSO` وهي اختصار لـ Single Sign-On.

لكن استخدام `OpenID Connect` كوسيلة الـ `Authentication` الأساسية والموقع لا يتعامل مع طرف ثالث هيكون إضافة تعقيد بلا هدف!

---


## أمثلة عملية على OpenID Connect

- **الـ Google Sign-In**: يتيح للمستخدمين تسجيل الدخول إلى تطبيقات الطرف الثالث باستخدام حساب Google الخاص بهم.
- **الـ Microsoft Azure AD**: يوفر تسجيل دخول موحد وخدمات مصادقة للتطبيقات التي تستخدم خدمات Azure.
- **الـ GitHub OAuth**: يتيح للمطورين تسجيل الدخول إلى تطبيقات وخدمات مختلفة باستخدام حساب GitHub الخاص بهم.
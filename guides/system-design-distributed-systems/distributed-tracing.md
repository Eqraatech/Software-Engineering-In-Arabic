---
title: "Distributed Tracing"
description: "Distributed tracing tracks requests across microservices, helping you pinpoint performance issues and understand system behavior end-to-end. This guide explains how it works and why it’s key for observability."
excerpt: "الهدف الأساسي من الـ Distributed Tracing هو توفير رؤية واضحة لرحلة الطلب (Request) عشان لو فيه مشاكل أو بطء في الأداء نقدر نحدد مصدرها. بنقدر نعرف فين بالتحديد الـ bottleneck أو الخدمة اللي فيها مشكلة."
tags: ["tracing", "monitoring", "observability", "metrics", "distributed-systems", "system-design"]
updatedAt: "2024-10-25"
featured: false
image: "https://assets.eqraatech.com/guides/distributed-tracing.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/distributed-tracing.png" alt="Distributed Tracing" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

في التطبيقات الكبيرة وخصوصًا اللي بتتعامل مع المايكروسيرفسز (`Microservices`)، بيبقى عندنا الـ System مُقسم لمجموعة خدمات (Services) صغيرة بتشتغل مع بعض عشان تنفذ المهام.

ولما بيجي طلب (`Request`)، بيعدي من خلال كذا خدمة، وأحياناً ممكن يعدي على سيرفرات مختلفة. هنا بيجي دور الـ `Distributed Tracing`، اللي هو عملية تتبع الطلب عبر النظام كله عشان نعرف مشواره من أول ما وصل لحد ما خلص.

والهدف الأساسي من الـ Distributed Tracing هو توفير رؤية واضحة لرحلة الطلب (`Request`) عشان لو فيه مشاكل أو بطء في الأداء نقدر نحدد مصدرها. بنقدر نعرف فين بالتحديد الـ bottleneck أو الخدمة اللي فيها مشكلة. الفكرة ببساطة إننا بنخلي النظام زي خريطة واضحة للـ `flow` بتاع الطلبات عشان نقدر نفهم كل خطوة.

وعشان نفهم اكتر رحلة الـ `Request Flow` ونتعرف ازاي الـ Distributed Tracing بيتم محتاجين نتعرف اصلا على الـ `TraceID`.

---

## TraceID

  
وقت ما بتعمل Order من تطبيق توصيل للأكل الطلب بتاعك بيمر ب Services كتير من اول تحديد المطاعم المتاحة لحساب وقت التوصل و إرسال الطلبات لعامل التوصيل و خدمة تتبع الطلب إلخ…  
  
فالـ Trace Id بيكون " مُعرف التتبع " بيكون مع الطلب و هو رايح لكل Service من دي عشان يميز الـ Order دا عن غيره و نعرف نتتبع مساره من أول خدمة لاخر خدمة.

ودا لأن كل Service بتعامل الـ Order كـ Request جديد وممكن متكونش عارفة حاجة عن الـ Service اللي قبلها او اللي بعدها.

> الـ `TraceID` هو حاجة أساسية جداً في عملية التتبع دي. ده عبارة عن `Identifier` (معرف) بيبقى مميز لكل طلب، بيتولد مع أول خطوة بيعملها الطلب في النظام. الهدف منه إنه يخلي كل خطوة أو خدمة تشتغل مع الطلب ده تقدر تتعرف عليه.

وقت الـ `Monitoring` نقدر نستخدم الـ `TraceID` عشان نحصل علي ال `Logs` او الـ `Errors` المرتبطة بالطلب دا من كل الخدمات في نظامنا في مكان واحد.

---

## أهم الأدوات المستخدمة لتنفيذ الـ Tracing

يوجد أدوات كثيرة متاحة لتوليد و دمج الـ TraceID في نظامك منها المفتوح المصدر أو المدفوع و منها ما يوفر خدمات Monitoring إضافية من أمثلة هذه الأدوات:

- Open telemetry
- Jaeger
- Google cloud trace
- Datadog
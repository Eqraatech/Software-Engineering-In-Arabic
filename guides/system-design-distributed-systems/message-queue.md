---
title: "Message Queue"
description: "A message queue enables asynchronous communication between services by sending, storing, and delivering messages reliably. This guide explains how it decouples systems and improves scalability and fault tolerance."
excerpt: "الـ Message Queue هو عبارة عن وسيلة تواصل بين الـ Services وبعضها البعض فيقدروا يتبادلوا المعلومات بشكل Asynchronous وعشان كده النوع ده من التواصل بنسميه Asynchronous Communication."
tags: ["message-queue", "kafka", "rabitmq", "backend", "distributed-systems", "system-design"]
updatedAt: "2024-01-26"
featured: false
image: "https://assets.eqraatech.com/guides/message-queue.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/message-queue.png" alt="Message Queues" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

تخيلوا ان عندنا مطعم وشغال فيه اكتر من طباخ بيعملوا اكلات كتيرة ومتنوعة في نفس الوقت, وكل واحد شغال على الطبق اللي بيجهزه, فعشان الطباخين دول يبقى فيه بينهم تناسق وترتيب على حسب الاوردرات لازم يكون فيه نظام بيحققلهم ده فهم بيعملوا ايه ؟

بيحطوا الاوردرات كلها ورا بعض في شكل طابور، وكل طباخ بيلاقي اوردر متاح بياخد الاوردر اللي عليه الدور. 

**هو ده ببساطة الـ Message Queue** 

---

## Message Queue

الـ Message Queue هو عبارة عن وسيلة تواصل بين الـ Services وبعضها البعض فيقدروا يتبادلوا المعلومات بشكل `Asynchronous` وعشان كده النوع ده من التواصل بنسميه `Asynchronous` Communication.

**طب يعني ايه Async ؟** 

>💡الـ `Asynchronous` Communication معناه ان الطرفين مش بيتواصلوا مع بعض In Real Time ومش محتاجين الاجابة تحصل بشكل Immediate زي الـ MailBox 

فالـ Message Queue بيكون عبارة عن وسيط بين طرفين وبيضمنلك ان الرسالة هيتم استلامها من طرف واستقبالها من الطرف الآخر.

---

## المكونات الأساسية لأي Message Queue

1. **الـ Producer :** وده دوره انه يـ `Create` ويبعت الـ `Message` اللي عاوزة تتبعت للـ Message Queue 
2. **الـ Message :** ودي الحاجة اللي الـ Producer بيبعتها للـ Message Queue عشان الـ Consumer يعملها Processing وممكن يكون ليها اكتر من شكل زي `Data` او `Event` حصل أو `Task` وكلهم عبارة عن `Message` في الأول والآخر .. 
3. **الـ Message Queue :** وده المكان اللي بتتخزن فيه الـ `Message` لحد ما يتم استلامها وعمل Processing عليها 
4. **الـ Consumer :** وده دوره انه يستقبل الـ `Message` اللي اتبعتت ويعملها Processing بالشكل المطلوب

---

## فايدة الـ Message Queue ؟

1. **الـ Decoupling**: وده معناه اني مبخليش الـ Components عندي في الـ System معتمدة على بعضها , ولكن بخليها مستقلة بذاتها وده من خلال اني بفصل الاعتمادية دي واخليهم مثلا يتواصلوا من خلال الـ Message Queue

2. **الـ Scalability**: فهي بتساعد بشكل كبير في الـ Horizontal Scalability وده من خلال ان لو عندي Workload كبير زي مثال المطعم فانا ممكن اعمل Scale للطباخين ,, وبالتالي يبقى عندي اكتر من طباخ بياخدوا الـ Orders ويعملوا ليها Processing فازود الـ Throughput بتاعي واقدر اتعامل مع عدد كبير من الـ Orders 

3. **الـ Resiliency**: وده معناه ان لو حصل عندي اي خطأ او مشكلة فانا ممكن اعتمد على الـ Message Queue في اني احتفظ بالـ `Message` وارجع اعملها Processing مرة تانية , تخيلوا مثلا واحد من الطباخين وهو بياخد الاوردر جاتله مكالمة طارئة .. فهو ممكن يخلصها ويرجع يكمل الاوردر اللي بيعمله تاني .. حتى لو هيبدا فيها من جديد طالما السلوك ده مقبول بالنسبالي .. او ممكن يسيبه تاني لحد تاني من الطباخين ياخده ويشتغل عليه .. 

---

## أشهر تطبيقات الـ Message Queue 

- RabbitMQ
- Kafka
- Amazon SQS
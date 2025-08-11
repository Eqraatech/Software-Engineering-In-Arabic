---
title: "Protocol Buffer (ProtoBuf)"
description: "Protocol Buffers is a language-neutral, platform-neutral format for serializing structured data. This guide explains how ProtoBuf enables efficient communication between services with compact, fast binary messages."
excerpt: "اختيار الـ Format المناسب للـ Data Serialization أصبح موضوع حيوي حاليًا خصوصًا في التعامل مع الأنظمة اللي بتتميز بكونها Large-Scale واللي الأداء فيها حيوي ومهم جدًا. ومن أشهر الـ Formats اللي فضلت موجودة على مر السنين"
tags: ["ProtoBuf", "microservices", "network", "backend", "HTTP2", "distributed-systems", "system-design"]
updatedAt: "2024-09-17"
featured: false
image: "https://assets.eqraatech.com/guides/protocol-buffer-protobuf.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/protocol-buffer-protobuf.png" alt="Protocol Buffer (ProtoBuf)" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

اختيار الـ `Format` المناسب للـ `Data Serialization` أصبح موضوع حيوي حاليًا خصوصًا في التعامل مع الأنظمة اللي بتتميز بكونها Large-Scale واللي الأداء فيها حيوي ومهم جدًا. ومن أشهر الـ `Formats` اللي فضلت موجودة على مر السنين هو الـ `JSON` وهو اختصار لـ `JavaScript Object Notation`.

ولكن بسبب احتياج الـ Large-Scale Systems للأداء العالي والـ `Bandwidth` القليلية ظهر `Format` تاني ألا وهو الـ `ProtoBuf`.

طب ايه هو الـ `ProtoBuf` وايه سبب ظهوره ؟ وايه اللي بيميزه عن الـ `JSON` وليه بنختاره في الـ Large-Scale Systems ، ده اللي هنعرفه انهاردة فورقة وقلم وتعالوا نتكلم عن الـ `ProtoBuf` vs `JSON` 🚀

---

## Protocol Buffer (ProtoBuf)

الـ Protocol Buffer أو الـ `ProtoBuf` هو طريقة طورتها Google عشان تعمل بيها `Serialization` للـ Structured Data. بالإضافة لإنه مش معتمد على لغة برمجة بعينها أو Platform بعينه.

وممكن يتم الاعتماد عليه في الـ Communication بين الـ Services وبعضها أو في أي موقف احتجنا فيه إننا نخزن بيانات أو نتبادل بيانات تكون Structured.

بالإضافة لإنه كمان نظام مفتوح المصدر (open-source).

---

## JSON vs. ProtoBuf

الـ JSON معروف عند كتير من المطورين، وبيستخدموه في كتير من التطبيقات عشان ينقلوا البيانات ما بين الـ Client والـ Server. **لكن فيه فروق مهمة بينه وبين الـ ProtoBuf واللي في الأساس أدت لظهوره**:

1. **الحجم:** الـ ProtoBuf بيـ `Serialize` البيانات بطريقة مدمجة أكتر من الـ `JSON`.
2. **الأداء:** الـ ProtoBuf أسرع في قراءة وكتابة البيانات مقارنة بـ `JSON`. وده لإنه بيخزن البيانات على هيئة Binary مش نصوص `Texts` زي `JSON`.
3. **قابلية التوسع أو ما يعرف بالـ Extensibility:** الـ `ProtoBuf` بيتيح ليك تضيف أو تعدل في البيانات اللي بتعملها Serialize بدون ما تتسبب في مشاكل للنسخ القديمة. يعني بيحقق الـ Backward Compatibility على عكس JSON مفيهوش نفس المرونة دي.
4. **سهولة القراءة Human-Readability:** الـ `JSON` بيتميز إنه مقروء للإنسان بشكل مباشر، يعني تقدر تشوف البيانات وتفهمها بسهولة. على العكس، الـ ProtoBuf بيخزن البيانات في هيئة Binary مش مفهومة للبشر.
---

## How ProtoBuf Works

أول حاجة، بنبدأ إننا نكتب ملف `.proto` وده ملف بنحدد فيه شكل البيانات اللي عاوزينها. الملف ده هو اللي هيكون المرجع واللي منه هنـ Create الـ Classes اللي هتستخدمها في الكود بتاعنا.

**مثال بسيط لملف .proto:**

<!-- Basic Message -->
```proto
syntax = "proto3";

message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
}
```

<!-- JSON Equivalent -->
```json
{
  "name": "Ahmed Ali",
  "id": 12345,
  "email": "ahmed@example.com"
}
```

الملف ده بيقول ان عندي رسالة اسمها `Person` فيها 3 Fields وهم: `name` و `id` و `email`. لما نيجي نعمل Serialization للبيانات دي بالـ ProtoBuf، هيتم تحويل الرسالة دي لشيء بسيط جدًا سواءًا في التخزين في قاعدة بيانات أو من خلال اننا نبعتها بين الـ Services وبعضهم.
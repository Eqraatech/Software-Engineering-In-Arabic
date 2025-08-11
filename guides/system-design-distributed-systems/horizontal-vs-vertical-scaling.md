---
title: "Horizontal vs. Vertical Scaling"
description: "Horizontal scaling adds more machines to handle increased load, while vertical scaling upgrades the resources (CPU, RAM) of a single machine. This guide explains the trade-offs, use cases, and which approach suits different system needs."
excerpt: "التوسع أو ما يعرف بالـ Scaling هو ببساطة قدرة النظام على تحمل أي حمل زائد أثناء استخدامه، فمثلا: لو فيه نظام بيخدم 20 مستخدم في نفس الوقت، وفجأة العدد ارتفع لـ2000 مستخدم مرة واحدة والنظام قدر يتعامل مع الزيادة دي ويخدمهم من غير أعطال."
tags: ["scaling", "microservices", "backend", "distributed-systems", "system-design"]
updatedAt: "2023-10-23"
featured: false
image: "https://assets.eqraatech.com/guides/horizontal-vs-vertical-scaling.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/horizontal-vs-vertical-scaling.png" alt="Horizontal vs. Vertical Scaling" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

التوسع أو ما يعرف بالـ Scaling هو ببساطة قدرة النظام على تحمل أي حمل زائد أثناء استخدامه، فمثلا:  
**لو فيه نظام بيخدم 20 مستخدم في نفس الوقت، وفجأة العدد ارتفع لـ2000 مستخدم مرة واحدة والنظام قدر يتعامل مع الزيادة دي ويخدمهم من غير أعطال أو مشاكل، فده معناه إن النظام Scalable** 

### إزاي نحقق الـ Scaling؟ 

 في طريقتين لتحقيق الـ Scaling في النظام اللي بنحاول نبنيه: 

1.  التوسع الرأسي أو ما يعرف بالـ Vertical Scaling أو Scaling-Up
2.  التوسع الأفقي أو ما يعرف بالـ Horizontal Scaling أو Scaling-Out

---
###  ايه هو الـ Vertical Scaling؟ 

هو زيادة قدرة وإمكانية النظام الواحد من خلال زيادة عدد الـ Resources في الـ Machine اللي بيكون فيها الـ Server، أو استبدال الـ Machine بواحدة تانية أقوى منها عشان تتحمل الحمل الزائد.  
  
وده بيتم بأكثر من شكل زي:

1. زيادة الـ CPU/RAM عشان التطبيق يتحمل خدمة عدد أكبر من المستخدمين.
2.  زيادة الـ Storage عشان قاعدة البيانات تقدر تخزن عدد أكبر من البيانات.

---
###  ايه هو الـ Horizontal Scaling؟ 

هو زيادة عدد الـ Nodes أو الـ Machines اللي بيكون فيها الـ Server، فبدل ما يكون فيه Node واحدة بس نعتمد عليها، بنعتمد على أكثر من Node.  
  
وده بيتم بأكثر من شكل زي:

1.  زيادة عدد الـNodes فلو كانت الـNode الواحدة قادرة على خدمة 20 مستخدم في وقت واحد، هيكون عندنا No.Nodes * 20 مستخدم نقدر نخدمهم في وقت واحد.
2.  زيادة عدد الـNodes وزيادة سعة التخزين، فلو كانت قاعدة البيانات الواحدة تقدر تخزن 1TB، فنقدر دلوقتي نخزن No.Nodes * 1TB من البيانات.

**تحقيق الـ Scalability مش حاجة سهلة زي ما يبان ولكن الموضوع محتاج لدراسة وفهم لطبيعة النظام والمتطلبات اللي مفروض يحققها في نطاق العمل أو ما يعرف بالـ Business Domain**
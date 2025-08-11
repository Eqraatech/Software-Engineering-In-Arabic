---
title: "CAP Theorem"
description: "The CAP Theorem states that in a distributed system, you can only guarantee two out of three: Consistency, Availability, and Partition Tolerance. This guide explains each property and the trade-offs system designers must make."
excerpt: "الـCAP Theorem واحدة من أهم النظريات الأساسية والمهمة في علوم الحاسب عامةً وفي النظم الموزعة خاصةً وبتنص على: إن في النظم الموزعة ما ينفعش الـSystem يوفر إلا ضمانين أو خاصيتين اتنين بس في نفس ذات الوقت."
tags: ["api-gateway", "microservices", "network", "backend", "load-balancer", "distributed-systems", "system-design"]
updatedAt: "2023-10-23"
featured: false
image: "https://assets.eqraatech.com/guides/cap-theorem.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/cap-theorem.png" alt="CAP Theorem" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـCAP Theorem واحدة من أهم النظريات الأساسية والمهمة في علوم الحاسب عامةً وفي النظم الموزعة خاصةً وبتنص على:  
إن في النظم الموزعة ما ينفعش الـSystem يوفر إلا ضمانين أو خاصيتين اتنين بس في نفس ذات الوقت. 

### ايه اللي بتمثله الـ CAP والضمانات اللي بتقدمها ؟

الـ C بتمثل الـ **Consistency**، والـ A بتمثل الـ **Availability**، والـ P بتمثل الـ **Partition Tolerance**..  
  
طب كل واحدة من دول معناها إيه؟ 

1. الـ **Consistency**: معناها إن كل الـClients يقدروا يشوفوا نفس البيانات في أي وقت من غير أي اختلافات، فبنقول على البيانات أنها متسقة أو Consistent
2. الـ **Availability**: معناها إن كل Request الـSystem هيستقبله مفروض يكون ليه Response والنظام يقدر يكمل شغله من غير مشاكل حتى في وجود Nodes أو Servers واقعة وفيها مشاكل.
3. الـ **Partition Tolerance**: معناه قدرة الـSystem على إنه يكمل شغله بدون مشاكل حتى في وجود مشاكل في الـNetwork Communication بين الـNodes وبعضها.

وبما إن النظرية دي بتنص على وجود ضمانين اتنين بس يتحققوا في نفس الوقت فممكن يكون عندنا الـSystem حاجة من (3):

### Consistency & Partition Tolerance

 الـCP وده معناه إن في وجود الـParition Tolerance، الـSystem محتاج يضحي بالـAvailbility في سبيل توفر الـConsistency بين البيانات وبعضها.  
  
وممكن نشوف مثال على ده مثلا في البنوك، اللي بنسبة كبيرة بتحتاج إن البيانات تكون متسقة ومفيهاش أي اختلاف في أي وقت الـClient هيطلب فيه ده، وده لإن الـClient مش هيحب إنه كل شوية يشوف حسابه فيه أرقام مختلفة ومتغيرة..

### Availability & Partition Tolerance

 الـAP وده معناه إن في وجود الـParition Tolerance، الـSystem محتاج يضحي بالـConsistency في سبيل توفر الـAvailability وده معناه إن مش لازم البيانات تكون متسقة في نفس ذات الوقت ممكن يكون فيه تغيير وتأخير لحد ما يحصل الاتساق وده يسمى بالـEventual Consistency، بس الأهم إن أي Request الـClient هيعمله لازم النظام يفضل شغال وبيرد عليه بدون مشاكل.  
  
وممكن نشوف مثال على ده في مواقع التواصل الإجتماعي، فالـClient هيسمح بوجود تأخير على ما يحصل إن البيانات تبقى موحدة أو مستقرة زي عدد الـLikes والـNewsfeed Updates بس مش هيبقى مبسوط إن الـSystem مش متاح اصلًا.

### Consistency & Availability

 الـCA وده معناه إن الـSystem هيضحي بالـPartition Tolerance في سبيل تحقيق الـConsistency والـAvailability لكن ده غير منطقي في النظم الموزعة لإن مستحيل يكون فيه نظام متأكد بنسبة ١٠٠٪ من عدم غياب مشاكل في الـNetwork لإي سبب، وصعب تحقيق الـAvailability والـConsistency في نفس الوقت مع وجود Partition Tolerance..  
  
وممكن نشوف مثال على ده في الـRDBMS الـSingle Node اللي مش بتحتاج لـNetwork Communication مع Nodes تانية.  
  
وعشان كده ممكن نغير في نص النظرية **ونقول إن في حالة وجود Partition Tolerance** إما إن النظام يفضل الـConsistency أو الـAvailability كـTrade-Offs ويضحي بالتانية.  
  
**و وجب التنويه برضو إن تحقيق الـAvailability أو الـConsistency بنسبة ١٠٠٪ مستحيل، وإن النظرية دي بتفيدنا في التفكير بشكل مختلف أثناء تصميم النظام وإننا نسأل نفسنا إيه الـTrade-Offs اللي بنتعامل معاها.**
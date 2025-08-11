---
title: "Java Exceptions Cheatsheet"
description: "A quick guide to Java’s core collection types—List, Set, Map, Queue—and their key implementations. Perfect for understanding usage, performance, and choosing the right data structure."
excerpt: "الـ Exception Handling من الأساسيات في تعلم أي لغة ، وده لانك وانت شغال أكيد هيقابلك سيناريوهات هتضطر تـ Throw فيها Exceptions ، واحيانًا هتلاقيهم في وشك وأنت مش عارف ليه ، فلازم تكون فاهمهم كويس وعارف تتعامل معاهم ازاي."
tags: ["java", "exceptions", "oop", "programming-language", "best-practices"]
updatedAt: "2024-08-03"
featured: false
image: "https://assets.eqraatech.com/guides/java-exceptions-cheatsheet.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/java-exceptions-cheatsheet.png" alt="Java Exceptions Cheatsheet" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ Exception Handling من الأساسيات في تعلم أي لغة ، وده لانك وانت شغال أكيد هيقابلك سيناريوهات هتضطر تـ `Throw` فيها `Exceptions` ، واحيانًا هتلاقيهم في وشك وأنت مش عارف ليه ، فلازم تكون فاهمهم كويس وعارف تتعامل معاهم ازاي.

فورقة وقلم وتعالوا نتعرف على الـ `Java Exceptions` و إزاي بنعملها Handeling بطريقة سليمة.

---

الكود عبارة عن "سيناريو" بينفذه الكمبيوتر وفي أي سيناريو ممكن تحصل مشكلة أو حدث غير متوقع ودا بيكون استثناء للسيناريو اللي يعرفه.

في الحالة دي الكمبيوتر مش هيعرف يتصرف وهيعمل Program Crash وعشان نتفادى دا لازم نعلم الكمبيوتر إزاي يتعامل مع الاستثناءات دي.

**ال Exceptions أو الاستثناءات دي في ال Java بتنقسم ل 3 أنواع:**

1. **الـ Checked Exceptions** 

النوع دا من ال `Exceptions` بيتم فحصه والتأكد من عدم وجوده في ال `Compile time` وهنا ال `Java` Compiler  بيديك تحذير من وجوده وبيقولك اعمله `handle` بدل ما يوقعلنا البرنامج. ومن أشهرها الـ `IOException`, `SQLException`

2. **الـ Unchecked Exceptions** 

ودي `Exceptions` أسوء من ال `checked` لسببين:

- مبنعرفش بوجودها غير في وقت تشغيل البرنامج فعلاً ولذلك بتكون كلها من نوع `Runtime Exceptions` 
- ال `Exceptions` دي بتكون نتيجة لأخطاء برمجية, يعني المبرمج كان ممكن يتفادها ويحلها لو بستخدم Good Programming Practices بس دا محصلش والجافا مشهورة بال `Null pointer exception` الناتج من محاولة تنفيذ عملية علي `Object` غير موجود, واللي ببساطة بيتحل لو المبرمج عمل تأكيد على وجود ال object قبل ما ينفذ عليه أي عملية هتؤدي لهذا ال `Exception`.

**ومن أشهرهم كذلك:**

- الـ `ArithmeticException`
- الـ `IllegalArgumentException` 
- الـ `IndexOutOfBoundsExceptions`  
- الـ Errors 

هنا ال Errors بتشير للأخطاء اللي بتحصل خارج نطاق البرنامج بتاعنا ولكنها بتؤدي في النهاية انه يحصله crash و من أشهرها ال `Out of memory Exception` و `Stack overflow Exception` 

---

## Exception Class Hierarchy 

مننساش إن ال `Java` هي `OOP Language` ولذلك كل ال `Exceptions` بتورث من ال `Throwable Interface` ومن هنا بتيجي كلمة "رمي اكسبشن" ال `Interface` دي بتضمن إن كل `Exception` يبقي عنده `Error Message` و `Stack Track`

ال `Throwable Interface` بينفذها 2 classes وهما ال `Exceptions` ودا اللي بيعبر عن ال `Checked and Unchecked classes` و ال `Error Class` اللي اتكلمنا عنه.

**وكل الـ Exceptions اللي بنستخدمها بتورث من واحد من الاتنين دول.**

و طبعًا تقدروا تكتبوا **Customized Exceptions** بتحل مشاكل مخصصة في المشاريع بتاعتكم.
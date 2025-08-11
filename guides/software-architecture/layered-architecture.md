---
title: "Layered Architecture"
description: "Layered Architecture organizes software into logical layers—like presentation, business, and data access—to separate concerns and improve maintainability. This guide explains each layer's role and how they interact."
excerpt: "الـ Layered Architecture طريقة شائعة جدًا بنستخدمها علشان نرتب بيها الكود في أي software system. الفكرة ببساطة إننا بنقسم المشروع بتاعنا لكذا layer، وكل layer بيكون ليه وظيفة محددة."
tags: ["layered-architecture", "3-tier", "software-architecture", "backend", "dependency-inversion", "domain"]
updatedAt: "2025-04-18"
featured: true
image: "https://assets.eqraatech.com/guides/layered-architecture.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/layered-architecture.png" alt="Layered Architecture" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ Layered Architecture طريقة شائعة جدًا بنستخدمها علشان نرتب بيها الكود في أي software system. الفكرة ببساطة إننا بنقسم المشروع بتاعنا لكذا layer، وكل layer بيكون ليه وظيفة محددة، ومش بيكلم غير layer اللي تحته.

الـ layers دي ممكن تكون 1 أو 2 أو 3 ، فعدد الـ Layers مش بيفرق ولكن كلهم بيتبعوا نفس الـ Rule الا وهو ان كل Layer بتعتمد على الـ Layer اللي تحتها.

يعني بكل بساطة بنفصل المسئوليات بحيث كل layer طبقة مسئولة عن حاجة واحدة، وده بيسهّل علينا نشتغل على كل جزء من السيستم بأريحية ومن غير مانكون خايفين إننا نأثر بالسلب على باقي الأجزاء.

---

## مميزات الـ Layered Architecture

في كذا ميزة للـ Layered Architecture:

1. **الـ Code هيبقى أسهل في الفهم**: لما كل حاجة تبقى في مكانها، تقدر بسهولة تعرف فين الـ business logic، فين الـ database access، وفين الـ UI.
2. **الـ Testability**: تقدر تختبر كل layer لوحده. يعني مثلًا تقدر تعمل unit testing للـ service layer اللي هيكون فيها الـ Business Logic بتاعك من غير ما تكون مرتبط بالـ Database.
3. **الـ Maintainability وقابلية التعديل والتوسع**: لو عايز تغيّر طريقة حفظ الداتا، ممكن تشتغل بس في الـ data access layer من غير ما تلمس باقي السيستم وده هيديق ثقة وأنت شغال.
4. **الإنتاجية كـ Team**: كل حد ممكن يشتغل على layer معينة في الـ Project من غير ما يأثر على باقي شغل الناس التانية خصوصًا لو بيشتغلوا على Features مختلفة.

---

## أشهر Layers في أي Layered Architecture

الترتيب بيختلف من مشروع للتاني، بس غالبًا هنلاقي أغلب الحاجات دي:

1. **الـ Presentation Layer (أو UI Layer)**  
    ودي اللي بتتعامل مع اليوزر، سواء كانت Web UI أو Mobile أو حتى Command Line. وفي حالة الـ Backend الـ Controller بتمثلنا احنا الـ UI لانها بتـ Represent البيانات للـ Frontend على هيئة `JSON` أو أي Data Format محددينه.
2. **الـ Application Layer / Service Layer**  
    فيها الـ business logic بتاعنا، يعني القواعد اللي السيستم ماشي بيها. وكذلك ممكن تتضمن وجود الـ Domain / Model Layer والـ Entities
3. **الـ Persistence / Data Access Layer**  
    ودي اللي بتتعامل مع الـ database أو أي data source تاني أو حتى `APIs` أو Web Services.

---

## مثال بسيط

لو عندنا system بيحجز مواعيد لدكتور على سبيل المثال:

- فالـ UI بياخد من الـ user التاريخ اللي عايز يحجز فيه الميعاد.
- الـ Business Layer فيها الـ Logic واللي من خلاله بتشوف لو التاريخ ده الدكتور متاح فيه ولا لأ.
- الـ Data Access Layer بتشوف في الـ database المواعيد المحجوزة فعليًا والاتاحية بتاعة الدكتور وبعدين تخزن الميعاد بتاع الحجز لو فيه اتاحة.

---

## ليه الناس بتقول إن Layered Architecture “قديم” أو “مش أفضل اختيار”؟

الـ Layered Architecture فعلاً كان هو **الـ default** من زمان، خصوصًا في التطبيقات الكبيرة زي اللي كانت بتتبني بالـ `Java EE` أو `.NET`، لأنه بسيط وسهل يتفهم. بس مع الوقت، ظهرت مشاكل معينة خلت الناس تدور على بدائل أفضل، زي `Clean، Onion، وHexagonal`.

### طيب إيه مشاكله؟

رغم المميزات اللي قولناها، لكن فيه شوية مشاكل بتبان في الـ real world:

1. **مبدأ الـ Dependency Inversion:** في الـ layered architecture، الطبقات اللي فوق (UI مثلاً) بتعتمد بشكل مباشر على اللي تحتها (Services → Repositories → Database). وده بيخلي الـ business logic مربوط بحاجة زي SQL أو حتى ORM، وده بيصعّب التستينج وإعادة الاستخدام الا لو اضطرينا اننا نستعمل في الوقت ده الـ **Dependency Inversion**. عشان نكسر الاعتمادية دي.
2. **صعوبة التغيير**: لما تحب تغيّر حاجة في النص (مثلاً تعدل الـ business rules)، ساعات بتضطر تلمس كذا layer علشان تعمل التغيير ده فبنعدي برحلة طويلة.
3. **مش بيعبر كويس عن الـ Domain**: يعني لو شغال على مشروع فيه `domain` معقد (زي البنوك أو الأنظمة الطبية)، الـ layered approach مش بيعكس الـ domain نفسه ولكن بيعبر أكتر عن الجزء الـ Technical بتاع الكود.
4. **الـ Coupling عالي بين الـ layers**: طبقة الـ services ممكن تبقى مربوطة بـ database entities مباشرة، وده بيخلي في tight coupling وصعب التعامل أو التغيير في المستقبل.

---

## في الختام

مش كل المشاريع معقدة أو فيها domain rules تقيلة تستاهل architecture معقد زي Clean Architecture. فببساطة:

- لو السيستم عبارة عن `CRUD` شغال على `database`، والـ business logic بسيط، فالـ layered architecture ممكن يكون كفاية وفعال جدًا.
- ولو التيم لسه جديد أو عايز يبني حاجة بسرعة، الـ layered بيكون حل واقعي بدل ما تدخلهم في abstraction وتقسيمات معقدة من الأول.
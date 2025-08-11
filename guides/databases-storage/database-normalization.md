---
title: "Database Normalization"
description: "Database normalization organizes data into structured tables to reduce redundancy and improve integrity. This guide explains normal forms (1NF to 3NF) and how they help design efficient relational databases."
excerpt: "لما تيجي تصمّم قاعدة بيانات، الهدف مش بس تخزن البيانات، لكن تخزنها بشكل منظم وفعّال. هنا بييجي دور Database Normalization — وهي عملية ترتيب البيانات داخل الجداول لتقليل التكرار، وتجنب التعارض، وتحسين الاتساق."
tags: ["normalization", "database", "consistency", "backend" , "performance"]
updatedAt: "2024-04-14"
featured: false
image: "https://assets.eqraatech.com/guides/database-normalization.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/database-normalization.png" alt="Database Normalization" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

أما بنروح المكتبة بنلاقي الكتب والروايات والمراجع مقسمة بشكل كويس يسهل للناس انها تروح تجيب اللي هي عاوزاه من غير ما تبذل مجهود كبير , نفس الكلام في الدولاب اما بتكون الهدوم مترتبة ده هيسهل عليك انك تلاقي اللبس اللي انت محتاجه بسهولة. 

وهي دي ببساطة فكرة الـ **Database Normalization** هي عملية الـ **Categorization** أو الفصل اللي بنعمله بحيث نخلي كل جزء مترتب في مكان لوحده. 

---

تعالوا نتخيل ان عندنا بيانات مجموعة من الطلاب , بس بيانات الطلاب دي كلها موجودة في Table واحد , الـ Table ده يشتمل على ايه ؟ يشتمل على كل حاجة خاصة بالطالب (بيانات الطالب - الكورسات اللي بيشوفها - درجاته - المدرسين اللي بيشرحوله) الخ.. 

اللي عندنا ده دلوقتي اسمه **Database De-Normalization** طب ايه الـ **Database Normalization** ؟

الـ **Normalization** هو اني ابدأ اعمل **Categorization** واعمل **فصل لبيانات الطلاب** دي فاخلي بيانات الطالب في Table وليكن Students اخلي الكورسات في Table تاني اسمه Courses وهكذا.. 

> 💡فبدل ما كان عندي ****Table واحد كبير فيه البيانات كلها**** , اصبح دلوقتي ****عندي اكتر من Table**** وكل واحد شايل الجزء الخاص بيه او الـ Category بتاعته بمعنى اصح. 

---

## مميزات الـ Normalization 

### Reduce Redundancy 

أول ميزة مهمة من الـ Normalization هي أنه بيقلل التكرار اللي ممكن يحصل, فزي ما شوفنا لو انا عندي بيانات الطلاب في Table واحد , لو كان عندي Student Enrolled في 5 كورسات هيكون عندي 5 Entries

الفكرة مش في كده بس الفكرة **ماذا لو بيانات الطالب دي كبيرة** يعني بتشتمل على (عنوان - اسم - رقم تليفون - ايميل) وتفاصيل تانية كتير ؟ هنلاقي ان كل البيانات دي بتتكرر 

ولكن لو لجأنا للـ Normalization **فاحنا هنقلل الـ Storage وهتبقى Efficient** لاننا ممكن نبدل كل ده بالـ StudentID ويكون بيانات الطالب في Table منفصل والـ Courses كذلك. 

### Improve Data Integrity

اما بنفصل كل جزء خاص بيه لوحده من خلال الـ Normaliztion , **عمليات الـ Update والـ Modifications عامة هتكون أقل عرضة للمشاكل** وده لانك **بتغير في مكان واحد بس** , فانت لو بتغير عنوان الطالب مش محتاج **تروح تغيره في 5 اماكن في نفس الـ Table** وبالتالي بتكون أقل عرضة للمشاكل وتحسن من الـ Data Integrity 

### Enhance Query Performance 

ده هيحسن بنسبة كبيرة من الـ **Query Performance** خصوصا في **عمليات الـ Write** وكذلك الـ Fetching بنسبة بسيطة خصوصا اني دلوقتي باه **عندي Tables صغيرة + الـ Indexing** هيكون على كل Table منهم فهيساعد في تحسين الـ Overall Query Performance ولكن فيه **عيب قاتل هنتكلم عنه في العيوب ليه علاقة بالـ Joins** فهي مش معانا دلوقتي.

---

## عيوب الـ Normalization 

### Complexity 

الـ Normalization بيزود بطبيعته صعوبة في عملية الـ **Schema Design والتغييرات اللي ممكن تطرأ عليها** بعد كده واننا نحافظ عليها بشكل دوري من خلال الـ Maintenance فده بيتطلب صعوبة خصوصا لو الـ Normalization واصل لمرحلة عالية.
### Increased Joins

اتكلمنا في المميزات انها بتحسن من الـ Query Performance ولكن على النقيض فهي **بتزود Joins** خصوصا انك دلوقتي فصلت كل جزء لوحده في Table منفصل, فلو انت احتجت تجيب البيانات دي مع بعض او تجيب جزء منها مع بعض فده **هيتطلب منك تعمل Joins وبالتالي هيبقى فيه هنا صعوبة شوية في تحسين اداء الـ Queries** اللي معتمدة على انك تـ **Fetch اكتر من Table مع بعض**.

---

## مميزات الـ De-Normalization 

### Improve Read Performance 

الـ De-Normalization بيحسن بشكل عام من الـ **Read Queries** وده لان دلوقتي كل البيانات موجودة في Table واحد فأنت يدوب هتروح **تقراها علطول خصوصا لو الـ Indexing كمان معمول بشكل كويس** فهتبقى سريعة جدًا. 

### Simplicity 

على العكس من الـ Normalization فهنا هتلاقي **اغلب الـ Queries Simplified وسهلة** بشكل كبير جدًا لأنك مبتعملش حاجة غير انك بتجيب البيانات من Table واحد بس. 

---

## عيوب الـ De-Normalization 

### Data Redundancy 

وشوفنا ده في مثال الـ Students وانه ازاي وجود التكرار ده هيؤدي الى زيادة في الـ Storage وطبعا ممكن يحصل مشاكل في الـ Data Consistencies خصوصا لو **عمليات الـ Update متمتش بشكل كويس ومتعملهاش Handle** كويس وده لأن زي ما قولنا فيه **اكتر من Record بتعمله Update** دلوقتي. 

### Decrease Write Performance 

بالرغم من أن عمليات الـ **Read ممكن تبقى سريعة جدًا** الا ان على النقيض **عمليات الـ Write / Update ممكن تبقى مكلفة وبطيئة** وده لان الداتا زي ما اتفقنا متكررة فعشان نعمل Insert لـ Student جديد وعندنا مثلا 5 كورسات , **فانا هعمل 5 Insertions وكذلك الـ Update هيكون بطيء**.

---

الـ Normalization والـ De-Normalization الاتنين من الـ Strategies المهمة جدًا واللي اختيار بينهم محتاج **دراسة للـ Business Requirements بشكل كويس** , لان كل واحدة فيهم بتقدم مميزات وعيوب , ودورك هنا انك **تختار ما يناسب الـ Business Requirements واللي يحققلك اللي مطلوب** وانك **توازن بين الـ Trade-Offs** دي.
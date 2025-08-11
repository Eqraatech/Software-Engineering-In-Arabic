---
title: "Continuous Integration"
description: "Continuous Integration (CI) is a development practice where code changes are automatically tested and merged frequently. This guide explains how CI improves code quality, speeds up development, and reduces integration issues."
excerpt: "في فرق البرمجيات الحديثة، التغيير المستمر في الكود شيء طبيعي… لكن الدمج اليدوي للتغييرات ممكن يكون كابوس ، وهنا بييجي دور الـ Continuous Integration — أسلوب تطوير بيخلي كل مبرمج يدمج شغله بشكل متكرر وآمن في الكود الأساسي، مع تشغيل اختبارات أوتوماتيكية لضمان إن كل حاجة شغالة."
tags: ["cicd", "devops", "git", "version-control", "jenkins", "circleci", "pipeline"]
updatedAt: "2024-02-24"
featured: false
image: "https://assets.eqraatech.com/guides/continuous-integration.png"
author: "ikhaledabdelfattah"
---

<img src="https://assets.eqraatech.com/guides/continuous-integration.png" alt="Continuous Integration" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

سمعت قبل كده عن CI & CD؟ خلينا النهارده ورقة وقلم وهنتكلم عن أول مصطلح منهم وهو ال Continues Integration (CI). 

دايما واحنا شغالين في بناء مشروع برمجي كبير بندور علي طرق تساعدنا في نشر المشروع بشكل أسرع ونفس الوقت بكفاءه عالية. بشكل بسيط عايزين نبدأ `Pipeline` بإننا ندمج الكود اللي كتبناه مع الكود الرئيسي للمشروع بشكل سريع ونفس الوقت نضمن الكفاءة.

### **ما هي ال Pipeline ؟**

ببساطه هي مجموعه من الخطوات - Processes - بنمشي عليها علشان نبدأ نطلع منتج نهائي يقدر المستخدم يشوفه. بيكون غالبًا بداية الProcess دي هو الكود بتاعك من بداية ال Pull Request اللي بتعمله لحد ما نوصل لمنتج تقدر تشغله والمستخدم يقدر يشوفه (يبقي الPipeline هو كود بيدخل مجموعه من ال Steps علشان يحصله `build` لمنتج نهائي).

### **ما هو الهدف من ال Continues Integration؟**

الهدف منه إننا عايزين نعمل دمج للتغيرات اللي بتتعمل علي الكود بشكل منتظم بحيث نكتشف أي مشكلة تحصل بشكل سريع ونفس الوقت نضمن الكفاءة. 

### **كيف تعمل ال Contiunous Integration ؟**

1. كتابة الكود: البداية بتكون عند المبرمج إنه يبدأ يكتب كود أو يعدل علي كود موجود وبيقوم المبرمج بعمل اختبار الكود والتأكد إنه بيقوم بوظيفته بشكل صحيح.

2. نشر التعديلات: بعدها بيقوم المبرمج بنشر التغيرات اللي بتحصل علي ال `Version Control`.

3. اختبار الكود: بعد كده بيتم عمل اختبار للكود بشكل آلي -`Automated Testing` -علشان نتاكد إنه شغال مظبوط مهما كانت الظروف.

4. دمج الكود: لما بيتم اختبار الكود بيتم بعد كده دمج الكود مع الكود الرئيسي للمشروع.

---

### **مميزات ال Contiunous Integration**

- زيادة سرعة تطوير وبناء المشروع الخاص بيك: بدل ما تستني لآخر لحظة علشان تكتشف المشاكل, `CI` بيساعدك تعرفها من بدري.

- ضمان ان التطبيق خالي بنسبه كبيره من المشاكل: بسبب اختباره في اكتر من ظرف وده هيقلل لخفض التكاليف اللي هنتحتاجها لاصلاح التطبيق.

- خليك واثق ان التطبيق اللي انت نشرته مستقر بشكل كبير: عشان كل تغيير بيتم اختباره كويس جدا

### **أشهر الادوات اللي تساعدك تنفذ CI في مشروعك**

1. . **Jenkins**: أكتر أداة معروفة في مجال `CI`. `Jenkins` هو open source وبيوفر إمكانية عمل `automate` لكل عمليات البناء والتستينج للكود، وكمان بيسمح بدمج الكود بشكل آلي مع الكود الأصلي في ال `repository`. 
2.  **CircleCI**: بتوفر دعم كامل لل CI و CD مع إمكانية الدمج مع `GitHub` و `Bitbucket`. بتتميز بسرعتها وبتوفر إمكانية عمل `containers` للتستينج.

وغيرهم كتير , زي:

- TeamCity
- Bitbucket Pipelines
- Travis CII
- Azure DevOps
- GitHub Actions

في النهاية, `CI` ده جزء مهم جدُا في عالم البرمجة الحديثة علشان يساعد الفرق تشتغل بكفاءة وتسرع في العملية بتاعت التطوير بتاعتهم. وبكده نكون قدرنا نضمن إن المنتج النهائي هيكون علي أعلي مستوي من الكفاءة والاستقرار.
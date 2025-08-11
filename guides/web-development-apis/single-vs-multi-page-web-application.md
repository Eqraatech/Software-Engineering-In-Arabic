---
title: "Single vs. Multi Page Web Application"
description: "Single Page Applications (SPAs) load one HTML page and update content dynamically, offering faster, smoother user experiences. Multi Page Applications (MPAs) load a new page for each view, better suited for SEO and complex sites. This guide compares both to help you choose the right approach."
excerpt: "الـ Web Applications تعد من أهم البرمجيات التي لا يمكن الاستغناء عنها في حياة الإنسان المعاصر وبتثبت كل يوم مدى فعاليتها وتأثيرها, و كمبرمج معاصر محتاج تعرف الفرق بين Single Page Application أو Multiple Page Application لأنه أول قرار بتاخده في برمجتك للموقع."
tags: ["SPA", "web-development", "frontend", "backend"]
updatedAt: "2024-01-15"
featured: false
image: "https://assets.eqraatech.com/guides/single-vs-multi-page-web-application.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/single-vs-multi-page-web-application.png" alt="Single vs. Multi Page Web Application" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ Web Applications تعد من أهم البرمجيات التي لا يمكن الاستغناء عنها في حياة الإنسان المعاصر وبتثبت كل يوم مدى فعاليتها وتأثيرها, و كمبرمج معاصر محتاج تعرف الفرق بين Single Page Application أو Multiple Page Application لأنه أول قرار بتاخده في برمجتك للموقع.

فورقة وقلم و تعالوا نكتشف واحدة من أهم مفاهيم عالم الـ Frontend والـ Web 

بما اننا بنتكلم عن الـ Web يبقى حياتنا كلها هتبقي في الـ `Browser`, المتصفح بشكل عام بيشتغل بنظام الـ Client-Server فمع كتابتك لل `URL` الخاص بالموقع بيبتدي يكلم ال Server عشان يجيب صفحة الموقع وهنا بيت القصيد.

## كيف يتم تحميل الموقع في المتصفح

ال Server بيبعت الموقع علي شكل ملف `HTML` وبيقوم المتصفح بإظهار الملف ليك عن طريق عملية ال `Parsing` and `Rendering` ولو لاقى انه محتاج External Resources تانية زي ال `CSS` Files, `Javascript` , `Images`  بيقوم بتحميلها.

### في حالة الموقع متعدد الصفحات الـ MPA

 العملية دي بتتكرر كل لما تضغط على أي رابط في الصفحة أو تتفاعل معاها وال `Browser` هيحمّل صفحة جديدة من صفحات الموقع بنفس الطريقة, طبعًا ال Loading دا بياخد وقت ومكلف.

### في حالة الموقع ذو الصفحة الواحدة ال SPA

فزي ما اسمه موضح هو بيحمّل صفحة واحدة بتكون عبارة عن `HTML` Template أولية ومعاها الملفات المطلوبة, طيب وبقية الموقع اوصله ازاي؟

---

## Single Page Application

ال `SPA` بتعتمد بشكل كبير على الـ `Javascript` ولما بتتفاعل مع الصفحة وبدل ما اطلب صفحة جديدة كاملة بتسمح بعمل Requests لل Server تطلب بيها مكونات محددة هتغيرها في الصفحة وبكدا تتفادى انك تحمّل الصفحة كلها وتعملها `Re-Rendering` من الصفر واللي هي عملية مكلفة وتبدله بال Dynamic Rendering للمكونات المختلفة في الصفحة.

> 💡مثال على دا هو ال Navigation Bar الموجود أعلي أو على جانب أي موقع, المكون دا موجود في كل الصفحات. في الـ `MPA` هرجع أطلبه وأحمله في كل صفحة بطلبها, بينما في الـ `SPA` فبيتحمل أول مرة بس.

وكدا هو أداءه العام أسرع وسلس أكتر من الموقع متعدد الصفحات ولكن كل حاجة ليها مميزات وعيوب.

---

بشكل عام تطوير المواقع متعددة الصفحات أبسط ومناسب للمواقع اللي مش هتتطلب تفاعل كبير من المستخدم من أشهر الأمثلة المواقع الشخصية اللي بتعرف بيك وسيرتك الذاتية وطرق التواصل أو Blog بيتنشر عليه مقالات أو غيرها. هنا هتستفيد بميزة البساطة وكذلك `SEO` أحسن وأسهل.

بينما ال `SPA` وهي النجم الحالي في مجال تطوير المواقع مناسبة للمواقع اللي فيها تفاعل كبير من المستخدم ومحتاج تجربة استخدام سلسة وسريعة وبتريحك في الـ Maintenance كمبرمج لأنها تعتمد على مفاهيم زي ال Components, Separation of Concerns ولكن لكل شيء ضريبة فهي أصعب في البرمجة مقارنة بال `MPA` وكذلك بتوجه تحديات في ال `SEO` لأن المتصفحات بتفهم الـ `HTML` أحسن بكتير من الـ `Javascript`.

---

كذلك النقاط الهامة في مقارتنا بينهم هيكون الحماية, فال Single Page Apps معرضة بشكل كبير للهجمات كونها تعتمد بشكل أكبر علي آل Javascript اللي بتشتغل في ال Client Side و دا بيعرضها لهجمات من الجانب دا زي ال `Cross Site Scripting , CSRF (Cross-Site Request Forgery)`

فبتحتاج عناية أكبر من المبرمج في تنفيذ `Input Validations` ويستخدم Secure Code Practices.



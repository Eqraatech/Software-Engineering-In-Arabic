<div style="direction: rtl;">
<p>
  <a href="https://eqraatech.com/"><img src="images/eqraatech-cover.png" /> </a>
</p>

  ![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)
  ![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)

[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40Eqraatechcom)](https://twitter.com/Eqraatechcom)

# ورقة وقلم
محتوى تقني متميز في مختلف مجالات هندسة البرمجيات عن طريق تبسيط المفاهيم البرمجية المعقدة بشكل سلس وباستخدام صور توضيحية مذهلة

<p>
  <img src="images/in-a-nutshell.webp" style="width: 640px">
</p>

# فهرس المواضيع

- [Authentication and Authorization](#authentication-and-authorization)
  - [Json Web Token](#json-web-token)


## Authentication and Authorization

في عالم التكنولوجيا وأمان المعلومات، تعتبر عملية الـ Authenitcaion مفتاحًا لضمان الحماية والتحقق من هوية المستخدم. عندما يتم تحقيق المصادقة بنجاح، يمكن للنظام التأكيد على هوية الفرد أو الكيان الذي يسعى للوصول، مما يفتح الباب أمام مرحلة مهمة تعرف بالتفويض.

بعد التحقق من هوية المستخدم، يأتي دور التفويض لتحديد نطاق وصوله. هنا، يتم تخصيص الصلاحيات بشكل دقيق لضمان أن يتمكن المستخدمون فقط من الوصول إلى المعلومات والموارد التي يحتاجون إليها. التفويض يسهم في حماية الخصوصية وضمان أمان النظام.

### Json Web Token

<p>
  <img src="images/json-web-token.png" style="width: 640px">
</p>

الـ JWT عبارة عن Secure Tokens بيتبعت مع كل Request أو Response عشان نتأكد ان البيانات بين الطرفين متغيرتش، كونها طريقة سهلة وفعالة بيخليها واحدة من أكثر الطرق المستخدمة في الـ User Authentication and Authorization (التحقق من هوية المستخدم و تحديد صلاحياته).

**أجزاء الـ JWT**

<ins>
ال JWT بيتكون من 3 أجزاء :
</ins>


1- الـ Headers
ودي بيتكتب فيها نوع الـ Token و كذلك الـ Algorithm المستخدم.


2- الـ Payload
ودا بيحتوي على معلومات المستخدم زي الـ Email و ممكن بعض صلاحياته وتاريخ اصدار وانتهاء الـ Token.


والجزئين دول بيكونوا Base64 Encoded وتقدر تاخدهم و وتستعملهم في أي Base64 Decoder علي الانترنت و وهيظهرلك القيمة بداخلهم، وعشان كدا مينفعش نحط فيهم أي معلومات سرية زي الـ Passwords.


 3- الـ Signature 

والجزء دا بيكون عبارة عن Hashing للجزئين ( 1 + 2 + Secret )

والـ Secret ده الـ Server بس اللي يعرفه وكل لما كان أصعب كان قوة الـ JWT Token أكبر. وعادة ما بيتخزن في الـ Environment Variables في الـ Server ده.


** طيب بنستفاد منه ازاي في الـ Authentication والـ Authorization؟**

<ins>
زمان عشان نعمل User Authentication كان بيتم بالخطوات دي:
</ins>

المستخدم بيعمل Login من خلال الـ Email والـ Password 
الـ Server بيتحقق منهم ويقوم بتحديد Session ID للمستخدم ويخزنها في الـ Database 
بعد كده الـ Server بيبعتها للمستخدم والمتصفح بيخزنها
 وفي كل Request المستخدم بيبعته للـ Server بيكون معاه الـ Session ID
هنا بنقابل مشكلتين:

 الـ Server كل مرة بيحتاج يتحقق من الـ Session ID بيبعت Request للـ Database ودا بيكلف Time وكمان Resources. 
الـ Sessions معرضة بسهولة لنوع من الـ Cyber Attacks اسمه Cross-Site Attacks 
إنما الـ JWT Token بيتم بنفس الشكل دا مع الفارق ان الـ Server هنا مش هيخزنها عنده (زي ما واضح في الجزء الثاني من الصورة).

**ازاي JWT حلت المشاكل دي ؟**

<ins>
الـ JWT بتحل المشكلة الأولى بكون الـ Server  مبيضطرش يرجع للـ Database مع كل Request، الـ Server  بكل بساطة بيعمل الآتي:
</ins>


1- بيقوم حاسب الـ Hash للجزئين 1 و 2 باستخدام الـ Secret المخزنة عنده في الـ Environment Variables على سبيل المثال، والـ Hashing ده بيتم باستخدام الـ Algorithm المحدد في الـ Token في الـ Headers زي ماوضحنا. 

2– بيقوم بعمل مقارنة للناتج بالـ Signature اللي هي جزء الثالث من الـ JWT واللي المستخدم بعتها مع الـ Request.

وبكدا اتأكدنا من هوية المستخدم لأن أي تغيير في الجزئين الأول والثاني أو أي تلاعب في قيمة الـ Secret هينتج عنه Hash مختلف تمامًا عن الجزء الثالث.

اما بالنسبة المشكلة الثانية

فنقدر نحلها باننا نحط في الـ Payload نوع معين من ال Security Tokens اسمه (CSRF (Cross-Site Request Forgery اللي من خلاله بتأكد أن الـ Request ده اتبعت من نفس المكان مش من مكان تاني واقدر بنفس الطريقة اتأكد انه محصلش تلاعب بقيمة الـ Token دي.

**طب ايه هي عيوب الـ JWT ؟**

<ins>
كعادة أي حاجة في العالم الـ JWT مش مثالي وليه بعض الـ Trade-Offs:
</ins>

من الصعب عمل Revoke للـ JWT بعد ما الـ Server يعملها Generate وعشان كده يفضل يتعملها Expiration Time صغير بعدها يقدر الـ User يسجل دخوله مرة تانية ويتعمله Generate لـ Token جديدة
حيث اننا بنبعت الـ JWT مع كل Request، فلو حجم الـ Payload كان كبير .. حجم الـ Request بالتابعية هيكبر ودا هيأثر بالسلب على الـ Network Latency و Network Bandwidth 
الـ JWT سهلة الاستخدام والتطبيق في الـ Code لأن كل اللي بنعمله اننا بنستخدم Libraries جاهزة ونحدد الـ Secret اللي هنستخدمه. 

وتقدروا تدخلوا على الموقع الرسمي لـ JWT وتجربوا الـ Decoder وتغيروا في القيم اللي في الـ Token.


## License

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-ND 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1"></a></p>

</div>

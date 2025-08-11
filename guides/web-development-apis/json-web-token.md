---
title: "Json Web Token"
description: "JSON Web Token (JWT) is a compact, URL-safe way to securely transmit data between parties as a JSON object. Commonly used for authentication and authorization, it includes a header, payload, and signature to ensure data integrity."
excerpt: "الـ JWT عبارة عن Secure Tokens بيتبعت مع كل Request أو Response عشان نتأكد ان البيانات بين الطرفين متغيرتش، كونها طريقة سهلة وفعالة بيخليها واحدة من أكثر الطرق المستخدمة في الـ User Authentication and Authorization."
tags: ["jwt", "security", "web-development", "backend", "authentication", "authroization"]
updatedAt: "2023-12-19"
featured: false
image: "https://assets.eqraatech.com/guides/json-web-token.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/json-web-token.png" alt="Json Web Token" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ JWT عبارة عن Secure Tokens بيتبعت مع كل Request أو Response عشان نتأكد ان البيانات بين الطرفين متغيرتش، كونها طريقة سهلة وفعالة بيخليها واحدة من أكثر الطرق المستخدمة في الـ User Authentication and Authorization (التحقق من هوية المستخدم و تحديد صلاحياته).

---

### أجزاء الـ JWT 

ال JWT بيتكون من 3 أجزاء:
1. **الـ Headers**: ودي بيتكتب فيها نوع الـ Token و كذلك الـ Algorithm المستخدم.
2. **الـ Payload**: ودا بيحتوي على معلومات المستخدم زي الـ Email و ممكن بعض صلاحياته وتاريخ اصدار وانتهاء الـ Token. والجزئين دول بيكونوا **Base64 Encoded** وتقدر تاخدهم و وتستعملهم في أي **Base64 Decoder** علي الانترنت و وهيظهرلك القيمة بداخلهم، وعشان كدا مينفعش نحط فيهم أي معلومات سرية زي الـ Passwords.
 3. **الـ Signature**: والجزء دا بيكون عبارة عن Hashing للجزئين ( 1 + 2 + Secret )

💡والـ Secret ده الـ Server بس اللي يعرفه وكل لما كان أصعب كان قوة الـ JWT Token أكبر. وعادة ما بيتخزن في الـ Environment Variables في الـ Server ده.

---

### **طيب بنستفاد منه ازاي في الـ Authentication والـ Authorization؟**

زمان عشان نعمل User Authentication كان بيتم بالخطوات دي:

1. المستخدم بيعمل Login من خلال الـ Email والـ Password 
2. الـ Server بيتحقق منهم ويقوم بتحديد Session ID للمستخدم ويخزنها في الـ Database 
3. بعد كده الـ Server بيبعتها للمستخدم والمتصفح بيخزنها
4.  وفي كل Request المستخدم بيبعته للـ Server بيكون معاه الـ Session ID

**هنا بنقابل مشكلتين:**

1.  الـ Server كل مرة بيحتاج يتحقق من الـ Session ID بيبعت Request للـ Database ودا بيكلف Time وكمان Resources. 
2. الـ Sessions معرضة بسهولة لنوع من الـ Cyber Attacks اسمه Cross-Site Attacks 

**إنما الـ JWT Token بيتم بنفس الشكل دا مع الفارق ان الـ Server هنا مش هيخزنها عنده (زي ما واضح في الجزء الثاني من الصورة).**

---

### ازاي JWT حلت المشاكل دي ؟

الـ JWT بتحل المشكلة الأولى بكون الـ Server  مبيضطرش يرجع للـ Database مع كل Request، الـ Server  بكل بساطة بيعمل الآتي:

1- بيقوم حاسب الـ Hash للجزئين 1 و 2 باستخدام الـ Secret المخزنة عنده في الـ Environment Variables على سبيل المثال، والـ Hashing ده بيتم باستخدام الـ Algorithm المحدد في الـ Token في الـ Headers زي ماوضحنا. 
2 – بيقوم بعمل مقارنة للناتج بالـ Signature اللي هي جزء الثالث من الـ JWT واللي المستخدم بعتها مع الـ Request.

وبكدا اتأكدنا من هوية المستخدم لأن أي تغيير في الجزئين الأول والثاني أو أي تلاعب في قيمة الـ Secret هينتج عنه Hash مختلف تمامًا عن الجزء الثالث.

**اما بالنسبة المشكلة الثانية**

فنقدر نحلها باننا نحط في الـ Payload نوع معين من ال Security Tokens اسمه (CSRF (Cross-Site Request Forgery اللي من خلاله بتأكد أن الـ Request ده اتبعت من نفس المكان مش من مكان تاني واقدر بنفس الطريقة اتأكد انه محصلش تلاعب بقيمة الـ Token دي.

---

الـ JWT سهلة الاستخدام والتطبيق في الـ Code لأن كل اللي بنعمله اننا بنستخدم Libraries جاهزة ونحدد الـ Secret اللي هنستخدمه. 

وتقدروا تدخلوا على الموقع الرسمي لـ [JWT](https://jwt.io/) وتجربوا الـ Decoder وتغيروا في القيم اللي في الـ Token.

---

## مثال عملي على استخدام JWT

خلينا نشوف مثال عملي على كيفية إنشاء والتحقق من JWT في لغات برمجة مختلفة:

<!-- Python (PyJWT) -->
```python
# Python (PyJWT)
import jwt
import datetime

SECRET = 'mysecretkey'

# إنشاء توكن
payload = {
    'user_id': 123,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}
token = jwt.encode(payload, SECRET, algorithm='HS256')
print('JWT:', token)

# التحقق من التوكن
try:
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    print('Decoded:', decoded)
except jwt.ExpiredSignatureError:
    print('Token expired')
except jwt.InvalidTokenError:
    print('Invalid token')
```

<!-- JavaScript (jsonwebtoken) -->
```javascript
// JavaScript (jsonwebtoken)
const jwt = require('jsonwebtoken');
const SECRET = 'mysecretkey';

// إنشاء توكن
const payload = {
  user_id: 123,
  exp: Math.floor(Date.now() / 1000) + (60 * 60) // ساعة واحدة
};
const token = jwt.sign(payload, SECRET);
console.log('JWT:', token);

// التحقق من التوكن
try {
  const decoded = jwt.verify(token, SECRET);
  console.log('Decoded:', decoded);
} catch (err) {
  if (err.name === 'TokenExpiredError') {
    console.log('Token expired');
  } else {
    console.log('Invalid token');
  }
}
```

<!-- Java (jjwt) -->
```java
// Java (jjwt)
import io.jsonwebtoken.*;
import java.util.Date;

String SECRET = "mysecretkey";

// إنشاء توكن
String token = Jwts.builder()
    .setSubject("123")
    .setExpiration(new Date(System.currentTimeMillis() + 3600_000))
    .signWith(SignatureAlgorithm.HS256, SECRET)
    .compact();
System.out.println("JWT: " + token);

// التحقق من التوكن
try {
    Claims claims = Jwts.parser()
        .setSigningKey(SECRET)
        .parseClaimsJws(token)
        .getBody();
    System.out.println("Decoded: " + claims);
} catch (ExpiredJwtException e) {
    System.out.println("Token expired");
} catch (JwtException e) {
    System.out.println("Invalid token");
}
```

في المثال ده:
- بننشئ JWT ونحدد بيانات المستخدم وتاريخ الانتهاء
- بنستخدم Secret للتحقق من صحة التوكن
- بنوضح كيفية التعامل مع انتهاء صلاحية التوكن أو كونه غير صالح
---
title: "SQL Injection"
description: "SQL Injection is a security vulnerability where attackers manipulate queries to access or alter data. This guide explains how it works, its risks, and how to prevent it using parameterized queries and input validation."
excerpt: "أكيد سمعنا كتير عن ال SQL Injection وقرأنا عنه كتير ، فاحنا هنقدملكم انهاردة دليلكم المختصر والوافي عنه  فورقة وقلم وتعالوا نتكلم عن ايه هو وليه بنسمع عنه كتير وازاي كمبرمج احمي التطبيقات بتاعتي تجاه النوع دا من الهجمات."
tags: ["database", "security", "sql", "hacking"]
updatedAt: "2024-04-17"
featured: false
image: "https://assets.eqraatech.com/guides/sql-injection.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/sql-injection.png" alt="SQL Injection" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

أكيد سمعنا كتير عن ال **SQL Injection** وقرأنا عنه كتير ، فاحنا هنقدملكم انهاردة دليلكم المختصر والوافي عنه 

فورقة وقلم وتعالوا نتكلم عن ايه هو وليه بنسمع عنه كتير وازاي كمبرمج احمي التطبيقات بتاعتي تجاه النوع دا من الهجمات.

---

## SQL Injection

الـ SQL Injection هو من أشهر أنواع الهجمات الأمنية على تطبيقات الويب و دا لسببين:

1. شيوع ال **SQL Injection vulnerabilities** أو الثغرات من النوع دا في التطبيقات لأنه أي موقع Web بيتعامل مع قواعد البيانات بـ **Code** معين معرض ان الـ **Code** دا يكون فيه هذه الثغرات وما علي الـ Attacker أو المهاجم انه يلاقيها ويستغلها.
2. لأنه بيستهدف دايمًا قواعد البيانات واللي دايمًا بتشيل بيانات مهمة ممكن الـ Hacker يستغلها.

---

## **طريقة الـ SQL Injection** 

النوع دا من الهجمات معتمد علي ال **dynamic sql queries** اللي بستخدم **String concatenation**  زي المثال دا 

## **طرق الحماية تجاه الـ Sql Injection** 

في 3 طرق وقاية أساسية تجاه النوع دا من الهجمات:

1. استخدام **Prepared Statements أو Parameterized Queries**
2. التحقق من أي بيانات يقوم المستخدم بإدخالها **Input Validation and Sanitation**
3. تحديد صلاحيات وامتيازات استخدام قواعد البيانات في التطبيق باستخدام (**Principle of Least Privilege**)

---

## مثال عملي على الـ SQL Injection والحماية منه

خلينا نشوف مثال عملي على الـ SQL Injection وكيفية الحماية منه:

<!-- Vulnerable Code -->
```java
// VULNERABLE CODE - SQL Injection
String query = "SELECT account_balance FROM user_data WHERE user_name = "
             + request.getParameter("customerName");
try {
    Statement statement = connection.createStatement();
    ResultSet results = statement.executeQuery(query);
}

// Attacker input: 'OR '1' = '1
// Result: SELECT account_balance FROM user_data WHERE user_name = 'OR '1' = '1
// This returns ALL user data!
```

<!-- Secure Code -->
```java
// SECURE CODE - Prepared Statement
String query = "SELECT account_balance FROM user_data WHERE user_name = ?";
try {
    PreparedStatement pstmt = connection.prepareStatement(query);
    pstmt.setString(1, request.getParameter("customerName"));
    ResultSet results = pstmt.executeQuery();
}

// Attacker input: 'OR '1' = '1
// Result: Treated as literal string, not SQL code
// Safe and secure!
```

<!-- Python Example -->
```python
# Python with SQLAlchemy (ORM)
from sqlalchemy import text

# VULNERABLE
query = f"SELECT * FROM users WHERE name = '{user_input}'"
result = connection.execute(query)

# SECURE
query = text("SELECT * FROM users WHERE name = :name")
result = connection.execute(query, {"name": user_input})

# ORM approach (safest)
user = session.query(User).filter_by(name=user_input).first()
```

في المثال ده:
- **Vulnerable Code**: يوضح الكود المعرض للـ SQL Injection
- **Secure Code**: يوضح كيفية الحماية باستخدام Prepared Statements
- **Python Example**: يوضح الحماية في Python مع ORM

---

وعيك كمبرمج بالنوع دا من الهجمات أساسي لأنه باستخدام الـ **best practices**  دي من البداية أثناء كتابتك للـ Code وتعاملك مع قاعدة البيانات بيوفر عليك مجهود كبير فيما بعد, غير طبعًا أن الهجمات المتعلقة بالبيانات وتسريبها لجهات غير معنية مكلفة جدًا من الناحية التقنية والعملية.

ولأن **منع الهجمات من الحدوث 100% ببساطة غير ممكن** لازم نعمل حسابنا اننا نزود تسجيل للأحداث (**Logging and Monitoring**) بحيث ان لو **حصل اي Unexpected Behaviour** أقدر **أحدد لو كان محاولة هجوم واخذ الاجراءات المناسبة**.
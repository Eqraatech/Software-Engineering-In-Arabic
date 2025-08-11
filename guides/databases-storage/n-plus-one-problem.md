---
title: "N+1 Problem"
description: "The N+1 problem occurs when an application makes one query to fetch a list, then N additional queries for related data—hurting performance. This guide explains the issue and how to fix it with techniques like eager loading and query optimization."
excerpt: "الـ N+1 Problem هي مشكلة في طريقة تعاملنا مع قواعد البيانات ، ومن المشاكل اللي لازم احنا كمطورين ناخد بالنا منها لانها ليها ضريبة كبيرة أوي خصوصا في التعامل مع البيانات الكبيرة."
tags: ["n+1", "database", "backend", "web-development"]
updatedAt: "2024-08-03"
featured: false
image: "https://assets.eqraatech.com/guides/n-plus-one-problem.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/n-plus-one-problem.png" alt="N+1 Problem" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ N+1 Problem هي مشكلة في طريقة تعاملنا مع قواعد البيانات ، ومن المشاكل اللي لازم احنا كمطورين ناخد بالنا منها لانها ليها ضريبة كبيرة أوي خصوصا في التعامل مع البيانات الكبيرة.

فورقة وقلم وتعالوا نتعرف على المشكلة دي وازاي نقدر نتجنبها

---

## N+1 Problem

الـ N+1 Problem هي مشكلة بتخلينا نعمل عدد Requests أكبر بكتير من اللي محتاجينه وعشان نكون محددين فبالتحديد N+1 Requests على الرغم اننا ممكن نحل نفس المشكلة بعدد Requests أقل.

وطبعًا الـ Requests الكثيرة اللي ملهاش لزمة بتشغل الـ Database وبالتالي الموقع أو التطبيق بتاعنا بيكون أبطأ و بيدينا Performance سيء.

وعشان نفهم كويس خلينا ناخد مثال, أنت بتبرمج موقع لمكتبة وعاوز بيانات الكتب الأكثر مبيعًا وكمان بيانات عن المؤلفين للكتب دي عشان تعرضها في صفحة مخصصة.

بيانات الكتب الأكثر مبيعًا في `Books Table` وبيانات المؤلفين في `Authors Table`

**فأول حل هيجي في بالنا:**

<!-- المشكلة (N+1 Queries) -->
```sql
-- أولاً: نجيب قائمة الكتب (1 query)
SELECT id, title, author_id FROM books WHERE bestseller = true;

-- ثانياً: لكل كتاب نجيب معلومات المؤلف (N queries)
SELECT id, name, bio FROM authors WHERE id = 1;
SELECT id, name, bio FROM authors WHERE id = 2;
SELECT id, name, bio FROM authors WHERE id = 3;
-- ... وهكذا لكل كتاب

-- النتيجة: 1 + N queries = N+1 problem
-- إذا كان لدينا 100 كتاب، سنحتاج 101 query!
```

<!-- الحل (JOIN) -->
```sql
-- الحل: استخدام JOIN (1 query فقط)
SELECT 
    b.id,
    b.title,
    b.price,
    a.name as author_name,
    a.bio as author_bio
FROM books b
INNER JOIN authors a ON b.author_id = a.id
WHERE b.bestseller = true;

-- النتيجة: 1 query فقط بدلاً من N+1
-- نفس النتيجة بسرعة أكبر بكثير
```

<!-- مثال آخر -->
```sql
-- مثال آخر: Posts مع Comments
-- المشكلة: N+1 queries
SELECT id, title, content FROM posts WHERE published = true;
SELECT id, content, user_id FROM comments WHERE post_id = 1;
SELECT id, content, user_id FROM comments WHERE post_id = 2;
-- ... لكل post

-- الحل: LEFT JOIN (للحصول على posts حتى لو ليس لها comments)
SELECT 
    p.id,
    p.title,
    p.content,
    c.id as comment_id,
    c.content as comment_content,
    c.created_at
FROM posts p
LEFT JOIN comments c ON p.id = c.post_id
WHERE p.published = true;
```

دا هيخلي تحميل الصفحة بتاعت الكتب الأكثر مبيعًا على موقعك بطيئة جدًا بينما ممكن نحسّن من ال Performance بتاعنا بإننا نطلب البيانات من قاعدة البيانات في عدد أقل من ال Requests ودا بإننا نعمل اعادة هيكلة للـ Queries بتاعتنا.

هنا إحنا حلينا المشكلة أننا استخدمنا `Join` وقد يبدو ال Query هنا أكبر ولكنه أكفأ لأنه قاعدة البيانات بتعمل `Query Optimization` فتقدر تسرع الـ Query اللي قد يبدوا انه كبير بينما العدد الكبير من الـ Queries المنفصلة بيشغل قاعدة البيانات ومفيهوش مجال للـ `Optimization`

الـ N+1 من المشكلات الشائعة لأن كل البيانات اللي بنتعامل معاها في التطبيقات والمواقع بتكون مرتبطة ببعض بشكل ما أو بآخر , فلو عندنا موقع تواصل وحبينا نجيب ال Posts و نجيب ال Comments علي كل Post أو عندنا موقع توصيل طلبات وحبينا نعرض المطاعم وكذلك الأكلات اللي بيقدمها كل مطعم إلخ…

**الحلول الممكنة:**

<!-- JOINs -->
```sql
-- 1. استخدام JOINs مع multiple tables
SELECT 
    b.id,
    b.title,
    b.price,
    a.name as author_name,
    p.name as publisher_name,
    p.location as publisher_location
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN publishers p ON b.publisher_id = p.id
WHERE b.bestseller = true
ORDER BY b.sales_count DESC;
```

<!-- Eager Loading -->
```javascript
// 2. Eager Loading في ORMs
// Sequelize مثال
const books = await Book.findAll({
  where: { bestseller: true },
  include: [
    { 
      model: Author,
      attributes: ['name', 'bio']
    },
    { 
      model: Publisher,
      attributes: ['name', 'location']
    }
  ],
  order: [['sales_count', 'DESC']]
});

// Prisma مثال
const books = await prisma.book.findMany({
  where: { bestseller: true },
  include: {
    author: {
      select: { name: true, bio: true }
    },
    publisher: {
      select: { name: true, location: true }
    }
  },
  orderBy: { sales_count: 'desc' }
});
```

<!-- Subqueries & IN -->
```sql
-- 3. استخدام Subqueries
SELECT 
    b.id,
    b.title,
    b.price,
    (SELECT name FROM authors WHERE id = b.author_id) as author_name,
    (SELECT name FROM publishers WHERE id = b.publisher_id) as publisher_name
FROM books b
WHERE b.bestseller = true;

-- 4. استخدام IN clause للـ batch operations
SELECT * FROM authors 
WHERE id IN (
    SELECT DISTINCT author_id 
    FROM books 
    WHERE bestseller = true
);

-- 5. استخدام EXISTS
SELECT * FROM books b
WHERE EXISTS (
    SELECT 1 FROM authors a 
    WHERE a.id = b.author_id 
    AND a.popular = true
);
```

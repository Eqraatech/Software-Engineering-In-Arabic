---
title: "Pessimistic Locking"
description: "Pessimistic locking prevents conflicts by locking data for a transaction, blocking others from modifying it until the lock is released. This guide explains how it works and when to use it in high-conflict environments."
excerpt: "الـ Pessimistic Locking في قواعد البيانات بيمنع الـ Conflicts الناتجة من الـ Concurrent Updates واللي بتحصل بشكل Frequent أو متكرر. فلما بنيجي نعمل عملية تحديث لـ Row أو Record معين، فالـPessimistic Locking بتحط قفل"
tags: ["lock", "transaction", "database", "shared-lock", "exclusive-lock", "backend" , "performance"]
updatedAt: "2024-05-07"
featured: true
image: "https://assets.eqraatech.com/guides/pessimistic-locking.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/pessimistic-locking.png" alt="Pessimistic Locking" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

يعتبر الـ Locking من أهم الآليات اللي بنعتمد عليها في الـ Databases بشكل أساسي عشان نتحكم في الـ Concurrent Access للبيانات من خلال أكثر من Transactions، فلو كان هناك عدد من الـ Transactions بيحاول يوصل للبيانات دي في نفس الوقت فأكيد هيحصل نتيجة لده تضارب بنسميه Conflicts.

> نقدر نتخيل الـ Locking كأنه زي القفل اللي بنقفل بيه على أي حاجة عشان نمنع أي حد من الوصول ليها. فالـ Databases أحيانًا بتحط قفل على الـ Row أو الـ Record لما يكون فيه Transaction شغال عليه عشان تمنع أي حد من الوصول للـ Row ده, اكنه دخل (الحمام وقفل وراه الباب) .. 

## طب هو ليه اصلا بنحتاج للـ Locking ؟

احنا بنحتاج للـ Locking لإنه بيقدملنا فوايد مهمة زي الـ Data Integrity & Data Consistency ودول من أهم الفوايد اللي بنحصل عليها من الـ Locking .. لإنه من غير Locking ممكن Two Concurrent Transactions يغيروا في قيمة الـ Column الواحد في نفس الوقت وده يسبب مشاكل كتير. 

**وعلى الرغم من فوايد الـ Locking الا انه بيجي مع تحديات كبيرة وتعقيدات في التعامل معاه، فلازم نكون فاهمينه عشان نقدر نتعامل معاه بشكل فعال.**

فيه نوعين من الـ Locking وهم الـ **Optimistic Locking** والـ **Pessimistic Locking** بس احنا هنتكلم النهاردة عن الـ Pessimistic.

---

## ايه هو الـ Pessimistic Locking ؟

الـ Pessimistic Locking جاي من اسمه انه شخص متشائم، بيعمل حسابه دايما على أسوء الظروف وبناء عليه بيفكر لقدام وبياخد احتياطه مسبقا.

الـ Pessimistic Locking في قواعد البيانات بيمنع الـ Conflicts الناتجة من الـ Concurrent Updates واللي بتحصل بشكل Frequent أو متكرر. فلما بنيجي نعمل عملية تحديث لـ Row أو Record معين، فالـPessimistic Locking بتحط قفل على الـRow أو الـRecord ده عشان تمنع عمليات الـ Updates التانية من انها توصل لنفس الـ Row أو الـ Record في نفس الوقت.

ممكن نتخيل أن القفل ده عبارة عن اشارة حصرية فقط لعملية الـ Update الحالية , وبالتالي مش ممكن لأي عملية تانية انها توصل لنفس البيانات اللي شغالين عليها وده لانها بتكون مقفول عليها بالقفل لحد ما العملية الحالية تنتهي.

---

**وفيه أنواع مختلفة من الـ Pessimistic Locking:**

زي الـ Exclusive Locks ودي غرضها انها تمنع كل العمليات من انها توصل للـ Row أو الـ Record اللي معمول عليه Locking

وفيه برضو الـ Shared Locks ودي بتسمح فقط لعمليات الـ Read انها تقرا البيانات عادي جدًا حتى لو فيه عملية حالية بتعمل على البيانات دي Update ولكن بتمنع عمليات الـ Write / Update التانية تماما.

---

## مثال عملي على الـ Pessimistic Locking

خلينا نشوف مثال عملي على كيفية استخدام الـ Pessimistic Locking في قواعد البيانات المختلفة:

<!-- MySQL/PostgreSQL -->
```sql
-- MySQL/PostgreSQL - SELECT FOR UPDATE
BEGIN TRANSACTION;

-- Lock specific row for update
SELECT * FROM inventory 
WHERE product_id = 123 
FOR UPDATE;

-- Update the locked row
UPDATE inventory 
SET quantity = quantity - 1 
WHERE product_id = 123;

COMMIT;
```

<!-- SQL Server -->
```sql
-- SQL Server - WITH (UPDLOCK)
BEGIN TRANSACTION;

-- Lock row with UPDLOCK hint
SELECT * FROM inventory 
WITH (UPDLOCK) 
WHERE product_id = 123;

-- Update the locked row
UPDATE inventory 
SET quantity = quantity - 1 
WHERE product_id = 123;

COMMIT;
```

<!-- Java (JPA) -->
```java
// Java with JPA/Hibernate
@Transactional
public void updateInventory(Long productId, int quantity) {
    // Lock the entity for update
    Inventory inventory = entityManager
        .find(Inventory.class, productId, 
              LockModeType.PESSIMISTIC_WRITE);
    
    // Update the locked entity
    inventory.setQuantity(inventory.getQuantity() - quantity);
    entityManager.persist(inventory);
}
```

في المثال ده:
- نستخدم `SELECT FOR UPDATE` في MySQL/PostgreSQL
- نستخدم `WITH (UPDLOCK)` في SQL Server  
- نستخدم `LockModeType.PESSIMISTIC_WRITE` في Java JPA
- كل الطرق دي بتحط قفل على الـ Row عشان تمنع الـ Concurrent Updates

---

## ملاحظات ختامية

بشكل عام، ممكن نقول أن Pessimistic Locking يعتبر مناسبًا للـ Systems التي بتتطلب Concurrent Updates بشكل متكرر ومحتاجة أن البيانات تكون Consistent مع بعضها بشكل دقيق!
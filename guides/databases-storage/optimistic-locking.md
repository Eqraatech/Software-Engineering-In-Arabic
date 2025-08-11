---
title: "Optimistic Locking"
description: "Optimistic locking allows multiple transactions to proceed without locks, checking for data changes before commit. This guide explains how it helps avoid conflicts in low-contention systems while improving performance."
excerpt: "يعتبر الـ Locking من أهم الآليات اللي بنعتمد عليها في الـ Databases بشكل أساسي عشان نتحكم في الـ Concurrent Access للبيانات من خلال أكثر من Transactions، فلو كان هناك عدد من الـ Transactions بيحاول يوصل للبيانات دي في نفس الوقت فأكيد هيحصل نتيجة لده تضارب بنسميه Conflicts."
tags: ["lock", "transaction", "database", "version", "optimistic-lock", "backend" , "performance"]
updatedAt: "2023-12-30"
featured: false
image: "https://assets.eqraatech.com/guides/optimistic-locking.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/optimistic-locking.png" alt="Optimistic Locking" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

يعتبر الـ Locking  من أهم الآليات اللي بنعتمد عليها في الـ Databases بشكل أساسي عشان نتحكم في الـ Concurrent Access للبيانات من خلال أكثر من Transactions، فلو كان هناك عدد من الـ Transactions بيحاول يوصل للبيانات دي في نفس الوقت فأكيد هيحصل نتيجة لده تضارب بنسميه Conflicts.

> نقدر نتخيل الـ Locking كأنه زي القفل اللي بنقفل بيه على أي حاجة عشان نمنع أي حد من الوصول ليها. فالـ Databases أحيانًا بتحط قفل على الـ Row أو الـ Record لما يكون فيه Transaction شغال عليه عشان تمنع أي حد من الوصول للـ Row ده, اكنه دخل (الحمام وقفل وراه الباب) .. 

## طب هو ليه اصلا بنحتاج للـ Locking ؟

احنا بنحتاج للـ Locking لإنه بيقدملنا فوايد مهمة زي الـ Data Integrity & Data Consistency ودول من أهم الفوايد اللي بنحصل عليها من الـ Locking .. لإنه من غير Locking ممكن Two Concurrent Transactions يغيروا في قيمة الـ Column الواحد في نفس الوقت وده يسبب مشاكل كتير. 

**وعلى الرغم من فوايد الـ Locking الا انه بيجي مع تحديات كبيرة وتعقيدات في التعامل معاه، فلازم نكون فاهمينه عشان نقدر نتعامل معاه بشكل فعال.**

فيه نوعين من الـ Locking وهم الـ **Optimistic Locking** والـ **Pessimistic Locking** بس احنا هنتكلم النهاردة عن الـ Optimistic. 

---

## ايه هو الـ Optimistic Locking ؟

الـ Optimistic Locking جاي من اسمه انه شخص متفائل، مبيفكرش في المشكلة الا لما تحصل ومبيشغلش باله، ولما تحصل مشكلة يبدأ يشوف هيتصرف ويحلها ازاي. 

الـ Optimistic Locking دوره انه يمنع الـ Conflicts بين الـ Transactions واللي بنسبة كبيرة بتحصل نتيجة عملية الـ Concurrent Update فلما يكون فيه Transaction بيحاول يعمل Update لقيمة Row معين هنا هيجي الـ Optimistic Locking ويزود بعض البيانات الإضافية Metadata زي الـ Version أو الـ Timestamp

---

**طب ليه بيضيف بيانات اضافية ؟**

عشان لو فيه Transaction تاني حاول يغير من قيمة نفس الـ Row هيعمل وقتها Check على الـ Version Number أو الـ Timestamp ولو كان مختلف فهيعرف وقتها انه فيه Transaction بيحاول يغير في الـ Row أثناء مالـ Transaction الأول بيغير فيها وده بسبب اختلاف قيم الـ Version Number أو الـ Timestamp. 

> فالخلاصة أن الـ Optimistic Locking بيشتغل على فرضية انه مفيش Conflicts هتحصل ، ولما بيحصل Conflict بيبدأ يـ Check ويتعامل معاه.

---

## مثال عملي على الـ Optimistic Locking

خلينا نشوف مثال عملي على كيفية استخدام الـ Optimistic Locking في قواعد البيانات المختلفة:

<!-- SQL with Version -->
```sql
-- Database table with version column
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    version INT DEFAULT 1
);

-- Update with version check
UPDATE products 
SET name = 'New Product Name', 
    price = 29.99, 
    version = version + 1
WHERE id = 123 
  AND version = 1;  -- Check current version

-- If no rows affected, version changed (conflict detected)
```

<!-- Java (JPA) -->
```java
// Java with JPA/Hibernate
@Entity
public class Product {
    @Id
    private Long id;
    private String name;
    private BigDecimal price;
    
    @Version
    private Integer version; // Optimistic lock field
}

@Transactional
public void updateProduct(Long id, String newName) {
    Product product = entityManager.find(Product.class, id);
    product.setName(newName);
    // Hibernate automatically checks version on commit
    // Throws OptimisticLockException if version changed
}
```

<!-- Python (SQLAlchemy) -->
```python
# Python with SQLAlchemy
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric)
    version = Column(Integer, default=1)  # Version field

# Update with version check
def update_product(session, product_id, new_name):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        product.name = new_name
        product.version += 1
        try:
            session.commit()
        except StaleDataError:
            session.rollback()
            raise Exception("Product was modified by another transaction")
```

في المثال ده:
- نضيف `version` column في الـ table عشان نتابع التغييرات
- نستخدم `@Version` annotation في JPA/Hibernate
- نستخدم `version` field في SQLAlchemy
- كل الطرق دي بتكتشف الـ conflicts عن طريق مقارنة الـ version

بشكل عام، ممكن نقول أن Optimistic Locking يعتبر مناسبًا للـ Systems التي بتتطلب Concurrent Updates محدودة!


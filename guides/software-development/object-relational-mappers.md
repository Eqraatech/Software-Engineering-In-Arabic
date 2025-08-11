---
title: "Object Relational Mappers"
description: "Object Relational Mappers (ORMs) simplify database access by mapping objects in code to relational tables. This guide explains how ORMs work, their pros and cons, and when to use them in your projects."
excerpt: "ورقة وقلم وتعالوا نتكلم عن واحدة من أهم المفاهيم في عالم صناعة البرمجيات واللي مبسطة علينا حياتنا اليومية كمبرمجين  ألا وهي الـ ORMs - Object Relational Mappers."
tags: ["database", "ORMs", "web-development", "backend", "programming-language"]
updatedAt: "2024-04-25"
featured: false
image: "https://assets.eqraatech.com/guides/object-relational-mappers.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/object-relational-mappers.png" alt="Object Relational Mappers" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

ورقة وقلم وتعالوا نتكلم عن واحدة من أهم المفاهيم في عالم صناعة البرمجيات واللي مبسطة علينا حياتنا اليومية كمبرمجين  ألا وهي الـ `ORMs` - Object Relational Mappers

---

هنتكلم النهارده عن هي ايه و مميزاتها وعيوبها, ولكن خلونا نتفق إن شكل العناصر في عالم قاعدة البيانات مختلف عن عالم ال Backend ففي قواعد البيانات غالبًا بنتكلم في جداول وصفوف من البيانات في حالة الـ `SQL` أو البيانات تكون محطوطة في `Blobs or Documents` في حالة ال `NoSQL` 

بينما أثناء تصميم و كتابة ال Backend غالبًا بننظم البيانات ونتعامل معها على هيئة `Objects` ومش شرط كل البيانات في صف ما في ال Database  مثلاً تكون في Object واحد في الكود والعكس صحيح.

فلو بنحتفظ ببيانات الطالب في قاعدة البيانات هتكون على شكل صف أو عدد من الصفوف في جداول مختلفة ولكن في الكود البيانات دي علي شكل Object و بعد ما نستعيد البيانات من ال Database ب `SQL Query` لازم نعمل Mapping بين الاثنين بشكل يدوي! 

ولو كتبنا `Pseudocode` للعملية دي هتكون كدا:

```Java Dummy Example
String studentSql =  "select * from student where studentId=1";
studentData = db.query(StudentSql);
Student studentObject = new Student();
studentObject.setID(studentData[0]);
studentObject.setName(studentData[1]);
```

طبعًا دا `Pseudocode` مبسط كثير من الخطوات المتواجدة في عملية ال `Mapping` دي واللي ممكن تبقى طويلة وصعبة ومرهقة وتخيل هتضطر تعمل دا في كل مرة تروح تجيب فيها أي بيانات من ال Database عشان تكون في هيئة صالحة للاستخدام في الكود!

وهنا تيجي ال `ORM` وهي طريقة `Mapping` بين البيانات في قاعدة البيانات والـ `Code`, ال `ORM` بتكون مكتبة Library قادرة تفهم الكود و قاعدة البيانات وتعمل هي الـ `Mapping` دا بدل ما نضطر نعمله بشكل يدوي.

وكل دا بإني بعرف `Data Model` أو `Schema` لل `ORM` وهي بتبتدي تتعامل مع ال `Database`  بنفسها لتكوين وطلب البيانات منها.

---

## مثال عملي على الـ ORMs

خلينا نشوف مثال عملي على كيفية استخدام الـ ORMs في لغات البرمجة المختلفة:

<!-- Python (SQLAlchemy) -->
```python
# Python with SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

# Create and query
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)
session = Session()

# ORM handles the SQL mapping
student = session.query(Student).filter_by(id=1).first()
print(f"Student: {student.name}")
```

<!-- Java (JPA/Hibernate) -->
```java
// Java with JPA/Hibernate
@Entity
@Table(name = "students")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "name")
    private String name;
    
    @Column(name = "email")
    private String email;
    
    // Getters and setters
}

// Usage with Spring Data JPA
@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
    Student findById(Long id);
}

// Simple query - ORM generates SQL
Student student = studentRepository.findById(1L);
```

<!-- JavaScript (Prisma) -->
```javascript
// JavaScript with Prisma ORM
// schema.prisma
model Student {
  id    Int     @id @default(autoincrement())
  name  String
  email String
}

// Usage
const { PrismaClient } = require('@prisma/client')
const prisma = new PrismaClient()

// ORM handles SQL generation
const student = await prisma.student.findUnique({
  where: { id: 1 }
})

console.log(student.name)
```

في المثال ده:
- **SQLAlchemy** في Python بيعمل mapping بين الـ Python classes والـ database tables
- **JPA/Hibernate** في Java بيعمل mapping بين الـ Java entities والـ database
- **Prisma** في JavaScript بيعمل mapping بين الـ JavaScript objects والـ database
- كل الـ ORMs دي بتوليد الـ SQL queries تلقائياً بدل ما نكتبها يدوياً

---

الـ `ORM` قد ما بتوفر امكانيات جبارة في التعامل مع الـ Databases الا ان ليها بعض العيوب , واختيارها من عدمه بيعتمد على عوامل كتير وبتفرق على حجم وطبيعة الـ Business اللي شغال عليه , ولكن من العيوب القاتلة ليها إن أحيانا ناس كتير بتعتمد عليها وبتكون شاطرة فيها ولكن بتبخس حق دراسة الـ Database والـ Internals وبالتالي لو قابلهم مشكلة في الـ Performance أو أي مشاكل تضطرهم لكتابة `Raw SQL` ممكن مايعرفوش يتصرفوا وقتها .. فقد ما الـ `ORM` مفيدة محتاجين منتجاهلش دراسة الـ Databases عشان تبقى اداة الـ `ORM` وقتها اداة قوية واحنا اللي بنتحكم فيها مش هي اللي بتتحكم فينا.
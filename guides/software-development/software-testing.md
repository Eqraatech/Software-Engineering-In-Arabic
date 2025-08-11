---
title: "Software Testing"
description: "Software testing ensures code works as expected and meets requirements. This guide covers key types like unit, integration, system, and acceptance testing—helping improve quality, reliability, and user confidence."
excerpt: "أنت بتبقى مبسوط أوي وأنت بتكتب الكود, لحد ما تيجي لحظة الحقيقة وتبتدي في الـ Testing الحقيقة أنت ممكن تختبر أداء الكود اللي كتبته بأنواع كثيرة جدًا من الاختبارات, فتعالوا نتكلم عن خطوات اختبار البرمجيات بشكل عام وايه أهم الأنواع ليك كمبرمج."
tags: ["unit-testing", "TDD", "integration-testing", "web-development", "backend", "programming-language"]
updatedAt: "2023-12-04"
featured: false
image: "https://assets.eqraatech.com/guides/software-testing.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/software-testing.png" alt="Software Testing" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

أنت بتبقى مبسوط أوي وأنت بتكتب الكود, لحد ما تيجي لحظة الحقيقة وتبتدي في الـ Testing

الحقيقة أنت ممكن تختبر أداء الكود اللي كتبته بأنواع كثيرة جدًا من الاختبارات, فتعالوا نتكلم عن خطوات اختبار البرمجيات بشكل عام وايه أهم الأنواع ليك كمبرمج

مع اختلاف الأنواع فأكثر طريقة شائعة بتتكون من 3 خطوات:

### **(Given – When – Then) Testing Paradigm**

Given -> When -> Then 

1. **Given**: هنا هتحدد المعطيات أو الdata inputs اللي هتدخل ال function اللى حابب تختبر أدائها. حدد وجهز البيانات من حيث المضمون والشكل كويس سواء هي بيانات ثابتة أو بيانات يتم إنتاجها من function ثانية.
2. **When**: وهنا ستقوم بتنفيذ الfunction المطلوب اختبار أدائها على المعطيات 
3. **Expected**: وهنا بتقارن ال output اللي ظهر ليك مع النتيجة الصحيحة المتوقعة 

طلعوا نفس الشئ مبروك الكود بتاعك شغال, طلع فيه مشكلة فمبروك برضو نعرف غلطاتنا دلوقتي ونصلحها أحسن ما نتفاجئ بيها في الـ production. ودي أكبر ميزة في الـ testing أنه في أوقات كتير بيلفت نظرك ل edge case أو تصرف غير متوقع للكود بتاعك تحت data معينة.

ولذلك يفضل انك تختبر الحالات اللي الكود بيفشل بيها زي ما هتختبر الحالات اللي بينجح فيها

---

### **مثال**

أنا عندي كود يقوم بوظيفة بسيطة وهي قسمة رقمين على بعض نقدر نختبره بأكثر من حالة ناجحة زي:

- لو قسمت رقمين موجبين مفروض يطلع لي رقم موجب
- لو قسمت رقم سالب علي رقم موجب أو العكس مفروض يطلع رقم سالب 

ولكن في كمان حالة مفروض اختبرها ان الكود هيفشل يحلها: **لو قسمت رقم على الصفر مفروض الكود يـ Throw Numeric Exception** 

المثال دا عبارة عن unit test لأنك اختبرت أداء وحدة صغيرة من البرنامج كله, لكن في انواع كثيرة جدًا من الاختبارات من أهمها:

1. **Integration testing**: ودي بتختبر أداء وحدتين أو أكثر من البرنامج مع بعض, ولنقل حابب تختبر ال api endpoint + database عشان تتأكد انهم شغالين سوا بشكل سليم.
2. **System Testing**:هنا انت بتختبر النظام كله مع بعضه و النوع دا يتضمن طرق وتقنيات مختلفة لاختبار النظام بشكل شامل. 
3. **Load Testing**:وهنا بتختبر أقصي حدود تحمل البرنامج بتاعك اللي بعدها بيقع ومش بيقدر يشتغل بنفس الكفاءة.
4. **Security Testing**:مهم تختبر أمان البرنامج بتاعك تجاه الهجمات المختلفة أو تسريب البيانات والنوع دا كذلك يتضمن أكثر من نوع اختبار.

 أما بالنسبة لأكثر أنواع هتحتاج تكتبها كمبرمج وهي معروفة بال Testing Pyramid:  

- **Unit Tests** 
- **Integration Tests**
- **End to end Testing** (نوع من أنواع الـ system testing) في النوع دا أنت بتختبر flow أو مسار كامل داخل البرنامج, ولنقل بتختبر عملية الـ sign in العميل على الموقع من أول الداتا ما دخلت لحد ما اتخزنت ورجع response ليه.

بقية الأنواع بتكون غالبًا عمل جماعي سواء مع مبرمجين أو product managers، بل في شركات ممكن تعين software testers أو quality assurance engineers متخصصين بس لاختبار البرمجيات اللي بتنتجها و أوقات بتخصص فرق كاملة أو شركات أخرى متخصصة في نوع معين من الاختبارات بالأخص ال security testing.

---

## مثال عملي على Unit Testing

خلينا نشوف مثال عملي على اختبار دالة قسمة رقمين (division) في لغات برمجة مختلفة:

<!-- Python (pytest) -->
```python
# division.py
def divide(a, b):
    return a / b

# test_division.py
import pytest
from division import divide

def test_divide_positive():
    assert divide(6, 2) == 3

def test_divide_negative():
    assert divide(-6, 2) == -3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```

<!-- JavaScript (Jest) -->
```javascript
// division.js
function divide(a, b) {
  if (b === 0) throw new Error('Cannot divide by zero');
  return a / b;
}
module.exports = divide;

// division.test.js
const divide = require('./division');

test('divides two positive numbers', () => {
  expect(divide(6, 2)).toBe(3);
});
test('divides negative by positive', () => {
  expect(divide(-6, 2)).toBe(-3);
});
test('throws on divide by zero', () => {
  expect(() => divide(5, 0)).toThrow('Cannot divide by zero');
});
```

<!-- Java (JUnit) -->
```java
// Division.java
public class Division {
    public static double divide(double a, double b) {
        if (b == 0) throw new ArithmeticException("Cannot divide by zero");
        return a / b;
    }
}

// DivisionTest.java (JUnit 5)
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class DivisionTest {
    @Test
    void testDividePositive() {
        assertEquals(3, Division.divide(6, 2));
    }
    @Test
    void testDivideNegative() {
        assertEquals(-3, Division.divide(-6, 2));
    }
    @Test
    void testDivideByZero() {
        assertThrows(ArithmeticException.class, () -> Division.divide(5, 0));
    }
}
```

في المثال ده:
- بنختبر حالات النجاح (قسمة أرقام موجبة وسالبة)
- بنختبر حالة الخطأ (قسمة على صفر)
- بنستخدم أدوات اختبار شائعة في كل لغة
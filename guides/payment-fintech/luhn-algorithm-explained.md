---
title: "Luhn Algorithm Explained"
description: "The Luhn algorithm is a simple checksum formula used to validate identification numbers like credit cards. This guide explains how it works, why it’s used, and walks through an example of detecting invalid numbers."
excerpt: "خوارزمية Luhn هي طريقة بسيطة للتحقق من صحة أرقام البطاقات زي بطاقات الائتمان. بتشتغل عن طريق حساب Checksum وتتأكد إن الرقم صالح أو لأ. في الدليل ده هنعرف إزاي بتشتغل وليه بتستخدم، مع مثال عملي للتوضيح."
tags: ["fintech", "payment", "backend"]
updatedAt: "2025-08-19"
featured: false
image: "https://assets.eqraatech.com/guides/luhn-algorithm-explained.png"
author: "alaaelkazaz"
resourcesfreeResources: [
    {type: "مقال", title: "What is the Luhn algorithm and how does it work?", link: "https://stripe.com/en-nl/resources/more/how-to-use-the-luhn-algorithm-a-guide-in-applications-for-businesses"},
]
---

<img src="https://assets.eqraatech.com/guides/luhn-algorithm-explained.png" alt="Luhn Algorithm Explained" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

استكمالاً لكلامنا عن أساسيات ال Fintech هنتكلم النهارده عن خوارزمية لوهن (Luhn Algorithm) أو Mod 10 Algorithm وهي خوارزمية رياضية بسيطة طورها العالم الألماني "هانز لوهن"في الخمسينات، وبنستخدمها بشكل كبير في أنظمة التحقق من صحة أرقام البطاقات البنكية زي ال Debit/Credit 

---

الهدف الأساسي من الخوارزمية دي هو اكتشاف الأخطاء البسيطة اللي ممكن تحصل وأنت بتدخل رقم البطاقة، زي كتابة رقم غلط أو تبديل رقمين. ومش بيقتصر استخدامها بس في عالم ال Fintech ولكن كثير من الجهات الحكومية ممكن تستخدمها في التحقق من الأرقام الرسمية اللي بتصدرها للبطاقات والمستندات.

الخوارزمية مش مصممة علشان تمنع الاحتيال، لكن دورها الأساسي هو التأكد إن الرقم المُدخل متوافق مع قواعد تكوين أرقام البطاقات، وده بيساعد كتير في التحقق المبدئي وبنقوم بتنبيه المستخدم في ال Frontend عشان يصلح الرقم قبل إرسال البيانات لل Payment Processor. طبعًا الاكتشاف المبكر للخطأ بيوفر علينا Processing Costs وبيوفر علينا Requests رايحة جاية. 
### ****خطوات خوارزمية Luhn:****

1. ابدأ من الرقم الأخير على اليمين (أقصى اليمين).
2. كل رقم في ****موقع فردي**** (من اليمين) سيبه زى ما هو.
3. كل رقم في ****موقع زوجي**** (من اليمين) ضاعفه.
4. لو الرقم الناتج من التضعيف أكبر من 9، اجمع الرقمين (مثال: 7 × 2 = 14 → 1 + 4 = 5).
5. اجمع كل الأرقام الناتجة مع بعض.
6. لو المجموع النهائي ****بيقبل القسمة على 10**** بدون باقي، يبقى رقم البطاقة صحيح.

تنفيذ الخوارزمية كود سهل و أغلب الوقت بنستخدمها في ال Frontend عشان تدينا Real-time feedback عن صحة الرقم, ولكن يمكن استخدامها أيضًا في ال Backend كخطوة تحقق إضافية

مثال على تطبيق الخوارزمية باستخدام لغات برمجة مختلفة

<!-- JavaScript -->
```javascript
function isValidCardNumber(cardNumber) {
    // إزالة أي مسافات من الرقم
    const sanitized = cardNumber.replace(/\s+/g, '');

    let sum = 0;
    let shouldDouble = false;

    // نبدأ من آخر رقم ونتجه لليسار
    for (let i = sanitized.length - 1; i >= 0; i--) {
        let digit = parseInt(sanitized[i]);

        if (shouldDouble) {
            digit *= 2;
            if (digit > 9) digit -= 9;
        }

        sum += digit;
        shouldDouble = !shouldDouble;
    }

    // إذا كان المجموع يقبل القسمة على 10 → الرقم صحيح
    return sum % 10 === 0;
}

// أمثلة للاختبار:
console.log(isValidCardNumber("4111 1111 1111 1111")); // true
console.log(isValidCardNumber("1234 5678 9012 3456")); // false
```

<!-- Python -->
```python
def is_valid_card_number(card_number):
    # إزالة أي مسافات من الرقم
    sanitized = card_number.replace(" ", "")
    
    if not sanitized.isdigit():
        return False
    
    sum_digits = 0
    should_double = False
    
    # نبدأ من آخر رقم ونتجه لليسار
    for digit in reversed(sanitized):
        digit_int = int(digit)
        
        if should_double:
            digit_int *= 2
            if digit_int > 9:
                digit_int = digit_int // 10 + digit_int % 10
        
        sum_digits += digit_int
        should_double = not should_double
    
    # إذا كان المجموع يقبل القسمة على 10 → الرقم صحيح
    return sum_digits % 10 == 0

# أمثلة للاختبار:
print(is_valid_card_number("4111 1111 1111 1111"))  # True
print(is_valid_card_number("1234 5678 9012 3456"))  # False
```

<!-- Java -->
```java
public class LuhnAlgorithm {
    public static boolean isValidCardNumber(String cardNumber) {
        // إزالة أي مسافات من الرقم
        String sanitized = cardNumber.replaceAll("\\s+", "");
        
        if (!sanitized.matches("\\d+")) {
            return false;
        }
        
        int sum = 0;
        boolean shouldDouble = false;
        
        // نبدأ من آخر رقم ونتجه لليسار
        for (int i = sanitized.length() - 1; i >= 0; i--) {
            int digit = Character.getNumericValue(sanitized.charAt(i));
            
            if (shouldDouble) {
                digit *= 2;
                if (digit > 9) {
                    digit = digit / 10 + digit % 10;
                }
            }
            
            sum += digit;
            shouldDouble = !shouldDouble;
        }
        
        // إذا كان المجموع يقبل القسمة على 10 → الرقم صحيح
        return sum % 10 == 0;
    }
    
    public static void main(String[] args) {
        // أمثلة للاختبار:
        System.out.println(isValidCardNumber("4111 1111 1111 1111")); // true
        System.out.println(isValidCardNumber("1234 5678 9012 3456")); // false
    }
}
```

---

## في الختام

الجدير بالذكر إن الخوارزمية زي ما قولنا ليها Limitations فهي تقدر تقول إن تسلسل معين من الأرقام صحيح ولكن مش بالضرورة يكون رقم بطاقة صالح لأنها بتعتمد إنها تكشف عن تبديل رقمين بالغلط لكن لو بدلت أكثر من رقم ورا بعض فممكن التبديل دا ينتج عنه رقم صحيح بالنهاية. نشوفكم في ورقة جديدة باذن الله سلام 👋
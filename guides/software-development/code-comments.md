---
title: "Code Comments"
description: "Code comments explain the why behind your code. This guide covers best practices for writing clear, helpful comments that improve readability without repeating what the code already says."
excerpt: "الكود الكويس بيشرح نفسه… لكن أحيانًا، الـ Comment الصح هو اللي بيفرق بين كود مفهوم، وكود يخليك محتار لمدة ساعة. فخلونا نعرف إزاي نكتب Comments تضيف قيمة، من غير ما نكرر اللي الكود بيقوله، ولا نسيب ملاحظات مبهمة مالهاش معنى."
tags: ["refactoring", "clean-code", "code-comments","web-development", "backend", "frontend", "programming-language"]
updatedAt: "2024-02-01"
featured: false
image: "https://assets.eqraatech.com/guides/code-comments.png"
author: "ikhaledabdelfattah"
---

<img src="https://assets.eqraatech.com/guides/code-comments.png" alt="Code Comments" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

  ورقه وقلم و خلينا نتكلم عن توثيق المشروع الخاص بك (Documentation)، أولاً وقبل كل شيء، فيه طرق كتير علشان تساعدك توثق مشروعك البرمجي منها (READMEs, Code Comments, How-to guides, tutorials, getting started guide, API documentation) وغيرهم كتير. لكن خلينا النهارده ندردش شويه عن نوع واحد وهو الجزء اللي بيكون مخفي بين سطور الكود، واللي ممكن يكون سر نجاح أو فشل المشروع في التواصل مع المطورين الآخرين وهو Code Comments.

---

### **الهدف الرئيسي من الCode Comments**

الهدف الرئيسي من ال Code Comments هو إنارة الطريق للي هيشوف الكود بعدك، يعني تخليه يفهم ليه اخترت الطريق ده  او ليه استخدمنا طريقه معينه او الجورزم معين    مش ازاي نفذته , لان ببساطة إجابة سوال ازاي نفذت الفكره أنت مجاوب عليه في الكود 😄( ولا أنت مش كاتب Clean Code👀). مثال: 

- ❌ looping over the list to print items
- ✅ looping over the list to filter and display only relevant data

### **توضيح Function أو Concept معقد**

لو بتوضح Function أو Concept معقد، حط مثال على شكل الOutput المتوقع، ده هيسهل على اللي بعدك يفهم المطلوب بشكل أسرع.

- ❌ the function calculates tax
- ✅ the function calculates tax, e.g., input 100, output will be 115 with 15% tax

### الدقة في الكتابة وتحديث التعليقات باستمرار

من الأمور المهمة كمان، إنك تكون دقيق وتحدث التعليقات دايمًا. لو عدلت في الكود، يبقى لازم تعدل في التعليقات كمان. تخيل لو معملتش كده، اللي هيجي بعدك هيتلخبط وممكن يبني على معلومات غلط!

### الطول المناسب للتعليق

متطولش أوي في التعليقات اللي بتكتبها. خليك مختصر وواضح، واشرح الأجزاء المعقدة بس، مش كل سطر كود كتبته. لأن ببساطة التعليقات الكتير ممكن تخلي فيه زحمة في الكود وده يخليه صعب القراءة.

   - ❌ this code checks the value of x then compares it with y and then prints the result if it's greater`
   - ✅ evaluate x against y and print if x is greater`

### كتابة التعليقات في وقت كتابة الكود وليس بعدها! 

حاول دايما تكتب التعليقات وانت بتكتب الكود , مش بعد ما تخلص الكتابة ده هيساعدك علي انك تتجنب النسيان او تفاصيل مهمة

---

## مثال عملي على كتابة الـ Code Comments

خلينا نشوف مثال عملي على كيفية كتابة الـ Comments بشكل صحيح في لغات البرمجة المختلفة:

<!-- Java -->
```java
// BAD COMMENTS - Poor examples
// loop through the list
for (int i = 0; i < users.size(); i++) {
    User user = users.get(i);
    System.out.println(user.getName());
}

// calculate tax
double tax = amount * 0.15;

// GOOD COMMENTS - Best practices
/**
 * Filters active users and sends them promotional emails
 * Only processes users who haven't received emails in the last 30 days
 * to avoid spam and comply with email regulations
 */
public void sendPromotionalEmails(List<User> users) {
    // Filter users who are active and haven't received emails recently
    List<User> eligibleUsers = users.stream()
        .filter(user -> user.isActive() && !hasRecentEmail(user))
        .collect(Collectors.toList());
    
    // Calculate tax with regional variations
    // Tax rates: 15% for standard, 20% for luxury items, 0% for essentials
    double taxRate = getTaxRate(item.getCategory(), user.getRegion());
    double tax = amount * taxRate;
    
    // TODO: Implement retry mechanism for failed email sends
    // This will help handle temporary email service outages
}
```

<!-- Python -->
```python
# BAD COMMENTS - Poor examples
# loop through the list
for user in users:
    print(user.name)

# calculate tax
tax = amount * 0.15

# GOOD COMMENTS - Best practices
def send_promotional_emails(users):
    """
    Filters active users and sends them promotional emails.
    
    Only processes users who haven't received emails in the last 30 days
    to avoid spam and comply with email regulations.
    
    Args:
        users: List of user objects to process
        
    Returns:
        int: Number of emails successfully sent
    """
    # Filter users who are active and haven't received emails recently
    eligible_users = [user for user in users 
                     if user.is_active and not has_recent_email(user)]
    
    # Calculate tax with regional variations
    # Tax rates: 15% for standard, 20% for luxury items, 0% for essentials
    tax_rate = get_tax_rate(item.category, user.region)
    tax = amount * tax_rate
    
    # TODO: Implement retry mechanism for failed email sends
    # This will help handle temporary email service outages
```

<!-- JavaScript -->
```javascript
// BAD COMMENTS - Poor examples
// loop through the list
for (let i = 0; i < users.length; i++) {
    console.log(users[i].name);
}

// calculate tax
const tax = amount * 0.15;

// GOOD COMMENTS - Best practices
/**
 * Filters active users and sends them promotional emails
 * Only processes users who haven't received emails in the last 30 days
 * to avoid spam and comply with email regulations
 * 
 * @param {Array} users - List of user objects to process
 * @returns {number} Number of emails successfully sent
 */
function sendPromotionalEmails(users) {
    // Filter users who are active and haven't received emails recently
    const eligibleUsers = users.filter(user => 
        user.isActive && !hasRecentEmail(user)
    );
    
    // Calculate tax with regional variations
    // Tax rates: 15% for standard, 20% for luxury items, 0% for essentials
    const taxRate = getTaxRate(item.category, user.region);
    const tax = amount * taxRate;
    
    // TODO: Implement retry mechanism for failed email sends
    // This will help handle temporary email service outages
}
```

في المثال ده:
- **BAD COMMENTS**: يوضح أمثلة سيئة للـ comments
- **GOOD COMMENTS**: يوضح أفضل الممارسات مع:
  - شرح الـ "Why" وليس الـ "How"
  - استخدام الـ Docstrings للـ functions
  - إضافة Context مفيد للـ business logic
  - استخدام الـ TODO comments للمهام المستقبلية

---

### في الختام

وهنا بقى نيجي لنقطة جدال كبيرة في عالم التكنولوجيا. فيه ناس كتير بتقول إن الCode Comment هو مجرد عذر لكود مكتوب بشكل مش منظم أو مش واضح، وإن الكود المكتوب كويس لازم يكون شارح نفسه بنفسه، وده اللي بيسموه "Self-Documenting Code". 

واللي ميعرفش ايه هو ال Self-Documenting Code فهو مفهوم في عالم البرمجة بيتكلم عن كتابة الكود بطريقة تخليه يشرح نفسه بنفسه من غير الاحتياج  لتعليقات مفصلة. الهدف من الكود الذاتي التوثيق هو تحقيق الوضوح والفهم السريع للكود من قبل المطورين الآخرين، منها  استخدام أسماء متغيرات ودوال واضحة ومعبره.

وأنا هنا بسألك، إيه رأيك في الكلام ده؟ هل أنت مع الفريق اللي بيقول التعليقات مهمة ولا الفريق اللي بيقول لو الكود كويس مش هيحتاج تعليقات؟ شاركنا برأيك في التعليقات، ويلا نفتح النقاش!
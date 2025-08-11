---
title: "How to Write Better Logs"
description: "Good logs make debugging easier. This guide covers best practices like using clear messages, consistent formats, log levels, and including context—so you can trace issues faster and improve observability."
excerpt: "الـ Logs مش مجرد سطور بتتطبع في الكونسول — دي شريان الحياة لأي نظام في الـ Production ، فلما تحصل مشكلة، أو الأداء يبقى بطيء، أو حد يسأل (إيه اللي حصل؟)، أول حاجة بنرجعلها هي الـ Logs. لكن… مش أي Log ينفع."
tags: ["logs", "observability", "traces", "web-development", "backend", "programming-language"]
updatedAt: "2024-02-07"
featured: true
image: "https://assets.eqraatech.com/guides/how-to-write-better-logs.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/how-to-write-better-logs.png" alt="How to Write Better Logs" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

ال logs من أساسيات شغلنا كمبرمجين بل تكاد تكون جزء يومي ولكنها من أهم الأمثلة على قاعدة "السهل الممتنع". فنعم كل المبرمجين بيستخدموها من أول الطلبة لل  principles engineers لكن عدد قليل جدًا اللي قادر يوظفها ويكتبها بشكل فعّال.

فورقة وقلم وتعالوا نشوف ازاي نكتب logs حلوة 😌

**أولاً لازم نعرف أننا بنتعامل يوميًا مع نوعين من الـ Logs:**

- ال **Infrastructure logs** ودي اللي بينتجها ال server or operating system or network devices 
-  ال **Application code logs** ودا اللي هنتكلم عليه دايمًا لأنه كمبرمج بكتبه بشكل شبه يومي وأنا أول واحد ينتفع أو يٌضر بيه.

### **أهداف كتابة ال Logs** 

💡

الهدف الأساسي لأي logs إنها تدينا Better observability أو رؤية أفضل على النظام بشكل عام وتمكنا من مراقبة ال events و المشاكل المهمة وتجميع معلومات عنها وبالتالي حلها أو تحسين أداء النظام.

ودا بنلجأ له لما بنشغل ال service علي آل production environment وقتها مش بنقدر نعملها debug وبالتالي متقدرش تتبع مسار البيانات وهي دخلت في انهي سيناريو داخل الكود وانهي لاء , وكذلك مش كل الناس عندها صلاحية دخول لل Codebase زي ال Tech support engineers مثلاً, في الحالات دي بيكون اعتمادنا على الـ logs -وأشياء أخري- عشان نقدر نتتبع رحلة البيانات داخل ال service ونستخدمها عشان نحل مشكلة أو سيناريو غير متوقع أو نحسن من ال service وأدائها.

فقبل ما أكتب أي Log line لازم أجاوب على السؤال: هل كتابة ال log line دا هتديني رؤية أفضل على سلوك التطبيق أو النظام؟

---

### **ما هي الـ Events التي يجب تسجيلها في ال Logs؟**

ال application logs بنستخدمها عشان نتابع أداء النظام بشكل عام, ولكن أكيد هنكون مهتمين أكثر بأننا نعمل log لو حصل مشكلة فلذلك أغلب ال log lines بتكون مرتبطة ب `Error` من نوع ما, لكن كذلك بنستخدمها لتسجيل معلومات عشان نتأكد أن البيانات عدت بمراحل معينة من ال Processing 

ودي قائمة بأمثلة عن ال `events` اللي من المفيد نعملها `logging`:

- Application errors
- Input and output validation failures
- Authentication successes and failures
- Authorization failures
- Session management failures
- Monitoring and performance improvement
- Security and auditing

---

### **ما هي البيانات التي يجب كتابتها** عن **الـ Events التي نسجلها؟**

ال `logs` لازم تكون معبّرة وفيها المعلومات اللي محتاجها عشان أفهم الغرض منه و لو كان في مشكلة أقدر أحلها,لأن في الـ `Production` مش هنلاقي `Debugger`  يتتبعلي البيانات فمن أهم المعلومات اللي لازم يتضمنها ال log line:

- **النوع:** هل ال `log line` دا عبارة عن معلومة بستخدمها في ال `audit` ولا هو عبارة عن `Error` ولا `Warning`. النوع يشار إليه باسم ال `Log level` وأساسي نعرف نفرق بينهم وبنستخدمها امتي وهتلاقوا أمثلة على كتابتها مع رسالة واضحة في الرسم
- **الوقت**: وقت حدوث ال `event` اللي بعمله `Log`
- **المكان**: لازم اقدر استدل منه علي ال `service` أو الـ `class` اللي أنتجته أو حصل فيها ال `event`  
- **الرسالة أو الوصف:** وتكون رسالة واضحة وقادرة توضح للقارئ فايدة الـ `log line`

### ما هي أنواع ال Log Lines

أنواع سطور ال `Log` تعرف باسم ال `Log Levels` وهي بتوضح نوع المعلومة اللي بيوفرها ال `log line` ولكن كذلك بتوضح أهميته وأولويته أثناء حل المشكلات وبالتالي مهم نعرف الاستخدام الصحيح لكل `level`:

- **Debug** ودا بنستخدمه كمبرمجين عشان يساعدنا نفهم الكود
- **Info** ودا بنستخدمه عشان نعمل `logging` لمعلومة عن أداء النظام الطبيعي 
- **Warn** ودا هنستخدمه وقت ما يكون في حدث ممكن يسبب مشكلة أو خطأ فيما بعد  زي `in-memory cache near limit`  أو `function retries` 
- **Error**  بنستخدمه وقت حدوث خطأ أو حصل `Exception` في مسار من مسارات البرنامج لكن يقدر البرنامج يكمل شغل 
- **Fatal** ودا استخدامه وقت حدوث خطأ يمنع استكمال البرنامج أو بيقفل ال Service تمامًا عن العمل ودا طبعًا استخدامه قليل نسبيًا

---

### البيانات التي لا يجب تضمينها داخل ال Logs 

ال `logs` زي ما هي أداة مفيدة جدًا لكنها ممكن تصبح نقطة ضعف أو ثغرة لأنها زي ما بتوفرلنا معلومات عن أداء النظام ممكن يتم استخدامها لسرقة بيانات أو اكتشاف ثغرات تؤدي لاختراق النظام فيما بعد,بل أن في أنواع مخصصة من ال attacks بتستهدف ال logging system الخاص بال service بتاعتك لأنها بالنسبة لل attacker كنز من المعلومات. فاحرص دومًا انك متعملش `log` لأي بيانات حساسة أو أجزاء من الكود, من أهم الأشياء التي لا يجب أن تُكتب في الـ logs:

-  أي معلومات بنكية أو حساسة تتعلق بالمستخدمين
- أي معلومات لا يجوز تجميعها عن المستخدم تبعًا لقوانين ولوائح حماية المستخدم
- ال `access tokens` الخاصة بالمستخدمين 
- ال `session ids` وعشان تقدر تتبع ال `session` تقدر تستخدم نسخة `hashed` لل `session id` بداخل ال `log` 
- ال `Source code`

---

## مثال عملي على كتابة الـ Logs

خلينا نشوف مثال عملي على كيفية كتابة الـ Logs بشكل صحيح في لغات البرمجة المختلفة:

<!-- Java (SLF4J) -->
```java
// BAD LOGGING - Poor examples
System.out.println("Error happened");
System.out.println("Order created with ID: " + order.getId() + " and amount: " + order.getAmount());
System.out.println("Processing payment...");

// GOOD LOGGING - Best practices
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class OrderService {
    private static final Logger logger = LoggerFactory.getLogger(OrderService.class);
    
    public void createOrder(OrderRequest request) {
        logger.info("Creating order for customer: {}", request.getCustomerId());
        
        try {
            // Process order creation
            logger.debug("Processing order with items: {}", request.getItems().size());
            
            Order order = orderRepository.save(request);
            logger.info("Order created successfully: {}", order.getId());
            
        } catch (PaymentException e) {
            logger.error("Payment processing failed for order: {}", request.getOrderId(), e);
            throw e;
        } catch (Exception e) {
            logger.error("Unexpected error creating order for customer: {}", request.getCustomerId(), e);
            throw new OrderCreationException("Failed to create order", e);
        }
    }
    
    public void retryPayment(String orderId, int attempt) {
        logger.warn("Retrying payment for order: {}, attempt: {}", orderId, attempt);
        
        if (attempt > 3) {
            logger.error("Max retry attempts reached for order: {}", orderId);
            return;
        }
        
        // Retry logic
        logger.debug("Processing payment retry attempt: {}", attempt);
    }
}
```

<!-- Python -->
```python
# BAD LOGGING - Poor examples
print("Error occurred")
print(f"Order {order.id} created with amount {order.amount}")
print("Processing...")

# GOOD LOGGING - Best practices
import logging

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_order(customer_id, items):
    logger.info("Creating order for customer: %s", customer_id)
    
    try:
        # Process order creation
        logger.debug("Processing order with %d items", len(items))
        
        order = order_repository.save(customer_id, items)
        logger.info("Order created successfully: %s", order.id)
        
    except PaymentError as e:
        logger.error("Payment processing failed for customer: %s", customer_id, exc_info=True)
        raise
    except Exception as e:
        logger.error("Unexpected error creating order for customer: %s", customer_id, exc_info=True)
        raise OrderCreationError("Failed to create order") from e

def retry_payment(order_id, attempt):
    logger.warning("Retrying payment for order: %s, attempt: %d", order_id, attempt)
    
    if attempt > 3:
        logger.error("Max retry attempts reached for order: %s", order_id)
        return
    
    # Retry logic
    logger.debug("Processing payment retry attempt: %d", attempt)
```

<!-- JavaScript (Winston) -->
```javascript
// BAD LOGGING - Poor examples
console.log("Error happened");
console.log("Order " + order.id + " created with amount " + order.amount);
console.log("Processing...");

// GOOD LOGGING - Best practices
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

async function createOrder(customerId, items) {
  logger.info('Creating order', { customerId, itemCount: items.length });
  
  try {
    // Process order creation
    logger.debug('Processing order creation', { customerId });
    
    const order = await orderRepository.save({ customerId, items });
    logger.info('Order created successfully', { orderId: order.id, customerId });
    
  } catch (error) {
    if (error.name === 'PaymentError') {
      logger.error('Payment processing failed', { customerId, error: error.message });
    } else {
      logger.error('Unexpected error creating order', { customerId, error: error.message });
    }
    throw error;
  }
}

function retryPayment(orderId, attempt) {
  logger.warn('Retrying payment', { orderId, attempt });
  
  if (attempt > 3) {
    logger.error('Max retry attempts reached', { orderId });
    return;
  }
  
  // Retry logic
  logger.debug('Processing payment retry', { orderId, attempt });
}
```

في المثال ده:
- **BAD LOGGING**: يوضح أمثلة سيئة للـ logging
- **GOOD LOGGING**: يوضح أفضل الممارسات مع:
  - استخدام الـ Log Levels المناسبة
  - عدم تسجيل البيانات الحساسة
  - إضافة Context مفيد
  - استخدام Structured Logging

---

في الورقة دي حاولنا نجمع أهم ما تحتاج معرفته عشان تكتب `log lines` بكفاءة ولكن كما البرمجة هي مهارة فاستغل المعرفة دي كنقطة بداية واتدرب علي كتابة `logs` أحسن واتناقش مع زملاء الفريق ازاي تحسنوا من ال `logging` في مشاريعكم وتتفقوا علي طريقة موحدة في كتابة ال `logs` وهتلمس أثر دا في تسهيل حل أي مشكلة بتحتاج تلجأ فيها ل ال `logs`.
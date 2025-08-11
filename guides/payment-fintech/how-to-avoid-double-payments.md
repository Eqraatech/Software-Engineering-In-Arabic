---
title: "How to Avoid Double Payments"
description: "Preventing double payments is critical in financial systems. This guide covers key techniques like idempotency keys, transaction locks, and proper database handling to ensure safe and accurate payment processing."
excerpt: "أحد أكبر المشاكل اللي ممكن نواجهها في تصميم الأنظمة الخاصة بالدفع , والمعاملات المالية هي أنك تدفع العميل أكتر من مرة, وعشان كده واحنا بنصمم Payment System محتاجين ناخد في الاعتبار ان عملية الدفع لازم نضمن انها هتتم مرة واحدة فقط لا غير."
tags: ["idempotency", "retry", "backend", "system-design", "microservices", "web-development", "distributed-transactions"]
updatedAt: "2024-06-28"
featured: true
image: "https://assets.eqraatech.com/guides/how-to-avoid-double-payments.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/how-to-avoid-double-payments.png" alt="How to Avoid Double Payments" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

أحد أكبر المشاكل اللي ممكن نواجهها في تصميم الأنظمة الخاصة بالدفع , والمعاملات المالية هي أنك تدفع العميل أكتر من مرة, وعشان كده واحنا بنصمم Payment System محتاجين ناخد في الاعتبار ان عملية الدفع لازم نضمن انها هتتم مرة واحدة فقط لا غير.

وطبعًا عشان نحقق الضمان ده واللي بنسميه `Exactly-Once Delivery` بيقابلنا تحديات مش سهلة خصوصًا لو بنتعامل كمان مع Distributed Systems.

---

## المعادلة الرياضية

لو جينا نبص للمشكلة اللي بنواجهها دي رياضيًا فالمفترض عشان نقول أن فيه حاجة تتم مرة واحدة بس فده معناه انها بتطبق الشروط دي:

1. **اتنفذت على الأقل مرة**
2. **اتنفذت كحد أقصى مرة**

يعني ايه الكلام الغريب ده باه ؟

بكل بساطة عشان نعالج مشكلة الـ Double Payment واننا منخليش الـ Customer يتحاسب مرتين أو أكتر, احنا عاوزين طريقة نضمن بيها , ان عملية الدفع على الأقل حصلت مرة .. وفي نفس الوقت نضمن أنها متحصلش أكتر من مرة عشان ميتحاسبش مرتين أو أكتر.

**وعشان نحقق ده هنستعمل:**

1. الـ `Retryer` عشان نضمن أول شرط ان عملية الدفع على الأقل حصلت مرة.
2. الـ `Idempotency Key` عشان نضمن تاني شرط وهو أن عملية الدفع ما تحصلش أكتر من مرة.

---

## Retryer

من خلال استعمالنا للـ `Retryer` كده احنا هنضمن أن لو حصل أي مشكلة في عملية الدفع , سواء كانت مشكلة `Network` أو `Timeout` مثلًا أو `Server Failure` أو أيا كان السبب ايه .. فاحنا ضامنين أن عملية الدفع هيتعاد تنفيذها تاني لحد ما تنجح وبالتالي هنا احنا بنحقق أول شرط الا وهو الـ `At Least Once Delivery`.

فكده احنا حققنا أول شرط وضمنا ان لو حصل أي مشكلة في الدفع , هنحاول أكتر من مرة لحد مالعملية تنجح , فعلى الأقل مرة واحدة هتنجح.

فاحنا لو بنحاول نشتري حاجة بـ 100 جنيه , والعملية دي فشلت , ممكن نفضل نحاول لحد ما تنجح ..

---

طب ماذا لو نجحت , وحاولنا مرة تانية بالخطأ ؟ أو حصل هنا ان اتبعت Retrying تاني بعد ما العملية نجحت ؟ هنا هنروح لتاني حل وهو الـ `Idempotency` Key عشان نضمن أننا منقعش في المشكلة دي وندفع الـ Customer أكتر من مرة.

---

## Idempotency Key

يعني ايه Idempotency ؟

الـ `Idempotency` معناها من وجهة نظر الـ `APIs` ان الـ `Request` مهما اتبعت هيلاقي نفس النتيجة فعشان كده مثلا بنقول أن الـ `POST Request` مش `Idempotent` لانه مع كل `Request` مش هيحصل على نفس النتائج عكس الـ `GET` على سبيل المثال.

الـ `Idempotency Key` محتاجين انه يكون Unique زي ما شوفنا عشان الـ Server يقدر يميز بين كل عملية دفع والتانية , وبالتالي الشائع في أغلب الشركات زي Stripe , PayPal وغيرهم كتير هو استعمال الـ `UUID`.

طب الـ `Idempotency Key` ده بيتبعت ازاي ؟

المتعارف عليه والشائع انه الـ Client هو اللي بيعمله Generate وبيكون بـ `Expiry` معينة على سبيل المثال فبعد وقت محدد بيحصله `Expiration` و بيتبعت في الـ `Request Headers` وبيكون بالشكل الآتي :

<!-- JavaScript Client -->
```javascript
// Client-side implementation
const idempotencyKey = crypto.randomUUID();

const paymentRequest = {
  amount: 100,
  currency: 'USD',
  customerId: 'cust_123'
};

fetch('/api/payments', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Idempotency-Key': idempotencyKey
  },
  body: JSON.stringify(paymentRequest)
});
```

<!-- Python Server -->
```python
# Server-side implementation with Redis
import redis
import uuid
import json

class PaymentService:
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    def process_payment(self, payment_data, idempotency_key):
        # Check if we've already processed this request
        if self.redis_client.exists(f"payment:{idempotency_key}"):
            return self.redis_client.get(f"payment:{idempotency_key}")
        
        # Process payment
        payment_result = self._execute_payment(payment_data)
        
        # Store result with expiration (24 hours)
        self.redis_client.setex(
            f"payment:{idempotency_key}",
            86400,  # 24 hours
            json.dumps(payment_result)
        )
        
        return payment_result
```

<!-- Java Spring -->
```java
// Database-based idempotency check
@Service
public class PaymentService {
    
    @Autowired
    private PaymentRepository paymentRepository;
    
    @Transactional
    public PaymentResult processPayment(PaymentRequest request, String idempotencyKey) {
        // Check if payment with this key already exists
        Optional<Payment> existingPayment = paymentRepository
            .findByIdempotencyKey(idempotencyKey);
        
        if (existingPayment.isPresent()) {
            return existingPayment.get().getResult();
        }
        
        // Create new payment record
        Payment payment = new Payment();
        payment.setIdempotencyKey(idempotencyKey);
        payment.setAmount(request.getAmount());
        payment.setStatus("PROCESSING");
        
        // Process payment logic here...
        PaymentResult result = executePayment(request);
        
        payment.setStatus("COMPLETED");
        payment.setResult(result);
        paymentRepository.save(payment);
        
        return result;
    }
}
```
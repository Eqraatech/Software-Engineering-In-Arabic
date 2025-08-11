---
title: "LLMs With Ollama"
description: "Ollama makes it easy to run and manage Large Language Models locally. This guide introduces how to get started with LLMs using Ollama for fast, private, and customizable AI workflows."
excerpt: "مشروع مفتوح المصدر هدفه الأساسي أنه يسهل عليك تشغيل الـ AI Models الكبيرة مثل ال LLMs (Large Language Models) علي جهازك الشخصي بدون إنترنت بدلاً من تشغيلها على الـ Cloud."
tags: ["AI", "LLMs", "machine-learning", "ollama"]
updatedAt: "2025-04-04"
featured: false
image: "https://assets.eqraatech.com/guides/llms-with-ollama.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/llms-with-ollama.png" alt="LLMs With Ollama" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

يعتبر `Ollam`a` مشروع مفتوح المصدر هدفه الأساسي أنه يسهل عليك تشغيل الـ AI Models الكبيرة مثل ال `LLMs` (Large Language Models) علي جهازك الشخصي بدون إنترنت بدلاً من تشغيلها على الـ Cloud.

---

## **مميزات Ollama**

- **لا يحتاج إلى الانترنت:** يمكنك استخدامه على جهازك الشخصي بعد تحميله بدون انترنت وهذه خاصية هامة للمطورين الذين يتعاملون مع بيانات حساسة والشركات التي تهتم بخصوصية بياناتها.
- **يدعم نماذج متعددة:** يمكنك تشغيل أنواع كثيرة من النماذج عليه مثل **Llama 2، Mistral، Gemma، و Code Llama** بسهولة وهذه المكتبة يتم تحديثها باستمرار فتقدر حتى تشغل `deepseek` عليه!
- **سهولة الاستخدام:** بيقدم Command Line Interface CLI بسيطة وتقدر تشغل النموذج بسطر واحد فقط

---

## **استخدامات Ollama**

- **إنشاء Local Chatbots:** يمكنك من تدريب Chatbots علي بيانات خاصة مما يجعلها تعطي إجابات أدق وأسرع وتشغيلها علي Local Servers
- **تطوير Privacy-focused AI Applications:**في شركات كثيرة تتعامل مع بيانات خاصة لا يمكنها تدريب النماذج السحابية عليها لأن ذلك يعرض بيانتها وبيانات عملائها للخطر مثل الشركات التي تعمل في مجال القانون والقطاع المالي

**الأبحاث وتطوير النماذج:** يستخدمه العديد من مطورين الذكاء الاصطناعي لإنشاء وتدريب النماذج على بيانات معينة وتقييم أدائها.

---

## **كيف يمكن استخدامه؟**

تحميله على نظام تشغيلك الشخصي **mac OS، Linux، و Windows**.

تشغيل النماذج بأوامر بسيطة مثل:

```bash
ollama run llama2
```

يمكن للمبرمجين دمجه في تطبيقاتهم باستخدام الـ APIs
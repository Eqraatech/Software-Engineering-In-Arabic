---
title: "Top 5 Prompting Techniques"
description: "Prompting techniques help you get better results from AI models. This guide covers top methods like Zero-Shot, Few-Shot, Chain-of-Thought, Role Prompting, and ReAct—each designed to improve output quality and relevance."
excerpt: "الكلام مع ال LLMs بقى جزء من حياتنا اليومية والنهارده في ورقة وقلم وهنتكلم عن أكثر من طريقة لتحسين ال Prompts وطريقة كلامك مع ال Models عشان تطلع لك نتائج أحسن وأكثر دقة."
tags: ["prompt", "LLMs", "mcp", "machine-learning", "chatgpt", "deepseek", "gemini", "ollama", "claude"]
updatedAt: "2025-07-11"
featured: true
image: "https://assets.eqraatech.com/guides/top-5-prompting-techniques.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/top-5-prompting-techniques.png" alt="Top 5 Prompting Techniques" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الكلام مع ال `LLMs` بقى جزء من حياتنا اليومية والنهارده في ورقة وقلم وهنتكلم عن أكثر من طريقة لتحسين ال Prompts وطريقة كلامك مع ال Models عشان تطلع لك نتائج أحسن وأكثر دقة. 

ال Prompt Engineering بتقدم مجموعة من الطرق والإرشادات المناسبة للتعامل مع نموذج ال `LLM` بناءًا على معرفتنا بطبيعة ال Model, هنعرض النهارده خمس طرق بأمثلة عليهم ومتى نستخدم كل واحدة منهم.

---
## **Zero Shot Technique** 

ال Shot هنا بتيجي بمعنى المثال, ودا بيكون ال Prompt العادي اللي بتكتبه من غير ما توفر أمثلة لل Model يتعلم منها 

**مثال:**

> Translate this sentence into Arabic: “I love Eqraatech”.

**متى تستخدمه؟**

عندما تكون المهمة التي تطلبها بسيطة ولا تتطلب توجيه إضافي منك, وقتها يعتمد النموذج علي معلوماته وما تدرب عليه.

---

## **One Shot / Few Shots Technique** 

هو كتابة الطلب مع إعطاء مثال أو أكثر للنموذج عن كيف يحققه أو أمثلة مع إجابتها ليتعلم منها, النموذج وقتها بيحاول يتعلم النمط من الأمثلة اللي أخذها ويستخدمها مع ما تدرب عليه مسبقًا ليعطيك النتيجة. حاول تخلي الأمثلة قصيرة وواضحة عشان متلخبطش النموذج.

**مثال:**

> Classify the sentiment of each sentence:

- "I love this product! It's amazing!" → Positive
- "This is the worst service I’ve ever had." → Negative
- "It's okay, not bad but not great." → Neutral
- "I'm really impressed with the performance." → [Your turn]

**متى تستخدمه؟**

عندما يكون هناك أكثر من طريقة لحل المهمة، وتريد توجيه النموذج لأسلوب معيّن.

---

## **Role Prompting  (Persona Prompting)**

في هذه الطريقة تقوم أنت بتحديد دور أو شخصية للنموذج، دا بيخلي الرد أكثر تخصصًا ودقة. استخدامك لهذه الطريقة مع تحديد سياق Context في الطلب ممكن يحسن دقة الإجابات اللي بتحصل عليها من النموذج بشكل كبير جدًا.

**مثال:**

> You are a professional fitness coach. Give me a weekly workout plan for a beginner.

**مثال مع إضافة سياق:** 

> You are a professional fitness coach. Give me a weekly workout plan for a beginner female trainee with moderate activity level to increase stamina and muscle strength 

**متى تستخدمه؟**

وقت ما تحتاج إجابة بأسلوب أو خبرة معيّنة.

---

## **Chain of Thought Technique** 

هو تشجيع للنموذج على التفكير بصوت عالٍ خطوة بخطوة قبل إعطاء الإجابة. ودا مهم لأن طريقة تدريب النماذج بتجعلها ضعيفة في بعض العمليات زي العمليات الحسابية اللفظية حتي لو كانت بسيطة وممكن تقدملك نتائج خاطئة وعشان كدا استخدام الطريقة دي في الطلب بتساعد النموذج على تفكيك الأمر لأوامر ابسط ويقوم بتنفيذها حتي يصل للإجابة الصحيحة 

**مثال:** 

> Q: If John has 3 apples and buys 2 more, then gives 1 to his friend, how many does he have ? think step by step

> A: First, John starts with 3 apples. Then he buys 2 more, which makes 5 apples. After that, he gives 1 apple to his friend, so he is left with 4 apples. Answer: 4.

**متى تستخدمه؟**

في طلب حل المسائل الرياضية أو المنطقية و عند طلبك لتحليل البيانات مثل تحليل البيانات الإحصائية أو المالية إلخ…

---

## Step-Back Prompting 

هو أنك تطلب من النموذج أنه يرجع خطوة "فكريًا" قبل ما يجاوب على طلبك عشان يحلل الطلب بشكل أفضل فبدل مايجيب مباشرة، تطلب منه أولاً أن "يفهم السياق العام" أو يحدد "ما نوع المشكلة؟"، وبعدها يبدأ في الحل. الطريقة دي  بتخليك تتفادي الإجابات السطحية أو السريعة من النماذج.

**مثال:**

> First, before answering, identify what factors influence user engagement in general. Then suggest the most relevant strategies based on those factors.

**متى تستخدمه؟**

- في الأسئلة التحليلية أو المفتوحة.
- عند العمل على محتوى تعليمي أو تدريبي.
- في البرمجة، لتحديد نوع الخطأ قبل اقتراح الحل.

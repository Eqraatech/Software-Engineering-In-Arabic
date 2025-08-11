---
title: "Model Context Protocol"
description: "Model Context Protocol defines how contextual information is passed to and used by AI models. This guide explores how context improves model accuracy, relevance, and interaction flow across applications."
excerpt: "بروتوكول أو أسلوب تواصل بيخلي نماذج الذكاء الاصطناعي (زي ChatGPT و Claude و Deepseek وغيرها) تقدر تفهم وتتفاعل مع العالم الخارجي زي التعامل مع الملفات، والـ APIs، والأدوات المختلفة، وقواعد البيانات."
tags: ["AI", "mcp", "LLMs", "machine-learning", "deepseek", "gemini", "ollama", "claude"]
updatedAt: "2025-05-15"
featured: false
image: "https://assets.eqraatech.com/guides/model-context-protocol.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/model-context-protocol.png" alt="Model Context Protocol" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

**الـ MCP** هو اختصار لـ **Model Context Protocol**، وده ببساطة بروتوكول أو أسلوب تواصل بيخلي نماذج الذكاء الاصطناعي (زي `ChatGPT` و `Claude` و `Deepseek` وغيرها) تقدر تفهم وتتفاعل مع العالم الخارجي زي التعامل مع الملفات، والـ APIs، والأدوات المختلفة، وقواعد البيانات.

كأننا بنوصّل مخ الذكاء الاصطناعي بالعالم الخارجي بشكل منظم أكتر وآمن.

---

## بداية المشكلة

لنتخيل إننا عندنا مساعد ذكي زي `ChatGPT`، وعاوزين نطلب منه الآتي:

احنا عندنا وليكن E-Commerce Application وعملنا `Export` لملف `Excel` بالـ Orders اللي وصلتنا وعاوز اطلب من `ChatGPT` يشوفلي كام عميل طلب منتج معين بدل ماعمل ده بشكل يدوي ، وعاوزه يقولي شوية احصائيات كده على الطلبات اللي موجودة ونسب الطلب عليها.

**هنعمل ده ازاي ؟**

**في الحالة العادية:** بنروح نكلم `ChatGPT` واكتبله الـ `Prompt` وبالشكل ده لاني بكلمه من الـ `Browser` على سبيل المثال فأنا بروح اخد البيانات بتاعتي `Copy` أو برفعله الملف عشان يكون ليه Access عليه ويبدأ يفهم الطلب بتاعي ويبدأ في تنفيذه مش كده ؟

النموذج في الحالة دي مش هيقدر يفتح ملفات على جهازنا من نفسه. هو "ذكي" أه، ولكن **ملوش Access ومش مربوط بالعالم الخارجي**. يعني مش شايف جهازنا، ولا المتصفح، ولا أي أدوات بره السياق بتاعه.

فلو عاوز اطلب منه مثلا يعمل `Code-Review` على Code انا كاتبه ، مش هعرف اديله Access على الـ Repo بتاعتي ولو قدرت اعمل ده فمش هعرف اعمله بطريقة آمنة.

**طب فيها ايه لو كتبنا Script يعمل Integration بالموضوع ده ؟**

- هنكتب `Script` يقدر يقرأ السياق من الـ Local Repository
- ويـ Integrate مع الـ `LLM Model` ويبعتلهم الـ `Prompt`
- وبعدين ننفذ الكلام ده

هنا هنلاقي اننا محتاجين كل واحد يعمل الموضوع ده ، عشان بس نقدر ندي Access للـ `LLM Models` على سبيل المثال انها تقدر تقرأ الـ Repositories والـ `Codebase` بتاعنا مش كده ؟

وهنا بالظبط بييجي دور الـ `MCP`.

---

## ربط الذكاء الاصطناعي بالعالم الخارجي

**الـ MCP** بيخلّي الذكاء الاصطناعي يقدر يتواصل مع الأدوات الخارجية **من خلال (MCP Servers)**.

الـ Servers دي هي اللي بتنفذ أوامر النموذج. ومن أمثلتها:

- **الـ File System MCP Server**: يفتح ملفات من جهازك أو يقرأ محتوياتها.
- **الـ GitHub MCP Server**: يفتح ملفات من مشاريع `GitHub` ويعدل عليها.
- **الـ Slack MCP Server**: يخلي النموذج يرد على الرسائل في `Slack`.
- **الـ PostgreSQL MCP Server**: يدي النموذج قدرة يقرأ قواعد بيانات `PostgreSQL`.
- **الـ Google Maps MCP Server**: يسأل عن أماكن ويستخدم خرائط جوجل.

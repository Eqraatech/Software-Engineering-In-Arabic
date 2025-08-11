---
title: "Overfitting vs. Underfitting in ML"
description: "Overfitting happens when a model learns the training data too well—including noise—while underfitting means it hasn’t learned enough patterns. This guide explains how to identify and avoid both for better model performance."
excerpt: "الـ Overfitting والـ Underfitting من أهم المواضيع المرتبطة بتدريب الـ Model في الـ Machine Learning وعشان نفهم الفرق بينهم بشكل كويس هنتناول الموضوع بشكل مختلف وبسيط."
tags: ["overfitting", "machine-learning","underfitting", "machine-learning", "AI"]
updatedAt: "2023-12-26"
featured: false
image: "https://assets.eqraatech.com/guides/overfitting-vs-underfitting-in-machine-learning.png"
author: "Anwar11234"
---

<img src="https://assets.eqraatech.com/guides/overfitting-vs-underfitting-in-machine-learning.png" alt="Overfitting vs. Underfitting in Machine Learning" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ Overfitting والـ Under-fitting من أهم المواضيع المرتبطة بتدريب الـ Model في الـ Machine Learning وعشان نفهم الفرق بينهم بشكل كويس هنتناول الموضوع بشكل مختلف وبسيط.

وقت الامتحانات بيكون في أنواع مختلفة من الطلاب، في طالب بيبقى مش مذاكر خالص أو مذاكر أي كلام وده غالباََ بيحل وحش في الامتحان، وفي طالب بيبقى مذاكر كويس وفاهم المنهج وده غالباََ بيحل حلو، وفي طالب تالت مش بيذاكر بس بيجيب امتحانات السنين اللي قبل كدة ويحفظ إجابات الأسئلة اللي فيها، الطالب ده أي سؤال هو حافظ إجابته هيجاوبه صح 100% بس لو جه سؤال جديد مش هيعرف يحله خالص.

### Supervised Learning

في الـ Machine Learning عندنا الـ `Model` ده كإنه هو الطالب اللي بيتعلم وفي مرحلة التدريب بندي الـ `Model` مجموعة بيانات ونقوله لما كان الـ `Input` يساوي x الـ `Output` كان يساوي y كإننا بنديله مجموعة أسئلة والإجابات بتاعتها ( ده نوع من الـ Machine Learning اسمه Supervised Learning). 

### Under-fitting

بعد ما نخلص مرحلة التدريب بنبدأ نمتحن الـ `Model` و نشوفه اتعلم ايه من البيانات اللي شافها فبنديله أسئلة بردو بس المرة دي من غير إجاباتها ونشوف هيجاوب إجابات صح ولا لأ وهنا ممكن الـ `Model` يجاوب إجابات أغلبها غلط أو مش دقيقة خالص شبه الطالب اللي دخل الامتحان مش مذاكر والحالة دي بنسميها Under-fitting بمعنى إن الـ `Model` مفهمش البيانات اللي شافها كويس.

### Overfitting

ممكن الـ `Model` يجاوب إجابات دقيقة 100% في حالة بس إنه شاف الأسئلة دي في مرحلة التدريب وغير كدة هيجاوب إجابات مش دقيقة خالص شبه الطالب اللي دخل الامتحان حافظ امتحانات السنين اللي فاتت وده بنسميه Overfitting بمعنى إن الـ `Model` حفظ البيانات اللي شافها بس مفهمش منها حاجة.

---

### طب ايه الهدف اللي عاوزين نوصله ؟

 ممكن الـ `Model` يجاوب إجابات كويسة على كل الأسئلة اللي امتحناه فيها سواء شافها قبل كدة أو لأ زي الطالب اللي داخل الامتحان مذاكر كويس وده الهدف اللي إحنا عايزين نوصله عايزين الـ `Model` يكون فاهم البيانات اللي شافها ويقدر يستخدم فهمه ده عشان يجاوب على أسئلة جديدة، مش عايزين يحصل under-fitting ولا overfitting.

### أسباب الـ Under-fitting

نستخدم `Model` بسيط زيادة عن اللزوم، وبالتالي مش هيقدر يفهم البيانات اللي بيشوفها

**ازاي نعالج المشكلة دي ؟**

نستخدم `Model` أكثر تعقيدًا، بس نخلي بالنا انه ميكون معقد زيادة عن اللزوم عشان ميحصلش Overfitting فمحتاجين حاجة وسط بين الاتنين.

### أسباب الـ Overfitting

1. نستخدم `Model` معقد زيادة عن اللزوم
2. بيانات التدريب تكون قليلة

**ازاي نعالج المشاكل دي ؟**

محتاجين حاجة وسط بين الاتنين زي ما وضحنا قبل كده بالإضافة لإننا نجمع أكبر قدر ممكن من البيانات وكمان فيه حاجة ممكن نطبقها وهي الـ Regularization ودي بتكون زي توجيه للـ `Model` انه ميحفظش البيانات اللي بيشوفها خلال مرحلة التدريب.
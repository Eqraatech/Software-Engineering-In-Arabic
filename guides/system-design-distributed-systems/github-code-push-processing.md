---
title: "GitHub Code Push Processing"
description: "When you push code to GitHub, it triggers a series of backend processes—updating branches, validating commits, running hooks, and possibly triggering CI/CD workflows. This guide explains what happens behind the scenes of a git push."
excerpt: "الـ Code Pushes هي أكيد واحدة من العمليات الشائعة والمتكررة اللي كلنا بنقوم بيها بشكل دوري. والتغييرات اللي مهندسين GitHub عملوها دي هدفها معالجة أي مشاكل محتملة وانهم يوفروا تجربة أكثر سلاسة لأي حد بيعمل Code Push على GitHub."
tags: ["database", "performance", "backend", "replication", "sharding", "caching", "cdn", "distributed-systems", "system-design"]
updatedAt: "2024-07-13"
featured: false
image: "https://assets.eqraatech.com/guides/github-code-push-processing.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/github-code-push-processing.png" alt="Strategies for Read Heavy Systems" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

كلنا عارفين GitHub وأهميته في كونه منصة لاستضافة الـ Code Repositories باستخدام Git Version Control. و GitHub بيتم استعماله على نطاق واسع من قبل المطورين لإدارة مشاريعهم البرمجية، والتعاون مع فرق العمل، واستضافة مشاريع مفتوحة المصدر.

بالإضافة إلى توفير أدوات لتتبع المشاكل، وإدارة المشاريع، وكمان فيه مميزات تانية زي GitHub Actions والي بتمكن المطورين من تنفيذ عمليات CI/CD.

وفي السنوات الأخيرة، أصبح GitHub جزء لا يتجزأ من عملية تطوير البرمجيات العالمية، مع مجتمع يضم ملايين المطورين والشركات.

---

## Enhance the Reliability and Efficiency of Code Pushes

قامت GitHub بعمل Rollout لأكتر من Technical Upgrade وده بهدف التحسين من الـ Reliability والكفاءة الخاصة بعملية الـ Code Pushes.

والـ Code Pushes هي أكيد واحدة من العمليات الشائعة والمتكررة اللي كلنا بنقوم بيها بشكل دوري. والحركة اللي عملوها دي هدفها معالجة أي مشاكل محتملة وانهم يوفروا تجربة أكثر سلاسة لأي حد بيعمل Code Push على GitHub.

فتعالوا نشوف ايه التحسينات اللي فريق مهندسين GitHub خدها عشان يحسن من كفاءة عملية الـ Code Push.

---

## ايه اللي بيحصل لما بنعمل Code Push ؟

الاجابة المنطقية واللي كتير عارفينها ان الـ Repository بالتأكيد هيبقى فيها الـ Updates بتاعتي اللي انا عملتلها Push , ولكن رغم ان الكلام ده صحيح الان ان فيه مجموعة من العمليات اللي بتحصل كمان واحنا ممكن مانكونش على دراية كاملة بيها.

ودي بعض الأمثلة للعمليات اللي بتحصل لما بنعمل Push لأي Code على GitHub:

- بيحصل مزامنة بين الـ Pull Requests وبعضها , وده معناه ان الـ Diffs والـ Commits اللي موجودين في الـ Pull Request بيتأثروا بالتغييرات اللي بتطرأ من الـ Code Push اللي عملناه
- بيتم عمل Dispatching للـ Push Webhooks
- بيتم عمل Triggering للـ Workflows
- لو عملنا Push لـ App Configuration File , التطبيق هيتم عمل ليه Installing بشكل اوتوماتيك على الـ Repository
- بيتم نشر الـ GitHub Pages
- وغيرهم كتير من العمليات اللي بتحصل واحنا ممكن ما نكونش على دراية كافية بيها.

فلما بتيجي تعمل Code Push بيكون فيها ما يقرب من 60 عملية مختلفة من الـ Logic مرتبطين تقريبًا بحوالي 20 Service مختلفة وكلهم بيحصلهم Run بعد ما تعمل Code Push وده طبعا في الـ Monolith GitHub اللي هم مصممينه.

فزي ما احنا شايفين احنا عندنا Monolith Application وفيه Sequential Operations بتحصل تباعًا مع كل Code Push بيتم.

---

## ايه هي المشاكل ؟

المشكلة ان لحد قبل ما يحصل أي تحسين في الـ System ده , كان الموضوع كله قايم على Background Job ضخمة جدًا , كل لما يحصل Notify للـ Ruby and Rails GitHub Monolith بأن حصل عملية Code Push, كان بيحصل عملية Enqueue لـ Job ضخمة اسمها `RepositoryPushJob` , والـ Job دي هي اللي كان فيها الـ Logic الضخم اللي اتكلمنا عنه واللي فيه أكتر من 60 Logic.

وبالتأكيد مع وجود كمية كبيرة من الـ Processing Logic اللي شايلاه وحجمها وتعقيدها , كل ده كان بيؤدي إلى مشاكل كتيرة , واللي من ضمنها : 

- Enormous Job and Retry
- Tightly Coupling and Catching Failures
- Bad Latency

---
title: "Top 16 Kubernetes Essential Components"
description: "Get to know the core building blocks of Kubernetes. This guide breaks down the top 16 components—from Pods and Services to etcd, the Scheduler, and more—that power container orchestration at scale."
excerpt: "أهم مكونات Kubernetes وهو  نظام مفتوح المصدر لإدارة ونشر وتشغيل التطبيقات داخل حاويات (Containers) بشكل آلي وفعّال."
tags: ["kubernetes", "microservices", "devops", "docker", "deployment"]
updatedAt: "2025-06-27"
featured: false
image: "https://assets.eqraatech.com/guides/top-16-kubernetes-essential-components.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/top-16-kubernetes-essential-components.png" alt="Top 16 Kubernetes Essential Components" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

**النهارده هنتكلم عن أهم مكونات Kubernetes وهو  نظام مفتوح المصدر لإدارة ونشر وتشغيل التطبيقات داخل حاويات (Containers)** بشكل آلي وفعّال.

يعتبر K8s أشهر ال Orchestrators حاليًا وبتظهر أهميته في الشركات الكبيرة وبيئات ال `Microservices` المعقدة لأنه يقدر يدير ويسهل عملية نشر التطبيقات بطريقة منظمة وقابلة للتوسع. هنتكلم بشكل مختصر عن أهم المكونات وإزاي بتتواصل مع بعضها البعض.

---
## أهم مكونات Kubernetes الأساسية

1- **Container:** هي حاوية تحمل بداخلها التطبيق مع بيئة كاملة تشمل كل ما يحتاجه من اعتماديات ليعمل. 

2- **Pod:** أصغر وحدة Deployable في K8s ، تحتوي على حاوية واحدة أو أكثر تُدار معًا وتشارك نفس الـ IP والـ Volume.

3- **Node:** خادم (فعلي أو افتراضي) يعمل عليه `K8s` ويشغّل الـ `Pods`. وتسمي ال `Node` ب `Worker Node` عندما تقوم بتشغيل ال(Pods) التي تم جدولة تشغيلها من قبل الـ Master.

4- **Cluster:** يُسمي النظام الذي يديره `K8S` بال `Cluster` ويتكون من مجموعة من الـ `Nodes` تُدار كوحدة واحدة لتشغيل التطبيقات.

5- **Control Plane:** أو تسمى بال `Master Node` وهي المسؤولة عن إدارة الـ `Cluster` بأكمله عن طريق عدة مكونات.

6- **Kubelet:** هو `Agent` يعمل على كل `Node`. وظيفته هي التأكد من أن الحاويات تعمل كما هو متوقع في الPod, بيعمل دا في عدة خطوات زي التواصل مع ال `Control Panel` وكذلك مع الـ `Container runtime` وتجميع تقارير عن حالة ال `Containers` وإرسالها لـ `Control Panel`. 

7- **Kube-proxy:** المكون المسؤول عن إدارة الشبكة وتوجيه ال `traffic` لل `worker node` وال Service الصحيحة.

8- **API Server:** هو العنصر الرئيسي في الـ `Control Plane`، ويُعتبر البوابة `(Gateway)`التي يتفاعل من خلالها كل شيء داخل أو خارج الـ `cluster` مع `k8s`. 

9- **Controller manager:** هو المسؤول عن إدارة الحالة داخل الـ `cluster` والتأكد من أن كل شيء يعمل كما هو "مطلوب" (وفقًا لتعريفك في ملفات `YAML` مثل `Deployments`، `ReplicaSets`، إلخ).

10- **Scheduler:** مكون من مكونات الـ `Control Plane` بيحدد أين يجب تشغيل الـ `Pods`, فوقت ما تطلب إنشاء `Pod` جديد بيقوم ال `Scheduler` باختيار الـ `Node` المناسبة من حيث الموارد وال `Constraints` لإنشاء الPod.

11- **ETCD:** هي قاعدة البيانات الأساسية والمركزية التي يستخدمها `k8s` لتخزين الحالة الكاملة لـ `cluster`. وهي بالأساس `Key-value Store` لضمان البساطة والسرعة في تخزين واسترجاع بيانات الـ cluster وبتعتبر هي ال Source of truth لباقي ال `Cluster`.

12- **Service:** هي كيان بيوفّر نقطة وصول ثابتة وثابتة الاسم (Stable Endpoint) لمجموعة من الـ `Pods`، حتى لو تغيّرت أو أُعيد تشغيلها.لأن ال `Pods` لما يعاد تشغيلها ممكن ال `IP` الخاص بيها يتغير ووقتها أنت كمستخدم هتحتاج تغير طريقة تواصلك معها وعشان نتجنب دا بنقدم ال `Service` فتفضل طريقة التواصل للتطبيق أو الخدمة ثابتة بغض النظر عن تفاصيل التشغيل.

13- **Kubectl:** ال Command line interface الأساسية للتفاعل مع `Kubernetes`

14- **ConfigMaps:** تُستخدم لتخزين الإعدادات غير السرية للتطبيقات.

15- **Secrets:** تُستخدم لتخزين معلومات حساسة (مثل كلمات المرور ، مفاتيح `API`).

16- **Ingress:** هو عبارة عن `Smart gateway` تُستخدم لتوجيه الزيارات الخارجية `(HTTP/HTTPS)` القادمة من الإنترنت إلى داخل ال `Cluster` وتحديدًا إلى الـ Services وال `Pods` المناسبة.

---

## في الختام

ال Cheatsheet إن شاء الله تساعدكم في المذاكرة أو وقت الشغل لو نسينا تعريف/استخدام مٌكون وحابين نفتكره بسرعة.

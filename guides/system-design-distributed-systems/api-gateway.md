---
title: "API Gateway"
description: "An API Gateway acts as a single entry point for client requests, managing routing, authentication, rate limiting, and more. This guide explores how API Gateways simplify and secure microservices communication."
excerpt: "نقطة دخول واحدة لكل الـ requests اللي جايه من الـ clients للـ backend. فبدل ما الـ client يتعامل مع كل service بشكل مباشر، هو بيتعامل بس مع الـ Gateway، والـ Gateway يتولى الباقي."
tags: ["api-gateway", "microservices", "network", "backend", "load-balancer", "distributed-systems", "system-design"]
updatedAt: "2025-05-21"
featured: false
image: "https://assets.eqraatech.com/guides/api-gateway.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/api-gateway.png" alt="API Gateway" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

في ظل وجود الـ Monolithic Applications ، الـ Client هنا مش بيتعب في انه يتواصل مع الـ Backend وده لإنه بيكلم Service واحدة في الأول والآخر ومش محتاج يشغل باله من أي مشاكل.

ولكن مع التقدم اللي حصل وبعد هوجة و Trend الـ Microservices بيبدأ الـ Monolithic Application ده يتكسر لـ Services صغيرة كل واحدة محدودة بالـ Boundaries بتاعتها.

وبيجي هنا السؤال اللي بيحير الناس ، يا ترى هنعمل ايه في الـ Client ؟ احنا كنا بنبعت `Request` لمكان واحد دلوقتي محتاجين نبعت `Requests` مختلفة لكل الـ Services دي. طب ازاي هنـ Manage التغيير اللي ممكن يحصل لو `Endpoint` اتغيرت ؟ وهل مفروض الـ Client يكون `Coupled` بالشكل العنيف ده مع كل Service في الـ `Backend` لما تتغير؟

وهنا بدأنا نفكر في اننا ليه مايكونش عندنا نقطة دخول واحدة بتتحكم في طلبات المستخدمين وبتوجهها للخدمات المناسبة جوا النظام ؟ وبالتالي اقدر اغير براحتي اي حاجة في الـ `Backend` طالما الـ `Contract` أو الـ `Interface` اللي بيستعمله الـ `Client` واحد.

ومنا هنا جت فكرة الـ `API Gateway` ، فخلونا نشوف مع بعض ايه هو والمميزات اللي بيقدمهالنا بالورقة والقلم 🚀

---

## API Gateway

الـ **API Gateway** هو نقطة دخول واحدة (single entry point) لكل الـ (`requests`) اللي جايه من الـ clients للـ backend. فبدل ما الـ client يتعامل مع كل service بشكل مباشر، هو بيتعامل بس مع الـ `Gateway`، والـ `Gateway` يتولى الباقي.

---

### API Gateway Benefits

الـ **API Gateway** مش بس نقطة دخول موحدة للـ APIs، لكنه بيقدّم مجموعة كبيرة من المميزات زي:

1. **Dynamic Routing**  
2. **Authentication & Authorization**  
3. **Rate Limiting & Throttling**  
4. **Parameter Validation**  
5. **Allow / Deny List**  
6. **Service Discovery**  
7. **Protocol Conversion**  
8. **Caching**  

---

### API Gateway Tools

فيه أكتر من Tool نقدر نستعملها كـ API Gateways:

- **Kong** وهو قوي جدًا ومفتوح المصدر مبني على `Nginx`.
- الـ **API Gateway من AWS** وطبعًا ده كله Managed من Amazon
- **Istio Gateway** وهو جزء من الـ `Service Mesh` وبيقدم مميزات قوية جدًا في الـ `Routing`
- **Traefik** مشهور جدًا في عالم الـ `containers` وخصوصًا مع `Docker` و `Kubernetes`.

---

### أمتى ممكن ما نحتاجش API Gateway؟

- لو التطبيق بسيط ومكوّن من خدمة واحدة أو خدمات قليلة جدًا.
- لو الـ communication بين الخدمات داخلي فقط ومفيش interaction مباشر مع clients خارجيين.
- لو الـ overhead اللي هيسببه الـ `Gateway` أكبر من الفايدة اللي بيقدمها.

---

## في الختام

الـ **API Gateway** هو عنصر مهم جدًا في تصميم الأنظمة الحديثة، خصوصًا لو شغالين بنظام الـ Microservices. لإنه بيوفر abstraction ممتازة، وبيسهل الـ Communication، وبيقدّم مميزات كتير من غير ما نكرّرها جوه كل service.

سؤال ممكن تفكروا فيه ايه الفرق بين الـ `Reverse Proxy` والـ `API Gateway` ؟ ويا ترى لو هل ممكن يكون عندنا في الـ System أكتر من `API Gateway` وامتة ؟
---
title: "gRPC"
description: "gRPC is a high-performance, open-source framework for remote procedure calls (RPC). This guide explains how gRPC enables efficient, language-agnostic communication between microservices using Protocol Buffers."
excerpt: "الـ gRPC هي اختصار لـ Google Remote Procedure Call وهي تكنولوجيا بتخلي الـ Service تقدر تنادي الـ function اللي موجودة في Service تانية كأنها بتناديها عادي كـ Function Call."
tags: ["gRPC", "microservices", "network", "backend", "HTTP2", "distributed-systems", "system-design"]
updatedAt: "2025-06-04"
featured: false
image: "https://assets.eqraatech.com/guides/grpc.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/grpc.png" alt="gRPC" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ `gRPC` هي اختصار لـ **Google Remote Procedure Call** وهي تكنولوجيا بتخلي الـ Service تقدر تنادي الـ function اللي موجودة في Service تانية كأنها بتناديها عادي كـ `Function Call`، حتى لو الـ Service التانية دي مكتوبة بلغة برمجة مختلفة ومش موجودة على نفس الـ Machine!

بشكل أبسط يعني لو عندنا Service مكتوبة بـ `Java` و Service تانية مكتوبة بـ `Python`، نقدر نخلي الـ `Python` ينادي Function في الـ `Java` بسهولة.

---

في الـ `Microservices` لو كل Service بدأت تعمل Generate لـ Client Library عشان الـ Services التانية تستخدمها ، هنضطر نعمل Client Library بلغات برمجة مختلفة على حسب الـ Services التانية ، وده مش حاجة منطقية! وهنا بتيجي ميزة الـ gRPC في انها بتوفر Unified Framework وكمان Language Agnostic ، فاحنا بنقول ده الـ proto اللي عاوزها والـ Client بيستعمل الـ gRPC Framework في انه يبعتلنا الـ Proto ويستقبل الـ Proto كـ Response وخلاص.

الـ `gRPC` بيبدأ من الـ `Schema` ، بـ Define الـ `APIs` بتاعتي وبقول دول الـ Functions اللي عندي أو الـ Contracts بتاعتي ، وبحدد الـ `Request/Response` كـ `proto` واللي هي اختصار للـ Protocol Buffer.

---

## الـ gRPC شغال إزاي؟

الـ `gRPC` بيعتمد على حاجة اسمها **Protocol Buffers (Protobuf)**. دي زي `JSON` كده، بس أخف وأسرع، بتستخدمها علشان توصف شكل البيانات اللي رايحة واللي جاية.

فبدل ما نبعت `JSON` كبير ومليان تفاصيل، بنكتب ملف `.proto` نعرف فيه الـ Message والـ Functions اللي عاوزين نتبادلها بين الـ Client والـ Server.

فانا بقول عندي service x بتشمل الـ functions الآتية وكل function بتستقبل proto request وبترجع proto response وخلاص كده ، فمش محتاج باه احدد الـ params دي هتيجي من الـ `query , url , body` والـ complexity بتاعة الـ `REST`

مثال سريع على ملف `.proto`:

<!-- Protocol Buffer -->
```protobuf
syntax = "proto3";

service KitchenService {
  rpc PrepareOrder (OrderRequest) returns (OrderResponse);
}

message OrderRequest {
  int32 order_id = 1;
  string meal = 2;
  string extra = 3;
}

message OrderResponse {
  bool ready = 1;
  string note = 2;
}
```

<!-- JSON Equivalent -->
```json
{
  "order_id": 123,
  "meal": "Pizza Margherita",
  "extra": "Extra cheese"
}
```

<!-- Python Client -->
```python
# Python gRPC Client Example
import grpc
import kitchen_pb2
import kitchen_pb2_grpc

def order_food():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = kitchen_pb2_grpc.KitchenServiceStub(channel)
        request = kitchen_pb2.OrderRequest(
            order_id=123,
            meal="Pizza Margherita",
            extra="Extra cheese"
        )
        response = stub.PrepareOrder(request)
        print(f"Order ready: {response.ready}")
        print(f"Note: {response.note}")
```

## استخدامات الـ gRPC

- **الـ Microservices**: لو عندنا نظام كبير متقسم لـ Services صغيرة، الـ gRPC بيخلي الـ Services دي تتكلم مع بعض بكفاءة.
- **في الـ Mobile apps**: لأنه خفيف وسريع جدًا.
- **في الـ Real-time systems**: زي الـ Chat apps أو Video streaming.

---

## في الختام

الـ `gRPC` بيلمع وبيظهر أكتر في الـ `Micro-services Arhcitecture` وخصوصا لو فيه عندنا Services كتير ويهمنا نحل مشاكل الـ Network والـ Communication بينهم وبين بعض. ودي بعض الحالات اللي ممكن يكون مميز فيها وبيستخدم فيها.
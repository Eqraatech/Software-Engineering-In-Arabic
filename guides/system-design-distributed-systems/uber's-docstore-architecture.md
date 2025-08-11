---
title: "Uber's Docstore Architecture"
description: "Docstore is Uber’s scalable, document-based storage system designed for high availability and low latency. This guide explores how Docstore supports diverse use cases through flexible schemas, strong consistency, and efficient indexing."
excerpt: "قاعدة البيانات دي بتتميز بعدة مميزات من ضمنها انها بتوفر الـ Strict Serializability Consistency Model على مستوى الـ Partition وده كان من ضمن المتطلبات اللي Uber عاوزة تحققها وبالتالي نقدر نستنج هنا ان Uber بتضحي بالـ Availability في سبيل الـ Consistency."
tags: ["microservices", "database", "cassandra", "docstore" , "mysql", "backend", "distributed-systems", "system-design", "cdc", "replication", "sharding", "raft"]
updatedAt: "2024-08-01"
featured: false
image: "https://assets.eqraatech.com/guides/uber's-docstore-architecture.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/uber's-docstore-architecture.png" alt="Uber's Docstore Architecture" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

شركة Uber بتستعمل Docstore وهو عبارة عن قاعدة البيانات الموزعة بتاعتهم واللي مبنية على MySQL و Docstore بتخزن عشرات الـ PetaBytes من البيانات وبتخدم عشرات الملايين من ال Requests في الثانية.

ودي واحدة من أكبر محركات قواعد البيانات عند Uber واللي بتستخدمها كتير من الـ Microservices في كل القطاعات التجارية أو اللي بنسميها Business Verticals عندهم.

والكلام ده من ساعة ما بدأت في 2020، عدد المستخدمين وحالات الاستخدام بتاعت Docstore في ازدياد، وكمان حجم الطلبات والبيانات في زيادة.

---

## Motivation

شركة Uber كانت بتستعمل الـ `Schemaless` Types من قواعد البيانات , واللي خلتها بعد كده تقابل شوية تحديات كبيرة والي خلتها تتجه لاستعمال `Cassandra` كـ Database وتبقى كـ General Purpose Database لمعظم الـ Business Verticals.

ولكن مع حجم الـ Scale بتاع Uber كان الـ Operations على `Cassandra` كبيرة جدًا ومش فعالة بالنسبة ليهم من ناحية الكفاءة بتاعتها والـ Scale بتاع Uber ، بالاضافة كمان لان `Cassandra` بتدعم الـ `Eventual Consistency` وده Consistency Level بالنسبة لـ Uber مكنش أفضل حاجة من ناحية المتطلبات بتاعتهم خصوصا ان هم بيطمحوا لتحقيق الـ `Strict Serializability Consistency` Level.

ومن ثم ظهر الحاجة لتصميم `Docstore` واللي مبني على `MySQL`.

---

## Docstore

قاعدة البيانات دي بتتميز بعدة مميزات من ضمنها انها بتوفر الـ `Strict Serializability Consistency Model` على مستوى الـ `Partition` وده كان من ضمن المتطلبات اللي Uber عاوزة تحققها وبالتالي نقدر نستنج هنا ان Uber بتضحي بالـ `Availability` في سبيل الـ `Consistency` من ناحية نظرية الـ `CAP Theorem`.

كمان نقدر نـ Scale Horizontally واللي اتاح الفرصة لـ Uber انها بالشكل ده قاعدة البيانات تكون بتدعم وبتخدم عدد كبير من الـ Heavy Workloads اللي عندهم.

ومش بس كده ده كمان بتوفر مميزات كتير بتحسن من انتاجية المطورين زي الـ Transactions / Materialized Views / CDC بالإضافة للمرونة في عمل الـ Modeling للبيانات وكذلك وفرة من الـ Query Support اللي الـ Clients ممكن يكونوا محتاجينها.

---

## Docstore Architecture

هنلاقي أن Docstore متقسمة بشكل رئيسي لثلاث أجزاء أو طبقات Layers:  
1- الـ Stateless Query Engine Layer  
2- الـ Stateful Storage Engine Layer  
3- الـ Control Plane

---

وللتذكير Stateless من اسمها يعني مش مسئولة عن الاحتفاظ بأي State نهائيًا أو معلومات ، بينما الـ Stateful فهي بتحتفظ بالـ State أو بعض المعلومات عشان تستفيد منها في أداء شغلها.

## Stateless Query Engine

الـ Stateless Query Engine مسئول بشكل أساسي عن الـ `Query Planning` والـ `Routing` والـ `Sharding` والـ `Schema Management` وكمان الـ Node Health Monitoring والـ `Request Parsing` والـ `Validation` والـ `AuthN/AuthZ`.

والـ `AuthN` اللي هي اختصار لـ `Authentication` والـ `AuthZ` اختصار للـ `Authorization`.

## Stateful Storage Engine

بينما الـ Stateful Storage Engine مسئول بشكل أساسي عن تحقيق الـ `Consensus` من خلال Raft وده طبعًا بيتم استعماله بشكل أساسي في النظم الموزعة لضمان تحقيق الـ `Replication` بكفاءة واتساق البيانات أو ما يعرف بالـ `Consistency`.

والـ Storage Engine كذلك مسئول عن الـ `Replication` والـ `Transactions` والـ `Concurrency Control` والـ `Load Management`.

## Control Plane

والـ Control Plane هم مسئول بشكل أساسي على انه يـ Assign الـ `Shards` للـ `Docstore Partitions` ويعدل ويغير من الـ `Shard` بناء على الـ Failure اللي ممكن تحصل في أي وقت. فهو زي المخ لعملية تحديد الـ `Shards` على الـ `Partitions`.
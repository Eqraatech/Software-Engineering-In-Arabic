---
title: "CI/CD with Jenkins"
description: "Apache Spark is a powerful engine for big data processing and analytics. This guide introduces how Spark handles large-scale data with speed, scalability, and support for SQL, streaming, and machine learning."
excerpt: "أداة مفتوحة المصدر بتساعدك تبني Pipelines عشان تختبر وتبني الكود بشكل مستمر مع كل إضافة وتتأكد من عمله بطريقة صحيحة ودي بتسمي بعملية CI/CD."
tags: ["ci/cd", "devops", "jenkins", "pipeline", "github", "gitlab", "docker"]
updatedAt: "2025-04-10"
featured: false
image: "https://assets.eqraatech.com/guides/ci-cd-with-jenkins.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/ci-cd-with-jenkins.png" alt="CI/CD with Jenkins" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

يعتبر `Jenkins` أداة مفتوحة المصدر بتساعدك تبني `Pipelines` عشان تختبر وتبني الكود بشكل مستمر مع كل إضافة وتتأكد من عمله بطريقة صحيحة ودي بتسمي بعملية `CI/CD`. 

قبل ال `CI/CD` كان كل فرد من الفريق بيشتغل على الجزء الخاص بيه و نتجمع في النهاية ونضيف الكود على بعضه ونحل المشاكل اللي بتظهر من عدم توافقه,طبعًا دي كانت عملية مرهقة وبتكلف وقت ومجهود واحم احم أعصاب.

فعملية التكامل المستمر تقوم بتجميع الكود الجديد والقديم و تختبرهم سوا في عدة خطوات أو ما يسمى بال `Pipeline` عشان تتأكد من عملهم وتظهر لك المشاكل علطول فبالتالي كفريق تقدروا تشتغلوا على التعديلات وتكتشفوا مواضع الخطأ.

---

## Pipeline Stages

`Jenkins` بيساعدك تكون `Pipeline` بسهولة عن طريق كتابة `Jenkins File` باستخدام لغة `Groovy` بتحدد فيه كل مرحلة ومفروض يعمل فيها ايه :

-  مرحلة البناء ( Build Stage) 
- مرحلة الاختبار (Testing Stage )
- مرحلة النشر على السيرفر  ( Deploy Stage )

مثال:

<!-- Jenkinsfile -->
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean install'  
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }
}
```

<!-- GitHub Actions -->
```yaml
# GitHub Actions equivalent
name: CI/CD Pipeline
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Build
      run: mvn clean install
    - name: Test
      run: mvn test
```

<!-- GitLab CI -->
```yaml
# GitLab CI equivalent
stages:
  - build
  - test

build:
  stage: build
  script:
    - mvn clean install

test:
  stage: test
  script:
    - mvn test
```
    
بكدا تكون عملت `Automation` لبناء واختبار ونشر المشروع الخاص بك بدل مع كل تغيير بدل ما تقوم  بالمراحل دي كلها بشكل يدوي.

---

## مميزات Jenkins 

1. مفتوح المصدر ومجاني – لا يحتاج إلى ترخيص مدفوع.
2. دعم كبير للإضافات (Plugins) – بيتيح عدد كبير من الـ `Plugins` لتوسيع وظائفه (مثل دعم Git، `Docker`، `Kubernetes`، وغيرها).
3. بيتشغل مع معظم الأدوات مثل `GitHub`، `GitLab`، `Bitbucket`، `Maven`، `Docker`، وغيرها.
4. يدعم `CI/CD` بالكامل – من البناء إلى الاختبار إلى النشر.
5. مجتمع نشط ودعم فني قوي – بسبب شعبيته هتلاقي Community قوي وكذلك الكثير من الأمثلة والدعم

---

## عيوب Jenkins 

1. واجهة المستخدم قديمة: أي حد اشتغل مع `Jenkins` هيواجه في الأول صعوبة معرفة منين بيودي على فين, بينما الوضع أسهل في البدائل الحديثة من ناحية الـ UI
2. تعلم منحنى متوسط:  بيحتاج شوية وقت عشان  تفهمه بالكامل، خاصةً عند استخدام `Jenkinsfile`.

---

## البدائل المتاحة 

في بدائل أكثر حداثة ل `Jenkins` ولكنه لا يزال واحد من أكثر أدوات الـ `CI/CD` استخدامًا وبالأخص للشركات اللي بتحتاج Scaling.

البدائل -مفتوحة المصدر- مثل: `Openshift pipelines, Gitlab CI/CD, Circle CI`

شاركونا خبراتكم في التعامل مع جينكينز ايه المميزات اللى بتحبوها فيه وايه العيوب من وجهة نظركم والبدايل اللي بتأخذوها في عين الاعتبار 👋
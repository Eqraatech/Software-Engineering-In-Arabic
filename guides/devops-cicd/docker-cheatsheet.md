---
title: "Docker Cheatsheet"
description: "A quick reference for essential Docker commands and concepts. This cheatsheet covers images, containers, volumes, networks, and tips to streamline your container workflow."
excerpt: "تشغيل التطبيقات بسرعة وسهولة من أولوياتنا كمبرمجين لأنه بيسهل علينا يوم العمل ، وعشان كدا Docker أصبح من أهم أدوات المبرمج في السنين اللي فاتت."
tags: ["docker", "microservices", "containerization", "devops", "Kubernetes"]
updatedAt: "2024-10-14"
featured: false
image: "https://assets.eqraatech.com/guides/docker-cheatsheet.png"
author: "alaaelkazaz"
---

<img src="https://assets.eqraatech.com/guides/docker-cheatsheet.png" alt="Docker Cheatsheet" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

تشغيل التطبيقات بسرعة وسهولة من أولوياتنا كمبرمجين لأنه بيسهل علينا يوم العمل ، وعشان كدا `Docker` أصبح من أهم أدوات المبرمج في السنين اللي فاتت. وده لإنه بيوفرلنا بيئات معزولة (`Containers`) بتحتوي على كل الملفات اللي التطبيق محتاجها علشان يشتغل، وده معناه إن التطبيق هيشتغل بنفس الطريقة على أي جهاز، سواء كان جهازك كمبرمج أو جهاز زميلك في الشغل أو حتى سيرفر الإنتاج.

---

## Docker Cheatsheet

جمعنالك أهم الأوامر اللي ممكن تحتاجها في شغلك اليومي ب `docker` في مكان واحد وبالعربي عشان نوفر مجهود الترجمة ل اللغة الأم اللي طول النهار بنعمله دا 😅

**الأوامر متقسمة ل ٣ فئات:**

### Docker Images Commands

أوامر خاصة بالتعامل مع ال `docker images` و هي دي ورقة المواصفات اللي بنبني علي أساسها ال `containers` بتاعتنا.

بناء `Image` من `DockerFile`

<!-- Build Image -->
```bash
docker build -t <image_name>
```

<!-- Example -->
```bash
docker build -t myapp:latest .
```

قائمة ال Local Images

<!-- List Images -->
```bash
docker images
```

<!-- Alternative -->
```bash
docker image ls
```

حذف Image

<!-- Remove Image -->
```bash
docker rmi <image_name>
```

<!-- Example -->
```bash
docker rmi myapp:latest
```

حذف جميع ال Images الغير مستخدمة

<!-- Prune Images -->
```bash
docker image prune
```

<!-- Remove All -->
```bash
docker image prune -a
```

### Docker Containers Commands

أوامر خاصة بالتعامل مع ال docker containers ودي بتبقي عبارة عن التطبيق بتاعك مع البيئة الكاملة اللي محتاجها عشان يشتغل

إنشاء وتشغيل Container من Image

<!-- Run Container -->
```bash
docker run --name <container_name> <image_name>
```

<!-- Example -->
```bash
docker run --name myapp-container myapp:latest
```

تشغيل Container مع نشر رقم ال Port

<!-- Port Mapping -->
```bash
docker run -p <host_port>:<container_port> <image_name>
```

<!-- Example -->
```bash
docker run -p 8080:80 nginx
```

تشغيل Container في الخلفية

<!-- Detached Mode -->
```bash
docker run -d <container_name>
```

<!-- Example -->
```bash
docker run -d --name myapp myapp:latest
```

تشغيل أو إيقاف Running Container

<!-- Start/Stop -->
```bash
docker start|stop <container_name>
```

<!-- Examples -->
```bash
docker start myapp-container
docker stop myapp-container
```

قائمة ال Running Containers

<!-- Running Containers -->
```bash
docker ps
```

<!-- All Containers -->
```bash
docker ps --all
```

حذف الContainer المتوقف

<!-- Remove Container -->
```bash
docker rm <container_name>
```

<!-- Example -->
```bash
docker rm myapp-container
```

---

### General Commands

أوامر عامة و أوامر للتعامل مع `DockerHub` وهو ال `Repository` الأساسي اللي كل الناس بتنشر عليه ال Docker Images الخاصة بتطبيقاتها ويقدر بقية المطورين ينزلوا منه ال `Images` و ينشأوا منها `Containers` ويستخدموها.

تشغيل Docker Daemon

<!-- Docker Daemon -->
```bash
docker -d
```

<!-- System Service -->
```bash
sudo systemctl start docker
```

تسجيل الدخول ل Docker

<!-- Login -->
```bash
docker login -u <username>
```

<!-- Example -->
```bash
docker login -u myusername
```

نشر Image على Docker Hub

<!-- Push Image -->
```bash
docker push <username>/<image_name>
```

<!-- Example -->
```bash
docker push myusername/myapp:latest
```

---

## في الختام

يعتبر Docker أداة قوية لتبسيط عملية تطوير ونشر البرمجيات، ويساعد المطورين في تجنب الكثير من المشاكل المتعلقة بالتوافق بين البيئات المختلفة.
---
title: "Process Scheduling"
description: "Process scheduling is how an operating system decides which process runs next. This guide covers key algorithms like Round Robin, Priority, and Shortest Job First to manage CPU time efficiently."
excerpt: "الـ Scheduler في أنظمة التشغيل هو عبارة عن العنصر اللي بيحدد إزاي وإمتى المعالجات (CPUs) تستغل وقتها في تنفيذ البرامج المختلفة. يعني لو عندنا أكتر من برنامج شغال في نفس الوقت، الـ Scheduler هو اللي بيتحكم في توزيع وقت الـ CPU على البرامج دي."
tags: ["scheduler", "operating-system", "computer-science", "process", "thread", "CPU"]
updatedAt: "2024-09-15"
featured: false
image: "https://assets.eqraatech.com/guides/process-scheduling.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/process-scheduling.png" alt="Process Scheduling" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

الـ **Scheduler** في أنظمة التشغيل هو عبارة عن العنصر اللي بيحدد إزاي وإمتى المعالجات (`CPUs`) تستغل وقتها في تنفيذ البرامج المختلفة. يعني لو عندنا أكتر من برنامج شغال في نفس الوقت، الـ **Scheduler** هو اللي بيتحكم في توزيع وقت الـ CPU على البرامج دي.

خلينا نتخيل إننا قاعدين بنذاكر وفي نفس الوقت بنحاول نرد على رسايل مابعوتالنا في السوشيال ميديا وعاوزين نشغل حاجة نسمعها. عقلنا هنا بيقوم بدور الـ **Scheduler** فهو اللي بيحدد إزاي هيقسم وقتنا بين التلات حاجات دول. ممكن نذاكر شوية وبعدين نرد على الرسايل وبعدين نرجع تذاكر تاني ونشغل معاها حاجة. فنفس الموضوع بالظبط بالنسبة للـ **CPU** والبرامج اللي شغالة.

---
## Process Scheduling

فيه عندنا 3 أنواع من الـ **Process Schedulers** اللي أنظمة التشغيل بتستخدمهم:

1. **الـ Long-Term Scheduler (Job Scheduler)**: وده المسؤول عن إنه يقرر انهي برنامج يدخل الـ **Ready Queue**، اللي هو Queue البرامج بتستنى فيه لحد ما الـ **CPU** يبقى فاضي ويبدأ يشتغل عليها. ده زي ما بنكون كده بنقرر إيه المواد اللي هنذاكرها في يومنا قبل ما نبدأ فعليا في مذاكرتها.
2. **الـ Short-Term Scheduler (CPU Scheduler)**: ده بيكون المسؤول عن إنه يقرر انهي البرامج الموجودة في الـ **Ready Queue** هياخد الـ **CPU** ويبدأ يشتغل عليه فعليًا. او بمعنى اصح يعني مين اللي عليه الدور دلوقتي ياخد وقت من دماغك.
3. **الـ Medium-Term Scheduler**: وده بيشتغل في بعض الأنظمة اللي بتستخدم تقنية الـ **Swapping**. فبيقرر إمتى يوقف برنامج من الشغل ويطلعه برا الذاكرة (RAM) عشان يدي امكانية لباقي البرامج انها تشتغل على الـ CPU. وبعدين لما يبقى فيه مكان فاضي يرجعه تاني.

---

## مصطلحات خاصة بالـ CPU Scheduling

- **الـ Arrival Time:** هو الوقت اللي الـ Process بتدخل فيه الـ Ready Queue وتكون مستنية يكون ليها وقت الـ CPU وتشتغل عليه.
- **الـ Completion Time:** ده الوقت اللي فيه الـ Process بتخلص الـ Execution بتاعها أو بتكون خلاص اتنفذت.
- **الـ Burst Time:** وده الوقت اللي بتحتاجه الـ Process عشان تتنفذ على الـ CPU.
- **الـ Turn-Around Time:** وده فرق الوقت بين الـ Completion Time والـ Arrival Time
- **الـ Waiting Time:** وده فرق الوقت بين الـ Turn-Around Time والـ Burst Time

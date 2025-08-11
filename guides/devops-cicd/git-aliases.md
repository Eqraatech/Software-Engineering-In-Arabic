---
title: "Git Aliases"
description: "Git aliases let you simplify and speed up your workflow with custom shortcuts for common commands. This guide shows how to create and use aliases to boost your productivity in Git."
excerpt: "بنستخدم Git للتعامل مع النسخ المختلفة من المشروع، لكن بعض أوامر Git ممكن تكون طويلة ومعقدة شوية. هنا بيجي دور Git Aliases، اللي هي أسماء مستعارة بتكون من إنشائك علشان تخلي استخدام Git أسرع وأكثر كفاءة."
tags: ["version-control", "git", "github", "gitlab"]
updatedAt: "2024-08-13"
featured: false
image: "https://assets.eqraatech.com/guides/git-aliases.png"
author: "ikhaledabdelfattah"
---

<img src="https://assets.eqraatech.com/guides/git-aliases.png" alt="Git Aliases" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

من المعروف أن Git واحدة من أهم الأدوات اللي لازم كل مطور يكون على دراية بيها.

بنستخدم Git للتعامل مع النسخ المختلفة من المشروع، لكن بعض أوامر Git ممكن تكون طويلة ومعقدة شوية. هنا بيجي دور Git Aliases، اللي هي أسماء مستعارة بتكون من إنشائك علشان تخلي استخدام Git أسرع وأكثر كفاءة.

الهدف من الأسماء المستعارة (Aliases) هو إنها تكون اختصارات لأوامر Git الطويلة والمعقدة. بدلاً من كتابة الأوامر الكاملة في كل مرة، تقدر تنشئ اسم مستعار قصير وسهل تتذكره لتنفيذ نفس الأمر بسرعة.

**فورقة وقلم وتعالوا نتكلم عن ازاي نقدر نستخدم Git Aliases في تسريع شغلنا 🚀**

---

## ازاي تنشئ اسم مستعار في Git؟

علشان تعمل كده، هتستخدم أمر **git config** بالشكل ده:

<!-- إنشاء Aliases -->
```bash
# إنشاء اسم مستعار عام
git config --global alias.<name> "<command>"

# مثال: إنشاء اختصار لـ git status
git config --global alias.st "status"

# مثال: إنشاء اختصار لـ git log مع خيارات متقدمة
git config --global alias.lg "log --oneline --graph --decorate --all"
```

<!-- إدارة Aliases -->
```bash
# عرض جميع الأسماء المستعارة
git config --global --get-regexp alias

# حذف اسم مستعار
git config --global --unset alias.<name>

# مثال: حذف الاسم المستعار st
git config --global --unset alias.st
```

<!-- استخدام Aliases -->
```bash
# استخدام الأسماء المستعارة
git st          # بدلاً من git status
git lg          # بدلاً من git log --oneline --graph --decorate --all
git co          # بدلاً من git checkout
git br          # بدلاً من git branch
```

---

## أمثلة على الأسماء المستعارة في Git

<!-- اختصارات أساسية -->
```bash
# اختصارات أساسية
git config --global alias.st "status"
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.ci "commit"
git config --global alias.cm "commit -m"
```

<!-- اختصارات الـ Log -->
```bash
# اختصارات متقدمة للـ log
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.lg1 "log --oneline -1"
git config --global alias.lg10 "log --oneline -10"
git config --global alias.lga "log --oneline --graph --decorate --all --author"
```

<!-- اختصارات الـ Diff -->
```bash
# اختصارات للـ diff
git config --global alias.df "diff"
git config --global alias.dfs "diff --staged"
git config --global alias.df1 "diff HEAD~1"
git config --global alias.df2 "diff HEAD~2"
```

<!-- اختصارات مفيدة -->
```bash
# اختصارات مفيدة أخرى
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
git config --global alias.visual "!gitk"
git config --global alias.staged "diff --cached"
```

---

## في الختام

ختاما استخدامك ل Git Aliases هيحسن كفاءتك ويوفر وقتك وانت بتتعامل مع اوامر GIt المتكرره , فابدا من دلوقتي واعمل اسماء مستعاره للاوامر اللي بتستخدمها بشكل متكرر , كل ما اتعودت علي استخدامها هتلاقي انتاجيتك زادت بشكل ملحوظ , وشاركنا تجربتك في التعليقات!
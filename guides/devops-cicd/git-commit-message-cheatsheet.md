---
title: "Git Commit Message Cheatsheet"
description: "Write clear and consistent commit messages with this quick guide. Covers best practices, common prefixes (feat, fix, refactor), and tips for meaningful version history and collaboration."
excerpt: "بعد كل تغيير بتحب تسجله علي ال Version Control اللي عليه المشروع الخاص بيك بتحتاج تكتب رسالة , الرسالة دي بتوضح ايه التغيير اللي أنت عملته في الكود  اللي أنت حاليا بترفعه علي Version Control."
tags: ["version-control", "git", "github", "gitlab"]
updatedAt: "2023-12-21"
featured: false
image: "https://assets.eqraatech.com/guides/git-commit-message-cheatsheet.png"
author: "ikhaledabdelfattah"
---

<img src="https://assets.eqraatech.com/guides/git-commit-message-cheatsheet.png" alt="Git Commit Message Cheatsheet" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

بعد كل تغيير بتحب تسجله علي ال Version Control اللي عليه المشروع الخاص بيك بتحتاج تكتب رسالة , الرسالة دي بتوضح ايه التغيير اللي أنت عملته في الكود  اللي أنت حاليا بترفعه علي Version Controlو كتير مننا بيتجاهل إنه يكتب الرسالة بشكل واضح يسهل عليه وعلي اللي بعده إنه يفهم من عنوان الرساله إيه اللي اتغير في الكود.

خلينا نقولك بسرعة على كلمات تقدر تبتدي بيها رسالتك، علشان تسهل عليك وتفهم اللي بعدك إيه اللي اتغير:

<!-- Feat (ميزة جديدة) -->
```bash
git commit -m 'feat: Add user profile picture upload functionality'
```
ميزة جديدة أضفتها للمشروع (Feature)

<!-- Fix (إصلاح مشكلة) -->
```bash
git commit -m 'fix: Resolve issue with login button not responding'
```
إصلاح مشكلة أو خطأ في الكود (Fix)

<!-- Chore (عمل روتيني) -->
```bash
git commit -m 'chore: Update project dependencies'
```
تغييرات روتينية أو صيانة لا تؤثر على منطق التطبيق (Chore)

<!-- Refactor (تحسين الكود) -->
```bash
git commit -m 'refactor: Improve code readability in authentication module'
```
تحسين الكود بدون إضافة ميزة أو إصلاح مشكلة (Refactor)

<!-- Docs (تحديث الوثائق) -->
```bash
git commit -m 'docs: Update README with installation instructions'
```
تحديث أو إضافة توثيق للمشروع (Docs)

<!-- Style (تنسيق الكود) -->
```bash
git commit -m 'style: Format code according to coding guidelines'
```
تغييرات في تنسيق الكود فقط (Style)

<!-- Test (اختبارات) -->
```bash
git commit -m 'test: Add unit tests for user authentication'
```
إضافة أو تعديل اختبارات (Test)

<!-- Perf (تحسين الأداء) -->
```bash
git commit -m 'perf: Optimize database queries for faster user retrieval'
```
تحسين أداء التطبيق (Performance)

<!-- Build (تغييرات في البناء) -->
```bash
git commit -m 'build: Update build process to include new dependencies'
```
تغييرات في نظام البناء أو الأدوات (Build)

<!-- Revert (تراجع عن تغيير) -->
```bash
git commit -m 'revert: Revert previous commit that caused issues'
```
تراجع عن تغيير سابق (Revert)

<!-- CI (تكامل مستمر) -->
```bash
git commit -m 'ci: Integrate automated testing into continuous integration pipeline'
```
تغييرات في إعدادات التكامل المستمر (CI)
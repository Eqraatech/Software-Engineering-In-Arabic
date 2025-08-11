---
title: "Program vs Process vs Thread"
description: "A program is a passive set of instructions, a process is an active instance of a program running with its own memory, and a thread is the smallest unit of execution within a process. This guide explains their differences and roles in computing."
excerpt: "في البرمجة ونظم التشغيل، بتستخدم مصطلحات زي الـ Program والـ Process والـ Thread بشكل متكرر. فخلونا نفهم الفرق بين المصطلحات دي بطريقة مبسطة وسهلة."
tags: ["process", "thread", "program", "operating-system", "computer-science"]
updatedAt: "2024-06-12"
featured: false
image: "https://assets.eqraatech.com/guides/program-vs-process-vs-thread.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/program-vs-process-vs-thread.png" alt="Program vs Process vs Thread" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

سؤال من ضمن أسئلة كتير كانت بتتسأل قبل كده في الانترفيوهات هو ايه الفرق بين الـ Process والـ Threads ؟  
وفي البرمجة ونظم التشغيل، بتستخدم مصطلحات زي الـ Program والـ Process والـ Thread بشكل متكرر. فخلونا نفهم الفرق بين المصطلحات دي بطريقة مبسطة وسهلة.

## ايه هو الـ Program ؟

الـ Program هو مجموعة من التعليمات المكتوبة بلغة برمجة معينة لتنفيذ مهمة محددة. ببساطة، هو الـ Code اللي بتكتبه وتخزنه في ملف. على سبيل المثال، ابسط برنامج هو ملف `hello_world.py` المكتوب بلغة بايثون واللي ممكن يكون بالشكل ده:

<!-- Python -->
```python
print("Hello, World!")
```

فالملف ده هو عبارة عن برنامج. وعشان يتم تنفيذ البرنامج ده، لازم يتم تحميله وتشغيله بواسطة نظام التشغيل.

وأمثلة تانية للـ Program هي التطبيقات اللي بنشغلها وموجودة بطبعيتها على سطح المكتب زي الـ Chrome أو الـ Microsoft Word على سبيل المثال

---

## ايه هي الـ Process ؟

الـ Process هو برنامج قيد التشغيل. يعني ايه ؟ يعني هو عبارة عن Program اتعمله Execute فلما نظام التشغيل بيروح يحمل البرنامج من الـ Disk للـ (RAM) ويبدأ في تنفيذه، بيتحول البرنامج بتاعنا إلى عملية (Process).

الـ Process بتحتوي على الـ Code القابل للتنفيذ، وبيانات البرنامج الخاصة بيه، ومجموعة من الموارد التي يستخدمها البرنامج أثناء تشغيله زي الـ Registers والـ Program Counter والـ Stack.

#### مثال:

لو جينا نشغل برنامج `hello_world.py` على جهازنا، نظام التشغيل هيروح يـ Create Process للبرنامج بتاعنا. والـ Process دي هتشمل جميع الموارد اللازمة لتنفيذ الـ Code بتاعنا وطباعته على الشاشة.

وعشان نبسط الموضوع أكتر , اما بنروح نفتح Chrome أو أي برنامج زي Microsoft Word , نظام التشغيل بيروح ينفذ الـ Instructions والـ Code اللي البرنامج بيتكون منه ويبدأ يحمله في الـ RAM ويجهز كل الموارد اللي البرنامج ده محتاجها.

وممكن البرنامج اما يروح للـ RAM ويشتغل يبقى عبارة عن أكتر من Process فالـ Chrome مثلا بتخلي كل Tab هتعملها تبقى في Process منفصلة تمامًا.

---

## ايه هو الـ Thread ؟

الـ Thread هو أصغر وحدة تنفيذ ممكن نظام التشغيل يديرها، فكل عملية (Process) بتحتوي على الأقل على Thread واحد بنسميه الـ Main Thread, والـ Thread ده بيمثل سلسلة من التعليمات اللي ممكن تنفيذها.

والـ Process الواحدة ممكن تحتوي على أكتر من Threads بتشتغل بشكل متوازي لتحسين الأداء.

**مثال 1**

فعلى سبيل المثال في الـ Microsoft Word كنا اتكلمنا في الـ Parallelism في مقال سابق عن ازاي بيستغل الـ Multi-Threading في انه بيخلي عملية الـ Find and Replace سهلة فهو يقدر لو عندك ملف ضخم وكبير انه يوزع عملية البحث دي على أكتر من Threads عشان يسرع عملية البحث.

**مثال 2**

وممكن برضو يكون عندنا أكتر من Thread غير الـ Main Thread زي انك تكتب عادي جدًا في ملف الـ Microsoft Word ده بيقوم بدوره Thread وفيه Thread تاني دوره انه يعمل Spell Checking.

**مثال 3**

ممكن يكون عندي مجموعة من الـ Files اللي عاوز احملها من على الانترنت واستغل في ده أكتر من Thread واحد عشان احسن من الأداء.

فبدل ما انزل كل File ورا التاني بشكل Sequential في الـ Main Thread, فده هيكون بطئ جدًا وده لان لو كل File هياخد مثلا دقيقة وعندي 3 ملفات فكده هستنى 3 دقائق , ولكن انا ممكن اعمل ده بشكل متوازي واحمل الـ 3 والـ 3 ينزلوا في دقيقة واحدة بس بحيث أخلي كل Thread ينزل ملف من الملفات.

**وده مثال بسيط بالـ python :**

<!-- Python Threading -->
```python
import threading
import time

def download_file(file_url):
    # Simulate file download
    time.sleep(1)
    print(f"Downloaded {file_url}")

file_urls = ["file1.txt", "file2.txt", "file3.txt"]

# Create threads for parallel download
threads = []
for url in file_urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All files downloaded!")
```

<!-- JavaScript Web Workers -->
```javascript
// JavaScript Web Workers (browser-based threading)
// main.js
const worker = new Worker('worker.js');

worker.postMessage({
    files: ['file1.txt', 'file2.txt', 'file3.txt']
});

worker.onmessage = function(e) {
    console.log('Downloaded:', e.data);
};

// worker.js
self.onmessage = function(e) {
    const files = e.data.files;
    
    files.forEach(file => {
        // Simulate download
        setTimeout(() => {
            self.postMessage(`Downloaded \${file}`);
        }, 1000);
    });
};
```

<!-- Java ThreadPool -->
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class FileDownloader {
    public static void main(String[] args) {
        String[] files = {"file1.txt", "file2.txt", "file3.txt"};
        
        // Create thread pool
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        for (String file : files) {
            executor.submit(() -> {
                try {
                    Thread.sleep(1000); // Simulate download
                    System.out.println("Downloaded " + file);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
        }
        
        executor.shutdown();
    }
}
```

---

## في الختام

- **الـ Program**: هو الـ Code المكتوب بلغة برمجة معينة واللي بيحتوي على مجموعة من الـ Instructions.
- **الـ Process**: هو برنامج قيد التشغيل يعني Runnable Program وبيتضمن الـ Code القابل للتنفيذ والبيانات والموارد الخاصة بيه.
- **الـ Thread**: هو أصغر وحدة تنفيذ داخل الـ Process، وممكن الـ Thread الواحد يشتغل بشكل متوازي مع Threads تانية لتحسين الأداء.
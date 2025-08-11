---
title: "WebSockets"
description: "WebSockets provide full-duplex communication between client and server over a single connection. This guide explains how they enable real-time features like chat, live updates, and multiplayer apps."
excerpt: "هي عبارة عن Communication Protocol مزدوجة الاتجاه بنقول عليها Full-Duplex Communication Channels وده كله من خلال TCP Connection واحد بس. وبالتالي بتسمح بعملية الـ Real-time والـ Event-Driven Connections بين الـ Client والـ Server."
tags: ["realtime", "websocket", "http", "sse", "long-polling", "short-polling", "web-development", "communication"]
updatedAt: "2024-05-12"
featured: true
image: "https://assets.eqraatech.com/guides/websockets-in-a-nutshell.png"
author: "mahyoussef"
---

<img src="https://assets.eqraatech.com/guides/websockets-in-a-nutshell.png" alt="WebSockets In a Nutshell" ondragstart="return false;" oncontextmenu="return false;" style="display: block; margin: 2rem auto; border-radius: 1rem; box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);" />

عشان نعرف قد ايه الـ Web Sockets ساعدت بشكل كبير في تطور صناعة البرمجيات محتاجين نبص على المثالين دول:

تخيلوا ان دلوقتي عاوزين نبعت رسالة لحد , فاللي هيحصل كالآتي هنروح نودي الرسالة لمكتب البريد , وبعدين هنفضل مستنين ان الشخص اللي استلمها يرد علينا , والرد ممكن يجي بسرعة وممكن ياخد وقت في بعض الاحيان وده بيعتمد على عوامل كتير زي مثلا المسافة اللي الرسالة دي محتاجة توصل من جهة للتانية وكذلك وقت الـ Processing بتاعها , وهكذا ..

وخلونا نتخيل مثال تاني ان عندنا تليفون أرضي بس بشكل مختلف شوية وهو ان عشان تكلم حد من صحابك محتاج تتصل وتساله سؤال وبعدين تقفل الخط وهو يرجع يتصل بيك يجاوبك على السؤال بتاعك ويسالك اللي هو عاوزه , وبعدين يقفل وتتصل تاني وترد عليه ..

الـ Paradigm في المثالين اللي فاتوا هو الـ **HTTP Request Response** وده التقليدي واللي بيتم استعماله في اغلب التطبيات حاليا .. وبكل بساطة الـ Client بيبعت Request للـ Server والـ Server يرد على الـ Client من خلال Response.

---

## **الفرق بين الـ WebSockets والـ HTTP Req/Res**

الـ `WebSockets` جت عشان تسمح بمشاركة البيانات بين الطرفين بشكل بيحصل in-real time بمعنى ان دلوقتي باه عندي وسيلة تواصل ثنائية الاتجاه او بنقول عليه `Bi-Directional Communication` وده معناه ان دلوقتي اصبح عندي الـ Server والـ Client الاتنين يقدروا يكلموا بعض في نفس الوقت.

خلونا نرجع لمثال الرسالة بتاعة مكتب البريد , بدل ما كنا هنبعت الرسالة ونستنى وقت ما معين لحد ما يجيلنا الرد , دلوقتي باه عندنا Messenger نقدر من خلاله نبعت الرسالة ونحصل على الرد بشكل لحظي ونتكلم في نفس الوقت مع بعض من غير منبعت كل شوية رسالة ونستنى الرد عليها.

وبالنسبة لمثال التليفون فاحنا في وقتنا الحالي نقدر نتكلم في التليفون احنا الاتنين في خط واحد ونسمع بعض ونتكلم في نفس الوقت

هو ده فرق الـ `WebSockets` عن البروتوكول التقليدي للـ `HTTP Request Response`.

---

## اي هي الـ Web Sockets ؟

هي عبارة عن `Communication Protocol` مزدوجة الاتجاه بنقول عليها `Full-Duplex Communication` Channels وده كله من خلال `TCP Connection` واحد بس. وبالتالي بتسمح بعملية الـ `Real-time` والـ `Event-Driven Connections` بين الـ Client والـ Server.

وعشان كده هنعرف كمان شوية في استعمالاتها انها كويسة اوي مع الـ Paradigms دي جدا.

---

## بنستعمل الـ Web Sockets في ايه ؟

احنا بنستعملها في التطبيقات وصناعة الـ Software اللي بتحتاج تحديث لحظي واستجابة لحظية بين طرفين زي:

1. الـ Real-time chats
2. الـ Messaging / Notifications
3. الألعاب الـ Multiplayer

---

## ازاي الـ WebSockets بيشتغل ؟

الـ `WebSockets` بتعمل `Persistent Connection` بين الـ Client والـ Server , وده معناه ان مجرد مالـ `Connection` يتفتح , الاتنين يقدروا يبعتوا البينات لبعض في اي وقت من غير اي عملية `Polling` مستمرة وبالتالي الـ Paradigm ده بيسمح بالـ `Real-time Communication` وان التحديثات تتبعت ويتم استقبالها بشكل لحظي.

---

## مثال عملي على الـ WebSockets 

خلينا نشوف مثال عملي على كيفية استخدام الـ WebSockets في تطبيق chat بسيط:

<!-- Server (Node.js) -->
```javascript
// Server-side (Node.js with ws library)
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function connection(ws) {
  console.log('Client connected');
  
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    
    // Broadcast message to all connected clients
    wss.clients.forEach(function each(client) {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message.toString());
      }
    });
  });
  
  ws.on('close', function close() {
    console.log('Client disconnected');
  });
});
```

<!-- Client (Browser) -->
```javascript
// Client-side (Browser JavaScript)
const ws = new WebSocket('ws://localhost:8080');

ws.onopen = function(event) {
  console.log('Connected to WebSocket server');
};

ws.onmessage = function(event) {
  console.log('Message from server:', event.data);
  // Display message in chat UI
  displayMessage(event.data);
};

ws.onclose = function(event) {
  console.log('Disconnected from WebSocket server');
};

// Send message function
function sendMessage(message) {
  if (ws.readyState === WebSocket.OPEN) {
    ws.send(message);
  }
}
```

<!-- Server (Python) -->
```python
# Server-side (Python with websockets)
import asyncio
import websockets

async def chat_handler(websocket, path):
    async for message in websocket:
        # Broadcast to all connected clients
        await websocket.send(f"Server received: {message}")

async def main():
    async with websockets.serve(chat_handler, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
```

في المثال ده:
- الـ Server بيستقبل اتصالات من الـ Clients
- كل client بيقدر يبعت رسائل للـ Server
- الـ Server بيبعت الرسائل لجميع الـ Clients المتصلين
- ده بيخلينا نقدر نعمل chat room بسيط

---

## في الختام

الـ `WebSockets` زيه زي أي `Protocol` للتواصل , بيقدم مميزات وليه عيوب , والشطارة هي اننا نفهم متطلبات الـ Business ونقرر اذا كان وجوده مفيد ولا لا , ونكون فاهمين ومتسعدين للتحديات اللي ممكن نواجهها , وفي بعض الاحيان بيكون كويس جدا ان يكون عندنا خطة بديلة زي الـ `HTTP Streaming` أو الـ `Long Polling` في الظروف اللي مش هيكون الـ `WebSockets` فيها متاح ومدعوم.
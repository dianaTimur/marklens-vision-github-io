<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>تفاعل مع السؤال</title>
  <style>
    .answer {
      display: none;
      margin-top: 10px;
      color: green;
      font-weight: bold;
    }
    .button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 20px;
      border: none;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <div>
    <p id="question">هل أنت مستعد لتحقيق نجاحك؟</p>
    <button class="button" onclick="toggleAnswer()">اضغط هنا لعرض الإجابة</button>
    <p class="answer" id="answer">نعم، النجاح يبدأ بخطوات صغيرة يومية. استمر في السعي نحو حلمك!</p>
  </div>

  <script>
    function toggleAnswer() {
      var answer = document.getElementById("answer");
      if (answer.style.display === "none") {
        answer.style.display = "block";
      } else {
        answer.style.display = "none";
      }
    }
  </script>

</body>
</html>
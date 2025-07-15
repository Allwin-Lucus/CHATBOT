async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chat-box");

  // Show user's message
  chatBox.innerHTML += `<div class="message user"><b>You:</b> ${message}</div>`;
  input.value = "";

  // Call backend API
  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    const reply = data.reply;

    chatBox.innerHTML += `<div class="message bot"><b>Bot:</b> ${reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

  } catch (err) {
    chatBox.innerHTML += `<div class="message bot"><b>Bot:</b> Error connecting to server.</div>`;
  }
}
    

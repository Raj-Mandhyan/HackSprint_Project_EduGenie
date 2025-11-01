document.getElementById("pingBtn").addEventListener("click", async () => {
  try {
    const res = await fetch("http://localhost:3000/");
    const text = await res.text();
    document.getElementById("response").innerText = text;
  } catch (error) {
    document.getElementById("response").innerText = "Backend not reachable 😢";
  }
});

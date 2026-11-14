// fetch() client for api_server.py — works in a browser or Node 18+.
// © Computational Classnotes · CC BY-NC-SA 4.0

async function callApi(message, url = "http://localhost:8000/api") {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });
  const data = await res.json();
  if (!data.ok) throw new Error(data.error);
  return data.result;
}

callApi("hi").then(console.log).catch(console.error); // -> "I am here"

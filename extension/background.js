chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === "scrape") {
      console.log("Scraped comments:", message.data);
  
      // Send comments to backend for processing
      fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ comments: message.data })
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Analysis results:", data);
          chrome.runtime.sendMessage({ type: "results", data: data });
        })
        .catch((error) => console.error("Error:", error));
    }
  });
  
document.getElementById("scrape-comments").addEventListener("click", () => {
    // Trigger content script to scrape comments
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        files: ["content.js"]
      });
    });
  });
  
  // Listen for results from background script
  chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === "results") {
      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = `
        <h2>Analysis Results</h2>
        <p>Positive: ${message.data.positive}</p>
        <p>Neutral: ${message.data.neutral}</p>
        <p>Negative: ${message.data.negative}</p>
        <h3>Key Phrases:</h3>
        <ul>
          ${message.data.key_phrases.map((phrase) => `<li>${phrase}</li>`).join("")}
        </ul>
      `;
    }
  });
  
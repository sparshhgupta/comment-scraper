async function scrapeComments() {
    const COMMENT_SELECTOR = "#content-text"; // Selector for main comment text
    const COMMENT_CONTAINER = "#comments"; // Selector for comment container
    const TOTAL_COUNT_SELECTOR = "yt-formatted-string.count-text"; // Selector for total comment count

    let comments = new Set(); // Using Set to avoid duplicates
    let commentContainer = document.querySelector(COMMENT_CONTAINER);

    if (!commentContainer) {
        console.error("Comment container not found.");
        return;
    }

    // Retrieve the total comment count
    let totalCountElement = document.querySelector(TOTAL_COUNT_SELECTOR);
    let totalCommentCount = 0;

    if (totalCountElement) {
        totalCommentCount = parseInt(totalCountElement.textContent.replace(/[^0-9]/g, ""), 10);
        console.log(`Total comments expected: ${totalCommentCount}`);
    } else {
        console.warn("Could not find total comment count. Proceeding without a limit.");
    }

    // Use MutationObserver to capture dynamically loaded comments
    let observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.nodeType === 1 && node.matches(COMMENT_SELECTOR)) {
                    comments.add(node.textContent.trim());
                }
            });
        });
    });

    observer.observe(commentContainer, { childList: true, subtree: true });

    // Scroll and process visible comments
    let scrollContainer = document.documentElement;
    let previousHeight = 0;
    let retries = 0;

    while (true) {
        // Process all currently visible comments
        const visibleComments = document.querySelectorAll(COMMENT_SELECTOR);
        visibleComments.forEach((comment) => {
            comments.add(comment.textContent.trim());
        });

        console.log(`Current scraped: ${comments.size}/${totalCommentCount || "unknown"}`);

        if (totalCommentCount && comments.size >= totalCommentCount) {
            console.log("All comments scraped.");
            break;
        }

        // Scroll to load more comments
        scrollContainer.scrollBy(0, 1000);
        await new Promise((resolve) => setTimeout(resolve, 1000));

        let currentHeight = scrollContainer.scrollHeight;

        if (currentHeight === previousHeight) {
            retries++;
            if (retries > 5) {
                console.warn("No more comments are loading. Stopping.");
                break;
            }
        } else {
            retries = 0; // Reset retries if new content is loaded
            previousHeight = currentHeight;
        }
    }

    observer.disconnect(); // Stop observing after scraping
    console.log("Final comments scraped:", Array.from(comments));

    // Send comments to background script
    chrome.runtime.sendMessage({ type: "comments", data: Array.from(comments) });
}

scrapeComments();
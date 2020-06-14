var resdata;

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    if (msg.action.localeCompare("renderSummary") === 0) {
        console.log(msg.data);
        resdata = msg.data;
        // chrome.runtime.openOptionsPage();
        chrome.tabs.create({ url: "src/html/options.html" });

    } else if (msg.action.localeCompare("ready") === 0) {
        sendResponse({ resdata });
    }
    return true;
});
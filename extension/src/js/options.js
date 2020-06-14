chrome.runtime.sendMessage({
    action: "ready"
}, function (res) {
    console.log(res.resdata);
    document.getElementById("title").innerHTML = res.resdata.Title;
    document.getElementById("summary").innerHTML = res.resdata.Summary;
});
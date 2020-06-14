function summarize() {
  chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {

    const data = {
      url: tabs[0].url,
    };

    fetch("http://localhost:5000/api", {
      method: "POST",
      credentials: "include",
      body: JSON.stringify(data),
      cache: 'no-cache',
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",

    })
      .then((response) => {
        return response.json();
      })
      .then((response) => {
        console.log(response);
        chrome.runtime.sendMessage({
          action: "renderSummary",
          data: response
        }, function () { });

      });
  });
}

document.addEventListener("DOMContentLoaded", function () {
  var btn = document.getElementById("btn");
  btn.addEventListener("click", summarize);
});
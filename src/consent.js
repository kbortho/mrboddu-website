/* Cookie consent for the Google tag (Analytics/Ads). Google's tag loads only after the visitor clicks Accept. */
(function () {
  var s = document.currentScript, ID = s.dataset.ads, BOOK = s.dataset.book, CALL = s.dataset.call, KEY = "mb-consent";
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  var loaded = false;
  function load() {
    if (loaded) return; loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("consent", "default", { ad_storage: "granted", ad_user_data: "granted", ad_personalization: "denied", analytics_storage: "granted" });
    gtag("js", new Date()); gtag("config", ID);
    var t = document.createElement("script"); t.async = true;
    t.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(ID);
    document.head.appendChild(t);
  }
  function track(label, name) {
    if (!loaded) return;
    if (label && ID.indexOf("AW-") === 0) gtag("event", "conversion", { send_to: ID + "/" + label });
    else gtag("event", name);
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a"); if (!a) return;
    var h = a.getAttribute("href") || "";
    if (h.indexOf("tel:") === 0) track(CALL, "phone_click");
    else if (h.indexOf("nuffieldhealth.com/consultants/mr-krishna-boddu#book") > -1) track(BOOK, "book_online_click");
  });
  function clear() {
    document.cookie.split(";").forEach(function (c) {
      var n = c.split("=")[0].trim();
      if (/^(_gcl|_ga|_gid)/.test(n)) ["", "; domain=.mrboddu.co.uk", "; domain=www.mrboddu.co.uk"].forEach(function (d) {
        document.cookie = n + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + d;
      });
    });
  }
  function banner() {
    if (document.getElementById("consent")) return;
    var d = document.createElement("div"); d.id = "consent"; d.className = "consent"; d.setAttribute("role", "region"); d.setAttribute("aria-label", "Cookie choice");
    d.innerHTML = '<p>With your permission, we use Google cookies to count visits and see whether our adverts help patients find us. <a href="/privacy/#cookies">More about cookies</a></p>' +
      '<div class="consent-btns"><button type="button" class="btn" data-c="yes">Accept</button><button type="button" class="btn btn-outline" data-c="no">Reject</button></div>';
    d.addEventListener("click", function (e) {
      var c = e.target.getAttribute && e.target.getAttribute("data-c"); if (!c) return;
      set(c); d.remove(); if (c === "yes") load(); else { clear(); if (loaded) location.reload(); }
    });
    document.body.appendChild(d);
  }
  var v = get();
  if (v === "yes") load(); else if (v !== "no") banner();
  document.addEventListener("click", function (e) {
    if (e.target.closest && e.target.closest("[data-cookie-settings]")) { e.preventDefault(); banner(); }
  });
})();

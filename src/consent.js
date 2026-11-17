/* Cookie consent for the Google tag (Analytics/Ads) and the Microsoft Advertising UET tag. Both load only after the visitor clicks Accept. */
(function () {
  var s = document.currentScript, ID = s.dataset.ads, BOOK = s.dataset.book, CALL = s.dataset.call, UETID = s.dataset.uet || "", KEY = "mb-consent";
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
    if (UETID) loadUet();
  }
  function loadUet() {
    /* Microsoft's standard UET snippet, run only after Accept. */
    window.uetq = window.uetq || [];
    window.uetq.push("consent", "default", { ad_storage: "granted" });
    var o = { ti: UETID, enableAutoSpaTracking: false, q: null }, n = document.createElement("script");
    n.src = "https://bat.bing.net/bat.js?ti=" + encodeURIComponent(UETID); n.async = 1;
    n.onload = function () { o.q = window.uetq; window.uetq = new window.UET(o); window.uetq.push("pageLoad"); };
    document.head.appendChild(n);
  }
  function track(label, name, done) {
    if (!loaded) return false;
    var p = { transport_type: "beacon" };
    if (done) { var called = false; p.event_callback = function () { if (!called) { called = true; done(); } }; setTimeout(p.event_callback, 600); }
    if (UETID && window.uetq) window.uetq.push("event", name, {});
    if (label && ID.indexOf("AW-") === 0) { p.send_to = ID + "/" + label; gtag("event", "conversion", p); }
    else gtag("event", name, p);
    return true;
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a"); if (!a) return;
    var h = a.getAttribute("href") || "";
    if (h.indexOf("tel:") === 0) {
      /* Phones switch to the dialler at once, which can stop the event being sent, so send it first, then dial. */
      if (track(CALL, "phone_click", function () { window.location.href = h; })) e.preventDefault();
    }
    else if (h.indexOf("nuffieldhealth.com/consultants/mr-krishna-boddu#book") > -1) track(BOOK, "book_online_click");
  });
  function clear() {
    document.cookie.split(";").forEach(function (c) {
      var n = c.split("=")[0].trim();
      if (/^(_gcl|_ga|_gid|_uet)/.test(n)) ["", "; domain=.mrboddu.co.uk", "; domain=www.mrboddu.co.uk"].forEach(function (d) {
        document.cookie = n + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + d;
      });
    });
    ["_uetsid", "_uetvid", "_uetsid_exp", "_uetvid_exp"].forEach(function (k) { try { localStorage.removeItem(k); } catch (e) {} });
  }
  function banner() {
    if (document.getElementById("consent")) return;
    var d = document.createElement("div"); d.id = "consent"; d.className = "consent"; d.setAttribute("role", "region"); d.setAttribute("aria-label", "Cookie choice");
    d.innerHTML = '<p>With your permission, we use Google and Microsoft cookies to count visits and see whether our adverts help patients find us. <a href="/privacy/#cookies">More about cookies</a></p>' +
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

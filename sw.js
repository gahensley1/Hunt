/* Scavenger & Hunt Co. — service worker.
   Scope: OFFLINE PLAY ONLY. The bandwidth argument is dead — a returning hunter
   already gets a 304 with zero bytes (SUPERHANDOFF s49 rule 1n). This exists so the
   app OPENS in a park with no signal, with the hunter's progress already safe in
   localStorage.

   NON-NEGOTIABLE RULES, in order of how badly they bite:

   1. NETWORK-FIRST FOR THE DOCUMENT. index.html is a single 3.8 MB file. Cache-first
      would pin every returning hunter to whatever build they last loaded, forever,
      with no way to push them off it. Network wins; the cache is only the fallback.
   2. NEVER TOUCH THE WORKER. Anything bound for the sync host is passed straight to
      the network, uncached. A cached roster is worse than no roster.
   3. NEVER CACHE A NON-GET, A NON-200, OR AN OPAQUE RESPONSE.
   4. VERSIONED CACHE. Bump CACHE on every ship that changes an asset; old caches are
      deleted on activate.

   This worker stores NO hunter data. Finds, status and credentials live in
   localStorage and on the Worker; losing this cache loses nothing. */

const CACHE = "shco-v3";
const SHELL = ["./", "./index.html", "./j.html", "./og-card.jpeg", "./award-card.jpeg"];

self.addEventListener("install", function(e){
  e.waitUntil(caches.open(CACHE).then(function(c){
    /* addAll is all-or-nothing; a single 404 would fail the whole install. */
    return Promise.all(SHELL.map(function(u){
      return c.add(new Request(u, {cache:"reload"})).catch(function(){});
    }));
  }));
  self.skipWaiting();
});

self.addEventListener("activate", function(e){
  e.waitUntil(caches.keys().then(function(ks){
    return Promise.all(ks.map(function(k){ return k===CACHE ? null : caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});

self.addEventListener("message", function(e){
  if(e.data && e.data.type==="SKIP_WAITING") self.skipWaiting();
});

/* 32u - WEB PUSH RECEIVE. Fires with the app CLOSED, which is the entire point:
   new Notification() and a page-context showNotification() only work while the app is on
   screen, and on iOS neither works at all. This handler plus a subscription is the ONLY
   path that reaches an iPhone - and there, only once the app is installed to the home
   screen (iOS 16.4+; unavailable in the EU under 17.4+).

   🔴 SCOPE, owner decision recorded at §64.3: GAME PLAY ONLY. A find is filed - finds are
   returned by the builder - a case is finished. NO re-engagement nudges, NO "come back and
   play", NO marketing of any kind. The boundary is easy to hold now and hard later. */
self.addEventListener("push", function(e){
  let d = {};
  try{ d = e.data ? e.data.json() : {}; }catch(_e){ try{ d = {body: e.data.text()}; }catch(__e){} }
  const title = d.title || "Scavenger & Hunt Co.";
  const opts = {
    body:  d.body || "",
    icon:  "./icons/icon-192.png",
    badge: "./icons/icon-192.png",
    tag:   d.tag || "shco",
    data:  {url: d.url || "./"}
  };
  e.waitUntil(self.registration.showNotification(title, opts));
});

/* 32r - NOTIFICATION CLICK. The client shows notifications through
   registration.showNotification(); without this handler a tap does nothing.
   Focus an open window if there is one, otherwise open the app. */
self.addEventListener("notificationclick", function(e){
  e.notification.close();
  e.waitUntil(
    self.clients.matchAll({type:"window", includeUncontrolled:true}).then(function(list){
      var u = (e.notification.data && e.notification.data.url) || "./";
      for(var i=0;i<list.length;i++){
        var c=list[i];
        if(c.url.indexOf(self.location.origin)===0 && "focus" in c){
          /* 32u - WARM ARRIVAL. The app is already open, so tell the page to open the
             roster in place. Reloading would re-download four megabytes to show a screen
             it is already holding. */
          try{ c.postMessage({type:"open-roster", code:(u.split("roster=")[1]||"")}); }catch(_e){}
          return c.focus();
        }
      }
      if(self.clients.openWindow) return self.clients.openWindow(u);
    })
  );
});

self.addEventListener("fetch", function(e){
  const req = e.request;
  if(req.method !== "GET") return;

  const url = new URL(req.url);

  /* Rule 2 — the sync host is never intercepted. */
  if(url.hostname.indexOf("workers.dev") > -1) return;
  /* Cross-origin (fonts, anything else) is left to the browser. */
  if(url.origin !== self.location.origin) return;

  const isDoc = req.mode === "navigate" || (req.headers.get("accept")||"").indexOf("text/html") > -1;

  if(isDoc){
    /* Rule 1 — network-first, cache only as a fallback. */
    e.respondWith(
      fetch(req).then(function(r){
        if(r && r.status===200 && r.type==="basic"){
          const copy = r.clone();
          caches.open(CACHE).then(function(c){ c.put(req, copy); }).catch(function(){});
        }
        return r;
      }).catch(function(){
        return caches.match(req).then(function(m){ return m || caches.match("./index.html"); });
      })
    );
    return;
  }

  /* Static same-origin assets: cache-first, revalidate in the background. */
  e.respondWith(
    caches.match(req).then(function(m){
      const net = fetch(req).then(function(r){
        if(r && r.status===200 && r.type==="basic"){
          const copy = r.clone();
          caches.open(CACHE).then(function(c){ c.put(req, copy); }).catch(function(){});
        }
        return r;
      }).catch(function(){ return m; });
      return m || net;
    })
  );
});

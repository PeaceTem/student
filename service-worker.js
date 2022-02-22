

self.addEventListener('install', e => {
    // console.log("installed");
    e.waitUntil(
        caches.open('static').then(cache => {
            return cache.addAll(["./images/tothex_192.png", "./images/tothex_500.png",
            "./images/tothex_512.png"]);
        })
    );
});

self.addEventListener('fetch', e => {
    console.log('Intercepting fetch request for: ${e.request.url}');
    e.respondWith(
        caches.match(e.request).then(response => {
            return response || fetch(e.request);
        })
    )
})
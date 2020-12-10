// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/web/css/estilos.css',
    '/static/web/img/001-24-hours.png',
    '/static/web/img/049-sedan.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
/*self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});*/

self.addEventListener("fetch", function(event) {
    event.respondWith(
        fetch(event.request)
        .then(function(result){
            return caches.open(staticCacheName)
            .then(function(c) {
                c.put(event.request.url, result.clone())
                return result;
            }
            )
        })
        .catch(function(e){
            return caches.match(event.request);

        })
    )
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyC4D_r_77OCvnPHTeDB6pTGFKPgzhl5LCA",
    authDomain: "mi-car-fd5ac.firebaseapp.com",
    projectId: "mi-car-fd5ac",
    storageBucket: "mi-car-fd5ac.appspot.com",
    messagingSenderId: "706690136311",
    appId: "1:706690136311:web:26c93c97b2c79a3674fbf2"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging  = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {

    let title = payload.notification.title;
    let options = {
        body: payload.notification.body,
        icon: payload.notification.icon
    }

    self.registration.showNotification(title, options);
});

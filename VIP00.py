<!DOCTYPE html>
<html>
    <head>
        <title>Snap! Build Your Own Blocks</title>
        <link rel="icon" href="src/favicon.ico" type="image/x-icon">
        <link rel="manifest" href="manifest.json">
        <link rel="apple-touch-icon" href="img/snap-icon-152.png">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="theme-color" content="white"/>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black">
        <meta name="apple-mobile-web-app-title" content="Snap!">
        <meta name="msapplication-TileImage" content="img/snap-icon-144.png">
        <meta name="msapplication-TileColor" content="#FFFFFF">
        <script src="src/morphic.js?version=2023-03-16"></script>
        <script src="src/symbols.js?version=2023-07-13"></script>
        <script src="src/widgets.js?version=2023-05-24"></script>
        <script src="src/blocks.js?version=2023-07-19"></script>
        <script src="src/threads.js?version=2023-07-14"></script>
        <script src="src/objects.js?version=2023-07-14"></script>
        <script src="src/scenes.js?version=2022-10-25"></script>
        <script src="src/gui.js?version=2023-07-19"></script>
        <script src="src/paint.js?version=2023-05-24"></script>
        <script src="src/lists.js?version=2023-07-18"></script>
        <script src="src/byob.js?version=2023-07-14"></script>
        <script src="src/tables.js?version=2023-07-05"></script>
        <script src="src/sketch.js?version=2023-05-24"></script>
        <script src="src/video.js?version=2019-06-27"></script>
        <script src="src/maps.js?version=2021-06-15"></script>
        <script src="src/extensions.js?version=2023-05-09"></script>
        <script src="src/xml.js?version=2021-07-05"></script>
        <script src="src/store.js?version=2023-06-29"></script>
        <script src="src/locale.js?version=2023-07-12"></script>
        <script src="src/cloud.js?version=2023-04-12"></script>
        <script src="src/api.js?version=2022-11-28"></script>
        <script src="src/sha512.js?version=2019-06-27"></script>
        <script src="src/FileSaver.min.js?version=2019-06-27"></script>
        <script>
            var world;
            window.onload = function () {
                var FPS = 67,
                    lastTime = 0,

                loop = (timestamp) => {
                    requestAnimationFrame(loop);
                    if (timestamp - lastTime < 1000 / FPS) {
                        return;
                    }
                    world.doOneCycle();
                    lastTime = Math.max(
                        lastTime + 1000 / FPS,
                        timestamp - 1000 / FPS
                    );
                };

                if ('serviceWorker' in navigator) {
                    navigator.serviceWorker.register('sw.js');
                }
                world = new WorldMorph(document.getElementById('world'));
                new IDE_Morph().openIn(world);
                requestAnimationFrame(loop);
            };
        </script>
    </head>
    <body style="margin: 0;">
        <canvas id="world" tabindex="1" style="position: absolute;"></canvas>
    </body>
</html>

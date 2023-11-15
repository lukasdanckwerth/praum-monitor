let index = {
    startTime: new Date(),

    loopDelay: 2000,
    loopTimer: null,
    loopCount: 0,

    startTimeFormatted() {
        return [
            new Date().toLocaleDateString("de-DE", {
                weekday: "long",
                year: "numeric",
                month: "long",
                day: "numeric",
            }),
            new Date().toLocaleTimeString("de-DE"),
        ].join(" ");
    },

    secondsElapsed() {
        return Math.floor(
            ((new Date().getTime() - index.startTime.getTime()) / 1000) % 60
        );
    },

    timeElapsedFormatted() {
        return new Date(index.secondsElapsed() * 1000)
            .toISOString()
            .substring(11, 19);
    },

    updateTimeElapsed() {
        document.getElementById("time-elapsed").innerText =
            index.timeElapsedFormatted();
    },

    loop() {
        index.loopCount += 1
        index.loopTimer = setTimeout(index.loop, index.loopDelay)
        document.getElementById("loop-count").innerText = "Loop: " + index.loopCount
    },

    startLoop() {
        index.loopTimer = setTimeout(index.loop, index.loopDelay)
    }
};

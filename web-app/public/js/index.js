let index = {
  startTime: new Date(),

  loopDelay: 2000,
  loopTimer: null,
  loopCount: 0,

  gasChart: null,

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
    index.loopCount += 1;
    index.loopTimer = setTimeout(index.loop, index.loopDelay);
    document.getElementById("loop-count").innerText =
      "Loop: " + index.loopCount;

    fetch("http://localhost:1312")
      .then((data) => data.json())
      .then((record) => {
        document.getElementById("celsius").innerText =
          Number(record.CELSIUS).toFixed(2) + " °C";
        document.getElementById("humidity").innerText =
          Number(record.HUMIDITY).toFixed(2) + " % r.F.";

        const labels = [...Array(index.loopCount).keys()].map((num) => num + 1);

        index.gasChart.data.labels = labels;
        index.gasChart.data.datasets[2].data.push(Number(record.CH4));
        index.gasChart.data.datasets[1].data.push(Number(record.SMOKE));
        index.gasChart.data.datasets[0].data.push(Number(record.ALCOHOL));
        index.gasChart.update();

        index.smokeChart.data.labels = labels;
        index.smokeChart.data.datasets[0].data.push(Number(record.SMOKE));
        index.smokeChart.update();

        index.alcoholChart.data.labels = labels;
        index.alcoholChart.data.datasets[0].data.push(Number(record.ALCOHOL));
        index.alcoholChart.update();

        index.ch4Chart.data.labels = labels;
        index.ch4Chart.data.datasets[0].data.push(Number(record.CH4));
        index.ch4Chart.update();

        document.getElementById("alcohol").innerText =
          Number(record.ALCOHOL).toFixed(2) + " alcohol";
        document.getElementById("humidity").innerText =
          Number(record.HUMIDITY).toFixed(2) + " % r.F.";
      });
  },

  startLoop() {
    index.loopTimer = setTimeout(index.loop, index.loopDelay);
  },
};

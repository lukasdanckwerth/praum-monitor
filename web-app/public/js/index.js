let index = {
  apiUrl: "http://localhost:1312",
  // apiUrl: "http://192.168.178.38:1312",
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
      (new Date().getTime() - index.startTime.getTime()) / 1000
    );
  },

  timeElapsedFormatted() {
    return new Date(index.secondsElapsed() * 1000)
      .toISOString()
      .substring(11, 19);
  },

  updateTimeElapsed() {
    index.updateElement("time-elapsed", index.timeElapsedFormatted());
  },

  updateElement(elementId, value) {
    document.getElementById(elementId).innerText = value;
  },

  loop() {
    index.loopCount += 1;
    index.loopTimer = setTimeout(index.loop, index.loopDelay);

    index.updateElement("loop-count", index.loopCount);

    fetch(index.apiUrl)
      .then((data) => data.json())
      .then((record) => {
        index.updateElement("celsius", Number(record.CELSIUS).toFixed(2));
        index.updateElement("humidity", Number(record.HUMIDITY).toFixed(2));

        const labels = [...Array(index.loopCount).keys()].map((num) => num + 1);

        index.gasChart.data.labels = labels;
        index.gasChart.data.datasets[2].data.push(Number(record.CH4));
        index.gasChart.data.datasets[1].data.push(Number(record.SMOKE));
        index.gasChart.data.datasets[0].data.push(Number(record.ALCOHOL));
        index.gasChart.data.datasets[3].data.push(Number(record.MOV));
        index.gasChart.data.datasets[4].data.push(Number(record.CELSIUS));
        index.gasChart.update();

        // index.movementChart.data.labels = labels;
        // index.movementChart.data.datasets[0].data.push(Number(record.MOV));
        // index.movementChart.update();

        // index.temperatureChart.data.labels = labels;
        // index.temperatureChart.data.datasets[0].data.push(
        //   Number(record.CELSIUS)
        // );
        // index.temperatureChart.update();

        // index.smokeChart.data.labels = labels;
        // index.smokeChart.data.datasets[0].data.push(Number(record.SMOKE));
        // index.smokeChart.update();

        // index.alcoholChart.data.labels = labels;
        // index.alcoholChart.data.datasets[0].data.push(Number(record.ALCOHOL));
        // index.alcoholChart.update();

        // index.ch4Chart.data.labels = labels;
        // index.ch4Chart.data.datasets[0].data.push(Number(record.CH4));
        // index.ch4Chart.update();
      });
  },
};

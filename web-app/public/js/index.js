let index = {
  apiUrl: "http://localhost:1312",
  // apiUrl: "http://192.168.178.38:1312",
  startTime: new Date(),

  loopDelay: 2000,
  loopTimer: null,
  loopCount: 0,

  averages: {
    co2: 0,
    mov: 0,
    sound: 0,
    celsius: 0,
    humidity: 0,
  },

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
    const el = document.getElementById(elementId);
    if (el) {
      el.innerText = value;
    }
  },

  loop() {
    console.log("averages", index.averages);

    index.loopCount += 1;
    index.loopTimer = setTimeout(index.loop, index.loopDelay);

    index.updateElement("loop-count", index.loopCount);

    const tempMin = 15;
    const tempMax = 25;

    fetch(index.apiUrl)
      .then((data) => data.json())
      .then((record) => {
        console.log(record);

        index.updateElement("celsius", Number(record.CELSIUS).toFixed(2));
        index.updateElement("humidity", Number(record.HUMIDITY).toFixed(2));

        const labels = [...Array(index.loopCount).keys()].map((num) => num + 1);

        index.gasChart.data.labels = labels;
        index.gasChart.data.datasets[0].data.push(Number(record.CO2) / 2);
        index.gasChart.data.datasets[1].data.push(Number(record.MOV));
        index.gasChart.data.datasets[2].data.push(Number(record.CELSIUS));
        index.gasChart.data.datasets[3].data.push(Number(record.SOUND));
        index.gasChart.update();

        const co2Gauge = Number(record.CO2 || 0) / 3000;
        gaugeChart.animateTo(co2Gauge);

        var temperatureGauge =
          (Number(record.CELSIUS || 0) - tempMin) / (tempMax - tempMin);
        temperatureGauge = Math.max(temperatureGauge, 0);
        // temperatureGauge = Math.min(temperatureGauge, tempMax);
        temperatureGaugeChart.animateTo(temperatureGauge);

        const percentage = {
          co2: co2Gauge,
          mov: Number(record.MOV),
          sound: Number(record.SOUND),
          temperature: temperatureGauge,
          humidity: Number(record.HUMIDITY) / 100,
        };

        function calcAverage(old, curr) {
          if (old === 0 || !old || index.loopCount == 0) {
            return curr;
          }

          const oldVal = ((index.loopCount - 1) / index.loopCount) * old;
          const newVal = (1 / index.loopCount) * curr;

          return oldVal + newVal;
        }

        index.averages.co2 = calcAverage(index.averages.co2, percentage.co2);
        index.averages.mov = calcAverage(index.averages.mov, percentage.mov);
        index.averages.sound = calcAverage(
          index.averages.sound,
          percentage.sound
        );
        index.averages.temperature = calcAverage(
          index.averages.temperature,
          percentage.temperature
        );
        index.averages.humidity = calcAverage(
          index.averages.humidity,
          percentage.humidity
        );

        // console.log("loop", index.loopCount);
        // console.log("percentage", percentage);
        // console.log("averages", index.averages);

        index.radar.data.datasets[0].data = [
          index.averages.co2,
          index.averages.mov,
          index.averages.sound,
          index.averages.temperature,
          index.averages.humidity,
        ];

        index.radar.update();
      });
  },
};

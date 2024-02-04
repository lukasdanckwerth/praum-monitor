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

  sumLoop: 0,
  movementCurr: 0,
  movementSum: 0,
  soundCurr: 0,
  soundSum: 0,
  loopIterations: 2,

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
    index.loopCount += 1;
    index.loopTimer = setTimeout(index.loop, index.loopDelay);

    index.updateElement("loop-count", index.loopCount);

    const tempMin = 15;
    const tempMax = 25;

    const gradient = document
      .getElementById("gas-chart")
      .getContext("2d")
      .createLinearGradient(0, 540, 0, 0);

    gradient.addColorStop(0, "#87CEFA66");
    gradient.addColorStop(0.4, "#87CEFA66");
    gradient.addColorStop(0.5, "#FFC10766");
    gradient.addColorStop(0.65, "#FFC10766");
    gradient.addColorStop(0.75, "#dc354566");
    gradient.addColorStop(1, "#dc354566");

    fetch(index.apiUrl)
      .then((data) => data.json())
      .then((record) => {
        console.log(record);

        index.sumLoop += 1;

        index.updateElement("celsius", Number(record.CELSIUS).toFixed(1));
        index.updateElement("humidity", Number(record.HUMIDITY).toFixed(1));
        index.updateElement("co2", Number(record.CO2).toFixed(0));

        const labels = [...Array(index.loopCount).keys()].map((num) => num + 1);
        index.gasChart.data.datasets[0].backgroundColor = gradient;
        index.gasChart.data.labels = labels;
        index.gasChart.data.datasets[0].data.push(Number(record.CO2));
        index.gasChart.data.datasets[1].data.push(Number(record.CELSIUS));
        index.gasChart.update();

        index.movementSum += record.MOV;
        index.soundSum += record.SOUND;

        console.log("sumLoop", index.sumLoop);
        console.log("movementCurr", index.movementCurr);
        console.log("movementSum", index.movementSum);

        if (index.sumLoop == index.loopIterations) {
          index.movementCurr = index.movementSum / index.loopIterations;
          index.movementSum = 0;

          index.soundCurr = index.soundSum / index.loopIterations;
          index.soundSum = 0;

          index.sumLoop = 0;

          const labels2 = [
            ...Array(Math.floor(index.loopCount / index.loopIterations)).keys(),
          ].map((num) => num + 1);

          console.log("labels2", labels2);

          index.otherChart.data.labels = labels2;
          index.otherChart.data.datasets[0].data.push(index.movementCurr);
          index.otherChart.data.datasets[1].data.push(index.soundCurr);
          index.otherChart.update();
        }

        // make gauge min to 400
        const co2Value = Math.max(Number(record.CO2 || 0), 400);
        const co2Gauge = (co2Value - 400) / (3000 - 400);

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

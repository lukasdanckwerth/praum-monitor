<script>
import TheGauge from "./components/TheGauge.vue";
import TheRadar from "./components/TheRadar.vue";
import Co2Chart from "./components/Co2Chart.vue";
import MovChart from "./components/MovChart.vue";

export default {
  components: {
    TheGauge,
    TheRadar,
    Co2Chart,
    MovChart,
  },
  mounted() {
    this.timeInterval = setInterval(this.updateTime, 1000);
    this.fetchData();
  },
  data() {
    this.apiUrl =
      process.env.NODE_ENV == "development"
        ? "http://192.168.178.38:1312"
        : "http://localhost:1312";
    this.currCelsius = 0;
    this.currHumidity = 0;
    this.currCo2 = 0;
    this.co2GaugeValue = 0;
    this.sumLoop = 0;
    this.loopCount = 0;
    this.loopTimer = null;
    this.movAggr = 0;
    this.movCurr = 0;
    this.soundAggr = 0;
    this.soundCurr = 0;
    this.radarData = [];
    this.groupSize = 5;
    this.avrgs = {
      co2: 0,
      mov: 0,
      sound: 0,
      temperature: 0,
      humidity: 0,
    };

    this.record = {};
    this.startTimeFormatted = [
      new Date().toLocaleDateString("de-DE", {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
      }),
      new Date().toLocaleTimeString("de-DE"),
    ].join(" ");

    this.loopTimer = null;
    this.startTime = new Date();

    return {
      loopCount: 0,
      secondsElapsed: 0,
    };
  },
  methods: {
    updateTime() {
      this.secondsElapsed = Math.floor(
        (Date.now() - this.startTime.getTime()) / 1000
      );
    },
    fetchData() {
      fetch(this.apiUrl)
        .then((data) => data.json())
        .then((record) => {
          console.log(record);

          const tempMin = 15;
          const tempMax = 25;
          const tempDif = tempMax - tempMin;

          this.loopCount += 1;

          this.currCelsius = Number(record.CELSIUS).toFixed(1);
          this.currHumidity = Number(record.HUMIDITY).toFixed(1);
          this.currCo2 = Number(record.CO2).toFixed(0);

          this.$refs.co2Chart.chart.data.labels.push("" + this.loopCount);
          this.$refs.co2Chart.chart.data.datasets[0].data.push(record.CO2);
          this.$refs.co2Chart.chart.data.datasets[1].data.push(record.CELSIUS);
          this.$refs.co2Chart.update();

          this.movAggr += record.MOV;
          this.soundAggr += record.SOUND;

          if (this.loopCount % this.groupSize == 0) {
            this.$refs.movChart.chart.data.labels.push("" + this.loopCount);
            this.$refs.movChart.chart.data.datasets[0].data.push(
              this.movAggr / this.groupSize
            );
            this.$refs.movChart.chart.data.datasets[1].data.push(
              this.soundAggr / this.groupSize
            );

            this.movAggr = 0;
            this.soundAggr = 0;

            this.$refs.movChart.update();
          }

          // make gauge min to 400
          const co2Value = Math.max(Number(record.CO2 || 0), 400);
          this.co2GaugeValue = (co2Value - 400) / (3000 - 400);

          const tempRelValue = (Number(record.CELSIUS) - tempMin) / tempDif;
          this.tempRelValue = Math.max(tempRelValue, 0);

          const perc = {
            co2: this.co2GaugeValue,
            mov: Number(record.MOV),
            sound: Number(record.SOUND),
            celsius: tempRelValue,
            hum: Number(record.HUMIDITY) / 100,
          };

          this.avrgs.co2 = this.average(this.avrgs.co2, perc.co2);
          this.avrgs.mov = this.average(this.avrgs.mov, perc.mov);
          this.avrgs.sound = this.average(this.avrgs.sound, perc.sound);
          this.avrgs.celsius = this.average(this.avrgs.celsius, perc.celsius);
          this.avrgs.hum = this.average(this.avrgs.hum, perc.hum);

          this.$refs.radar.chart.data.datasets[0].data = [
            this.avrgs.co2,
            this.avrgs.mov,
            this.avrgs.sound,
            this.avrgs.celsius,
            this.avrgs.hum,
          ];
          this.$refs.radar.chart.update();

          this.fetchTimer = setTimeout(this.fetchData, 3000);
        });
    },
    average(old, curr) {
      if (old === 0 || !old || this.loopCount == 0) {
        return curr;
      }

      const oldVal = ((this.loopCount - 1) / this.loopCount) * old;
      const newVal = (1 / this.loopCount) * curr;

      return oldVal + newVal;
    },
  },
  computed: {
    timeElapsed() {
      return new Date(this.secondsElapsed * 1000)
        .toISOString()
        .substring(11, 19);
    },
  },
};
</script>

<template>
  <main>
    <div class="app">
      <div class="row">
        <div class="col-3 text-center">
          <div style="margin-top: -10px">Co2</div>

          <TheGauge
            :value="co2GaugeValue"
            label-min="Clean"
            label-max="Dirty"
            stopColor1="MediumSeaGreen"
            stopColor2="orange"
            stopColor3="dimgray"
          />

	  <div> 
            <strong id="co2">{{ currCo2 }}</strong> ppm
          </div>
        </div>
        <div class="col-3 text-center">
          <div style="margin-top: -10px">Temparature</div>

          <TheGauge
            :value="co2GaugeValue"
            label-min="Cold"
            label-max="Hot"
            stopColor1="DodgerBlue"
            stopColor2="orange"
            stopColor3="#dc3545"
          />

	  <div> 
            <strong>{{ currCelsius }}</strong> °C (
            <strong>
              {{ currHumidity }}
            </strong>
            &nbsp;%&nbsp;r.F. )
          </div>
        </div>
        <div
          class="col-3"
          style="height: 300px; margin-top: -10px; padding-left: 50px"
        >
          <TheRadar ref="radar" class="mx-auto" />
        </div>

        <div class="col-3" style="text-align: right">
          <div class="mb-4">{{ startTimeFormatted }}</div>
          <div>
            Uptime: <strong> {{ timeElapsed }}</strong>
          </div>
          <div>
            Loop: <strong>{{ loopCount }}</strong>
          </div>
        </div>
      </div>

      <div class="row mt-4">
        <div
          class="col-12"
          style="height: 540px; width: 1900px; position: relative"
        >
          <Co2Chart ref="co2Chart" />

          <MovChart
            ref="movChart"
            style="position: absolute; top: 0; left: 0"
          />
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped></style>

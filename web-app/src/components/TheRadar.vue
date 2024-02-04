<script>
import {
  Chart as ChartJS,
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  RadialLinearScale,
  Title,
  RadarController,
  CategoryScale,
  Filler,
} from "chart.js";

ChartJS.register(
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  RadarController,
  RadialLinearScale,
  CategoryScale,
  Title,
  Filler,
);

export default {
  name: "TheChart",
  components: {},
  mounted() {
    this.labels = ["Co2", "Mov", "Sound", "Temperature", "Humidity"];
    this.config = {
      type: "radar",
      data: {
        labels: this.labels,
        datasets: [
          {
            data: this.dataArray,
            fill: true,
            backgroundColor: "rgba(54, 162, 235, 0.5)",
            borderColor: "rgb(54, 162, 235)",
            pointBackgroundColor: "rgb(54, 162, 235)",
            pointBorderColor: "#fff",
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: false,
          },
          title: {
            display: false,
          },
        },
        scales: {
          r: {
            min: 0,
            max: 1,
          },
        },
      },
    };

    this.ctx = this.$refs.chart;
    this.chart = new ChartJS(this.ctx, this.config);
  },
  methods: {},
};
</script>

<template>
  <canvas ref="chart" class="chart"></canvas>
</template>

<style scoped></style>

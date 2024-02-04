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
  BarController,
  BarElement,
} from "chart.js";

ChartJS.register(
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  RadialLinearScale,
  Title,
  RadarController,
  CategoryScale,
  BarController,
  BarElement
);

const lineWidth = 6;
const alphaHex = "77";
const alphaHexPoints = "77";

export default {
  name: "TheChart",
  props: {
    // labels: {
    //   type: Array,
    //   require: true,
    // },
    // co2Data: {
    //   type: Array,
    //   require: true,
    // },
    // celsiusData: {
    //   type: Array,
    //   require: true,
    // },
  },
  mounted() {
    this.labels = [];
    this.co2Data = [];
    this.celsiusData = [];
    this.ctx = this.$refs.chart;

    const gradient = this.ctx
      .getContext("2d")
      .createLinearGradient(0, 540, 0, 0);

    gradient.addColorStop(0, "#87CEFA66");
    gradient.addColorStop(0.4, "#87CEFA66");
    gradient.addColorStop(0.5, "#FFC10766");
    gradient.addColorStop(0.65, "#FFC10766");
    gradient.addColorStop(0.75, "#dc354566");
    gradient.addColorStop(1, "#dc354566");

    this.chart = new ChartJS(this.ctx, {
      type: "bar",
      data: {
        labels: this.computedLabels,
        datasets: [
          {
            label:
              "CO2                                                            ",
            data: this.co2Data,
            tension: 0.1,
            borderColor: "#87CEFA66",
            borderWidth: 2,
            borderRadius: 5,
            borderSkipped: false,
            backgroundColor: gradient,
            yAxisID: "y",
            order: 2,
          },
          {
            label: "Temperature",
            type: "line",
            data: this.celsiusData,
            tension: 0.3,
            borderColor: "#dc3545" + alphaHex,
            borderWidth: lineWidth,
            backgroundColor: "#dc3545" + alphaHexPoints,
            yAxisID: "yTemperature",
            order: 0,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        animation: true,

        elements: {
          point: {
            radius: 0,
          },
        },

        plugins: {
          legend: {
            reverse: true,
            labels: {
              font: {
                size: 20,
              },
            },
          },
        },
        scales: {
          x: {
            // stacked: true,
            grid: {
              drawOnChartArea: false, // only want the grid lines for one axis to show up
            },
            afterFit(scale) {
              scale.height = 30;
            },
          },
          y: {
            beginAtZero: true,
            min: 0,
            max: 3000,

            afterFit(scale) {
              scale.width = 60;
            },
          },

          yTemperature: {
            min: 15,
            max: 25,
            position: "right",
            // afterFit(scale) {
            //   scale.width = 90;
            // },
            grid: {
              drawOnChartArea: false, // only want the grid lines for one axis to show up
            },
          },
        },
      },
    });
  },
  methods: {
    update() {
      this.chart.update();
    },
  },
};
</script>

<template>
  <canvas ref="chart" class="chart"></canvas>
</template>

<style scoped></style>

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
    labels: {
      type: Array,
      require: true,
    },
    movData: {
      type: Array,
      require: true,
    },
    soundData: {
      type: Array,
      require: true,
    },
  },
  mounted() {
    this.ctx = this.$refs.chart;
    this.chart = new ChartJS(this.ctx, {
      type: "line",
      data: {
        labels: this.labels,
        datasets: [
          {
            label: "Movement",
            type: "line",
            data: this.movData,
            tension: 0.3,
            borderColor: "#6610f2" + alphaHex,
            borderWidth: lineWidth,
            backgroundColor: "#6610f2" + alphaHexPoints,
            order: 1,
          },
          {
            label: "Sound",
            type: "line",
            data: this.soundData,
            tension: 0.3,
            borderColor: "#2E8B57" + alphaHex,
            borderWidth: lineWidth,
            backgroundColor: "#2E8B57" + alphaHexPoints,
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
            labels: {
              font: {
                size: 20,
              },
            },
          },
        },
        layout: {
          padding: {
            left: 10,
          },
        },
        scales: {
          x: {
            display: false,
            stacked: true,
            ticks: {
              display: false,
            },
            grid: {
              drawOnChartArea: false, // only want the grid lines for one axis to show up
            },
            afterFit(scale) {
              scale.height = 30;
            },
          },

          y: {
            display: false,
            stacked: false,
            min: 0,
            max: 1.2,
            ticks: {
              display: false,
            },
            grid: {
              drawOnChartArea: false, // only want the grid lines for one axis to show up
            },
            afterFit(scale) {
              scale.width = 60;
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

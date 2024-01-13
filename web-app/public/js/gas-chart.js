const lineWidth = 6;
const alphaHex = "77";
const alphaHexPoints = "77";

const gasChartConfig = {
  type: "bar",
  data: {
    labels: [],
    datasets: [
      {
        label: "CO2",
        data: [],
        tension: 0.1,
        borderColor: "#99999999",
        borderWidth: 2,
        borderRadius: 5,
        borderSkipped: false,
        backgroundColor: "#99999966",
        yAxisID: "y",
        order: 2,
      },
      {
        label: "Movement",
        type: "line",
        data: [],
        tension: 0.3,
        borderColor: "#6610f2" + alphaHex,
        borderWidth: lineWidth,
        backgroundColor: "#6610f2" + alphaHexPoints,
        yAxisID: "yMovement",
        order: 1,
      },
      {
        label: "Temperature",
        type: "line",
        data: [],
        tension: 0.3,
        borderColor: "#dc3545" + alphaHex,
        borderWidth: lineWidth,
        backgroundColor: "#dc3545" + alphaHexPoints,
        yAxisID: "yTemperature",
        order: 0,
      },
      {
        label: "Sound",
        type: "line",
        data: [],
        tension: 0.3,
        borderColor: "#435Ba8" + alphaHex,
        borderWidth: lineWidth,
        backgroundColor: "#435Ba8" + alphaHexPoints,
        yAxisID: "ySound",
        order: 0,
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,

    animation: true,

    scales: {
      x: {
        stacked: true,
      },
      y: {
        stacked: true,
        beginAtZero: true,
        // type: "logarithmic",

        afterFit(scale) {
          scale.width = 44;
        },
      },
      yMovement: {
        display: false,
        stacked: false,
        min: 0,
        max: 1.2,
        ticks: {
          display: false,
        },
      },

      yTemperature: {
        stacked: false,
        min: 15,
        max: 25,
        position: "right",
        // afterFit(scale) {
        //   scale.width = 90;
        // },
      },

      ySound: {
        display: false,
        stacked: false,
        min: 0,
        max: 1.2,
        ticks: {
          display: false,
        },
      },
    },
  },
};

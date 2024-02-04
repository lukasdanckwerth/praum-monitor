const lineWidth = 6;
const alphaHex = "77";
const alphaHexPoints = "77";

var data1 = [];
var data2 = [];

const gasChartConfig = {
  type: "bar",
  data: {
    labels: [],
    datasets: [
      {
        label:
          "CO2                                                            ",
        data: data1,
        tension: 0.1,
        borderColor: "#87CEFA66",
        borderWidth: 2,
        borderRadius: 5,
        borderSkipped: false,
        backgroundColor: "#87CEFA66",
        yAxisID: "y",
        order: 2,
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
        stacked: true,
        grid: {
          drawOnChartArea: false, // only want the grid lines for one axis to show up
        },
        afterFit(scale) {
          scale.height = 30;
        },
      },
      y: {
        stacked: true,
        beginAtZero: true,
        // type: "logarithmic",
        min: 0,
        max: 3000,

        afterFit(scale) {
          scale.width = 60;
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
        grid: {
          drawOnChartArea: false, // only want the grid lines for one axis to show up
        },
      },
    },
  },
};

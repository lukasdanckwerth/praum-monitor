const otherChartConfig = {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Movement",
        type: "line",
        data: [],
        tension: 0.3,
        borderColor: "#6610f2" + alphaHex,
        borderWidth: lineWidth,
        backgroundColor: "#6610f2" + alphaHexPoints,
        order: 1,
      },
      {
        label: "Sound",
        type: "line",
        data: [],
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
};

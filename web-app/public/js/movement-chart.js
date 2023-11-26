const movementChartConfig = {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        type: "line",
        label: "Movement",
        data: [],
        borderColor: "#dc3545",
        backgroundColor: "#dc3545",
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        min: 0,
        max: 1.2,
        afterFit(scale) {
          scale.width = 90;
        },
        ticks: {
          display: false,
        },
      },
    },
  },
};

const temperatureChartConfig = {
  type: "line",
  data: {
    labels: [],
    datasets: [
      {
        label: "Temperature",
        data: [],
        tension: 0.1,
        borderColor: "gray",
        backgroundColor: "gray",
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        min: -10,
        max: 50,
        afterFit(scale) {
          scale.width = 90;
        },
      },
    },
  },
};

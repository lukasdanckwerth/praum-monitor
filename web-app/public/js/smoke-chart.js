const smokeChartConfig = {
  type: "bar",
  data: {
    labels: [],
    datasets: [
      {
        label: "SMOKE",
        data: [],
        tension: 0.1,
        borderColor: "gray",
        backgroundColor: "gray",
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        type: "logarithmic",
      },
    },
  },
};

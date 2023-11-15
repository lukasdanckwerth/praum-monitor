const alcoholChartConfig = {
  type: "bar",
  data: {
    labels: [],
    datasets: [
      {
        label: "ALCOHOL",
        data: [],
        tension: 0.1,
        borderColor: "yellow",
        backgroundColor: "yellow",
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

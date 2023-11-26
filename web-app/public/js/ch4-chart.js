const ch4ChartConfig = {
  type: "bar",
  data: {
    labels: [],
    datasets: [
      {
        label: "CH4",
        data: [],
        tension: 0.1,
        borderColor: "green",
        backgroundColor: "green",
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
};

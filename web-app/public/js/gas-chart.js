const gasChartConfig = {
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
      {
        label: "SMOKE",
        data: [],
        tension: 0.1,
        borderColor: "gray",
        backgroundColor: "gray",
      },
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
      x: {
        stacked: true,
      },
      y: {
        stacked: true,
        beginAtZero: true,
        type: "logarithmic",
      },
    },
  },
};

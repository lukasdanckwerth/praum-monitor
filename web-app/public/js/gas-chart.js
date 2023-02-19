const gasChartConfig = {
  type: "line",
  data: {
    labels: [1, 2, 3, 4, 5, 6, 7],
    datasets: [
      {
        label: "CH4",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
      {
        label: "LPG",
        data: [65, 59, 80, 81, 56, 55, 40],
        // fill: false,
        // borderColor: "rgb(75, 192, 192)",
        tension: 0.1,
      },
      {
        label: "H2",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
      {
        label: "SMOKE",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
      {
        label: "ALCOHOL",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
      {
        label: "CO",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
      {
        label: "ACETON",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
      {
        label: "TOLUENO",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
      {
        label: "CO2",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
      {
        label: "NH4",
        data: [65, 59, 80, 81, 56, 55, 40].map((item) => Math.random() * 100),
        tension: 0.1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
};

const gasChartConfig = {
  type: "bar",
  data: {
    labels: [],
    datasets: [
      {
        label: "Alcohol",
        data: [],
        tension: 0.1,
        borderColor: "#0d6efd",
        backgroundColor: "#0d6efd",
        yAxisID: "y",
        order: 2,
      },
      {
        label: "Smoke",
        data: [],
        tension: 0.1,
        borderColor: "#6c757d",
        backgroundColor: "#6c757d",
        yAxisID: "y",
        order: 2,
      },
      {
        label: "CH4",
        data: [],
        tension: 0.1,
        borderColor: "#198754",
        backgroundColor: "#198754",
        yAxisID: "y",
        order: 2,
      },
      {
        label: "Movement",
        type: "line",
        data: [],
        tension: 0.3,
        borderColor: "#dc3545",
        backgroundColor: "#dc3545",
        yAxisID: "yMovement",
        order: 1,
      },
      {
        label: "Temperature",
        type: "line",
        data: [],
        tension: 0.3,
        borderColor: "#fd7e14",
        backgroundColor: "#fd7e14",
        yAxisID: "yTemperature",
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
        type: "logarithmic",

        afterFit(scale) {
          scale.width = 90;
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
        min: -10,
        max: 50,
        position: "right",
        afterFit(scale) {
          scale.width = 90;
        },
      },
    },
  },
};

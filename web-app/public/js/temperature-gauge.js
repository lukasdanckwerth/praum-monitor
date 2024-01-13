function doIt() {
  const percentToDegree = (p) => p * 360;
  const degreeToRadian = (d) => (d * Math.PI) / 180;
  const percentToRadian = (p) => degreeToRadian(percentToDegree(p));

  class TemperatureGaugeChart {
    constructor(props) {
      this.svg = props.svg;
      this.group = this.svg.append("g");
      this.outerRadius = props.outerRadius;
      this.innerRadius = props.innerRadius;
      this.width = this.outerRadius * 2;
      this.height = this.outerRadius * 1.2;

      this.needle = new Needle({
        svg: this.svg,
        len: this.outerRadius * 0.65,
        radius: this.innerRadius * 0.15,
        x: this.outerRadius,
        y: this.outerRadius,
      });
    }

    render() {
      const gradient = this.svg
        .append("defs")
        .append("linearGradient")
        .attr("id", "c-chart-temperature__gradient");

      const arc = d3.arc();

      this.svg.attr("width", this.width).attr("height", this.height);

      gradient
        .append("stop")
        .attr("offset", "5%")
        .attr("class", "c-chart-temperature__gradient-stop1");
      gradient
        .append("stop")
        .attr("offset", "42%")
        .attr("class", "c-chart-temperature__gradient-stop2");
      gradient
        .append("stop")
        .attr("offset", "58%")
        .attr("class", "c-chart-temperature__gradient-stop3");
      gradient
        .append("stop")
        .attr("offset", "100%")
        .attr("class", "c-chart-temperature__gradient-stop4");

      arc
        .innerRadius(this.innerRadius)
        .outerRadius(this.outerRadius)
        .startAngle(-Math.PI / 2)
        .endAngle(Math.PI / 2);

      this.group
        .attr("width", this.width)
        .attr("height", this.height)
        .append("path")
        .attr("d", arc)
        .attr("fill", "url(#c-chart-temperature__gradient)")
        .attr(
          "transform",
          `translate(${this.outerRadius},${this.outerRadius})`
        );

      this.group.append("text").attr("x", 9).attr("y", 180).text("Cold");
      this.group.append("text").attr("x", 279).attr("y", 180).text("Hot");

      this.needle.render();
    }

    animateTo(p) {
      this.needle.animateTo(p);
    }
  }

  const svg = d3
    .select(".temperature-gauge")
    .append("svg")
    .attr("class", "c-chart-temperature");

  const temperatureGauge = new TemperatureGaugeChart({
    svg: svg,
    outerRadius: 160,
    innerRadius: 100,
  });

  temperatureGauge.render();
  temperatureGauge.animateTo(1);

  window.temperatureGaugeChart = temperatureGauge;
}

doIt();

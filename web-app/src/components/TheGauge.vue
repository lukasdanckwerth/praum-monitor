<script>
import * as d3 from "d3";

const percentToDegree = (p) => p * 360;
const degreeToRadian = (d) => (d * Math.PI) / 180;
const percentToRadian = (p) => degreeToRadian(percentToDegree(p));

export class Needle {
  constructor(props) {
    this.svg = props.svg;
    this.group = this.svg.append("g");
    this.len = props.len;
    this.radius = props.radius;
    this.x = props.x;
    this.y = props.y;
  }

  render() {
    this.group.attr("transform", `translate(${this.x},${this.y})`);

    this.group
      .append("circle")
      .style("fill", "#555555")
      .attr("cx", 0)
      .attr("cy", 0)
      .attr("r", this.radius);

    this.group
      .append("path")
      .style("fill", "#555555")
      .attr("d", this._getPath(0));
  }

  animateTo(p) {
    this.group
      .transition()
      .ease(d3.easeCubic)
      .select("path")
      .tween("progress", () => {
        const self = this;
        const lastP = this.lastP || 0;
        return function (step) {
          const progress = lastP + step * (p - lastP);
          d3.select(this).attr("d", self._getPath(progress));
        };
      })
      .each(() => (this.lastP = p));
  }

  _getPath(p) {
    const thetaRad = percentToRadian(p / 2),
      centerX = 0,
      centerY = 0,
      topX = centerX - this.len * Math.cos(thetaRad),
      topY = centerY - this.len * Math.sin(thetaRad),
      leftX = centerX - this.radius * Math.cos(thetaRad - Math.PI / 2),
      leftY = centerY - this.radius * Math.sin(thetaRad - Math.PI / 2),
      rightX = centerX - this.radius * Math.cos(thetaRad + Math.PI / 2),
      rightY = centerY - this.radius * Math.sin(thetaRad + Math.PI / 2);

    return `M ${leftX} ${leftY} L ${topX} ${topY} L ${rightX} ${rightY}`;
  }
}

export default {
  name: "TheGauge",
  props: {
    value: {
      type: Number,
      required: true,
    },
    title: {
      type: String,
      default: "Title",
    },
    labelMin: {
      type: String,
      default: "Min",
    },
    labelMax: {
      type: String,
      default: "Max",
    },
    stopColor1: {
      type: String,
      default: null,
    },
    stopColor2: {
      type: String,
      default: null,
    },
    stopColor3: {
      type: String,
      default: null,
    },
  },
  mounted() {
    const container = d3.select(this.$refs.gauge);
    this.svg = container.append("svg").attr("class", "c-chart-gauge");

    this.group = this.svg.append("g");
    this.outerRadius = 160;
    this.innerRadius = 100;
    this.width = this.outerRadius * 2;
    this.height = this.outerRadius * 1.2;

    this.needle = new Needle({
      svg: this.svg,
      len: this.outerRadius * 0.65,
      radius: this.innerRadius * 0.15,
      x: this.outerRadius,
      y: this.outerRadius,
    });

    const id = "c-chart-gauge__gradient" + Math.random();
    console.log("id", id);
    const gradient = this.svg
      .append("defs")
      .append("linearGradient")
      .attr("id", id);

    const arc = d3.arc();

    this.svg.attr("width", this.width).attr("height", this.height);

    gradient
      .append("stop")
      .attr("offset", "5%")
      .attr("stop-color", "" + this.stopColor1);

    gradient
      .append("stop")
      .attr("offset", "50%")
      .attr("stop-color", "" + this.stopColor2);

    gradient
      .append("stop")
      .attr("offset", "100%")
      .style("stop-color", "" + this.stopColor3);

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
      .attr("fill", "url(#" + id + ")")
      .attr("transform", `translate(${this.outerRadius},${this.outerRadius})`);

    this.group.append("text").attr("x", 7).attr("y", 180).text("Clean");
    this.group.append("text").attr("x", 270).attr("y", 180).text("Dirty");

    this.needle.render();
  },
  watch: {
    value(newValue) {
      this.needle.animateTo(newValue);
    },
  },
};
</script>

<template>
  <div ref="gauge" class="gauge"></div>
</template>

<style scoped></style>

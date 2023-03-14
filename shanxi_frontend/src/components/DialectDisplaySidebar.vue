<template>
  <div>
    <el-tabs tab-position="left" v-model="tabs0" class="tab1">
      <el-tab-pane label="方言展示"></el-tab-pane>
      <el-tab-pane label="查看分区"></el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tabs0: "0",
    };
  },
  mounted() {
    if (this.$route.path.toLowerCase() === "/dialectdisplay") {
      this.tabs0 = "0";
    } else if (this.$route.path.toLowerCase() === "/dialectclassification") {
      this.tabs0 = "1";
    }
  },
  watch: {
    tabs0(val) {
      if (val === "0") {
        if (this.$route.path.toLowerCase() !== "/dialectdisplay") {
          this.$router.push("/DialectDisplay");
        }
      } else if (val === "1") {
        if (this.$route.path.toLowerCase() !== "/dialectclassification") {
          this.$router.push("/DialectClassification");
        }
      }
    },
  },
};
</script>

<style scoped>
.el-tabs /deep/ .el-tabs__active-bar {
  background-color: #f79216;
}
.el-tabs /deep/ .el-tabs__item:hover {
  color: #d48906;
}
.el-tabs /deep/ .el-tabs__item {
  margin-right: 10px;
}
.el-tabs /deep/ .el-tabs__item.is-active {
  color: #fff;
  background-color: #f79216;
}
.el-tabs /deep/ .el-tabs__nav-wrap:after {
  background-color: #fae0b4;
}
</style>
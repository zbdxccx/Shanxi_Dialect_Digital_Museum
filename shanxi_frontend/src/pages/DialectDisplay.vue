<!--
    @description: 方言展示页面
    @author: longxiaoming
-->

<template>
  <div class="dialect-display-whole">
    <Header></Header>
    <div class="page-main">
      <div class="side-bar">
        <sidebar></sidebar>
      </div>
      <div class="dialect-main">
        <dialect-display-list></dialect-display-list>
      </div>
      <div class="dialect-side">
        <div style="font-size: 20px; border-bottom: 2px #fa8b06 solid">
          常见分区
        </div>
        <div>
          <div
            class="side-tag"
            v-for="item in commonClassifications"
            :key="item.name"
            @click="handleClickTag(item)">
            {{ item.name }}
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "@/components/header";
import Footer from "@/components/ShanxiFooter";
import DialectDisplayList from "@/components/DialectDisplayList";
import Sidebar from "@/components/DialectDisplaySidebar.vue";
export default {
  components: {
    Header,
    Footer,
    DialectDisplayList,
    Sidebar,
  },
  data() {
    return {
      commonClassifications: [],
    };
  },

  methods: {
    getCommonClassifications() {
      this.$http
        .post("/display/dialect_display/get_common_classification/")
        .then((res) => {
          this.commonClassifications = res.data.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    handleClickTag(item) {
      this.$router.push({
        path: "/DialectClassification",
        query: {
          classification: item.name,
        },
      });
    },
  },

  mounted() {
    this.getCommonClassifications();
  },
};
</script>

<style scoped>
.dialect-display-whole {
  background: rgb(190, 171, 143);
}
.page-main {
  background: #efdac3;
  width: 1100px;
  margin: 0 auto;
  padding: 10px;
  min-height: 800px;
}
.side-bar {
  display: inline-block;
  vertical-align: top;
  width: 120px;
}
.dialect-main {
  width: 670px;
  display: inline-block;
  vertical-align: top;
}
.dialect-side {
  width: 200px;
  display: inline-block;
  vertical-align: top;
  text-align: left;
  margin: 10px 0 0 10px;
  border-left: #f78b06 2px dashed;
  padding-left: 5px;
  height: 500px;
}
.side-tag {
  margin: 10px;
  background-color: #fff;
  display: inline-block;
  border-radius: 10px;
  padding: 7px;
  box-shadow: 0 0 5px #f78b06;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  vertical-align: top;
}
.side-tag:hover {
  background-color: #f4bf80;
  color: #fff;
}
</style>
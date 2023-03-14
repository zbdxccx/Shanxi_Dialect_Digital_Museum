<!--
    @description: 方言展示页面
    @author: longxiaoming
-->

<template>
  <div class="dialect-classification-whole">
    <Header></Header>
    <div class="page-main">
      <div class="side-bar">
        <sidebar></sidebar>
      </div>
      <div class="dialect-main">
        <dialect-classification-list></dialect-classification-list>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>
    
<script>
import Header from "@/components/header";
import Footer from "@/components/ShanxiFooter";
import DialectClassificationList from "@/components/DialectClassificationList.vue";
import Sidebar from "@/components/DialectDisplaySidebar.vue";
export default {
  components: {
    Header,
    Footer,
    DialectClassificationList,
    Sidebar,
  },
  data() {
    return {
    };
  },

  mounted() {},
};
</script>
    
<style scoped>
.dialect-classification-whole {
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
</style>
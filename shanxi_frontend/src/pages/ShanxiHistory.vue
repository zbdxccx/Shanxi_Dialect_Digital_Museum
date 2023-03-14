<template>
  <a-layout id="components-layout-demo-top-side-2">
    <a-layout-header class="header">
      <Header></Header>
    </a-layout-header>
    <a-layout>
      <a-layout-sider width="200" style="background: #fff">
        <a-menu theme="light" mode="inline" :default-selected-keys="['0']" @click="handelClick">
          <a-menu-item key="0">
            <span class="nav-text">简介</span>
          </a-menu-item>
          <a-menu-item key="1" ref="first">
            <span class="nav-text">古晋语的形成与扩张</span>
          </a-menu-item>
          <a-menu-item key="2" ref="second">
            <span class="nav-text">古晋语的分化</span>
          </a-menu-item>
          <a-menu-item key="3" ref="third">
            <span class="nav-text">民族融合与境外扩散</span>
          </a-menu-item>
         </a-menu>
      </a-layout-sider>
        <a-layout style="padding: 0 ">
          <a-layout-content
            :style="{ background: '#fff', margin: 0, minHeight: '280px' }"
          >
            <history-images v-if="isHistoryImages" @prefer="handelSonClick"></history-images>
            <history-form v-if="isHistoryForm"></history-form>
            <history-division v-if="isHistoryDivision"></history-division>
            <history-fusion v-if="isHistoryFusion"></history-fusion>
          </a-layout-content>
        </a-layout>
    </a-layout>
    <a-layout-footer style="text-align: center">
        <Footer></Footer>
    </a-layout-footer>
  </a-layout>
</template>
<script>
import HistoryImages from '../components/HistoryImages'
import HistoryForm from '../components/HistoryForm'
import HistoryDivision from '../components/HistoryDivision.vue';
import HistoryFusion from '../components/HistoryFusion.vue';
import Header from '../components/header.vue';
import Footer from '../components/ShanxiFooter.vue';
export default {
  components: { HistoryImages, HistoryForm, HistoryDivision, HistoryFusion, Header, Footer },
    data () {
      return {
        isHistoryImages: true,
        isHistoryForm: false,
        isHistoryDivision: false,
        isHistoryFusion: false,
      }
    },
    methods: {
      handelClick (item) {
        switch (item.key) {
          case '0':
            this.$data.isHistoryImages = true;
            this.$data.isHistoryForm = false;
            this.$data.isHistoryDivision = false;
            this.$data.isHistoryFusion = false;
          break;
          case '1':
            this.$data.isHistoryImages = false;
            this.$data.isHistoryForm = true;
            this.$data.isHistoryDivision = false;
            this.$data.isHistoryFusion = false;
          break;
          case '2':
            this.$data.isHistoryImages = false;
            this.$data.isHistoryForm = false;
            this.$data.isHistoryDivision = true;
            this.$data.isHistoryFusion = false;
          break;
          case '3':
            this.$data.isHistoryImages = false;
            this.$data.isHistoryForm = false;
            this.$data.isHistoryDivision = false;
            this.$data.isHistoryFusion = true;
          break;
          default:
            console.log("error");
        }
      },
      handelSonClick (index) {
        switch (index) {
          case 1:
            this.$refs.first.$el.click()
          break;
          case 2:
            this.$refs.second.$el.click()
          break;
          case 3:
            this.$refs.third.$el.click()
          break;
          default:
            console.log("error");
        }
      }
    }
};
</script>

<style scoped>
#components-layout-demo-top-side-2 {
  background-color: #fff;
}
.ant-layout-header {
  padding: 0;
  height: auto;
  margin-bottom: 10px;
}
.ant-menu-item-selected {
    background-color: rgba(171, 117, 42) !important;
    color: #fff !important;
}
.ant-menu-item-selected::after {
  border-right: 3px solid rgba(171, 117, 42) !important;
}
.ant-menu-item-active{
  background-color: rgba(171, 117, 42) !important;
  color: #fff !important;
}
#components-layout-demo-fixed-side {
  background-color: rgba(255, 255, 255) !important;
}
.ant-layout-footer {
  padding: 0;
}
</style>

<template>
  <div>
    <a-button type="primary" @click="showDrawer" ghost>
      产品收藏夹
    </a-button>
    <a-drawer
      title="产品收藏夹"
      placement="right"
      :closable="true"
      :visible="visible"
      :after-visible-change="afterVisibleChange"
      @close="onClose"
    >
      <product-card v-for="collection in collections" :product-item="collection"></product-card>
    </a-drawer>
  </div>
</template>
<script>
import ProductCard from "./ProductCard"
import {Message} from "element-ui"
export default {
  name: "GoodsCollection",
  components: {ProductCard},
  data() {
    return {
      visible: false,
      collections: []
    }
  },
  methods: {
    afterVisibleChange(val) {
    },
    showDrawer() {
      this.getCollections()
      this.visible = true
    },
    onClose() {
      this.visible = false
    },
    getCollections() {
      this.collections = []
      const params = new URLSearchParams()
      params.append("name", this.inputValue)
      this.$http.post("/display/product/getCollections/", params)
        .then(res => {
          if (res.data === 'error') {
            Message.warning('后端函数错误')
          }
          else {
            for(const element of res.data) {
              this.collections.push(element.fields)
            }
          }
        })
        .catch(() => {
          Message.error('出现错误！')
        })
    }

  },
}
</script>

<style scoped>
.ant-btn-background-ghost.ant-btn-primary {
  color: #232324 !important;
  border-color: #8a8a8a !important;
}
</style>

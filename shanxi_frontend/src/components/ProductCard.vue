<template>
  <div class="book-example">
    <a-card :title="productItem.name" :hoverable="true" style="max-width: 180px">
      <img
        :src="productItem.image_url"
        slot="cover"
        referrerpolicy="no-referrer"
        @click="jumpToMall"
      >
      <a-card-meta class="description"
        :description="productItem.introduction"
      ></a-card-meta>
      <a-icon class="save" type="check" @click="collect"/>
      <a-icon class="save" type="close" @click="deleteCollection"/>
    </a-card>
  </div>
</template>

<script>
import {Message} from "element-ui";

export default {
  name: "ProductCard",
  props: {
    productItem: {
      type: [],
      default: function (){
        return {
          name : "default_product",
          category: "产品大厅",
          introduction: "山西古书籍概览, 卫青，字仲卿，河东平阳（今山西临汾市）人。",
          image_url: "https://img.dpm.org.cn/Uploads/Picture/2016/12/29/s5864b06921de3.png",
          product_url: "https://space.bilibili.com/594844283?spm_id_from=333.337.0.0"
        }
      }
    }
  },
  methods: {
    jumpToMall() {
      window.open(this.productItem.product_url)
    },
    collect() {
      const params = new URLSearchParams()
      params.append("name", this.productItem.name)
      this.$http.post("/display/product/collect/", params)
        .then(res => {
          if (res.data === 'error') {
            Message.warning('后端函数错误！')
          }
          else {
            Message.success('收藏成功！')
          }
        })
        .catch(() => {
          Message.error('出现错误！')
        })
    },
    deleteCollection() {
      const params = new URLSearchParams()
      params.append("name", this.productItem.name)
      this.$http.post("/display/product/deleteCollection/", params)
        .then(res => {
          if (res.data === 'error') {
            Message.warning('后端函数错误！')
          }
          else {
            Message.success("取消收藏成功！")
          }
        })
        .catch(() => {
          Message.error('出现错误！')
        })
    },
  }
}
</script>

<style scoped>
.book-example {
  display: inline-block;
  justify-content: space-around;
  padding-bottom: 20px;
  width: 250px;
  padding-left: 30px;
}
.save {
  margin-left: 20px;
  margin-right: 20px;
}
.description {
  font-size: 10px;
  margin-bottom: 10px;
}
</style>

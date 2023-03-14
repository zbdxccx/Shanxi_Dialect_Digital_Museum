<template>
  <div>
    <a-layout>
      <Header></Header>
      <carousel :image-list="imageList"></carousel>
      <a-layout>
        <a-layout-sider width="200" style="background: #fff">
          <a-menu theme="light" mode="inline" :default-selected-keys="['0']" @click="handelClick">
            <a-menu-item key="0">
              <span class="nav-text">产品大厅</span>
            </a-menu-item>
            <a-menu-item key="1" ref="first">
              <span class="nav-text">笔墨纸砚</span>
            </a-menu-item>
            <a-menu-item key="2" ref="second">
              <span class="nav-text">锦罗绸缎</span>
            </a-menu-item>
            <a-menu-item key="3" ref="third">
              <span class="nav-text">民俗小吃</span>
            </a-menu-item>
           </a-menu>
          <goods-collection></goods-collection>
        </a-layout-sider>
        <a-layout-content class="content">
          <div class="layout-content">
            <p class="main-font1"><img src="./../assets/images/cultural_product/title.png" width="300"></p>
            <p class="main-history">卷卷古籍、琅琅衣饰</p>
            <p class="main-history">通过自己的方式</p>
            <p class="main-history">讲述了闺阁佳丽、逸士高隐、市井生活、明君贤臣的典故或故事……</p>
            <p class="main-history">让我们了解古人思想情趣，体验古人文娱暇时</p>
            <p class="main-history">山西方言数字博物馆是南开大学软件学院软件工程课程，山西方言小组的作业展示，与商业无关</p>

            <div>
              <a-input-search class="search" placeholder="输入产品名" style="width: 400px" @search="getProduct" v-model="inputValue"/>
            </div>
            <div class="books">
              <product-card v-for="item in productList" :product-item="item"></product-card>
            </div>
          </div>
        </a-layout-content>
      </a-layout>
      <shanxi-footer></shanxi-footer>
    </a-layout>

  </div>
</template>

<script>
import ProductCard from "../components/ProductCard"
import Header from "../components/header"
import ShanxiFooter from "../components/ShanxiFooter"
import GoodsCollection from "../components/GoodsCollection"
import Carousel from "../components/carousel"
import {Message} from 'element-ui'
export default {
  name: "CulturalProduct",
  components :{Carousel, GoodsCollection, ProductCard, Header, ShanxiFooter },
  created: function() {
    this.getProduct()
  },
  data () {
      return {
        inputValue:"",
        isOverView: true,
        isBooks: false,
        isClothes: false,
        isFood: false,
        imageList: [
          require("../assets/images/cultural_product/masks.jpg"),
          require("../assets/images/cultural_product/hats.jpg"),
          require("../assets/images/cultural_product/plates.jpg"),
          require("../assets/images/cultural_product/books.jpg"),
        ],
        productList: []
      }
    },
    methods: {
      handelClick(item) {
        switch (item.key) {
          case '0':
            this.$data.isOverView = true
            this.$data.isBooks = false
            this.$data.isClothes = false
            this.$data.isFood = false
            this.getProduct()
            break
          case '1':
            this.$data.isOverView = false
            this.$data.isBooks = true
            this.$data.isClothes = false
            this.$data.isFood = false
            this.getProduct()
            break;
          case '2':
            this.$data.isOverView = false
            this.$data.isBooks = false
            this.$data.isClothes = true
            this.$data.isFood = false
            this.getProduct()
            break;
          case '3':
            this.$data.isOverView = false
            this.$data.isBooks = false
            this.$data.isClothes = false
            this.$data.isFood = true
            this.getProduct()
            break;
          default:
            Message.error("error")
        }
      },
      getProduct() {
        this.productList = []
        const params = new URLSearchParams()
        params.append("name", this.inputValue)
        this.$http.post("/display/product/getProduct/", params)
          .then(res => {
            if (res.data === 'Haven\'t found') {
              Message.warning('未找到该产品！请检查输入')
              this.inputValue = ""
              this.getProduct()
            }
            else if (res.data === 'error') {
              Message.error('后端错误！')
            }
            else {
              for(const element of res.data) {
                if(this.isFood && element.fields.category === "民俗小吃") {
                  this.productList.push(element.fields)
                }
                else if(this.isBooks && element.fields.category === "笔墨纸砚") {
                  this.productList.push(element.fields)
                }
                else if(this.isClothes && element.fields.category === "锦罗绸缎") {
                  this.productList.push(element.fields)
                }
                else if(this.isOverView){
                  this.productList.push(element.fields)
                }
                else if(res.data.length <= 5) {
                  if(res.data[0] === element)
                    Message.success('检索成功！')
                  this.productList.push(element.fields)
                }
              }
            }
          })
          .catch(() => {
            Message.error('出现错误！')
          })
        this.inputValue = ""
      }
    }
}
</script>

<style scoped>
.layout-content {
  min-height: 300px;
  background: url("../assets/images/work/background.png") repeat;
}
.search {
  margin-bottom: 50px;
}
.main-font1 {
  font-size: 45px;
  padding-top: 40px;
}
.main-history {
  font-size: 20px;
  margin-top: -10px;
  font-family:  cursive;
}
.content {
  overflow: auto;
  height: 500px;
  min-height: 800px;
}

</style>

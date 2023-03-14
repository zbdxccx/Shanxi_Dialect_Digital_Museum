<template>
  <div class="block">
    <el-carousel :height="bannerHeight+'px'" loop>
      <el-carousel-item v-for="item in imageList" :key="item">
        <img :src="item" class="rightImg" alt="轮播图无法打开">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: "Carousel",
  props: {
    imageList: {
      type: [],
      default: [
        require("../assets/home/home1.png"),
        require("../assets/carousel/lunbotu1.jpg"),
        require("./../assets/carousel/lunbotu3.jpg"),
        require("./../assets/carousel/lunbotu4.jpg"),
      ]
    }
  },
  data() {
    return {
      images : [],
      imgList: [
        // require("../assets/carousel/lunbotu1.jpg"),
        //  require("./../assets/carousel/lunbotu2.jpg"),
        //  require("./../assets/carousel/lunbotu3.jpg"),
        //  require("./../assets/carousel/lunbotu4.jpg"),
      ],
      // 图片父容器高度
      bannerHeight: 1000,
      // 浏览器宽度
      screenWidth: 0

    }
  },
  methods: {
    setSize: function () {
      // 通过浏览器宽度(图片宽度)计算高度
      this.bannerHeight = 600 / 1550 * this.screenWidth
    }
  },
  mounted () {
    // 首次加载时,需要调用一次
    this.screenWidth = window.innerWidth
    this.setSize()
    // 窗口大小发生改变时,调用一次
    window.onresize = () => {
      this.screenWidth = window.innerWidth
      this.setSize()
    }
  }


}
</script>
<style scoped>
  .el-carousel-item{
      color: #fff;
      /*font-size: 14px;*/
      /*opacity: 1;*/
      /*line-height: 100%;*/
      margin: 0;
    }
  .el-carousel-item:nth-child(2n) {
       background-color: #fff;
    }
  .el-carousel-item:nth-child(2n+1) {
       background-color: #fff;
    }
  .rightImg {
    width: 100%;
    height: inherit;
  }

</style>

<template>
  <div class="background_picture font-center">
    <div>
      <div class="font-center">
        <h1>
          <span ><img src="./../assets/booknum/public-icon1.png"></span>
<!--          <span class="product-font">山西方言</span>-->
          <span class="product-font">方言</span>
          <span class="product-font">作品</span>
          <span ><img src="./../assets/booknum/public-icon2.png"></span>
        </h1>
      </div>
      <div class="font-center">
        <img src="./../assets/booknum/home_line.png">
        <div style="padding-bottom:40px">&nbsp;</div>
      </div>
      <div class="font-center">
          <span class="num-font">{{this.book_num}}&nbsp;</span>
          <span ><img src="./../assets/booknum/indexicon1.png" alt=""></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BookNum",
  data() {
      return {
        book_num:'',
      }
  },
  methods: {
    search_book_num() {
      const path = "/display/shanxi_book/search_book_num/"
      const param = new URLSearchParams()
      this.$http.post(path,param).then(res => {
        this.book_num = res.data
      })
    }
  },
  mounted() {
    this.search_book_num()
  }
}
</script>

<style scoped>
  .background_picture {
    background:url("./../assets/booknum/home_block2_box_bg1920.jpg");
    max-width: 400px;
    min-height: 416px;

  }
  .product-font {
    color: #ffffff;
  }
  .num-font {
    color: #ffffff;
    font-size: 35px;
  }
  .font-center {
      display: -moz-box;/*兼容Firefox*/
      display: -webkit-box;/*兼容FSafari、Chrome*/
      -moz-box-align: center;/*兼容Firefox*/
      -webkit-box-align: center;/*兼容FSafari、Chrome */
      -moz-box-pack: center;/*兼容Firefox*/
      -webkit-box-pack: center;/*兼容FSafari、Chrome */
  }

</style>

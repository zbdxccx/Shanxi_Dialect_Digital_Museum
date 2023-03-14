<template>
 <!-- Header Section End -->
<div>
  <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="section breadcrumb-section overlay back" data-bg-image="../assets/images/work/literature.jpg">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <!-- Breadcrumb wrapper Start -->
                    <div class="breadcrumb-wrapper">
                        <h1 class="title text-white" data-aos="fade-up" data-aos-duration="1100">山西方言•文学</h1>
                        <ul class="breadcrumb-menu" data-aos="fade-up" data-aos-duration="1500">
                            <li>
                                <span>literature</span>
                            </li>
                        </ul>
                    </div>
                    <!-- Breadcrumb wrapper End -->
                </div>
            </div>
        </div>
    </div>
    <!-- Breadcrumb Section End -->

    <!-- Portfolio Section Start -->
    <div class="section section-margin">
        <div class="container">
            <div class="row m-b-n50">
                <div class="col-lg-8 m-b-50" data-aos="fade-up" data-aos-duration="1100">
                    <div class="portfolio-details-image-wrapper m-b-n40">
                        <div class="portfolio-details-image m-b-40">
                             <img :src="book.img_path" width="500" class='img-circle img-shadow' :title="book.name" :alt="book.name"/>
<!--                            <img class="img-circle img-shadow" src="../assets/images/work/literature1_3.jpg" alt="Porfolio Image">-->
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 m-b-50" data-aos="fade-up" data-aos-duration="1500">
                    <div class="portfolio-content-wrapper">
                        <div class="section-title text-start p-b-20">
                            <h2 class="title">山西•文化作品</h2>
                            <span class="d-flex justify-content-start"></span>
                        </div>
                        <div class="portfolio-content">
                            <ul>
                                <li><span>书名:</span>{{book.name}} </li>
                                <li><span>作者:</span> {{book.author}} </li>
                                <li><span>出版社:</span>{{book.publisher}}</li>
                            </ul>
                        </div>

                    </div>
                </div>
            </div>
        </div>
      <Footer class="foot"></Footer>
    </div>
    <!-- Portfolio Section End -->

</div>
</template>

<script>
import Header from "../components/header";
import Footer from "../components/ShanxiFooter";



export default {
  name: "ShanxiLiterature",
  components: {
      Header,
      Footer,
  },
  data() {
    return {
      book: {}
    }
  },
  methods: {
    getBook () {
      let bookName = this.$route.query.bookName

      let url = '/display/shanxi_book/get_book_by_name/'
      let params = new URLSearchParams()
      params.append('bookname', bookName)
      this.$http.post(url, params).then(res => {
        console.log(res)
        this.book = res.data.data[0]
        let s= this.book.img_path
        let imgstr = this.book.img_path.substring(s.indexOf('images'))
        this.book.img_path = require('../assets/' + imgstr)
      })

    }
  },
  mounted() {
    this.getBook()
  }
}
</script>

<style scoped>
.foot{
  margin-top: 120px;
}
.head{
  position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 999;
}
.back{
  background-image: url("../assets/images/work/literature.jpg");

}
.overlay::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1;
    height: 650px;
    background: -webkit-gradient(linear, left top, right top, from(rgba(20,20,20,0.8)), color-stop(0%, rgba(20,20,20,0.8)));
    background: -webkit-linear-gradient(left, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);
    background: -o-linear-gradient(left, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);
    background: linear-gradient(to right, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);
}
.container {
    padding-right: var(--bs-gutter-x, 15px);
    padding-left: var(--bs-gutter-x, 15px);
    margin-right: auto;
    margin-left: auto;
    max-width: 1200px;
}
.row {
    --bs-gutter-x: 30px;
    --bs-gutter-y: 0;
    display: flex;
    flex-wrap: wrap;
    margin-top: calc(var(--bs-gutter-y) * -1);
    margin-right: calc(var(--bs-gutter-x)/ -2);
    margin-left: calc(var(--bs-gutter-x)/ -2);
}
.col-12 {
    flex: 0 0 auto;
    width: 100%;
}
.breadcrumb-wrapper {
    text-align: center;
    position: relative;
    z-index: 99;
    padding-top: 40px;
}

.breadcrumb-section {
    height: 650px;
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center;
}
.breadcrumb-wrapper .title {
    font-weight: 400;
    font-size: 56px;
    margin-bottom: 0;
}
.breadcrumb-wrapper .breadcrumb-menu {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    -webkit-align-items: center;
    -ms-flex-align: center;
    align-items: center;
    margin-top: 30px;
}
ul {
    margin: 0;
    padding: 0;
}
.text-white {
    color: #fff!important;
}
.breadcrumb-wrapper .breadcrumb-menu li span {
    color: #ffffff;
    font-size: 16px;
}
ul li {
    list-style: none;
}
.section-margin {
    margin-top: 120px;
    margin-bottom: 120px;
}
.section, .section-fluid {
    float: left;
    width: 100%;
}
.m-b-n50 {
    margin-bottom: -50px;
}
.m-b-40 {
    margin-bottom: 40px;
    text-align: left;
}
.row {
    --bs-gutter-x: 30px;
}
.row {
    --bs-gutter-x: 1.5rem;
    --bs-gutter-y: 0;
    display: flex;
    flex-wrap: wrap;
    margin-top: calc(var(--bs-gutter-y) * -1);
    margin-right: calc(var(--bs-gutter-x)/ -2);
    margin-left: calc(var(--bs-gutter-x)/ -2);
}
.m-b-50 {
    margin-bottom: 50px;
}
.col-lg-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
}
.m-b-n40 {
    margin-bottom: -40px;
}
.img-shadow {
    box-shadow: #959ea5 0px 0px 41px;
}
.img-circle {
    border-radius: 50px;
}
img {
    max-width: 100%;
  ertical-align: middle;
}
.portfolio-content-wrapper {
    position: -webkit-sticky;
    position: sticky;
    top: 100px;
    z-index: 1020;
}
.p-b-20 {
    padding-bottom: 20px;
}
.section-title {
    padding-bottom: 0px;
}
.text-start {
    text-align: left!important;
}
.section-title .title {
    margin-top: -5px;
}
h2 {
    font-size: 36px;
}
h1, h2, h3, h4, h5, h6 {
    font-family: "Vidaloka", serif;
    font-weight: 600;
    line-height: 1.2;
    color: #232324;
}
.section-title span {
    position: relative;
    margin-top: 20px;
    padding-bottom: 20px;
    display: block;
}
.justify-content-start {
    justify-content: flex-start!important;
}
.d-flex {
    display: flex!important;
}
ul {
    margin: 0;
    padding: 0;
}
.portfolio-content-wrapper .portfolio-content ul li {
    display: flex;
    color: #232324;
    font-size: 20px;
    margin-bottom: 10px;
}
.portfolio-content-wrapper .portfolio-content ul li span {
    font-weight: 500;
    margin-right: 10px;
}

</style>

<template>
  <div>
    <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="background_picture overlay">
      <div class="container" style="background:url(../assets/images/work/flower1.jpg);">
        <div class="row">
          <div class="col-12">

            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos-duration="1100">花糕</h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Flower Cake</span>
                </li>
              </ul>
            </div>
            <!-- Breadcrumb wrapper End -->

          </div>
        </div>
      </div>
    </div>


    <!-- Breadcrumb Section End -->

    <!-- About Section Start -->
    <div class="section section-margin ">
      <div class="container1 ">
        <div class="row m-b-n30 align-items-center">
          <div class="col-lg-6 m-b-30" data-aos="fade-up" data-aos-duration="1100">
            <div class="about-content mw-100">
              <h2 class="title">花糕</h2>
              <span></span>
              <p>菜品简介：用米粉或面粉掺和其他材料蒸制或烘烤而成的食品。以米粉、豆粉等为原料，发酵，更点缀以枣、栗、杏仁等果馕、加糖蒸制而成。</p>
              <p>菜品做法：先将红绿果脯切成丝，待用。将赤豆、白糖(250克)、豆油制成干豆沙，备用。将糯米粉、粳米粉掺和，取150克拌入红糖，加水50克左右，拌成糊状。将其余的粉拌上白糖(750克)，加水250克后，拌和拌透。取糕屉，铺上清洁湿布，放入1/2糕粉刮平，将豆沙均匀的撒在上面，再把剩下的1/2的糕粉铺在豆沙上面刮平，随即用旺火沸水蒸。待汽透出面粉时，把糊状粉浆均匀地铺在上面，洒上红、绿果脯丝，再继续蒸至糕熟，即可离火。</p>
              <p>菜品由来：时珍曰∶糕以黍、糯合粳米粉蒸成，状如凝膏也。单糯粉作者，曰粢。米粉合豆末、 糖、蜜蒸成者曰饵。《释名》云∶粢，慈软也。饵，而也，相粘而也。扬雄《方言》云∶ 饵谓之糕，或谓之粢。然亦微有分别，不可不知之也。</p>
            </div>
          </div>
          <div class="col-lg-6 order-first order-lg-last m-b-30" data-aos="fade-up" data-aos-duration="1500">
            <div class="about-image service-layer-image ms-auto">
              <img class="about-image-1" src="../assets/images/work/flower2.jpg" alt="About Image">
              <img class="about-image-2 img-circle" src="../assets/images/work/flower3.jpg" alt="About Image">
            </div>
          </div>
        </div>
      </div>
      <Footer class="foot"></Footer>
    </div>
    <!-- About Section End -->


  </div>


</template>

<script>

import Header from "../components/header";
import Footer from "../components/ShanxiFooter";

export default {
  name: "Food3",
  components: {
    Header,
    Footer,
  },
}
</script>


<style scoped>
.foot {
  margin-top: 220px;
}

.head {
  z-index: 99;
}

.background_picture {
  height: 618px;
  background: url(../assets/images/work/flower1.jpg);
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  overflow: hidden;
  /*background-image: linear-gradient(to right, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);*/
}

.text-white {
  color: #fff !important;
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

.container {
  padding-right: 15px;
  padding-left: 15px;
  margin-left: 109px;
  margin-right: 109px;
  margin-top: 200px;
}

.container1 {
  padding-right: 15px;
  padding-left: 15px;
  margin-left: 109px;
  margin-right: 109px;
  margin-top: 100px;
}

.overlay::before {
  content: '';
  position: absolute;
  top: 60px;
  right: 0;
  bottom: 170px;
  left: 0;
  z-index: 1;
  background: -webkit-gradient(linear, left top, right top, from(rgba(20, 20, 20, 0.8)), color-stop(0%, rgba(20, 20, 20, 0.8)));
  background: -webkit-linear-gradient(left, rgba(20, 20, 20, 0.8) 0%, rgba(20, 20, 20, 0.8) 0%);
  background: -o-linear-gradient(left, rgba(20, 20, 20, 0.8) 0%, rgba(20, 20, 20, 0.8) 0%);
  background: linear-gradient(to right, rgba(20, 20, 20, 0.8) 0%, rgba(20, 20, 20, 0.8) 0%);
}

.container {
  max-width: 1200px;
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
  margin-right: calc(var(--bs-gutter-x) / -2);
  margin-left: calc(var(--bs-gutter-x) / -2);
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

.about-content {
  text-align: left;
}

.about-content span {
  position: relative;
  margin-top: 20px;
  padding-bottom: 30px;
  display: block;
  text-align: left;
}

.about-content span:after {
  position: absolute;
  content: '';
  width: 60px;
  height: 1px;
  background: #a295df;
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
  list-style-type: disc;
}

ul li {
  list-style: none;
}

.breadcrumb-wrapper .breadcrumb-menu li span {
  color: #ffffff;
  font-size: 16px;
}

.section-margin {
  margin-top: 0px;
  margin-bottom: 0px;
}

.section, .section-fluid {
  float: left;
  width: 100%;
}


.m-b-n30 {
  margin-bottom: -30px;
}

.row {
  --bs-gutter-x: 30px;
}

.align-items-center {
  align-items: center !important;
}

.row {
  --bs-gutter-x: 1.5rem;
  --bs-gutter-y: 0;
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(var(--bs-gutter-y) * -1);
  margin-right: calc(var(--bs-gutter-x) / -2);
  margin-left: calc(var(--bs-gutter-x) / -2);
}

.aos-animate {
  opacity: 1;
  transform: translateZ(0);
}

.col-lg-6 {
  flex: 0 0 auto;
  width: 50%;

}

.mw-100 {
  max-width: 100% !important;
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


p {
  margin-top: 0;
  margin-bottom: 1rem;
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  color: #8a8a8a;
  line-height: 2;
  visibility: visible;
}

.service-layer-image {
  position: relative;
  height: 577px;
}

.about-image {
  max-width: 530px;
  margin-left: -100px;
}

.ms-auto {
  margin-left: 0px;
}

.service-layer-image .about-image-1 {
  -webkit-box-shadow: #959ea5 0px 0px 41px;
  box-shadow: #959ea5 0px 0px 41px;
  border-radius: 50px;
}

.service-layer-image .about-image-2 {
  position: absolute;
  right: 0px;
  top: 255px;
}

.img-circle {
  border-radius: 50px;
}

img {
  max-width: 100%;
}

img, svg {
  vertical-align: middle;
}


</style>

<template>
  <div>
    <Header class="head"></Header>
    <!-- Breadcrumb Section Start -->
    <div class="background_picture overlay">
      <div class="container" style="background:url(../assets/images/work/cake1.jpg);">
        <div class="row">
          <div class="col-12">

            <!-- Breadcrumb wrapper Start -->
            <div class="breadcrumb-wrapper">
              <h1 class="title text-white" data-aos-duration="1100">烙饼</h1>

              <ul class="breadcrumb-menu" data-aos-duration="1500">
                <li>
                  <span>Baked Pancake</span>
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
              <h2 class="title">烙饼</h2>
              <span></span>
              <p>菜品简介：烙饼是用面粉、鸡蛋等材料烙制而成并深受百姓喜爱的中国传统面食之一，可以配各种肉、蛋、蔬菜一起食用。主要营养成分是碳水化合物、蛋白质、脂肪等，营养充足而丰富。烙饼的营养素损失较少。</p>
              <p>
                菜品做法：将擀好的面上洒上一层盐(适量)，然后轻轻的擀几下。之后涂上薄薄一层油，之后将面从一册卷起来。卷好之后用擀面杖擀成一个大圆饼。厚度再4毫米左右。擀好之后将其放入已经烧热，并涂上一层油的平底锅中。OK，盖上锅盖，开始烙吧。锅不宜太热，太热了大饼会糊。1-2分钟之后掀开锅盖，看看朝下的那面是否已经处于半成熟状态。如果是，OK。将朝上的那面涂上一层油，然后再翻面。之后盖上锅盖，再等一两分钟，然后打开锅，再涂上一层油，再翻一次。然后盖上盖子，等大饼开始上酥，并因气体热胀冷缩到胀大面积膨胀的时候，，就可以出锅了。</p>
              <p>营养价值：每100克烙饼(标准粉)营养成分
                能量255千卡；蛋白质7.5克；脂肪2.3克；碳水化合物52.9克；膳食纤维1.9克；胆固醇257毫克；
                硫胺素0.02毫克；核黄素0.04毫克；维生素E1.03毫克；钙20毫克；磷146毫克；钾141毫克；
                钠149.3毫克；镁51毫克；铁2.4毫克；锌0.94毫克；硒7.5微克；铜0.15毫克；锰1.15毫克。。</p>
            </div>
          </div>
          <div class="col-lg-6 order-first order-lg-last m-b-30" data-aos="fade-up" data-aos-duration="1500">
            <div class="about-image service-layer-image ms-auto">
              <img class="about-image-1" src="../assets/images/work/cake2.jpg" alt="About Image">
              <img class="about-image-2 img-circle" src="../assets/images/work/cake3.jpg" alt="About Image">
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
  name: "MaterialFolk",
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
  background: url(../assets/images/work/cake1.jpg);
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

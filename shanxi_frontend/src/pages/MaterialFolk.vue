<template>
<div>
  <Header class="head"></Header>
   <!-- Breadcrumb Section Start -->
   <div class="background_picture overlay">
         <div class="container" style="background:url(../assets/images/work/mfolk1.jpg);">
            <div class="row">
                <div class="col-12">

                    <!-- Breadcrumb wrapper Start -->
                    <div class="breadcrumb-wrapper">
                        <h1 class="title text-white"  data-aos-duration="1100">物质民俗</h1>

                        <ul class="breadcrumb-menu"   data-aos-duration="1500">
                            <li>
                                <span>Material Folk</span>
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
    <div class="section section-margin">
        <div class="container1">
            <div class="row m-b-n30">
                <div class="col-lg-6 align-self-center m-b-30" data-aos="fade-up" data-aos-duration="1100">
                    <div class="about-content">
                        <h2 class="title m-b-40">物质民俗</h2>
                        <p>物质民俗，是指劳动人民在创造和消费物质财富的过程中不断重复的带有模式性的活动，以及由这种活动所产生的带有类型性的产品形式。它主要包括生产民俗、商贸民俗、饮食民俗、服饰民俗、交通民俗、医药民俗等等。山西民歌中反映的物质民俗主要是衣食住行等生活民俗。</p>
                        <p>衣的民俗：“白布衫衫白圪生白，高粱红裤子绿西瓜鞋。”“白布衫衫呀袖袖长，羊肚肚手巾呀遮荫凉。”“羊肚手巾呀歪罩转，又遮荫凉又好看。”</p>
                        <p>食的民俗：“半斤莜面推窝窝，挨打受气为哥哥。”“猪油软糕包白糖，不如娘家下糠窝窝香。”“沙梁沙洼好地脉，海红红是咱好土产。”“妹妹不想吃干凝凝粥，我给妹妹熬上那二不溜溜不稠不稀清个沾沾酸稀粥呀亲亲。”</p>
                        <p>山西的历史上，从清末民国初年直到解放初期，人们大多数以莜面、豆面、山药蛋为主食，而海红果则是当地有名的土特产。莜麦面有推窝窝、捻鱼、猫耳朵、卜烂子等多种做法，吃时往往调以酸菜汤、羊肉汤、盐水汤等，这是山西城乡百姓经常食用的家常饭。酸粥是山西民间普遍喜食的浆米饭。</p>
                        <p>住的民俗：“十八根白椽盖平房，不想我活下这下场。”“你走西口我上房，手板住烟囱泪汪汪。”“青石板沿台砖漫院，灰小子管我成一条线。”</p>
                        <p>山西人多住平顶房，房顶上可以晒粮食、乘凉，也常是人们远望的地方，在山西民歌的歌词里，常有描写妇女站在屋顶上远望情人的情节。</p>
                        <p>行的民俗：“不大大小青马喂上二升料，三天路程两天到。”“黑赤墨毛驴光脊梁，鞭子一甩急忙回。”“二套牛车你慢慢游，真魂魂跟在你车后头。”山西农村多为山区，旧时农民多以马、驴、牛车做为交通工具。至现代，则各种交通工具一应俱全。</p>

                    </div>
                </div>
                <div class="col-lg-6 order-first m-b-30" data-aos="fade-up" data-aos-duration="1500">
                    <div class="about-image me-auto">
                        <img class="img-circle img-shadow" src="../assets/images/work/mfolk2.jpg" alt="About Image">
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
.foot{
  margin-top: 150px;
}
.head{
  z-index: 99;
}

.background_picture{
  height: 618px;
  background:url(../assets/images/work/mfolk1.jpg) ;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  overflow: hidden;
  /*background-image: linear-gradient(to right, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);*/
}

.text-white {
    color: #fff!important;
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
    padding-right:  15px ;
    padding-left:   15px ;
    margin-left: 109px;
    margin-right: 109px;
    margin-top: 200px;
}

.container1 {
    padding-right:  15px ;
    padding-left:   15px ;
    margin-left: 109px;
    margin-right: 109px;
    margin-top: 150px;
}

.overlay::before {
    content: '';
    position: absolute;
    top: 60px;
    right: 0px;
    bottom: 170px;
    left: 0;
    z-index: 1;
    background: -webkit-gradient(linear, left top, right top, from(rgba(20,20,20,0.8)), color-stop(0%, rgba(20,20,20,0.8)));
    background: -webkit-linear-gradient(left, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);
    background: -o-linear-gradient(left, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);
    background: linear-gradient(to right, rgba(20,20,20,0.8) 0%, rgba(20,20,20,0.8) 0%);
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

.about-content{
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

.about-content {
    max-width: 495px;
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
    margin-bottom:  0px;
}

.section{
    float: left;
    width: 100%;
}


.m-b-n30 {
    margin-bottom: -30px;
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



.col-lg-6 {
    flex: 0 0 auto;
    width: 50%;

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


.m-b-40 {
    margin-bottom: 40px;
}

.about-image {
    max-width: 530px;
}
.me-auto {
    margin-right: auto!important;
}

.img-shadow {
    box-shadow: #959ea5 0px 0px 41px;
}



p{
      color: #8a8a8a;
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

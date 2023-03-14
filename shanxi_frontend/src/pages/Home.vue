<template>
  <!--    <div>-->

  <div style="background-image: url('./../static/HomeBackground.png')">
    <Header></Header>
    <Carousel></Carousel>
    <div>

      <p class="main-font1"><img src="./../assets/home/hometitle.png" width="600"></p>
      <p class="main-history">静心品酌，历史艺术之美沁人心脾。</p>
      <p class="main-history"> 文明的起源、三代的辉煌、五霸的雄奇，以及中外交流的史政、晋商崛起的奥秘......</p>
      <p class="main-history">画廊、典藏三代晋重宝的庄严府库。基本陈列以“晋魂”为主题，为您讲述人类的由来、</p>
      <p class="main-history">山西方言博物馆，向往知识者的温馨家园，陶冶人文素养的优雅殿堂，荟萃艺术珍品的美丽</p>
      <p class="main-history">山西方言数字博物馆是南开大学软件学院软件工程课程，山西方言小组的作业展示，与商业无关</p>

    </div>

    <Zuopintitle></Zuopintitle>
    <el-row>
      <el-col :span="2">&nbsp;</el-col>
      <el-col :span="20">
        <MainCard></MainCard>
      </el-col>
      <el-col :span="2">&nbsp;</el-col>
    </el-row>
    <Shubotitle></Shubotitle>
    <News></News>
    <Zhanshititle></Zhanshititle>
    <Dialect></Dialect>
    <Footer></Footer>
  </div>

</template>

<script>
import Header from "../components/header";
import Carousel from "../components/carousel";
import Footer from "../components/ShanxiFooter";
import MainCard from "../components/maincard";
import Dialect from "../components/Dialect";
import BookNum from "../components/BookNum";
import News from "../components/News";
import Zhanshititle from "../components/zhanshititle";
import Shubotitle from "../components/shubotitle";
import Zuopintitle from "../components/Zuopintitle";
import dialectmaincard from "../components/dialectmaincard";

export default {
  name: "Home",
  components: {
    BookNum,
    Header,
    Carousel,
    Footer,
    MainCard,
    Dialect,
    News,
    Zhanshititle,
    Shubotitle,
    Zuopintitle,
    dialectmaincard,
  }
}
</script>

<style scoped>
.main-font1 {
  font-size: 45px;
  margin-top: 50px;
  margin-bottom: 20px;
}

.main-font2 {
  font-size: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
}

.main-history {
  font-size: 20px;
  margin-top: -5px;
  font-family:  cursive;
}

.home-yellow-rectangle {
  width: 40px;
  height: 9px;
  background: #ffb400;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 30px;
}

.home-sub-title {
  padding-top: 35px;
  text-align: center;
}
</style>

<template>
  <!-- 饮食文化 -->
  <div class="block city-wrap ld_library">
    <div class="content city">
      <div class="card-list">
        <div class="card1 img-shadow1">
          <router-link to="/CulturalWork">
            <div class="img-wrap1">
              <img class="img1" src="../assets/home/xiaoerhei.jpg" />
            </div>
            <h3 class="g-ellipsis h3-1" @click="changePage(1)">小二黑结婚</h3>
            <p class="title g-ellipsis p2">作者：赵树理</p>
            <p class="p2">
              出版社: 文化发展出版社。
            </p>
          </router-link>
          <div class="item-list">
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">作品简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">作者简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">出版社简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">销售渠道</router-link>
          </div>
        </div>
        <div class="card1 img-shadow1">
          <router-link to="/CulturalWork">
            <div class="img-wrap1">
              <img class="img1" src="../assets/home/qingfengsantan.jpg" />
            </div>
            <h3 class="g-ellipsis h3-1">清风三叹</h3>
            <p class="title g-ellipsis p2">作者: 曹乃谦</p>
            <p class="p2">
              出版社: 人民文学出版社
            </p>
          </router-link>
          <div class="item-list">
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">作品简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">作者简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">出版社简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">销售渠道</router-link>
          </div>
        </div>
        <div class="card1 img-shadow1">
          <router-link to="/CulturalWork">
            <div class="img-wrap1">
              <img class="img1" src="../assets/home/lvliang.jpg" />
            </div>
            <h3 class="g-ellipsis h3-1">吕梁英雄传</h3>
            <p class="title g-ellipsis p2">作者: 马烽</p>
            <p class="p2">
              出版社: 人民文学出版社
            </p>
          </router-link>
          <div class="item-list">
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">作品简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">作者简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">出版社简介</router-link>
            <router-link to="/ShanxiLiterature" class="item g-ellipsis a1">销售渠道</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "dialectmaincard"
}
</script>

<style scoped>
@import url("https://img.dpm.org.cn/Public/static/themes/css/page.css?v=415121113");
@import url("https://img.dpm.org.cn/Public/static/themes/css/global.css?v=415121113");

/* 图文巨幕 */

.pic {
  left: 0;
  bottom: 0;
  opacity: 1;
}

.bigp {
  height: 688px;
}

.head1 {
  padding-top: 90px;
  font-size: 36px;
}

.p1-pic {
  margin-top: 20px;
  color: #4f4f4f;
}

.p2-pic {
  margin-bottom: 55px;
}

.mar-pic {
  margin-left: 100px;
}

.back {
  text-align: left;
  background-image: url(../assets/images/work/big_picture2.png);
}

.line {
  width: 700px;
  color: #474747;
}

/*山西民俗*/
h2 {
  font-size: 36px;
  font-weight: 600;
  color: #343434;
}

h3 {
  font-size: 14px;
  font-weight: 300;
  color: #8e8d8d;
  margin: 10px;
  line-height: 2;
}

.img-wrap {
  height: 423px;
}

.main {
  color: #330;
  /*background: #f7f6f8;*/
  min-width: 1200px;
  position: relative;
}
.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

.img-shadow1 {
  box-shadow: #959ea5 0px 0px 20px;
}

.pic {
  padding-top: 70px;
}

.sub-title {
  text-align: center;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

.news img {
  width: 751px;
  height: 423px;
  position: absolute;
  top: 0;
  left: 0;
}

.news .list {
  position: absolute;
  top: 0;
  right: 0;
  width: 449px;
}

.news .list a {
  position: relative;
  display: block;
  height: 141px;
  font-size: 14px;
  line-height: 21px;
  color: #8e8d8d;
  padding: 27px;
  box-sizing: border-box;
  transition: 0.3s;
  text-decoration: none;
}

.news {
  height: 628px;
}

.content {
  width: 1200px;
  position: relative;
  margin: 0 auto;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

a {
  text-decoration: none;
}

.news .list {
  position: absolute;
  top: 0;
  right: 0;
  width: 449px;
}

.news .list .title {
  font-size: 24px;
  font-weight: 400;
  color: #343434;
  line-height: 30px;
  margin-bottom: 14px;
  margin-top: 0;
}

.g-ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.p1 {
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}

.list a:hover p {
  color: cornflowerblue;
}

.city-hr {
  margin: 0;
}

body,
td,
th {
  font: 14px -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Ubuntu,
  Helvetica Neue, Helvetica, Arial, PingFang SC, Hiragino Sans GB,
  Microsoft YaHei UI, Microsoft YaHei, Source Han Sans CN, sans-serif;
}

h3,
li,
ol,
p,
ul {
  list-style: none;
}

h1,
h2,
h3,
h4,
h5,
h6,
p,
ul {
  margin: 0;
  padding: 0;
}

.yellow-rectangle {
  width: 40px;
  height: 9px;
  background: #ffb400;
  border-radius: 4px;
  display: inline-block;
  margin-bottom: 30px;
}

.news .card-wrap {
  position: relative;
  background: #fff;
  box-shadow: 0 3px 20px 0 rgba(0, 0, 0, 0.1);
}

/*文学作品*/
.inp {
  margin-top: 10px;
}

.adjust {
  height: 343px !important;
}

.ld_library_3 {
  height: 940px;
  padding-top: 60px;
  position: relative;
  z-index: 10;
}

/* 特色美食 */
.city {
  height: 400px;
}

.content {
  width: 1200px;
  position: relative;
  margin: 0 auto;
}

.city .sub-title {
  padding-top: 50px;
  margin-bottom: 20px;
}

.sub-title[data-v-6f74154e] {
  text-align: center;
}

.city .card-list {
  margin-left: -380px;
}

.card1 {
  width: 256px;
  height: 416px;
  background: #fff;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.05);
  display: inline-block;
  margin-left: 30px;
  margin-bottom: 35px;
  vertical-align: top;
  font-size: 14px;
  color: #8e8d8d;
  line-height: 21px;
  position: relative;
}

.img-wrap1 {
  width: 266px;
  height: 180px;
  margin-top: 15px;
  overflow: hidden;
}

.img1 {
  width: 150px;
  height: 265px;
  vertical-align: middle;
  border: 0px;
}

.p2 {
  color: #8e8d8d;
  margin: 0 23px 7px;
}

.item-list {
  margin-left: -10px;
  position: absolute;
  bottom: 9px;
  width: 270px;
}

.item {
  width: 93px;
  line-height: 29px;
  padding: 0 5px;
  text-align: center;
  border-radius: 15px;
  color: #8e8d8d;
  display: inline-block;
  border: 1px solid #8e8d8d;
  margin-left: 16px;
  margin-bottom: 11px;
}

.h3-1 {
  font-size: 24px;
  line-height: 25px;
  font-weight: 300;
  margin: 21px 23px 7px;
  color: #000;
}

.item:hover {
  width: 95px;
  line-height: 31px;
  background: #ffb400;
  color: #fff;
  border: none;
  text-decoration: none;
}

.card1 a:hover {
  color: gray;
}

.card1 a:hover h3 {
  color: #00cb86;
}

/*5张图*/
.introduction {
  width: 100%;
  padding-top: 80px;
  padding-bottom: 100px;
}

.introduction_main {
  width: 1000px;
  margin: 0px auto 0px;
}
.introduction_tit {
  margin-top: 10px;
  margin-bottom: 10px;
  line-height: 20px;
}

.introduction_i {
  display: block;
  width: 30px;
  height: 3px;
  background-color: blue;
  margin-top: 15px;
  margin-bottom: 10px;
}

.introduction_ul {
  width: 1000px;
  overflow: hidden;
  padding-left: 0;
  margin-top: 0;
  margin-bottom: 0;
}

.introduction_ul li {
  list-style: none;
  width: 230px;
  float: left;
  margin-right: 26px;
}

.introduction_div {
  width: 230px;
  height: 165px;
  border: 1px solid gray;
}

.introduction_picture {
  width: 220px;
  height: 155px;
  padding-left: 1px;
  padding-right: 1px;
  padding-top: 4px;
  padding-bottom: 2px;
  vertical-align: top;
}

.introduction_text {
  width: 230px;
  margin-top: 10px;
}

.introduction_ul .introduction_li {
  list-style: none;
  width: 230px;
  float: left;
  margin-right: 0px;
}

/*<roll>*/

.roll_img {
  width: 158px;
  height: 120px;
  padding-left: 0px;
  padding-right: 0px;
  padding-top: 0px;
  padding-bottom: 0px;
  vertical-align: top;
}

.roll_pic1 {
  margin: 0px 5px 0 0;
  flex-shrink: 0;
}

.wrag {
  position: absolute;
  margin: 0 auto;

  left: auto;
  right: auto;
  width: 1000px;
  height: 150px;
  white-space: nowrap;
  overflow-x: scroll;
  overflow-y: hidden;
}

.roll {
  display: flex;
}

.roll_div {
  width: 100%;
}

.rollmain_div {
  width: 1000px;
  margin: 60px auto 230px;
}

.roll_tit {
  margin-bottom: 15px;
}

.roll_pic {
  margin: 0px 5px;
  flex-shrink: 0;
}
</style>


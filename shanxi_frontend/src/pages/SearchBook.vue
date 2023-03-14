<template>
  <div>
    <Header class="head"></Header>
    <div class="page-visit readlist">
      <div class="wrap">

        <div class="title">
          <h2>
                  <span class="tit-span">
                    <img src="../assets/images/work/public-icon3.png">
                  </span>
            <span>方言文学</span>
            <span class="tit-span">
                    <img src="../assets/images/work/public-icon4.png">
                  </span>
          </h2>
          <div class="t_head">
            <div class="border1"></div>
            <div class="icon1"></div>
            <div class="border2"></div>
            <div class="box">
              <div class="text" style="height: auto;">
                <div class="th" deep="7">
                  <p>　　
                    当代山西小说农村题材居多，以民俗生活为叙事背景，大量运用方言俗语，营造出浓厚的乡土氛围，反映了文化个体与民俗文化传统的爱恨情仇。
                    爱，民俗文化的地域情感，谁不说俺家乡好；恨，民俗对文化个体人性的束缚：情，民俗个体的任何情感，产生于特定的民俗生活，借用民俗范式传情达意；仇，文化个体之间的矛盾，在民俗生活中产生、发展。
                  </p>
                  <p>　　
                    打开赵树理、马烽、西戎、胡正等作家的作品，浓郁的乡土气息扑面而来。这些“山药蛋派”作品深受广大读者的喜爱，并在当代中国文坛上产生过较大的影响。
                  </p>
                  <p>　　
                    为了表达的需要，“山药蛋派”作品常常恰当而贴切地运用一些山西方言词语。这些方言词语，对人物的刻画起着重要的作用。有些方言词语反映了农村的风俗民情。有些方言俗语反映了当地的饮食习俗。在反映农村题材的作品中适当地加入一些方言，无疑可以增强作品的乡土气和表现力，但是，读者是否能够读懂这些方言所表达的意思，是对作家实力的检验。
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="page-visit readlist" id="page-visit">
      <div class="wrap">
        <div class="title">
          <h2>
                  <span class="tit-span">
                    <img src="../assets/images/work/public-icon3.png">
                  </span>
            <span>出版物</span>
            <span class="tit-span">
                    <img src="../assets/images/work/public-icon4.png">
                  </span>
          </h2>
        </div>
        <div id="ajax-list">
          <div class="filter t_searchbar" style="margin-top:35px;">


          </div>
          <!--<div class="list clearfix">-->
          <!--  <div class="item" :class="i%3==0 ? 'first':''"  v-for="(item, i) in bookList" :key="i">-->
          <!--        <a target="_blank" href="/journal_detail/258084.html">-->
          <!--                <div class="box1">-->
          <!--                    <div class="img">-->
          <!--                      <img :src="item.img_path" height="139" :title="item.name" :alt="item.name" />-->

          <!--                    </div>-->
          <!--                    <div class="text">-->
          <!--                        <h2>{{item.name}}</h2>-->
          <!--                        <p>{{item.author}}</p>-->
          <!--                        <p>{{item.publisher}}</p>-->
          <!--                        &lt;!&ndash; <p>出版时间：2022-09-16</p> &ndash;&gt;-->
          <!--                        <p>&nbsp;</p>-->
          <!--                    </div>-->
          <!--                </div>-->
          <!--            </a>-->
          <!--        </div>-->
          <!--</div>-->
          <div class="list clearfix">
            <div v-if="bookList.length==0">
              暂无数据
            </div>
            <div v-else>
              <div class="item" :class="i%3==0 ? 'first':''" v-for="(item, i) in bookList" :key="i">
                <router-link :to="{path: 'SingleBook', query:{bookName: item.name}}">
                  <div class="box1">
                    <div class="img">
                      <img :src="item.img_path" height="139" :title="item.name" :alt="item.name"/>

                    </div>
                    <div class="text">
                      <h2>{{ item.name }}</h2>
                      <p>{{ item.author }}</p>
                      <p>{{ item.publisher }}</p>
                    </div>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
          <!--<div class="list clearfix">-->
          <!--  <div class="item" :class="i%3==0 ? 'first':''" v-for="(item, i) in exampleList" :key="i">-->
          <!--        <a target="_blank" href="/journal_detail/258084.html">-->
          <!--                <div class="box1">-->
          <!--                    <div class="img">-->
          <!--                      <img :src="item.img_path + `book${i}.jpg`" height="139" :title="item.name" :alt="item.name" />-->
          <!--                    </div>-->
          <!--                    <div class="text">-->
          <!--                        <h2>{{item.name}}</h2>-->
          <!--                        <p>{{item.author}}}</p>-->
          <!--                        <p>{{item.publisher}}</p>-->
          <!--                        &lt;!&ndash; <p>出版时间：2022-09-16</p> &ndash;&gt;-->
          <!--                        <p>&nbsp;</p>-->
          <!--                    </div>-->
          <!--                </div>-->
          <!--            </a>-->
          <!--        </div>-->
          <!--</div>-->
          <!--<div class="list clearfix">-->
          <!--  <div class="item" :class="i%3==0 ? 'first':''" v-for="(item, i) in exampleList" :key="i">-->
          <!--        <a target="_blank" href="/journal_detail/258084.html">-->
          <!--                <div class="box1">-->
          <!--                    <div class="img">-->
          <!--                      <img :src="item.img_path + `book${i}.jpg`" height="139" :title="item.name" :alt="item.name" />-->
          <!--                    </div>-->
          <!--                    <div class="text">-->
          <!--                        <h2>{{item.name}}</h2>-->
          <!--                        <p>{{item.author}}}</p>-->
          <!--                        <p>{{item.publisher}}</p>-->
          <!--                        &lt;!&ndash; <p>出版时间：2022-09-16</p> &ndash;&gt;-->
          <!--                        <p>&nbsp;</p>-->
          <!--                    </div>-->
          <!--                </div>-->
          <!--            </a>-->
          <!--        </div>-->
          <!--</div>-->
          <div class="public-icon-list">
            <div class="wrap">
              <div class="item">
                <a href="/librarys.html">
                  <img src="https://img.dpm.org.cn/Uploads/Picture/2017/03/06/s58bd6098f18ff.png" title="图书馆" alt="图书馆">
                </a>

              </div>
              <div class="item">
                <a href="/auditions.html">
                  <img src="https://img.dpm.org.cn/Uploads/Picture/2017/03/06/s58bd6098f1b06.png" title="视听馆" alt="视听馆">
                </a>

              </div>
              <div class="item">
                <a
                  href="https://palacemuseum.tmall.com/shop/view_shop.htm?spm=a220m.1000862.1000730.2.IS2lQC&amp;user_number_id=2893966855&amp;rn=68d7e1a1bf5ba21acef0322cb010ecf7"
                  target="_blank">
                  <img src="https://img.dpm.org.cn/Uploads/Picture/2017/03/06/s58bd6098f16fd.png" title="故宫旗舰店"
                       alt="故宫旗舰店">
                </a>

              </div>
              <div class="item">
                <a id="bdclick_btn9" href="http://webapp.vizen.cn/gugong_app_pc/index.html" target="_blank">
                  <img src="https://img.dpm.org.cn/Uploads/Picture/2017/03/06/s58bd6098f14ef.png" title="全景故宫"
                       alt="全景故宫">
                </a>
              </div>
              <div class="item">
                <a id="bdclick_btn10" href="http://v.dpm.org.cn" target="_blank">
                  <img src="https://img.dpm.org.cn/Uploads/Picture/2017/03/06/s58bd6098f127e.png" title="v故宫" alt="v故宫">
                </a>

              </div>
            </div>

          </div>
          <!--  <div class="pages">-->


          <!--                    <a class="now" href="javascript:void(0);">1</a>-->
          <!--                        <a href="/publishes/p/2.html">2</a>-->
          <!--                        <a href="/publishes/p/3.html">3</a>-->
          <!--                        <a href="/publishes/p/4.html">4</a>-->
          <!--                        <a href="/publishes/p/5.html">5</a>-->

          <!--        <a href="/publishes/p/11.html">...</a>        -->
          <!--        <a href="/publishes/p/160.html" class="dian">160</a>-->
          <!--        <a class="next" id="next" href="/publishes/p/2.html" ></a>-->

          <!--    </div>-->
        </div>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>

import Header from "../components/header";
import Footer from "../components/ShanxiFooter";

export default {
  name: "SearchBook",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      bookList: [],
      exampleList: [
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
        {name: '', author: '', publisher: '', img_path: '../assets/images/work/'},
      ]
    }

  },
  methods: {
    searchBook() {
      let title_search = this.$route.query.title_search
      let author_search = this.$route.query.author_search
      let publisher_search = this.$route.query.publisher_search

      let url = '/display/shanxi_book/search_book/'
      let params = new URLSearchParams()
      params.append('bookname', title_search)
      params.append('author', author_search)
      params.append('publisher', publisher_search)
      this.$http.post(url, params).then(res => {
        this.bookList = res.data.data
        for (let i = 0; i < this.bookList.length; i++) {
          let s = this.bookList[i].img_path
          let imgstr = this.bookList[i].img_path.substring(s.indexOf('images'))
          this.bookList[i].img_path = require('../assets/' + imgstr)
        }
      })
    }
  },

  mounted() {
    this.searchBook()
  }
}


</script>

<style scoped>

@import url("https://img.dpm.org.cn/Public/static/themes/css/page.css?v=415121113");
@import url('https://img.dpm.org.cn/Public/static/themes/css/global.css?v=415121113');

.page-visit .title h2 {
  margin-top: 75px;
}

.readlist .wrap {
  margin-bottom: 30px;
}

.wrap {
  width: 1258px;
  height: 100%;
  margin: 0 auto;
  position: relative;
}

.page-visit .title {
  text-align: center;
}

page-visit .title h2 {
  margin-bottom: 20px;
  font-size: 26px;
  color: #474747;
}

.t_searchbar {
  *zoom: 1;
  text-align: center;
}

.t_searchbar .border-wrap {
  font-size: 0;
  margin-left: 38px;
  vertical-align: middle;
  display: inline-block;
}

.t_searchbar .border-wrap {
  font-size: 0;
  margin-left: 0px;
}

.border-wrap {
  height: 40px;
  line-height: 40px;
  padding: 0 16px;
  position: relative;
  display: inline-block;
  background: url(../assets/images/work/border.png) repeat-x;
}

.border-wrap {
  height: 40px;
  line-height: 40px;
  padding: 0 9px;
  position: relative;
  display: inline-block;
}

.border-wrap:before {
  background: url(../assets/images/work/border_side.png) left center no-repeat;
  width: 6px;
  height: 100%;
  content: "";
  position: absolute;
  left: 0;
  top: 0;
}

.page-visit .t_searchbar .selectWarp {
  width: 230px;
}

.t_searchbar .selectWarp {
  display: inline-block;
  width: 212px;
  border: 0;
  vertical-align: top;
}

.t_searchbar .selectWarp {
  display: inline-block;
  width: 140px;
  border: 0;
  vertical-align: top;
}

.selectWarp {
  text-align: left;
  cursor: pointer;
  position: relative;
  border: 1px solid #a9a9a9;
}

.t_searchbar .selectWarp .selectBtn {
  font-size: 14px;
  height: 40px;
  line-height: 40px;
}

.selectWarp .selectBtn {
  position: relative;
  overflow: hidden;
  height: 26px;
  padding: 0 26px 0 12px;
  line-height: 26px;
  color: #474747;
}

.selectWarp {
  text-align: left;
  cursor: pointer;
  position: relative;
  border: 1px solid #a9a9a9;
}

.t_searchbar .selectWarp .selectBtn .arr {
  right: 0;
}

.selectWarp .selectBtn .arr {
  position: absolute;
  right: 10px;
  top: 0;
  width: 12px;
  height: 100%;
  background: url(../assets/images/work/select_arrow.png) left no-repeat;
}

.t_searchbar .selectWarp .options {
  left: 0;
  right: 0;
  top: 100%;
  border-top: 0;
  border-color: #e6e6e6;
}

.selectWarp .options {
  max-height: 128px;
  overflow: hidden;
  padding: 12px 2px 12px 12px;
  background-color: #fff;
  border: 1px solid #a9a9a9;
  position: absolute;
  left: -1px;
  right: -1px;
  top: 26px;
  z-index: 10;
  display: none;
}

.mCustomScrollBox {
  position: relative;
  overflow: hidden;
  height: 100%;
  max-width: 100%;
  outline: none;
  direction: ltr;
}

.selectWarp .mCSB_inside > .mCSB_container {
  margin: 0;
}

.mCSB_container {
  overflow: hidden;
  width: auto;
  height: auto;
}

.selectWarp ul {
  padding-right: 20px;
}

ol, ul, li {
  list-style: none;
  padding: 0;
  margin: 0;
}

.t_searchbar .selectWarp ul li {
  font-size: 14px;
  line-height: 1.5;
}

.selectWarp ul li {
  margin-bottom: 5px;
}

.filter .input {
  height: 40px;
  line-height: 40px;
  padding: 0 20px;
  width: 120px;
  position: relative;
  background: url(../assets/images/work/input.png) center center no-repeat;
  float: left;
  margin-left: 80px;
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
}

.filter .input:before {
  background: url(../assets/images/work/input.png) left center no-repeat;
  width: 6px;
  height: 100%;
  content: "";
  position: absolute;
  left: -6px;
  top: 0;
}

.filter .input label {
  float: left;
  -webkit-box-flex: 0;
  -moz-flex-shrink: 0;
  -webkit-flex-shrink: 0;
  flex-shrink: 0;
}

.filter.t_searchbar .input input {
  width: calc(100% - 75px);
}

.page-visit .filter .input input {
  width: 198px;
}

.filter .input input {
  height: 40px;
  width: 75px;
}

input, button, textarea, select {
  font: 14px/100% "Microsoft YaHei", Arial, Tahoma, Helvetica, sans-serif;
  outline: 0;
  border: 0;
  background: none;
  color: #707070;
}

.filter .input:after {
  background: url(../assets/images/work/input.png) right center no-repeat;
  width: 6px;
  height: 100%;
  content: "";
  position: absolute;
  right: -6px;
  top: 0;
}

.page-visit .t_searchbar .button.btn1 {
  width: 222px;
}

.t_searchbar .button {
  display: inline-block;
  margin-left: 78px;
}

.filter .button input {
  width: 100%;
  height: 100%;
  cursor: pointer;
  color: #474747;
}

.btn1 {
  cursor: pointer;
  min-width: 80px;
  text-align: center;
  height: 37px;
  line-height: 37px;
  padding: 0 20px;
  position: relative;
  display: inline-block;
  background: url(../assets/images/work/btn1.png) center center no-repeat;
  color: #474747;
}

.page-visit .list {
  margin-top: 38px;
  margin-bottom: 39px;
}

.page-visit .list .item.first {
  margin-left: 0;
}

.page-visit .list .item {
  background: url(../assets/images/work/visit-img2.jpg) no-repeat;
  width: 406px;
  height: 205px;
  float: left;
  margin-bottom: 20px;
  margin-left: 20px;
}

.page-visit .list .item .box1 {
  padding: 25px 30px;
  display: block;
}

.page-visit .list .item .img {
  float: left;
  width: 140px;
  text-align: center;
  margin-right: 10px;
}

img {
  border: 0;
  outline: 0;
  vertical-align: middle;
  max-width: 100%;
  max-height: 100%;
}

.page-visit .list .item .text {
  margin-left: 120px;
}

.page-visit .list .item h2 {
  font-size: 16px;
  color: #474747;
  margin-bottom: 5px;
  text-align: center;
}

.page-visit .list .item p {
  font-size: 14px;
  color: #474747;
  line-height: 24px;
}

.pages {
  padding: 35px 0;
  text-align: center;
}

.pages a.now {
  background: #987444;
  border-radius: 50%;
  padding: 5px;
  color: #fff;
}

.pages a {
  display: inline-block;
  min-width: 30px;
  min-height: 30px;
  line-height: 30px;
  margin: 0 5px;
  font-size: 18px;
  font-family: Arial;
  vertical-align: middle;
}

/*5张图*/
.public-icon-list {
  background: url(../assets/images/work/line1.png) no-repeat center top;
  padding-top: 80px;
  padding-bottom: 10px;
}

.wrap {
  width: 1258px;
  height: 100%;
  margin: 0 auto;
  position: relative;
}

.public-icon-list .item {
  text-align: center;
  display: inline-block;
  width: 104px;
  margin: 0 32px;
  padding: 0px;
}

.public-icon-list .item a {
  display: block;
  width: 104px;
  height: 101px;
  overflow: hidden;

}

.public-icon-list .item h2 {
  font-size: 16px;
  margin-top: 10px;
}

h1, h2, h3, h4, h5, h6 {
  font-weight: normal;
  color: #474747;
  line-height: 1.2;
}

a {
  text-decoration: none !important;
  color: inherit;
}
</style>

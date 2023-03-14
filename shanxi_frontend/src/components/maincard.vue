<template>
  <div>
    <el-row :gutter="50">
      <!--    <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">-->
      <el-col :span="2">
        <div class="grid-content bg-color-left"></div>
      </el-col>
      <el-col :span="20">
        <el-col :span="7">
          <BookNum></BookNum>
        </el-col>

<!--        <el-col :span="8">-->
<!--          <el-card :body-style="{ padding: '20px' }" shadow="hover">-->
<!--            <img src="./../assets/home/xiaoerhei.jpg" class="image">-->
<!--            <div style="padding: 0px;">-->
<!--              <span>小二黑结婚</span>-->
<!--              <p class="card-intro">作者: 赵树理</p>-->
<!--              <p class="card-intro">出版社: 文化发展出版社</p>-->
<!--              &lt;!&ndash;              <div class="bottom clearfix">&ndash;&gt;-->
<!--              &lt;!&ndash;                <a href="./../pages/ShanxiLiterature.vue" type="text" class="button">了解更多</a>&ndash;&gt;-->
<!--              &lt;!&ndash;              </div>&ndash;&gt;-->
<!--            </div>-->
<!--          </el-card>-->

<!--          <el-card :body-style="{ padding: '20px' }" shadow="hover">-->
<!--            <img src="./../assets/images/work/book9.jpg" class="image">-->
<!--            <div style="padding: 0px;">-->
<!--              <span>方言作品2</span>-->
<!--              <p class="card-intro">关于作品2的介绍</p>-->
<!--              <div class="bottom clearfix">-->
<!--                <a href="./../pages/ShanxiLiterature.vue" type="text" class="button">了解更多</a>-->
<!--              </div>-->
<!--            </div>-->
<!--          </el-card>-->
<!--        </el-col>-->

<!--        <el-col :span="8">-->
<!--          <el-card :body-style="{ padding: '20px' }" shadow="hover">-->
<!--            <img src="./../assets/images/work/book9.jpg" class="image">-->
<!--            <div style="padding: 0px;">-->
<!--              <span>方言作品1</span>-->
<!--              <p class="card-intro">关于作品1的介绍</p>-->
<!--              <div class="bottom clearfix">-->
<!--                <a href="./../pages/ShanxiLiterature.vue" type="text" class="button">了解更多</a>-->
<!--              </div>-->
<!--            </div>-->
<!--          </el-card>-->

<!--          <el-card :body-style="{ padding: '20px' }" shadow="hover">-->
<!--            <img src="./../assets/images/work/book9.jpg" class="image">-->
<!--            <div style="padding: 0px;">-->
<!--              <span>方言作品2</span>-->
<!--              <p class="card-intro">关于作品2的介绍</p>-->
<!--              <div class="bottom clearfix">-->
<!--                <a href="./../pages/ShanxiLiterature.vue" type="text" class="button">了解更多</a>-->
<!--              </div>-->
<!--            </div>-->
<!--          </el-card>-->
<!--        </el-col>-->

        <el-col :span="17">
          <dialectmaincard>
          </dialectmaincard>
        </el-col>

      </el-col>
      <el-col :span="2">
        <div class="grid-content bg-color-right"></div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import BookNum from "./BookNum";
import dialectmaincard from "./dialectmaincard";

export default {
  name: "MainCard",
  components: {
    BookNum,
    dialectmaincard
  },
  data() {
    return {
      currentDate: new Date()
    };
  }
}
</script>

<style scoped>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  max-height: 180px;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}

.bg-color-left,
.bg-color-right {
  /*background: #ffffff;*/
}

.grid-content {
  min-height: 36px;
}

.bg-color-left,
.bg-color-right {
  /*background: #ffffff;*/
}

.card-intro {
  margin-top: 10px;
  margin-bottom: 5px;
}
</style>

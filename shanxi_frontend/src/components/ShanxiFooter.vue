<template>
  <div>
    <el-row :gutter="0" class="grid-content bg-purple">
      <el-col :span="8"><div class="grid-content"></div></el-col>
      <el-col :span="2">
        <i class=""><img src="./../assets/footer/weibo.png" alt="" class="img-icon"><p class="font-icon">微博</p></i>
      </el-col>
      <el-col :span="2">
        <i class=""><img src="./../assets/footer/wechat.png" alt="" class="img-icon"><p class="font-icon">微信</p></i>
      </el-col>
      <el-col :span="2">
        <i class=""><img src="./../assets/footer/shipinghao.png" alt="" class="img-icon"><p class="font-icon">视频号</p></i>
      </el-col>
      <el-col :span="2">
        <i class=""><img src="./../assets/footer/douying.png" alt="" class="img-icon"><p class="font-icon">抖音</p></i>
      </el-col>
      <el-col :span="8"><div class="grid-content"></div></el-col>
    </el-row>

    <el-row :gutter="0">
      <el-col :span="4"><div class="grid-content bg-color-left"></div></el-col>
      <el-col :span="16">
        <div class="grid-content bg-purple">
          <el-col :span="6"><div class="grid-content"></div></el-col>
          <el-col :span="3"><div class="grid-content size-font-information">版本声明</div></el-col>
          <el-col :span="3"><div class="grid-content size-font-information">留言板</div></el-col>
          <el-col :span="3"><div class="grid-content size-font-information">联系我们</div></el-col>
          <el-col :span="3"><div class="grid-content size-font-information">关于</div></el-col>
          <el-col :span="6"><div class="grid-content"></div></el-col>
        </div>
      </el-col>
      <el-col :span="4"><div class="grid-content bg-color-right"></div></el-col>
    </el-row>
    <el-row :gutter="0">
      <el-col :span="7"><div class="grid-content bg-color-left"></div></el-col>
      <el-col :span="10">
        <div class="grid-content bg-purple">
          <el-col :span="12"><div class="grid-content size-font-information">网站维护: NKU软件工程小组</div></el-col>
          <el-col :span="12"><div class="grid-content size-font-information">联系方式: 2012286@mail.nankai.edu.cn</div></el-col>
        </div>
      </el-col>
      <el-col :span="7"><div class="grid-content bg-color-right"></div></el-col>
    </el-row>
    <el-row :gutter="0">
      <el-col :span="4"><div class="grid-content bg-color-left"></div></el-col>
      <el-col :span="16">
        <div class="grid-content bg-purple">
          Copyright©2022 NKU软件工程山西方言小组·中国方言数字博物馆 All Rights Reserved 津ICP备2022007843号-1 津公安网备
        </div>
      </el-col>
      <el-col :span="4"><div class="grid-content bg-color-right"></div></el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style scoped>

  .el-row {
    margin-bottom: 0px;
    color: #eae8e8;
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-color-left, .bg-color-right, .bg-purple{
    background: #272727;
  }
  .grid-content {
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #272727;
  }
  .font-icon{
    margin-top: -15px;
    font-size: 15px;
    margin-bottom: 15px;
  }
  .size-font-information {
    font-size: 15px;
  }
  .img-icon {
    margin-top: -15px;
    max-height: 100px;
  }


</style>

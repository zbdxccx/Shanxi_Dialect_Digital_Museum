<template>
  <div>
    <el-row type="flex" class="row-bg" justify="space-between">
      <el-col :span="12">
        <div class="grid-content row-size row-left">
          <img src="./../assets/logo.png" alt="" />
        </div>
      </el-col>
      <el-col :span="12">
        <div class="grid-content row-right">
          <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
            background-color="#272727"
            text-color="#fff"
            active-text-color="#ff9300"
          >
            <el-menu-item index="1">首页</el-menu-item>
            <el-submenu index="2" @click.native="changePage(1)">
              <template slot="title" ref="style2">方言作品</template>
              <el-menu-item index="2-0" v-show="false">简介</el-menu-item>
              <el-submenu index="2-1" @click.native="changePage(2)">
                <template slot="title">山西民俗</template>
                <el-menu-item index="2-1-0" v-show="false"
                  >山西民俗</el-menu-item
                >
                <el-menu-item index="2-1-1">物质民俗</el-menu-item>
                <el-menu-item index="2-1-2">精神民俗</el-menu-item>
                <el-menu-item index="2-1-3">语言民俗</el-menu-item>
              </el-submenu>
              <el-menu-item index="2-2">文学作品</el-menu-item>
              <el-submenu index="2-3" @click.native="changePage(3)">
                <template slot="title">饮食文化</template>
                <el-menu-item index="2-3-0" v-show="false"
                  >山西饮食</el-menu-item
                >
                <el-menu-item index="2-3-1">刀削面</el-menu-item>
                <el-menu-item index="2-3-2">烙饼</el-menu-item>
                <el-menu-item index="2-3-3">花糕</el-menu-item>
                <el-menu-item index="2-3-4">蒸饺</el-menu-item>
              </el-submenu>
              <el-submenu index="2-4" @click.native="changePage(4)">
                <template slot="title">山西戏曲</template>
                <el-menu-item index="2-4-0" v-show="false"
                  >山西戏曲</el-menu-item
                >
                <el-menu-item index="2-4-1">晋南戏曲</el-menu-item>
                <el-menu-item index="2-4-2">山西秧歌</el-menu-item>
                <el-menu-item index="2-4-3">道情戏</el-menu-item>
                <el-menu-item index="2-4-4">晋北戏曲</el-menu-item>
              </el-submenu>
            </el-submenu>
            <el-menu-item index="3">方言历史</el-menu-item>
            <el-menu-item index="4">方言展示</el-menu-item>
            <el-menu-item index="5">文创作品</el-menu-item>
            <el-menu-item index="6">联系我们</el-menu-item>
            <a-modal v-model="visible" title="联系我们" @ok="handleOk">
              <a-table
                :columns="columns"
                :data-source="data"
                :pagination="false"
              >
                <a slot="name" slot-scope="text">{{ text }}</a>
                <template slot="title" slot-scope="currentPageData">
                  软件工程小组
                </template>
              </a-table>
              <p class="project">
                <a
                  href="https://git.code.tencent.com/Dream-Acc/Shanxi_Dialect_Digital_Museum"
                  >点击查看项目地址</a
                >
              </p>
            </a-modal>
          </el-menu>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "NavMenu",
  data() {
    return {
      activeIndex: "1",
      visible: false,
      columns: [
        {
          title: "姓名",
          dataIndex: "name",
          key: "name",
          scopedSlots: { customRender: "name" },
        },
        {
          title: "学号",
          dataIndex: "age",
          key: "age",
        },
        {
          title: "邮箱",
          dataIndex: "address",
          key: "address",
          ellipsis: false,
        },
      ],
      data: [
        {
          key: "1",
          name: "李彦昊",
          age: 2012286,
          address: "1310724226@qq.com",
        },
        {
          key: "2",
          name: "陈子昂",
          age: 2012217,
          address: "1812432358@qq.com",
        },
        {
          key: "3",
          name: "陈世祺",
          age: 2012661,
          address: "2902529887@qq.com",
        },
        {
          key: "4",
          name: "龙肖明",
          age: 2010318,
          address: "1781092881@qq.com",
        },
        {
          key: "5",
          name: "谢宇杭",
          age: 2013282,
          address: "2896450802@qq.com",
        },
      ],
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      switch (key) {
        case "1":
          this.$router.push("/home");
          break;
        case "2-0":
          this.$router.push("/CulturalWork");
          break;
        case "2-1-0":
          this.$router.push("/ShanxiFolk");
          break;
        case "2-1-1":
          this.$router.push("/MaterialFolk");
          break;
        case "2-1-2":
          this.$router.push("/SpiritualFolk");
          break;
        case "2-1-3":
          this.$router.push("/DialectFolk");
          break;
        case "2-2":
          this.$router.push("/ShanxiLiterature");
          break;
        case "2-3-0":
          this.$router.push("/ShanxiFood");
          break;
        case "2-3-1":
          this.$router.push("/Food1");
          break;
        case "2-3-2":
          this.$router.push("/Food2");
          break;
        case "2-3-3":
          this.$router.push("/Food3");
          break;
        case "2-3-4":
          this.$router.push("/Food4");
          break;
        case "2-4-0":
          this.$router.push("/ShanxiOpera");
          break;
        case "2-4-1":
          this.$router.push("/Opera1");
          break;
        case "2-4-2":
          this.$router.push("/Opera2");
          break;
        case "2-4-3":
          this.$router.push("/Opera3");
          break;
        case "2-4-4":
          this.$router.push("/Opera4");
          break;
        case "3":
          this.$router.push("/history");
          break;
        case "4":
          this.$router.push("/DialectDisplay");
          break;
        case "5":
          this.$router.push("/product");
          break;
        case "6":
          this.visible = true;
          break;
        default:
          this.$router.push("/home");
      }
      console.log(key);
    },
    handleOk() {
      this.visible = false;
    },
    changePage(index) {
      switch (index) {
        case 1:
          this.$router.push("/CulturalWork");
          break;
        case 2:
          this.$router.push("/ShanxiFolk");
          break;
        case 3:
          this.$router.push("/ShanxiFood");
          break;
        case 4:
          this.$router.push("/ShanxiOpera");
          break;
      }
    },
  },
  watch: {
    $route: function (to, from) {
      switch (to.path) {
        case "/home":
          this.activeIndex = "1";
          break;
        case "/CulturalWork":
          this.activeIndex = "2-0";
          break;
        case "/ShanxiFolk":
          this.activeIndex = "2-1-0";
          break;
        case "/MaterialFolk":
          this.activeIndex = "2-1-1";
          break;
        case "/SpiritualFolk":
          this.activeIndex = "2-1-2";
          break;
        case "/DialectFolk":
          this.activeIndex = "2-1-3";
          break;
        case "/ShanxiLiterature":
          this.activeIndex = "2-2";
          break;
        case "/ShanxiFood":
          this.activeIndex = "2-3-0";
          break;
        case "/Food1":
          this.activeIndex = "2-3-1";
          break;
        case "/Food2":
          this.activeIndex = "2-3-2";
          break;
        case "/Food3":
          this.activeIndex = "2-3-3";
          break;
        case "/Food4":
          this.activeIndex = "2-3-4";
          break;
        case "/ShanxiOpera":
          this.activeIndex = "2-4-0";
          break;
        case "/Opera1":
          this.activeIndex = "2-4-1";
          break;
        case "/Opera2":
          this.activeIndex = "2-4-2";
          break;
        case "/Opera3":
          this.activeIndex = "2-4-3";
          break;
        case "/Opera4":
          this.activeIndex = "2-4-4";
          break;
        case "/history":
          this.activeIndex = "3";
          break;
        case "/DialectDisplay":
          this.activeIndex = "4";
          break;
        case "/product":
          this.activeIndex = "5";
          break;
        default:
          this.activeIndex = "1";
      }
    },
  },
  created() {
    switch (this.$route.path) {
      case "/home":
        this.activeIndex = "1";
        break;
      case "/CulturalWork":
        this.activeIndex = "2-0";
        break;
      case "/ShanxiFolk":
        this.activeIndex = "2-1-0";
        break;
      case "/MaterialFolk":
        this.activeIndex = "2-1-1";
        break;
      case "/SpiritualFolk":
        this.activeIndex = "2-1-2";
        break;
      case "/DialectFolk":
        this.activeIndex = "2-1-3";
        break;
      case "/ShanxiLiterature":
        this.activeIndex = "2-2";
        break;
      case "/ShanxiFood":
        this.activeIndex = "2-3-0";
        break;
      case "/Food1":
        this.activeIndex = "2-3-1";
        break;
      case "/Food2":
        this.activeIndex = "2-3-2";
        break;
      case "/Food3":
        this.activeIndex = "2-3-3";
        break;
      case "/Food4":
        this.activeIndex = "2-3-4";
        break;
      case "/ShanxiOpera":
        this.activeIndex = "2-4-0";
        break;
      case "/Opera1":
        this.activeIndex = "2-4-1";
        break;
      case "/Opera2":
        this.activeIndex = "2-4-2";
        break;
      case "/Opera3":
        this.activeIndex = "2-4-3";
        break;
      case "/Opera4":
        this.activeIndex = "2-4-4";
        break;
      case "/history":
        this.activeIndex = "3";
        break;
      case "/DialectDisplay":
        this.activeIndex = "4";
        break;
      case "/product":
        this.activeIndex = "5";
        break;
      default:
        this.activeIndex = "1";
    }
  },
};
</script>

<style scoped>
/*.el-row {*/
/*  margin-bottom: 0;*/
/*}*/
.grid-content {
  min-height: 100%;
}

.row-bg {
  background-color: #272727;
}

.row-left {
  float: left;
}

.row-right {
  float: right;
}

.row-size {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 30px;
  max-width: 100%;
  max-height: 100%;
}

a {
  text-decoration: none;
  outline: none;
  /*color:rgba(171, 117, 42, 0.6)*/
}

.project {
  float: right;
  margin-right: 20px;
}

.ant-pagination-item-active {
  border-color: #272727 !important;
}

.ant-pagination-item-active a {
  color: #272727 !important;
}

.ant-pagination-item-active:focus,
.ant-pagination-item-active:hover {
  border-color: #272727 !important;
}

.ant-btn-primary {
  background-color: #272727 !important;
  border-color: #272727 !important;
}

.el-menu.el-menu--horizontal {
  border-bottom: 0;
}
</style>
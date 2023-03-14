<template>
  <div>
    <div v-if="currentClassification" style="text-align: left">
      <div class="back">
        <i
          class="el-icon-arrow-left btn"
          style="color: #0a0a0a; font-size: 25px"
          @click="handleBack"
        >
          返回
        </i>
      </div>
      <div style="font-size: 30px; font-weight: bold; margin: 20px">
        分区名: {{ currentClassification.name }}
      </div>
      <div style="font-size: 20px; margin: 15px">
        描述:
        {{
          currentClassification.description
            ? currentClassification.description
            : "暂无内容"
        }}
      </div>
      <div style="font-size: 17px; margin: 15px" class="btn" @click="handleShowDialectOfClassification">
        查看该分区下的方言
      </div>
    </div>
    <div>
      <div style="width: 400px; margin: 20px auto">
        <el-input
          v-model="searchText"
          placeholder="请输入检索内容"
          @keyup.enter.native="getClaasifications"
        >
          <el-button
            slot="append"
            icon="el-icon-search"
            @click="getClaasifications"
          ></el-button>
        </el-input>
      </div>
      <div class="pagination" style="margin-top: 10px">
        <div class="item-tag" v-for="item in classifications" :key="item.name" @click="handleClickTag(item)">
          {{ item.name }}
        </div>
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="pagination.page"
          :page-sizes="[10, 20, 30, 40]"
          :page-size="pagination.pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="pagination.total"
        >
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentClassification: null,
      classifications: [],
      pagination: {
        page: 1,
        pageSize: 10,
        total: 0,
      },
      searchText: "",
    };
  },

  methods: {
    getClaasifications() {
      const params = new URLSearchParams();
      params.append("page", this.pagination.page);
      params.append("page_size", this.pagination.pageSize);
      params.append("search_content", this.searchText);
      this.$http
        .post(
          "/display/dialect_display/get_classification_search_result/",
          params
        )
        .then((res) => {
          this.classifications = res.data.data;
          this.pagination.total = res.data.length;
        });
    },

    getClaasificationByName(name) {
      const params = new URLSearchParams();
      params.append("name", name);
      this.$http
        .post("/display/dialect_display/get_classification_by_name/", params)
        .then((res) => {
          if (res.data && res.data !== "None") {
            this.currentClassification = res.data;
          }
        });
    },

    handleClickTag(item) {
      this.currentClassification = item;
      console.log(item);
    },

    handleBack() {
      this.currentClassification = null;
    },

    handleShowDialectOfClassification() {
      this.$router.push({
        path: "/DialectDisplay",
        query: {
          classification: this.currentClassification.name,
        },
      });
    },

    handleSizeChange(val) {
      this.pagination.pageSize = val;
      this.getClaasifications();
    },

    handleCurrentChange(val) {
      this.pagination.page = val;
      this.getClaasifications();
    },
  },

  mounted() {
    if (this.$route.query.classification) {
      this.getClaasificationByName(this.$route.query.classification);
    }
    this.getClaasifications();
  },
};
</script>

<style scoped>
.btn {
  cursor: pointer;
}
.btn:hover {
  color: #409eff !important;
}
.item-tag {
  margin: 10px;
  background-color: #fff;
  display: inline-block;
  border-radius: 10px;
  padding: 7px;
  box-shadow: 0 0 5px #f78b06;
  font-size: 15px;
  font-weight: bold;
  cursor: pointer;
  vertical-align: top;
}
.item-tag:hover {
  background-color: #f4bf80;
  color: #fff;
}
</style>
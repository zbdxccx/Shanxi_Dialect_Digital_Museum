<template>
  <div
    v-loading="loading.loading"
    :element-loading-text="loading.text"
    :element-loading-background="loading.background"
  >
    <div class="dialect-single" v-if="currentDialect">
      <div class="back">
        <i
          class="el-icon-arrow-left btn"
          style="color: #0a0a0a; font-size: 25px"
          @click="handleBack"
        >
          返回
        </i>
      </div>
      <div style="padding: 20px; padding-left: 40px">
        <div style="font-size: 30px; font-weight: bold">
          {{ currentDialect.name }}
        </div>
        <div style="font-size: 20px">含义: {{ currentDialect.meaning }}</div>
        <div style="font-size: 20px">
          分区:
          <span
            class="btn"
            style="color: #ca9116"
            @click="handleGoToClassification(currentDialect.classification)"
            >{{ currentDialect.classification }}</span
          >
        </div>
        <div style="font-size: 20px">
          备注: {{ currentDialect.remark ? currentDialect.remark : "暂无备注" }}
        </div>
        <div style="font-size: 25px">
          <audio :src="currentDialect.audioPath" v-show="false"></audio>
          <i class="el-icon-video-play btn"></i>
          <!-- 收藏 -->
          <i
            class="el-icon-star-off btn"
            v-if="!currentDialect.isFavoured"
            @click="handleFavour"
          ></i>
          <i class="el-icon-star-on btn" v-else @click="handleFavour"></i>
        </div>
        <div style="height: 20px"></div>
        <div style="font-size: 30px; font-weight: bold">评论</div>
        <div>暂无评论</div>
      </div>
    </div>
    <div class="dialect-main" v-else>
      <div class="search-box">
        <el-tabs v-model="tabs1">
          <el-tab-pane label="全检索">
            <div style="width: 600px; margin: 20px auto">
              <el-input
                v-model="searchText"
                placeholder="请输入检索内容"
                @keyup.enter.native="getTableData"
              >
                <el-button
                  slot="append"
                  icon="el-icon-search"
                  @click="getTableData"
                ></el-button>
              </el-input>
            </div>
          </el-tab-pane>
          <el-tab-pane label="高级检索">
            <el-form
              :inline="true"
              :model="searchForm"
              class="demo-form-inline"
              style="text-align: left"
            >
              <el-form-item label="读音">
                <el-input
                  v-model="searchForm.name"
                  placeholder="请输入方言名称"
                  @keyup.enter.native="getTableData"
                ></el-input>
              </el-form-item>
              <el-form-item label="含义">
                <el-input
                  v-model="searchForm.meaning"
                  placeholder="请输入方言含义"
                  @keyup.enter.native="getTableData"
                ></el-input>
              </el-form-item>
              <el-form-item label="分区">
                <el-input
                  v-model="searchForm.classification"
                  placeholder="请输入方言分区"
                  @keyup.enter.native="getTableData"
                ></el-input>
              </el-form-item>
              <el-form-item>
                <el-button
                  style="background: #f79216; border: none"
                  type="primary"
                  @click="getTableData"
                  >搜索</el-button
                >
              </el-form-item>
            </el-form>
          </el-tab-pane>
        </el-tabs>
      </div>
      <div style="height: 20px"></div>
      <el-tabs v-model="tabs2">
        <el-tab-pane label="卡片展示">
          <div
            class="card-list"
            v-loading="tableLoading.loading"
            :element-loading-text="tableLoading.text"
            :element-loading-background="tableLoading.background"
          >
            <div v-if="tableData.length == 0" style="height: 150px"></div>
            <div class="card-box" v-for="item in tableData" :key="item.id">
              <dialect-card
                :data="item"
                @click-card="handleClickCard"
                :highlight-word="highlightWord"
              ></dialect-card>
            </div>
          </div>
        </el-tab-pane>
        <el-tab-pane label="列表展示">
          <el-table
            :data="tableData"
            :header-cell-style="{ background: 'rgb(223, 217, 198)' }"
            cell-class-name="table-cell"
            v-loading="tableLoading.loading"
            :element-loading-text="tableLoading.text"
            @row-click="handleClickCard"
            :element-loading-background="tableLoading.background"
          >
            <el-table-column label="序号" type="index"></el-table-column>
            <el-table-column label="读音" prop="name"></el-table-column>
            <el-table-column label="含义" prop="meaning"></el-table-column>
            <el-table-column
              label="分区"
              prop="classification"
            ></el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <span class="table-btn">播放</span>
                <span class="table-btn">收藏</span>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>
      <div class="pagination" style="margin-top: 10px">
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
import DialectCard from "@/components/DialectAudioCard";
export default {
  components: {
    DialectCard,
  },

  data() {
    return {
      tabs1: "0",
      tabs2: "0",
      tableData: [],
      searchText: "",
      searchForm: {
        name: "",
        meaning: "",
        classification: "",
      },
      currentDialect: null,
      loading: {
        loading: false,
        text: "加载中",
        background: "rgb(239, 218, 195)",
      },
      tableLoading: {
        loading: false,
        text: "加载中",
        background: "rgb(239, 218, 195)",
      },
      pagination: {
        page: 1,
        pageSize: 10,
        total: 0,
      },
      highlightWord: "",
    };
  },

  methods: {
    searchFullText() {},
    advancedSearch() {},
    getDialectById() {
      if (!this.$route.query.dialectId) {
        return;
      }
      this.loading.loading = true;
      const params = new URLSearchParams();
      params.append("id", parseInt(this.$route.query.dialectId));
      this.$http
        .post("/display/dialect_display/get_dialect_by_id/", params)
        .then((res) => {
          if (res.data && res.data !== "None") {
            this.currentDialect = res.data;
          }
        })
        .finally(() => {
          this.loading.loading = false;
        });
    },
    getSearchResult() {
      this.tableLoading.loading = true;
      const params = new URLSearchParams();
      params.append("page", this.pagination.page);
      params.append("page_size", this.pagination.pageSize);
      params.append("search_content", this.searchText);
      this.$http
        .post("/display/dialect_display/get_dialect_search_result/", params)
        .then((res) => {
          this.tableData = res.data.data;
          this.pagination.total = res.data.length;
        })
        .finally(() => {
          this.tableLoading.loading = false;
        });
    },
    getAdvancedSearchResult() {
      this.tableLoading.loading = true;
      const params = new URLSearchParams();
      params.append("page", this.pagination.page);
      params.append("page_size", this.pagination.pageSize);
      params.append("name", this.searchForm.name);
      params.append("meaning", this.searchForm.meaning);
      params.append("classification", this.searchForm.classification);
      this.$http
        .post(
          "/display/dialect_display/get_dialect_advanced_search_result/",
          params
        )
        .then((res) => {
          this.tableData = res.data.data;
          this.pagination.total = res.data.length;
        })
        .finally(() => {
          this.tableLoading.loading = false;
        });
    },
    getTableData() {
      if (this.tabs1 === "0") {
        this.highlightWord = this.searchText;
        this.getSearchResult();
      } else {
        this.highlightWord = "";
        this.getAdvancedSearchResult();
      }
    },
    handleFavour() {},
    handleBack() {
      this.currentDialect = null;
    },
    handleClickCard(data) {
      console.log(data);
      this.currentDialect = data;
    },
    handleGoToClassification(name) {
      this.$router.push({
        path: "/DialectClassification",
        query: {
          classification: name,
        },
      });
    },
    handleSizeChange(val) {
      this.pagination.pageSize = val;
      this.getTableData();
    },
    handleCurrentChange(val) {
      this.pagination.page = val;
      this.getTableData();
    },
  },

  mounted() {
    if (this.$route.query.dialectId) {
      this.getDialectById();
    } else if (this.$route.query.classification) {
      this.searchForm.classification = this.$route.query.classification;
      this.tabs1 = "1";
    }
    this.getTableData();
  },
};
</script>

<style scoped>
.search-box {
  height: 150px;
}
.card-list {
  width: 650px;
  text-align: left;
}
.card-box {
  width: 300px;
  display: inline-block;
  vertical-align: top;
  margin: 5px 10px;
}
.dialect-single {
  text-align: left;
}
.btn {
  cursor: pointer;
}
.btn:hover {
  color: #409eff !important;
}
.table-btn {
  cursor: pointer;
  margin-right: 10px;
  color: #855605;
}
.table-btn:hover {
  color: #f00;
}
.el-table {
  animation: fadeIn 1s;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
    top: -100px;
  }
  100% {
    opacity: 1;
    top: 0;
  }
}
.el-table,
.el-table__expanded-cell {
  background-color: transparent;
}
.el-table/deep/.el-table__header-wrapper,
.el-table/deep/.el-table__header {
  background-color: transparent;
}
.el-table__expanded-cell:hover {
  background-color: #fff;
}
.el-table /deep/ .table-cell {
  background: rgb(237, 231, 215);
  cursor: pointer;
}
.dialect-main .el-tabs /deep/ .el-tabs__active-bar {
  background-color: #f79216;
}
.dialect-main .el-tabs /deep/ .el-tabs__item {
  margin: 0;
}
.dialect-main .el-tabs /deep/ .el-tabs__item:hover {
  color: #d48906;
}
.dialect-main .el-tabs /deep/ .el-tabs__item.is-active {
  color: #f78b06;
  background-color: transparent;
}
.dialect-main .el-tabs /deep/ .el-tabs__nav-wrap:after {
  background-color: #fae0b4;
}
</style>
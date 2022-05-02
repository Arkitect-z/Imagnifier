<template>
  <div class="p-20">
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="hover" class="image"> Always </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="image"> Hover </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="image"> Never </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<style scoped>
.image {
  width: 100%;
  display: block;
}
</style>
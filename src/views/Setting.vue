<template>
  <div class="p-20">
    <h2>模型库</h2>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="hover" class="model"> Always </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="model"> Hover </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="hover" class="model"> Never </el-card>
      </el-col>
    </el-row>
  </div>
</template>
<style scoped>
.dark * {
  color: #ffffff;
}
h2 {
  display: flex;
  align-items: center;
  position: relative;
  margin-top: 2.25rem;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  line-height: 1.25;
  font-size: 1.65rem;
}
p {
  display: flex;
  align-items: center;
  position: relative;
}
.model {
  width: 100%;
  display: block;
}
.dark .model {
  background-color: #4b5563;
}
</style>
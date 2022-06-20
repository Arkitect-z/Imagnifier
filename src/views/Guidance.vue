<template>
  <div class="img">
    <div class="container">
      <div class="header">
        <div class="jotform-icon"></div>
      </div>
      <div class="start">
        <h1 class="title2 dark:text-white">动漫图片智能放大App</h1>
        <h3 class="introduce dark:text-white">
          基于 Vue + Element Plus + PyQt + Flask
          <br />
          构建的桌面端应用。
        </h3>
      </div>
    </div>
  </div>
  <div class="page2">
    <div class="container" id="started">
      <h2 class="title3 dark:text-white">主要功能</h2>
      <div class="icon-list">
        <div class="three-icon">
          <svg
            class="icon1-img ml-24"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              d="M512 58.816v21.287c0 12.639-10.288 22.939-22.939 22.939h-3.108v257.801c0 12.639-10.3 22.939-22.939 22.939H267.47v33.663l84.989 62.337c5.115 3.751 6.217 10.93 2.466 16.034a11.455 11.455 0 0 1-9.256 4.691c-2.351 0-4.725-.723-6.767-2.225L267.47 445.89v43.148c0 6.331-5.138 11.47-11.47 11.47-6.331 0-11.47-5.138-11.47-11.47V445.89l-71.432 52.393c-5.104 3.739-12.284 2.638-16.023-2.466-3.751-5.104-2.649-12.284 2.466-16.034l84.989-62.337v-33.663H48.986c-12.639 0-22.939-10.3-22.939-22.939V103.042h-3.108C10.288 103.042 0 92.743 0 80.103V58.816c0-12.651 10.288-22.939 22.939-22.939H244.53V22.962c0-6.331 5.138-11.47 11.47-11.47 6.331 0 11.47 5.138 11.47 11.47v12.915h221.591c12.651 0 22.939 10.288 22.939 22.939zm-22.939 21.287V58.816H22.939v21.287h466.122zm-26.047 280.74V103.042H48.986v257.801h414.028z"
              fill="#201C1C"
            ></path>
            <path
              fill="#EF8E23"
              d="M22.939 58.816h466.122v21.287H22.939z"
            ></path>
            <path
              d="M463.014 103.042v257.801H48.986V103.042h414.028zM355.59 236.054c0-55.031-44.777-99.808-99.808-99.808-5.7 0-10.323 4.622-10.323 10.323v79.163h-79.163c-5.7 0-10.323 4.622-10.323 10.323 0 55.031 44.777 99.808 99.808 99.808s99.809-44.778 99.809-99.809zm-124.422-34.936v-65.227c0-5.7-4.622-10.323-10.323-10.323-41.657 0-75.538 33.892-75.538 75.55 0 5.7 4.622 10.323 10.323 10.323h65.216c5.7 0 10.322-4.622 10.322-10.323z"
              fill="#fff"
            ></path>
            <path
              d="M255.782 136.247c55.031 0 99.808 44.777 99.808 99.808s-44.777 99.808-99.808 99.808-99.808-44.777-99.808-99.808c0-5.7 4.622-10.323 10.323-10.323h79.163v-79.163c0-5.7 4.622-10.322 10.322-10.322zm79.163 99.807c0-40.155-30.05-73.417-68.84-78.486v78.486c0 5.7-4.622 10.323-10.323 10.323h-78.486c5.07 38.79 38.331 68.84 78.486 68.84 43.653 0 79.163-35.509 79.163-79.163z"
              fill="#201C1C"
            ></path>
            <path
              d="M266.105 157.568c38.79 5.07 68.84 38.331 68.84 78.486 0 43.653-35.51 79.163-79.163 79.163-40.155 0-73.417-30.05-78.486-68.84h78.486c5.7 0 10.323-4.622 10.323-10.323v-78.486z"
              fill="#CDCDCD"
            ></path>
            <path
              d="M231.168 135.891v65.227c0 5.7-4.622 10.323-10.323 10.323H155.63c-5.7 0-10.323-4.622-10.323-10.323 0-41.657 33.881-75.55 75.538-75.55 5.701 0 10.323 4.623 10.323 10.323zm-20.645 54.905v-43.607c-22.01 4.209-39.398 21.597-43.596 43.607h43.596z"
              fill="#201C1C"
            ></path>
            <path
              d="M210.523 147.189v43.607h-43.596c4.198-22.01 21.586-39.398 43.596-43.607z"
              fill="#FFFFFF"
            ></path>
          </svg>

          <div class="icon-title dark:text-white">图片放大对比</div>
          <div class="icon-description dark:text-white">
            可以实时查看图片放大的结果，对比放大效果
          </div>
        </div>
        <div class="three-icon">
          <svg
            svg
            class="icon1-img ml-24"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              fill="#201C1C"
              d="M512 264.941v155.401c0 19.161-15.589 34.749-34.749 34.749H34.749C15.589 455.091 0 439.503 0 420.342V264.941c0-6.582 1.841-12.733 5.027-17.981l-.154-.077L79.277 99.772c6.008-11.884 18.025-19.271 31.343-19.271h14.144v-13.67c0-5.49 4.432-9.922 9.922-9.922h242.627c5.49 0 9.922 4.432 9.922 9.922v13.67h14.144c13.318 0 25.334 7.386 31.343 19.271l74.404 147.111-.154.077c3.187 5.248 5.028 11.399 5.028 17.981zm-22.049 155.401V264.941c0-7.001-5.7-12.7-12.7-12.7H360.347c-.331 0-.628.187-.761.496l-14.299 31.706c-3.693 8.191-11.884 13.483-20.858 13.483H187.571c-8.974 0-17.165-5.292-20.858-13.483l-14.299-31.706c-.132-.309-.43-.496-.761-.496H34.749c-7.001 0-12.7 5.7-12.7 12.7v155.401c0 7.012 5.7 12.7 12.7 12.7h442.502c7 0 12.7-5.688 12.7-12.7zm-15.975-190.15l-60.921-120.465c-2.238-4.432-6.714-7.177-11.675-7.177h-14.144v17.507h13.196c5.479 0 9.922 4.432 9.922 9.922v53.226h12.27c5.49 0 9.922 4.443 9.922 9.922v37.064l41.43.001zm-61.274 0V203.05H99.298v27.142h52.355c8.985 0 17.176 5.292 20.858 13.483l14.299 31.706c.132.298.441.496.761.496h136.858c.32 0 .628-.198.761-.496l14.299-31.706c3.682-8.191 11.873-13.483 20.858-13.483h52.355zm-22.192-46.987v-43.304H121.49v43.304h269.02zm-23.118-63.148V76.753H144.608v43.304h222.784zm-242.628 0V102.55H110.62c-4.961 0-9.437 2.745-11.675 7.177L38.024 230.192h41.43v-37.064c0-5.479 4.432-9.922 9.922-9.922h12.27V129.98c0-5.49 4.443-9.922 9.922-9.922h13.196z"
            ></path>
            <path
              fill="#FFFFFF"
              d="M489.951 264.941v155.401c0 7.012-5.7 12.7-12.7 12.7H34.749c-7.001 0-12.7-5.689-12.7-12.7V264.941c0-7.001 5.7-12.7 12.7-12.7h116.904c.331 0 .628.187.761.496l14.299 31.706c3.693 8.191 11.884 13.483 20.858 13.483h136.858c8.974 0 17.165-5.292 20.858-13.483l14.299-31.706c.132-.309.43-.496.761-.496h116.904c7 0 12.7 5.699 12.7 12.7zm-162.06 117.863v-34.639c0-8.511-6.923-15.434-15.434-15.434H199.544c-8.511 0-15.434 6.923-15.434 15.434v34.639c0 8.511 6.923 15.434 15.434 15.434h112.913c8.51 0 15.434-6.923 15.434-15.434z"
            ></path>
            <path
              fill="#EF8E23"
              d="M413.055 109.727l60.921 120.465h-41.43v-37.064c0-5.479-4.432-9.922-9.922-9.922h-12.27V129.98c0-5.49-4.443-9.922-9.922-9.922h-13.196V102.55h14.144c4.961 0 9.437 2.745 11.675 7.177z"
            ></path>
            <path
              fill="#fff"
              d="M412.702 203.049v27.142h-52.355c-8.985 0-17.176 5.292-20.858 13.483L325.19 275.38c-.132.298-.441.496-.761.496H187.571c-.32 0-.628-.198-.761-.496l-14.299-31.706c-3.682-8.191-11.873-13.483-20.858-13.483H99.298v-27.142h313.404zM121.49 139.901h269.02v43.304H121.49zM144.608 76.753h222.783v43.304H144.608z"
            ></path>
            <path
              fill="#201C1C"
              d="M327.891 348.165v34.639c0 8.511-6.923 15.434-15.434 15.434H199.544c-8.511 0-15.434-6.923-15.434-15.434v-34.639c0-8.511 6.923-15.434 15.434-15.434h112.913c8.51 0 15.434 6.923 15.434 15.434zm-19.844 30.229v-25.819H203.953v25.819h104.094z"
            ></path>
            <path
              fill="#EF8E23"
              d="M203.953 352.575h104.093v25.819H203.953zM124.764 102.55v17.507h-13.196c-5.479 0-9.922 4.432-9.922 9.922v53.226h-12.27c-5.49 0-9.922 4.443-9.922 9.922v37.064h-41.43l60.921-120.465c2.238-4.432 6.714-7.177 11.675-7.177h14.144z"
            ></path>
          </svg>
          <h3 class="icon-title dark:text-white">图片选择与存储</h3>
          <div class="icon-description dark:text-white">自由选择图片与保存图片</div>
        </div>
        <div class="three-icon">
          <svg
            class="icon1-img ml-24"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              fill="#fff"
              d="M304.35 165.234c11.087 0 20.117 9.03 20.117 20.129 0 11.087-9.03 20.117-20.117 20.117-11.098 0-20.129-9.03-20.129-20.117 0-11.099 9.03-20.129 20.129-20.129z"
            ></path>
            <path
              fill="#201C1C"
              d="M512 67.461v377.078c0 12.466-10.138 22.604-22.604 22.604H22.604C10.138 467.143 0 457.005 0 444.539V67.461c0-12.466 10.138-22.604 22.604-22.604h466.792c12.466 0 22.604 10.138 22.604 22.604zm-22.604 377.078V67.461H22.604V444.55l466.792-.011z"
            ></path>
            <path
              fill="#fff"
              d="M489.396 67.461v377.078l-466.792.011V67.461h466.792zm-31.125 292.223V109.877c0-6.239-5.052-11.302-11.302-11.302H65.031c-6.25 0-11.302 5.063-11.302 11.302v249.807c0 6.239 5.052 11.302 11.302 11.302h381.937c6.251 0 11.303-5.063 11.303-11.302zm-206.283 48.078c0-6.25-5.052-11.302-11.302-11.302h-25.78c-6.239 0-11.302 5.052-11.302 11.302 0 6.239 5.063 11.302 11.302 11.302h25.78c6.25 0 11.302-5.063 11.302-11.302zm-77.351 0c0-6.25-5.063-11.302-11.302-11.302H65.031c-6.25 0-11.302 5.052-11.302 11.302 0 6.239 5.052 11.302 11.302 11.302h98.304c6.239 0 11.302-5.063 11.302-11.302z"
            ></path>
            <path
              fill="#201C1C"
              d="M458.271 109.877v249.807c0 6.239-5.052 11.302-11.302 11.302H65.031c-6.25 0-11.302-5.063-11.302-11.302V109.877c0-6.239 5.052-11.302 11.302-11.302h381.937c6.251 0 11.303 5.064 11.303 11.302zm-22.604 238.505v-4.566c-.927-.509-1.808-1.142-2.588-1.933l-76.627-76.616-35.432 35.432 47.683 47.683h66.964zm0-35.861V121.179H76.333v177.135l113.166-113.155c4.408-4.408 11.573-4.408 15.981 0l99.559 99.559 43.422-43.422c4.419-4.408 11.573-4.408 15.981 0l71.225 71.225zm-98.937 35.861L197.49 209.131 76.333 330.276v18.106H336.73z"
            ></path>
            <path
              fill="#FFFFFF"
              d="M435.667 343.816v4.566h-66.964l-47.683-47.683 35.432-35.432 76.627 76.616c.779.792 1.661 1.424 2.588 1.933z"
            ></path>
            <path
              fill="#EF8E23"
              d="M435.667 121.179v191.342l-71.225-71.225c-4.408-4.408-11.562-4.408-15.981 0l-43.422 43.422-99.559-99.558c-4.408-4.408-11.573-4.408-15.981 0L76.333 298.314V121.179h359.334zm-88.596 64.184c0-23.565-19.168-42.733-42.721-42.733-23.565 0-42.733 19.168-42.733 42.733 0 23.553 19.168 42.721 42.733 42.721 23.553 0 42.721-19.168 42.721-42.721z"
            ></path>
            <path
              fill="#FFFFFF"
              d="M197.49 209.131l139.24 139.251H76.333v-18.106z"
            ></path>
            <path
              fill="#201C1C"
              d="M304.35 142.63c23.553 0 42.721 19.168 42.721 42.733 0 23.553-19.168 42.721-42.721 42.721-23.565 0-42.733-19.168-42.733-42.721 0-23.565 19.168-42.733 42.733-42.733zm20.117 42.733c0-11.098-9.03-20.129-20.117-20.129-11.098 0-20.129 9.03-20.129 20.129 0 11.087 9.03 20.117 20.129 20.117 11.087 0 20.117-9.03 20.117-20.117zM240.686 396.46c6.25 0 11.302 5.052 11.302 11.302 0 6.239-5.052 11.302-11.302 11.302h-25.78c-6.239 0-11.302-5.063-11.302-11.302 0-6.25 5.063-11.302 11.302-11.302h25.78zM163.335 396.46c6.239 0 11.302 5.052 11.302 11.302 0 6.239-5.063 11.302-11.302 11.302H65.031c-6.25 0-11.302-5.063-11.302-11.302 0-6.25 5.052-11.302 11.302-11.302h98.304z"
            ></path>
          </svg>
          <h3 class="icon-title dark:text-white">图片超分辨率</h3>
          <div class="icon-description dark:text-white">通过ESRGAN网络实现图片清晰化效果</div>
        </div>
      </div>
    </div>
  </div>
  <br /><br /><br />
</template>

<style scoped>
* {
  box-sizing: border-box;
}
body {
  margin: 0;
}
.container {
  margin: auto;
  max-width: 1200px;
  padding: 0 20px;
  justify-content: space-between;
}
.img {
  background-size: cover;
  background-repeat: no-repeat;
  padding: 30px 0 0px;
  background-attachment: fixed;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
a {
  color: white;
  font-weight: 700;
  font-size: 15px;
  font-family: Sans-serif;
  text-decoration: none;
  margin-bottom: 70px;
}
.title1 {
  color: #ff8001;
  font-family: "Quicksand", sans-serif;
  letter-spacing: 2px;
  font-size: 14px;
}
.title2 {
  color: rgb(0, 0, 0);
  font-family: "Quicksand", sans-serif;
  font-size: 40px;
  font-weight: bold;
}
.introduce {
  color: #000000d0;
  font-family: "Quicksand", sans-serif;
  line-height: 1.5;
  font-size: 17px;
}
.jotform-icon {
  background-repeat: no-repeat;
  background-size: cover;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-bottom: 70px;
}
.button {
  padding: 12px 17px;
  border-radius: 5px;
  border: 0;
  font-family: "Quicksand", sans-serif;
  font-weight: bold;
  background-color: white;
  font-size: 100%;
  letter-spacing: 0.5px;
  margin-top: 5px;
}
.title3 {
  font-family: "Quicksand", sans-serif;
  font-size: 40px;
  text-align: center;
  margin-top: 90px;
}
.icon1-img {
  background-repeat: no-repeat;
  background-size: cover;
  width: 120px;
  height: 120px;
}

.icon-description {
  display: block;
  margin-top: 5px;
  text-align: center;
  font-family: "Quicksand", sans-serif;
  color: #000000;
  font-weight: 500;
  font-size: 17px;
}

.icon-list {
  display: flex;
  flex-wrap: wrap;
}
.three-icon {
  flex: 1;
  padding: 30px;
}
.icon-title {
  font-family: "Quicksand", sans-serif;
  font-size: 20px;
}
.page2 {
  text-align: center;
}
.page3 {
  background-color: #fbfbfb;
}
.page3-box {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  padding: 20px 0;
}
.page3-img {
  max-width: 540px;
  width: 100%;
}
.information {
  flex: 1;
  padding-left: 70px;
}
button.learn-more {
  background-color: #292b2c;
  color: white;
}
.info-title {
  font-family: "Quicksand", sans-serif;
  font-size: 30px;
  font-weight: bold;
}
.info-all {
  color: #000000b3;
  margin-bottom: 20px;
  line-height: 1.4;
  font-size: 17px;
}
.get-free {
  background-color: #292b2c;
  color: white;
}
.memberships {
  display: flex;
  flex-wrap: wrap;
}
.member {
  flex: auto;
  padding: 60px;
  text-align: center;
  font-family: "Quicksand", sans-serif;
  border-radius: 4px;
}
span {
  font-size: 40px;
}
.mem-title {
  font-size: 26px;
  font-weight: bold;
}
.orange {
  background-color: #ff8001;
  color: white;
}
.page4 {
  padding: 80px 0;
}
.under {
  background-color: #f5f5f5;
  padding: 10px;
  display: flex;
}
.under .container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  width: 100%;
}

.copy {
  font-family: "Work Sans", sans-serif;
}
.facebook {
  background-image: url("https://i.ibb.co/x6n6DNV/facebook-logo-button.png");
  background-repeat: no-repeat;
  background-size: cover;
  width: 30px;
  height: 30px;
}
.sos-med {
  display: flex;
  justify-content: space-between;
  width: 100px;
}

.twitter {
  background-image: url("https://i.ibb.co/wzstzsd/twitter.png");
  background-repeat: no-repeat;
  background-size: cover;
  width: 30px;
  height: 30px;
}
.linkedin {
  background-image: url("https://i.ibb.co/9T8kqqb/linkedin-logo-button.png");
  background-repeat: no-repeat;
  background-size: cover;
  width: 30px;
  height: 30px;
}

@media (max-width: 840px) {
  .information {
    padding-left: 0;
    text-align: center;
  }
  .page3-box {
    justify-content: center;
  }
}
</style>

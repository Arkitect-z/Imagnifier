<template>
    <div class="l-container">
  <div class="b-game-card">
    <div class="b-game-card__cover" style="background-image: url(https://andrewhawkes.github.io/codepen-assets/steam-game-cards/game_1.jpg);"></div>
  </div>
  <div class="b-game-card">
    <div class="b-game-card__cover" style="background-image: url(https://andrewhawkes.github.io/codepen-assets/steam-game-cards/game_2.jpg);"></div>
  </div>
  <div class="b-game-card">
    <div class="b-game-card__cover" style="background-image: url(https://andrewhawkes.github.io/codepen-assets/steam-game-cards/game_3.jpg);"></div>
  </div>
  <div class="b-game-card">
    <div class="b-game-card__cover" style="background-image: url(https://andrewhawkes.github.io/codepen-assets/steam-game-cards/game_4.jpg);"></div>
  </div>
</div>
</template>
<style lang="scss">
// Settings

$c_0: #000000;
$c_1: #353540;

// Basic reset


.l-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 30px;
  width: 50%;
  max-width: 1200px;
  padding: 30px;
  
  @media screen and (max-width: 760px) {
    grid-template-columns: repeat(2, 1fr);
  }
  
}

.b-game-card {
  position: relative;
  z-index: 1;
  width: 100%;
  padding-bottom: 150%;
  perspective: 1000px;
  
  &__cover {
    position: absolute;
    z-index: 1;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background-image: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
    background-size: cover;
    perspective-origin: 50% 50%;
    transform-style: preserve-3d;
    transform-origin: top center;
    will-change: transform;
    transform: skewX(.001deg);
    transition: transform .35s ease-in-out;
    
    // Gloss 
    
    &::after {
      display: block;
      content: '';
      position: absolute;
      z-index: 100;
      top: 0;
      left: 0;
      width: 100%;
      height: 120%;
      background: linear-gradient(226deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.4) 35%, rgba(255,255,255,0.2) 42%, rgba(255,255,255,0) 60%);
      transform: translateY(-20%);
      will-change: transform;
      transition: transform .65s cubic-bezier(0.18, 0.9, 0.58, 1);
    }
    
  }
  
  &:hover &__cover {
    transform: rotateX(7deg) translateY(-6px);

    &::after {
      transform: translateY(0%);
    }
    
  }
  
  // Shadows
  
  &::before {
    display: block;
    content: '';
    position: absolute;
    top: 5%;
    left: 5%;
    width: 90%;
    height: 90%;
    background: rgba($c_0, 0.5);
    box-shadow: 0 6px 12px 12px rgba($c_0, 0.4);
    will-change: opacity;
    transform-origin: top center;
    transform: skewX(.001deg);
    transition: transform .35s ease-in-out, opacity .5s ease-in-out;
  }
  
  &:hover::before {
    opacity: 0.6;
    transform: rotateX(7deg) translateY(-6px) scale(1.05);
  }
  
  
}
</style>
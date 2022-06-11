<template>
  <div class="PopupOuterButton">
    <div class="PopupOpenHackathon">
      <p>zurück</p>
      <i class="fa-solid fa-angle-right"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeButton"
}
</script>

<style scoped>

.PopupOuterButton{
  width:100%;
  position: relative;
  display: flex;
  justify-content: center;
  cursor: pointer;
}

.PopupOpenHackathon{
  display: flex;
  align-items: center;
  margin-top: 5%;
  width: 80%;
  color: white;
  font-size: 1rem;
  justify-content: space-between;
  flex-direction: row;
  align-content: center;
}
</style>

<template>
  <div></div>
</template>
  
  <script lang="ts">
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  setup() {
    return {};
  },
  head() {
    return {
      title: this.$t("general.favorites") as string,
    };
  },
});
</script>
  
  <style scoped>
</style>
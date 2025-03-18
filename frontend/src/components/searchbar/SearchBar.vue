<script setup lang="js">
import { computed } from 'vue';
import { useStore } from 'vuex';

const props = defineProps({
  module: {
    type: String,
    required: true, // Ensure the module name is always provided
  }
});

const store = useStore();

// Dynamically get and set searchQuery for the specified module
const search = computed({
  get: () => store.state[props.module].searchQuery,
  set: (value) => store.commit(`${props.module}/SET_SEARCH_QUERY`, value),
});
</script>

<template>
  <div class="d-flex justify-content-center mt-3">
    <div class="row w-50">
      <div class="col-md-8">
        <div class="input-group mb-3">
          <input 
            type="text" 
            v-model="search"
            class="form-control input-text" 
            :placeholder="`Search ${ module }...`" 
            :aria-label="`Search ${module}`"
            aria-describedby="search-btn"
          />
          <button class="btn search-btn" type="button" id="search-btn">
            <i class="fa fa-search search-icon"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped>
    @import '/src/assets/css/searchbar.css'
</style>
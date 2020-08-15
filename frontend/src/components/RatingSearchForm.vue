<template>
  <v-form ref="form">
    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @keyup.enter="onSubmit" @click="onSubmit">Search</v-btn>
    </v-layout>
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    },
    sorting: {
      type: String,
      default: ""
    }
  },
  data() {
    return{
      items:""
    }
  },
  methods: {
    onSubmit: function() {
      if (this.sorting=='평점(높은순)'){
        this.items = "up"
      }else {
        this.items = "down"
      }
      const params = {
        sorting: this.items
      };
      this.submit(params)
    }
  }
};
</script>